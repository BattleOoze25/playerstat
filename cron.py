# from __future__ import print_function
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from myapp.models import Player, Score

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1ObuwU_8xvhx7-X9YKKecyCdgSXtIUpCyMrGM0knzu0g'
SAMPLE_RANGE_NAME = 'A2:ZZ'


def main():

    # obj = Player(name="hello", match="hello1", score=23)
    # obj.save()
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'D:\DEV\SubtleRR\myproject\myapp\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return


        



        for row in values:
            name = row[0]
            objs = Player.objects.filter(name=name)
            if objs:
                scores = Score.objects.filter(player= objs[0])
                s_l = len(scores)
                r_l = len(row)
                for i in range(s_l+1, r_l):
                    score = Score(score=row[i], player=objs[0],match=i )
                    score.save()

            else:
                obj = Player(name=name)
                obj.save()
                for i in range(1, len(row)):
                    score = Score(score=row[i], player=obj,match=i )
                    score.save()
                
            # print(len(row))
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[1]))
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # sys.path.append(BASE_DIR)
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
    # django.setup()
    main()
# if __name__ == '__main__':
    