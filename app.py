from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

from twilio.twiml.messaging_response import MessagingResponse
import model

app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO( app )

@app.route( '/', methods=['GET','POST'])
def hello():
  return render_template( './Unibot.html' )

def messageRecived():
  print( 'message was received!!!' )


@socketio.on( 'my eventes' )
def handle_my_custom_event1( json1 ):
  
  message = json1['message']
  answer=model.chat(message)
  json1['answer'] = answer
  json1['bot']='UniBot'
  print( 'recived my event: ' + str(json1 ))
  socketio.emit( 'my response', json1, callback=messageRecived )
  


@app.route("/sms", methods=['POST'])
def sms():
 
    # Fetch the message
    resp = MessagingResponse()
    incoming_msg = request.values.get('Body')
	  #message = json1['message']
	  
    answer=model.chat(incoming_msg)
	  
    resp.message(answer)

    return str(resp)

if __name__ == '__main__':
  socketio.run( app, debug = True, use_reloader=False )
