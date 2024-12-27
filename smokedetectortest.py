# This code is only used for test run.

import random
import smtplib
import time
from email.mime.text import MIMEText
from datetime import datetime, timedelta

def simulate_sensor_data():
    for i in range(15):
        yield random.uniform(0, 500)
        time.sleep(10)

# 이메일 알림
def send_email_alert(detection_time):
    sender = "osp787199@gmail.com"
    recipient = "recipient4872759038@gmail.com"
    subject = "흡연이 감지되었습니다!"
    body = f"⚠️모니터링 중인 금연 구역에서 흡연이 감지되었습니다!\n{detection_time}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, "amht duea ifvg npfs")
            server.sendmail(sender, recipient, msg.as_string())
            print("감지 경보 이메일이 발송되었습니다.")
    except smtplib.SMTPException as e:
        print(f"이메일 발송 에러: {e}")

# 센서 데이터 처리
def monitor_smoke(cooldown_minutes=5):
    last_alert_time = None
    sensor_data = simulate_sensor_data()

    for smoke_level in sensor_data:
        print(f"Smoke Level: {smoke_level:.2f}")

        if smoke_level > 300:
            current_time = datetime.now()

            if last_alert_time is None or (current_time - last_alert_time) > timedelta(minutes=5):
                print("⚠️ 모니터링 중인 금연 구역에서 흡연이 감지되었습니다!")
                send_email_alert(current_time.strftime("%Y-%m-%d %H:%M:%S"))
                last_alert_time = current_time
            else:
                remaining_time = (timedelta(minutes=cooldown_minutes) - (current_time - last_alert_time)).total_seconds()
                print(f"경보 쿨다운 중... {int(remaining_time // 60)}분 {int(remaining_time % 60)}초 남음")
        else:
            print("경보가 없습니다.")

# 메인 실행
if __name__ == "__main__":
    print("흡연 감지 시스템 작동 중입니다.")
    monitor_smoke()