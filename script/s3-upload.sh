POD_NAME=$(kubectl get pods -l app=express-deployment -o jsonpath='{.items[0].metadata.name}')

kubectl exec -it $POD_NAME -- python /script.py