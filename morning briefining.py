import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
from bs4 import BeautifulSoup

# Portées d'accès (lire les mails uniquement)
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    creds = None
    # Vérifie si le fichier token.pickle existe (pour éviter de se reconnecter)
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # Si les identifiants ne sont pas valides, reconnecte-toi
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)  # Remplace par le nom de ton fichier JSON téléchargé
            creds = flow.run_local_server(port=0)
        # Sauvegarde les identifiants pour la prochaine fois
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('gmail', 'v1', credentials=creds)
    return service

def get_emails(service, max_results=10):
    # Récupère les mails reçus depuis hier
    results = service.users().messages().list(
        userId='me',
        labelIds=['INBOX', 'UNREAD'],
        maxResults=max_results
    ).execute()
    messages = results.get('messages', [])
    emails = []
    for message in messages:
        msg = service.users().messages().get(
            userId='me',
            id=message['id'],
            format='full'
        ).execute()
        # Extrait les infos du mail
        headers = msg['payload']['headers']
        subject = next(h['value'] for h in headers if h['name'] == 'Subject')
        sender = next(h['value'] for h in headers if h['name'] == 'From')
        date = next(h['value'] for h in headers if h['name'] == 'Date')
        # Extrait le corps du mail
        if 'parts' in msg['payload']:
            body = msg['payload']['parts'][0]['body']['data']
        else:
            body = msg['payload']['body']['data']
        body = base64.urlsafe_b64decode(body).decode('utf-8')
        body = BeautifulSoup(body, "html.parser").get_text()
        emails.append({
            'sender': sender,
            'subject': subject,
            'date': date,
            'body': body
        })
    return emails

if __name__ == '__main__':
    # Remplace 'credentials.json' par le nom de ton fichier JSON téléchargé
    service = get_gmail_service()
    emails = get_emails(service)
    for email in emails:
        print(f"De: {email['sender']}\nSujet: {email['subject']}\nDate: {email['date']}\nCorps: {email['body'][:200]}...\n---")
