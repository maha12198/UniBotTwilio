from flask import Flask, render_template, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/sms", methods=['POST'])
def sms():
	resp = MessagingResponse()
	incoming_msg = request.values.get('Body')
	import model      
	answer=model.chat(incoming_msg)  
	resp.message(answer)
	return str(resp)


if __name__ == '__main__':
   app.run()
