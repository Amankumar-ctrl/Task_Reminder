import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
load_dotenv()

# =========================
# YOUR EMAIL CONFIG
# =========================

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

# =========================
# YOUR DAILY SCHEDULE
# =========================

daily_schedule = """
6:00 AM - Wake up
7:00 AM - Workout
9:00 AM - Study Python
1:00 PM - Lunch
3:00 PM - Project Work
10:00 PM - Sleep

"""

# =========================
# EMAIL FUNCTION
# =========================

def send_email():

    subject = "Today's Schedule"

    body = f"""
Good Morning.

Here is your schedule for today:

{daily_schedule}
"""

    msg = MIMEMultipart()

    msg["From"] = "Task Reminder Service     <hellobox281@gmail.com>"
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login(
            EMAIL_SENDER,
            EMAIL_PASSWORD
        )

        server.sendmail(
            EMAIL_SENDER,
            EMAIL_RECEIVER,
            msg.as_string()
        )

        server.quit()

        print("Email sent successfully.")

    except Exception as e:
        print("Error:", e)

# =========================
# RUN DAILY AT 7 AM
# =========================

print("Sending scheduled email...")
send_email()
print("Done.")