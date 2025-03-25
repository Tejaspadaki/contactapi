from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend requests

# Email configuration
SMTP_SERVER = "smtp.gmail.com"  # Change if using a different email provider
SMTP_PORT = 587
EMAIL_ADDRESS = "heartcare726@gmail.com"  # Change to your email
EMAIL_PASSWORD = "afqt mccn osem hzaj"  # Use App Password if using Gmail

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        data = request.json
        name = data.get("name")
        email = data.get("email")
        message = data.get("message")

        # Construct email
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = "heartcare726@gmail.com"  # Change to recipient email
        msg["Subject"] = "New Contact Form Submission"

        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        msg.attach(MIMEText(body, "plain"))

        # Send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, "heartcare726@gmail.com", msg.as_string())

        return jsonify({"message": "Email sent successfully!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

