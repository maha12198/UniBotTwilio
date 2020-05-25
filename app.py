from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import model

app = Flask(__name__)

@app.route("/", methods=['POST'])
def sms():
    incoming_msg = request.values.get('Body')
    resp = MessagingResponse()
    answer=model.chat(incoming_msg)
    resp.message(answer)
    return str(resp)

if __name__ == '__main__':
    app.run()
