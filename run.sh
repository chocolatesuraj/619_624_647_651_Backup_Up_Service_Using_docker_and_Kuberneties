minikube start
docker context use default
eval $(minikube docker-env)
kubectl apply -f backuper.yaml