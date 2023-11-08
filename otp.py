import smtplib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to generate a random OTP
def generate_otp(length=6):
    characters = string.digits
    otp = ''.join(random.choice(characters) for _ in range(length))
    return otp

# Function to send an email with the OTP
def send_otp_email(receiver_email, otp):
    sender_email = "your_email@gmail.com"  # Replace with your email address
    sender_password = "your_password"  # Replace with your email password

    subject = "Your OTP Code"
    message = f"Your OTP code is: {otp}"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(message, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("OTP sent successfully.")
    except Exception as e:
        print(f"Error sending email: {str(e)}")

# Generate a random OTP
otp = generate_otp()

# Send the OTP to the specified email address
receiver_email = "recipient@example.com"  # Replace with the recipient's email address
send_otp_email(receiver_email, otp)
