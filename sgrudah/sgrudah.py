import os
import sys
import yaml
import re
#import kubernetes
from kubernetes import client, config
from flask import Flask, render_template, request, url_for, flash, copy_current_request_context, redirect, jsonify
from openshift.dynamic import DynamicClient

config.load_incluster_config()
k8s_config = client.Configuration()
k8s_client = client.api_client.ApiClient(configuration=k8s_config)
#k8s_client = kubernetes.config.new_client_from_config('node.kubeconfig')
dyn_client = DynamicClient(k8s_client)
v1_namespaces = dyn_client.resources.get(api_version='v1', kind='Namespace')
namespaces = v1_namespaces.get()

filter_projects = ['app-storage', 'default', 'kube-public', 'kube-system', 'management-infra', 'openshift', 'openshift-console', 'openshift-infra', 'openshift-logging', 'openshift-metrics-server', 'openshift-monitoring', 'openshift-node', 'openshift-sdn', 'openshift-web-console'] 

print(namespaces.items)

namespaces_list = []

print(type(namespaces_list))

print('##############################################')

for item in namespaces.items:
    namespaces_list.append(str(item.metadata.name))

print(namespaces_list)

print('########### REDUCED ############')

namespaces_filtered = [n for n in namespaces_list if n not in filter_projects]

print(namespaces_filtered)

print('######## BUILD N BURN #######')
for d in namespaces_filtered:
    dupa = re.findall(r'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', d)
    dupa = ' '.join(map(str, dupa))
    if d == dupa:
        print(dupa)
    else:
        pass

pods_list = []

v1_pods = dyn_client.resources.get(api_version='v1', kind='Pod')
pods = v1_pods.get()

def pots():
    for item in pods.items:
#    print (item.metadata.name)
        pods_list.append((item.metadata.name, item.spec.containers[0]["image"]))
# print (item.metadata.name, item.spec.containers[0]["image"])
#    return (item.metadata.name, item.spec.containers[0]["image"])
    return pods_list



app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    potsy=pots()
    return render_template('index.html', potsy=potsy)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
