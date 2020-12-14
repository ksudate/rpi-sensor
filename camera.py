from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
import picamera
import datetime
import shutil
import os

SCOPES = ['https://www.googleapis.com/auth/drive']

def main():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    # picture process start
    imgdir_path = '/home/pi/img/'
    if os.path.exists(imgdir_path):
        shutil.rmtree(imgdir_path)
        os.mkdir(imgdir_path)
    today = datetime.datetime.today().strftime('%Y-%m-%d-%H-%M')
    img_path = imgdir_path + today + '.jpg'
    with picamera.PiCamera() as camera:
        camera.resolution = (600,400)
        camera.capture(img_path)

    folder_id = '1j3lLV3JaaNzoRmQFsiflL19GE-bQtfEt'
    file_metadata = {
        'name': today + '.jpg',
        'parents': [folder_id]
    }
    media = MediaFileUpload(img_path, mimetype='image/jpeg')
    file = service.files().create(body=file_metadata,
        media_body=media,
        fields='id').execute()

if __name__ == '__main__':
    main()
