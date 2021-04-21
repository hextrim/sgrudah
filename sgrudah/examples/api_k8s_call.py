from kubernetes import client
configuration = client.Configuration()
configuration.api_key["authorization"] = '<oc token here>'
configuration.api_key_prefix['authorization'] = 'Bearer'
configuration.host = 'https://openshift.hextrim.com:8443'
configuration.ssl_ca_cert = 'ca.crt'

v1 = client.CoreV1Api(client.ApiClient(configuration))
ret = v1.list_pod_for_all_namespaces(watch=False)

for item in ret.items:
    print(
        "%s\t%s\t%s" %
        (item.status.pod_ip,
         item.metadata.namespace,
         item.metadata.name))
