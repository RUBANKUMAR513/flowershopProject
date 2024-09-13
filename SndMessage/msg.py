
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from SndMessage.models import ToEmail  # Import the ToEmail model
from Userauth.models import UserDetail
from django.core.exceptions import ObjectDoesNotExist
from SndMessage.models import Setting

def process(store_data_instance):
    try:
        # Fetch the email settings from the Setting model
        setting = Setting.objects.get()
        sender_email = setting.email
        email_password = setting.password
        smtp_host = setting.host
        smtp_port = setting.port
    except ObjectDoesNotExist:
        print("No email settings found. Please configure the email settings.")
        return

    # Get the User instance linked to the StoreData instance
    user = store_data_instance.user

    # Get the UserDetail instance linked to the User
    try:
        user_detail = UserDetail.objects.get(user=user)
    except UserDetail.DoesNotExist:
        user_detail = None  # Handle the case where UserDetail doesn't exist

    # Get all active recipients from the ToEmail model
    active_recipients = ToEmail.objects.filter(active_status=True)

    if not active_recipients.exists():
        print("No active recipients found.")
        return

    # Construct the email body with HTML formatting
    body_admin = f"""
    <html>
    <body>
        <p>Dear Admin,</p>

        <p><strong>Message:</strong> <strong>{store_data_instance.msg}</strong></p>
        <p><strong>User Name:</strong> {user.username}<br>
           <strong>User Email:</strong> {user.email}</p>

        {'<p>No additional user details available.</p>' if not user_detail else f"""
        <p>Address Details:</p>
        <ul>
            <li><strong>Address:</strong> {user_detail.address}</li>
            <li><strong>Phone Number:</strong> <a href="tel:{user_detail.phone_number}">{user_detail.phone_number}</a></li>
            <li><strong>Nation:</strong> {user_detail.nation if user_detail.nation else 'N/A'}</li>
            <li><strong>District:</strong> {user_detail.district if user_detail.district else 'N/A'}</li>
            <li><strong>State:</strong> {user_detail.state if user_detail.state else 'N/A'}</li>
            <li><strong>Taluk:</strong> {user_detail.taluk if user_detail.taluk else 'N/A'}</li>
            <li><strong>Pincode:</strong> {user_detail.pincode if user_detail.pincode else 'N/A'}</li>
        </ul>
        """}
        
        <p>Here are the contact details:</p>
        <ul>
            <li><strong>Name:</strong> {store_data_instance.name}</li>
            <li><strong>Contact Email:</strong> {store_data_instance.email}</li>
            <li><strong>Contact Phone Number:</strong> <a href="tel:{store_data_instance.phone_number}">{store_data_instance.phone_number}</a></li>
        </ul>
    </body>
    </html>
    """

    body_user = f"""
    <html>
    <body>
        <p>Dear {user.username},</p>

        <p>Thank you for reaching out. We have received your message:</p>
        <p><strong>{store_data_instance.msg}</strong></p>

        <p>We will get back to you soon.</p>

        <p>Best regards,<br>
        Team VKM Flower Shop</p>
    </body>
    </html>
    """

    # Loop through all active recipients and send emails to admin
    for recipient in active_recipients:
        receiver_email = recipient.email  # Email from the active ToEmail record
        subject = f"Message from {store_data_instance.name}"

        # Create the email message
        msg = MIMEMultipart('alternative')
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body_admin, 'html'))

        try:
            # Connect to the server
            server = smtplib.SMTP(smtp_host, smtp_port)
            server.starttls()  # Use TLS (Transport Layer Security)

            # Login to the email account
            print("From email:", sender_email)
            print("To Email:", receiver_email)
            server.login(sender_email, email_password)

            # Send the email
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)

            print(f"Email sent successfully to Admin at {receiver_email}!")

        except Exception as e:
            print(f"Error sending email to Admin ({receiver_email}): {e}")

        finally:
            # Quit the server connection
            server.quit()

    # Send an email to the user with their contact email
    subject_user = "Confirmation of Your Message"
    msg_user = MIMEMultipart('alternative')
    msg_user['From'] = sender_email
    msg_user['To'] = store_data_instance.email
    msg_user['Subject'] = subject_user
    msg_user.attach(MIMEText(body_user, 'html'))

    try:
        # Connect to the server
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()  # Use TLS (Transport Layer Security)

        # Login to the email account
        print("From email:", sender_email)
        print("To Email:", store_data_instance.email)
        server.login(sender_email, email_password)

        # Send the email
        text = msg_user.as_string()
        server.sendmail(sender_email, store_data_instance.email, text)

        print(f"Confirmation email sent successfully to {store_data_instance.email}!")

    except Exception as e:
        print(f"Error sending email to user ({store_data_instance.email}): {e}")

    finally:
        # Quit the server connection
        server.quit()