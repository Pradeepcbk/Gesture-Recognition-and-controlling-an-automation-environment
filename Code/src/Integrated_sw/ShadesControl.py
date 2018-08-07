import subprocess
import os

def controlShades(gesture):
    if(gesture == 'UP'):
        os.startfile('startGPupSB1.sh')
        os.startfile('UpSB1.sh')
    elif (gesture == 'DOWN'):
        os.startfile('startGPdownSB1.sh')
        os.startfile('DownSB1.sh')