from flask import Flask, request, render_template
import datetime
import threading
from twilio.rest import Client

app = Flask(__name__)

alert_time = None
canceled = False
fake_password = "fake123"
real_password = "secret123"

account_sid = "AC03d85c4bbb0ce64c5dd43f426b2af355"
auth_token = "de0c80206ae5ddf716dc0ac3be1d43f2"
twilio_phone_number = "+15734946310"  # Your Twilio phone number
recipient_phone_number = "+55051991823420"  # Recipient's phone number

client = Client(account_sid, auth_token)


def send_distress_message():
    global canceled
    if not canceled:
        print("Sending distress message now!")
        message = client.messages.create(
            body="Distress alert! Help needed!",
            from_=twilio_phone_number,
            to=recipient_phone_number
        )
        print("Distress message sent:", message.sid)
    else:
        print("SMS alert system canceled.")


def activate():
    global alert_time
    alert_time = datetime.datetime.now() + datetime.timedelta(seconds=60)
    threading.Timer(60, send_distress_message).start()
    return "SMS alert system activated!"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/activate', methods=['POST'])
def activate_route():
    return activate()


@app.route('/cancel', methods=['POST'])
def cancel():
    global canceled
    if request.form.get('password') == real_password:
        canceled = True
        return "SMS alert system canceled!"
    elif request.form.get('password') == fake_password:
        return "Fake cancelation password accepted!"
    else:
        return "Invalid password!"


@app.route('/status', methods=['GET'])
def status():
    global alert_time, canceled
    if alert_time is None:
        return "SMS alert system not activated."
    elif canceled:
        return "SMS alert system canceled."
    else:
        time_left = alert_time - datetime.datetime.now()
        if time_left.total_seconds() <= 0:
            return "Sending distress message now!"
        else:
            return f"Time left until distress message: {time_left}"


if __name__ == '__main__':
    app.run()