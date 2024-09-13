import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email parameters
sender_email = "rubanfebinosolutions@gmail.com"
receiver_email = "manikmanimurugan@gmail.com"
subject = "Test Email"
body = "This is a test email sent from Python."
email_password = "aijb eiho aoqo gvmf"  # Replace with your actual email password

# Create the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

try:
    # Connect to the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Use TLS (Transport Layer Security)

    # Login to the email account
    print("From email:",sender_email)
    print("To Email:",receiver_email)
    print("Password",email_password)
    server.login(sender_email, email_password)

    # Send the email
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)

    print("Email sent successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Quit the server connection
    server.quit()
