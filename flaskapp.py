from flask import Flask
from flask_socketio import SocketIO,emit, join_room, leave_room
import time

import threading
import os

app = Flask(__name__)

socketio = SocketIO(cors_allowed_origins='*')
socketio.init_app(app)



@socketio.on('join')
def y_join(data):
    value = data.get('room')
    join_room(value)
    emit('joined',{'msg':'start to process...'})

    exist=False
    fo = open("socketio_myroom.txt", "r")
    for a in fo.readlines():
        print(a.replace('\n',''),'--',value)
        if a.replace('\n','')==value:
            exist=True
    fo.close()
    if  exist==False:

        f = open("socketio_myroom.txt","a+")
        f.writelines(value+'\n')
        f.close()
        thread= socketio.start_background_task(robot,value)







def robot(r):
    while True:
        socketio.emit('room joined',{'msg':r},room=r)
        socketio.sleep(3)

@socketio.on('connect')
def connect():
    emit('response',{'code':'200','msg':'connected'})

if __name__ == '__main__':
    socketio.run(app,debug=True,host='0.0.0.0',port=5000)
