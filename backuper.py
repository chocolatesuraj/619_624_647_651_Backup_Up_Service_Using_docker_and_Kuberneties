from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate():
    """Authenticate user."""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def upload_file(service, file_path, folder_id=None):
    """Upload a file to Google Drive."""
    file_name = os.path.basename(file_path)
    file_metadata = {'name': file_name}
    if folder_id:
        file_metadata['parents'] = [folder_id]

    media = MediaFileUpload(file_path)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print('File ID: %s' % file.get('id'))

def main():
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    # Find the folder ID where you want to upload the files (optional)
    folder_id = None
    folder_name = 'Backup Folder Name'
    results = service.files().list(q=f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false", fields="files(id)").execute()
    items = results.get('files', [])
    if items:
        folder_id = items[0]['id']
    else:
        # Create the folder if it doesn't exist
        folder_metadata = {'name': folder_name, 'mimeType': 'application/vnd.google-apps.folder'}
        folder = service.files().create(body=folder_metadata, fields='id').execute()
        folder_id = folder.get('id')

    # Local directory to upload files from
    local_dir = './backupfolder'
    for filename in os.listdir(local_dir):
        if os.path.isfile(os.path.join(local_dir, filename)):
            upload_file(service, os.path.join(local_dir, filename), folder_id)

if __name__ == '__main__':
    main()