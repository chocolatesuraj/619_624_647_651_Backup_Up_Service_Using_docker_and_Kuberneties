minikube start
docker context use default
eval $(minikube docker-env)
kubectl create secret generic google-drive-credentials --from-file=token.json
kubectl apply -f backuper.yaml
