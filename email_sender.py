import smtplib  # simple mail transfer protocol
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Shubhi Puntambekar'
email['to'] = 'change_with_your_to_email'
email['subject'] = 'You won 1,000,000 dollars!'

# email.set_content('I am a python master!')
email.set_content(html.substitute({'name':'TinTin'}), 'html')
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('change_with_from_email', 'nabqamvsbghrdlan')
    smtp.send_message(email)

    print('all good boss.')
