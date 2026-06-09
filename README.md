# ⚡ CyberSec Lab Tracker

A full-stack Flask web application engineered as a local command center to log, track, and monitor cybersecurity laboratory training milestones, penetration testing targets, and active security research notes.

## 🚀 Key Features

* **Dynamic Operations Dashboard:** Real-time metrics visualizing overall targets, completed engagements, and active focus operations.
* **Granular Lab Logging:** Track lab instances with descriptive parameters including Platform (TryHackMe, Hack The Box, PortSwigger, etc.), Category (e.g., Privilege Escalation, Web Exploitation, Network Security), Target Name, and Live Status.
* **Terminal Logs & Payload Archiving:** Interactive modal popups to instantly view customized terminal histories, successful exploit scripts, or proof-of-concept steps.
* **Document & Image Management:** Secure attachment framework allowing late-stage file and report uploads to individual lab entries.

## 🛠️ Technical Stack

* **Backend Framework:** Python, Flask
* **Database & ORM:** SQLite, Flask-SQLAlchemy
* **Frontend Design:** HTML5, Bootstrap 5 (Dark Terminal Theme), Jinja2 Templating Engine
* **Version Control:** Git & GitHub

## 🔧 Local Installation & Setup

Follow these steps to spin up the tracker environment locally:

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/Monicah-cipher/cybersec-lab-tracker.git](https://github.com/Monicah-cipher/cybersec-lab-tracker.git)
   cd cybersec-lab-tracker
Initialize the Virtual Environment:

Bash
python3 -m venv venv
source venv/bin/activate
Install Dependencies:

Bash
pip install flask flask_sqlalchemy Werkzeug
Launch the Application:

Bash
python3 app.py
Open your browser and navigate to http://127.0.0.1:5000 to access the dashboard.
