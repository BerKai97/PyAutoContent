import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube",
          "https://www.googleapis.com/auth/youtube.force-ssl",
          "https://www.googleapis.com/auth/youtube.upload",
          "https://www.googleapis.com/auth/youtubepartner"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    creds = None


    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "./google_secret.json"

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                'google_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())



    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=creds)

    request = youtube.videos().insert(
        part="snippet,status",
        autoLevels=False,
        notifySubscribers=True,
        stabilize=False,
        body={
            "snippet": {
                "description": "This is a test video description heer yes.",
                "title": "Test Video Upload 2 of that thing",
                "tags": ["test", "video", "upload"],
                "categoryId": "22"
            },
            "status": {
                "privacyStatus": "private"
            }
        },
        
        # TODO: For this request to work, you must replace "YOUR_FILE"
        #       with a pointer to the actual file you are uploading.
        media_body=MediaFileUpload("./aab.mp4")
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()