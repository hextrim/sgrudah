import os
import sys
import kubernetes
from flask import Flask, render_template, request, url_for, flash, copy_current_request_context, redirect, jsonify
from openshift.dynamic import DynamicClient

k8s_client = kubernetes.config.new_client_from_config('../node.kubeconfig')
dyn_client = DynamicClient(k8s_client)


# Here should be projects and nested loops around it, but starting with namespaces
v1_namespaces = dyn_client.resources.get(api_version='v1', kind='Namespace')
namespaces = v1_namespaces.get()
filter_projects = ['app-storage', 'default', 'kube-public', 'kube-system', 'logging', 'management-infra', 'openshift', 'openshift-console', 'openshift-infra', 'openshift-logging', 'openshift-metrics-server', 'openshift-monitoring', 'openshift-node', 'openshift-sdn', 'openshift-web-console', 'hextrim-jenkins-slaves']

namespaces_list = []

for item in namespaces.items:
    namespaces_list.append(str(item.metadata.name))
    
namespaces_filtered = [n for n in namespaces_list if n not in filter_projects]

#print (namespaces_filtered)

v1_images = dyn_client.resources.get(api_version='v1', kind='ImageStreamTag')

#print (v1_images.get())

names = []
for ns in namespaces_filtered:
    images = v1_images.get(namespace=ns)
    for item in images.items:
        if item.metadata.namespace == "openshift":
            pass
        else:
            names.append({"name": item.metadata.name, "namespace": ns})

#print (names)        

def pods():
    pods_list = []
    for name in names:
        version = v1_images.get(name=name["name"], namespace=name["namespace"])
        try:
        #    print (str(name["namespace"]) + " " + str(name["name"]) + " " + str(version.image.dockerImageMetadata.ContainerConfig.Labels["CUSTOM-VERSION"]))
            pods_list.append({"namespace": name["namespace"], "name": name["name"], "version": version.image.dockerImageMetadata.ContainerConfig.Labels["version"]})
        except TypeError:
        #    print (str(name["namespace"]) + " " + str(name["name"]) + " " + "None")
            pods_list.append({"namespace": name["namespace"], "name": name["name"], "version": None})
    return pods_list

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    podsy=pods()
    return render_template('index.html', podsy=podsy)
    
if __name__ == "__main__":
    app.run(debug = True)
