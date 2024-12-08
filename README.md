## MinIO
Currently using a deployed pod.
<br>
Automate within pipeline if migrated to cloud, this is in the monitoring pipeline same as grafana, prometheus, kafka where each 
has its own pods. 
<br>
Can use S3 instead which does not require any pods.

 <!-- DO ONCE JUST LIKE S3 TO SET UP ONLY -->
- kubectl apply -f minio/minio-deployment.yaml
- kubectl apply -f minio/minio-service.yaml
- create bucket name models

<!-- This is to access the client not server, since server is at a deployed pod -->

- Client Installation
    - https://dl.min.io/server/minio/release/windows-amd64/minio.exe
    - https://dl.min.io/client/mc/release/windows-amd64/mc.exe

- Upload file
    - mc cp file myminio/bucket

## Access Pods
- kubectl exec -it pod-name -- /bin/bash              