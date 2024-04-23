#!/bin/bash

# Start Minikube with Mounts
minikube start --mount --mount-string="$(pwd)/backupfolder:/Mount"

# Switch Docker Context
eval $(minikube docker-env)

# Build Docker Image
docker build -t backuper .

# Create Kubernetes Secret
kubectl create secret generic google-drive-credentials --from-file=token.json

# Apply Kubernetes Manifests
kubectl apply -f backuper.yaml -f pv.yaml -f pvc.yaml
