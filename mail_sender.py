from reportlab.pdfgen.canvas import Canvas
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def create_cover_letter(cov_str):
    canvas          = Canvas("Cover_Letter.pdf")
    cov_str         = cov_str.replace("ı","i")
    cov_str_lines   = cov_str.splitlines( )
    # 70*12 x 50*12
    # 38 chars per line
    canvas.drawString(72, 61*12, cov_str_lines[0])
    cov_str = "\n".join(cov_str_lines[1:])
    line_counter    = 0
    line_max_char   = 82
    line_by_line = cov_str.split("\n")
    for line in line_by_line:
        while len(line) > line_max_char:
                end = line.rfind(" ", 0, line_max_char)
                canvas.drawString(72, (60-line_counter)*12, line[:end])
                line = line[end+1:]
                line_counter += 1
        if len(line) <= line_max_char:
            canvas.drawString(72, (60-line_counter)*12, line)
             
        line_counter += 1
    canvas.save()

def send_email(subject, body, to_email, attachment_paths):
    from_email = os.environ['EMAIL']
    password = os.environ["PASSWORD"]

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Attach each file in the list
    for attachment_path in attachment_paths:
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {attachment_path}")
        message.attach(part)

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.ehlo()
    session.starttls()  # enable security
    session.login(from_email, password)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(from_email, to_email, text)
    session.quit()

    print('Mail Sent')

def send(email_dict, file):
    create_cover_letter(email_dict["cover_letter"])
    send_email(email_dict["mail_subject"], email_dict["mail_content"], email_dict["mail_adress"], ["Ozcan_Ahmethan_CV.pdf","Cover_Letter.pdf"])
    file.write(email_dict["reference_number"]+"\n")
