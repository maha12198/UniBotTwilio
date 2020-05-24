from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import model

app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def sms():
    print('hh-') 
    incoming_msg = request.values.get('Body')
    print('a-') 
    resp = MessagingResponse()  
    print('b-') 
    answer=model.chat(incoming_msg)
    print('c-')  
    msg=resp.message()
    msg.Body(answer)
    print('d-') 
    return str(resp)

if __name__ == '__main__':
    app.run()
