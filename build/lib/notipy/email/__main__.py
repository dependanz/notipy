import sys
import ast
import smtplib
import argparse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

parser = argparse.ArgumentParser(
    prog = 'notipy.email',
    description = ''
)
parser.add_argument(
    '--source',
    required=True
)
parser.add_argument(
    '--destination',
    required=True
)
parser.add_argument(
    '--gmail_app_pass',
    required=True
)
parser.add_argument(
    'pipe_params',
    nargs="*"
)

args = parser.parse_args()
if not sys.stdin.isatty():
    args.pipe_params.extend(sys.stdin.read().splitlines())

GMAIL_APP_PASS = args.gmail_app_pass

msg = MIMEMultipart('alternative')
msg['Subject'] = "[notipy] - Process Complete"
msg['From']    = args.source
msg['To']      = args.destination

text = "Process Complete."
html = f"""
    <html>
        <head></head>
        <body>
            <div>
                <h1>[notipy] - Process Complete</h1>
                <div>
                    {'<br>'.join(ast.literal_eval(repr(args.pipe_params)))}
                </div>
            </div>
        </body>
    </html>
"""

msg.attach(MIMEText(text, 'plain'))
msg.attach(MIMEText(html, 'html'))

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
    smtp_server.login(
        args.source,
        GMAIL_APP_PASS
    )
    smtp_server.sendmail(
        args.source,
        args.destination,
        msg.as_string()
    )
