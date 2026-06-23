import csv
import os
import smtplib
from email.message import EmailMessage

# Gmail Details
sender_email = input("Enter Your Gmail: ")
app_password = input("Enter App Password: ")

# Email Details
subject = input("Enter Subject: ")
message = input("Enter Message: ")

# CSV file path
csv_path = os.path.join(
    os.path.dirname(__file__),
    "students.csv"
)

# Read CSV
with open(csv_path, "r", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:

        name = row["Name"]
        receiver_email = row["Email"]

        email = EmailMessage()

        email["From"] = sender_email
        email["To"] = receiver_email
        email["Subject"] = subject

        email.set_content(
            f"""Hello {name},

{message}

Regards,
Shlok
"""
        )

        try:

            with smtplib.SMTP_SSL(
                "smtp.gmail.com",
                465
            ) as smtp:

                smtp.login(
                    sender_email,
                    app_password
                )

                smtp.send_message(email)

            print(f"✅ Email sent successfully to {name}")

        except Exception as e:

            print(f"❌ Failed to send email to {name}")
            print(e)