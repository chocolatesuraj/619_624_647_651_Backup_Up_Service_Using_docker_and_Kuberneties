# Back-Up-Service
Creating a backup service that periodically backs up the contents of a folder to Google Drive using Docker and Kubernetes involves several steps.

# Steps to run:

1. Create credentials.json file using the following link https://python.plainenglish.io/automate-google-drive-backup-using-python-105f57e2151 or watch this youtube video https://www.youtube.com/watch?v=fkWM7A-MxR0 and add it with the other files.
2. Run the backuper.py file to generated token.json file.
3. Create a docker image:
   build -t backuper .
4. Run the script file to start minikube and create the cronjob
   
   For Windows:
   .\run.ps1
   
   For Linux:
   ./run.sh
6. In order to monitor the cronjob and pods created run the following command in a seperate terminal:
   minikube dashboard
7. To view all cronjobs:
   kubectl get cronjob
8. To stop/delete cronjob:
   kubectl delete -n default cronjob backup-job
