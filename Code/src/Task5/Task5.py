import subprocess

def controlShades(gesture):
    if(gesture == 'UP'):
        subprocess.call('./startGPupSB1.sh')
        subprocess.call('./UpSB1.sh')
    elif (gesture == 'DOWN'):
        subprocess.call('./startGPdownSB1.sh')
        subprocess.call('./DownSB1.sh')