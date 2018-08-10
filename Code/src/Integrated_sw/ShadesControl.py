import subprocess
import os

def controlShades(gesture):
    if(gesture == 'UP'):
        #os.startfile('startGPupSB1.sh')
	subprocess.call(['./startGPupSB1.sh'])
        #os.startfile('UpSB1.sh')
	subprocess.call(['./UpSB1.sh'])
    elif (gesture == 'DOWN'):
        #os.startfile('startGPdownSB1.sh')
	subprocess.call(['./startGPdownSB1.sh'])
	subprocess.call(['./DownSB1.sh'])
