import pickle
import os.path
import json
from datetime import datetime

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

from utils.utilities import Utilities

class Service:
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/calendar.events']
    creds = None
    service = None

    def login(self):
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)

        # create the service object
        self.service = build('calendar', 'v3', credentials=self.identity())
        print('---- Login Successful ----')

    def identity(self):
        return self.creds

    def log_workout(self, workout_name):
        current_date = json.dumps(datetime.utcnow(), default=Utilities.fix_date)

        event = {
            'summary': workout_name,
            'start': {
                # 'dateTime': str(current_date + 'T18:00:00.000Z').replace('"', ''),
                'dateTime': str(current_date).replace('"', ''),
                'timeZone': 'America/Los_Angeles',
            },
            'end': {
                # 'dateTime': str(current_date + 'T18:00:00.000Z').replace('"', ''),
                'dateTime': str(current_date).replace('"', ''),
                'timeZone': 'America/Los_Angeles',
            },
        }

        print(event)
        self.service.events().insert(calendarId='primary', body=event).execute()
        return event


    # unused
    # def get_upcoming_events(self):
    #     # Call the Calendar API
    #     now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    #     print('Getting the upcoming 10 events: \n')
    #     events_result = self.service.events().list(calendarId='primary', timeMin=now,
    #                                           maxResults=10, singleEvents=True,
    #                                           orderBy='startTime').execute()
    #     events = events_result.get('items', [])
    #
    #     if not events:
    #         print('No upcoming events found.')
    #     for event in events:
    #         start = event['start'].get('dateTime', event['start'].get('date'))
    #         print(start, event['summary'])
