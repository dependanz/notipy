import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_gmail(
    source,
    destination,
    app_password,
    label    = 'notipy',
    subject  = 'Process Complete',
    messages = []
):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"[{label}] {subject}"
    msg['From']    = source
    msg['To']      = destination

    text = f"\"[{label}] {subject}\"\n{'\n'.join(messages)}"
    html = f"""
        <html>
            <head></head>
            <body>
                <div>
                    <h1>[{label}] {subject}</h1>
                    <div>
                        {'<br>'.join(messages)}
                    </div>
                </div>
            </body>
        </html>
    """

    msg.attach(MIMEText(text, 'plain'))
    msg.attach(MIMEText(html, 'html'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(
            source,
            app_password
        )
        smtp_server.sendmail(
            source,
            destination,
            msg.as_string()
        )
