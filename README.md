# 🚭Smoke Detector🚭

This project is a **Smoke Detection System** designed to monitor smoking areas, particularly in places where it is difficult to directly detect smoking through CCTV. In areas such as public restrooms, stairwells, or secluded corners, traditional surveillance systems may not be effective at identifying smokers. This system addresses that gap by using sensors to detect smoke and sending an immediate alert via email when smoking is detected.

## Features

- **Smoke Detection**: Continuously monitors smoke levels in a designated area.
- **Email Alerts**: Sends an email alert if smoke levels exceed a predefined threshold using the `smtplib` and `email.mime.text` libraries.
- **Cooldown Timer**: Prevents multiple alerts from being sent within a short time frame to avoid spamming.
- **Simulated Sensor Data**: Can be used without physical sensors by generating random smoke data.

## Requirements

- **Hardware**:
  - Raspberry
  - Smoke sensor (e.g., MQ-2 or similar)
  - Internet connection for sending email alerts
 
- **Software**:
  - Python 3.x
  - `smtplib` (for sending email alerts)
  - `email.mime.text` (for composing the email body)
  - `random` (for simulated sensor data)
  - `time` (for controlling the timing of data collection)
  - `datetime` (for time-stamping events)
 
[Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/)
## Installation

  - Clone the repository:
   ```bash
   git clone https://github.com/UnjenN/smokedetector.git
   cd smokedetector
   ```

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python Version](https://img.shields.io/badge/python-3.x-blue)
