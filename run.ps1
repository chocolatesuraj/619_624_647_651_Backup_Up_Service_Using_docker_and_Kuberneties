minikube start
docker context use default
minikube docker-env
minikube docker-env | Invoke-Expression
kubectl apply -f backuper.yaml