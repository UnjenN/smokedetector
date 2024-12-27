import serial
import smtplib
import time
from email.mime.text import MIMEText
from datetime import datetime, timedelta

# Configuration variables
SERIAL_PORT = '/dev/ttyUSB0'  # Serial port connected to Arduino (change if necessary)
BAUD_RATE = 9600  # Baud rate for serial communication
THRESHOLD = 300  # Smoke level threshold to trigger alert (change as needed)
COOLDOWN_MINUTES = 5  # Cooldown time to prevent multiple alerts within a short time (change as needed)

# Email settings
SENDER_EMAIL = "sample_email@example.com"  # Sender's email address (replace with your email)
SENDER_PASSWORD = "your_app_password"    # App password for the sender's email (replace with your app password)
RECIPIENT_EMAIL = "sample_recipient@example.com"  # Recipient's email address (replace with recipient email)

# Open serial port to communicate with Arduino
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

# Function to send email alerts when smoke is detected
def send_email_alert(detection_time):
    subject = "Smoking Detected!"
    body = f"Smoking was detected in a non-monitored area.\nDetection Time: {detection_time}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL

    try:
        # Connect to Gmail's SMTP server and send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Start TLS encryption
            server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Login with sender's credentials
            server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())  # Send email
            print("Alert email has been sent successfully.")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")

# Function to monitor smoke levels and send alerts if needed
def monitor_smoke():
    last_alert_time = None  # Store the time when the last alert was sent

    while True:
        # Read the smoke level data sent by Arduino
        smoke_level = int(ser.readline().decode().strip())
        print(f"Smoke Level: {smoke_level}")

        # Check if the smoke level exceeds the threshold
        if smoke_level > THRESHOLD:
            current_time = datetime.now()

            # Check if the cooldown time has passed since the last alert
            if last_alert_time is None or (current_time - last_alert_time) > timedelta(minutes=COOLDOWN_MINUTES):
                print("Smoking detected! Sending alert...")
                send_email_alert(current_time.strftime("%Y-%m-%d %H:%M:%S"))  # Send email alert
                last_alert_time = current_time  # Update the time of the last alert
            else:
                remaining_time = (timedelta(minutes=COOLDOWN_MINUTES) - (current_time - last_alert_time)).total_seconds()
                print(f"Cooldown in progress... {int(remaining_time // 60)} minutes {int(remaining_time % 60)} seconds remaining")
        else:
            print("Safe state, no smoking detected.")

        time.sleep(2)  # Wait for 2 seconds before checking again

if __name__ == "__main__":
    print("Smoke detection system is now running.")
    monitor_smoke()
