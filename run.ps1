minikube start --mount --mount-string="$(pwd)\backupfolder:/Mount"
docker context use default
minikube docker-env
minikube docker-env | Invoke-Expression
docker build -t backuper .
kubectl apply -f backuper.yaml -f pv.yaml -f pvc.yaml