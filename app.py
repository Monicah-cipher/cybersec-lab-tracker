from flask import Flask, render_template, request, redirect, url_for
from models import db, Incident 

app = Flask(__name__)

# --- FROM YOUR ORIGINAL CODE ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cyber_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    # As seen in image_90b305.png
    incidents = Incident.query.order_by(Incident.date_posted.desc()).all()
    # We add 'count' to update your dashboard card in image_90a8b9.png
    return render_template('index.html', incidents=incidents, count=len(incidents))

# --- NEW ROUTES FOR YOUR FORM ---

@app.route('/log')
def log_page():
    # Renders the "Log New Security Incident" HTML you shared
    return render_template('log_incident.html')

@app.route('/report', methods=['POST'])
def report_incident():
    # This catches the data sent by your form action="/report"
    new_incident = Incident(
        title=request.form.get('title'),
        severity=request.form.get('severity'),
        content=request.form.get('description') # Matches name="description" in HTML
    )
    db.session.add(new_incident)
    db.session.commit()
    
    # Redirect back home to see the new incident in the dashboard
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)