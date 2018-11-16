import os
import subprocess

def control(gesture,meanArray):
    dataX = meanArray[0]
    dataY = meanArray[1]
    button = meanArray[2]

    if(dataX <= 3.8):
        if(gesture == 'UP'):
            if(button == 'True'):
                if(dataY >= 3.5 and dataY <= 7.0):
                    os.startfile('startGPupSc3.sh')
                    os.startfile('UpSc3.sh')
                else:
                    os.startfile('startGPupSc1.sh')
                    os.startfile('UpSc1.sh')
            else:
                os.startfile('startGPupSB1.sh')
                os.startfile('UpSB1.sh')
                os.startfile('startGPupSB2.sh')
                os.startfile('UpSB2.sh')

        if(gesture == 'DOWN'):
            if (button == 'True'):
                if (dataY >= 3.5 and dataY <= 7.0):
                    os.startfile('startGPdownSc3.sh')
                    os.startfile('DownSc3.sh')
                else:
                    os.startfile('startGPdownSc1.sh')
                    os.startfile('DownSc1.sh')
            else:
                os.startfile('startGPdownSB1.sh')
                os.startfile('DownSB1.sh')
                os.startfile('startGPdownSB2.sh')
                os.startfile('DownSB2.sh')

    if(dataX >= 3.81 and dataX <= 6.08):
        if (gesture == 'UP'):
            os.startfile('startGPupSB3.sh')
            os.startfile('UpSB3.sh')
            os.startfile('startGPupSB4.sh')
            os.startfile('UpSB4.sh')
        if (gesture == 'DOWN'):
            os.startfile('startGPdownSB3.sh')
            os.startfile('DownSB3.sh')
            os.startfile('startGPupSB4.sh')
            os.startfile('DownSB4.sh')


    if (dataX >= 6.09):
        if (gesture == 'UP'):
            if (button == 'True'):
                if (dataY >= 3.5 and dataY <= 7.0):
                    os.startfile('startGPupSc7.sh')
                    os.startfile('UpSc7.sh')
                else:
                    os.startfile('startGPupSc9.sh')
                    os.startfile('UpSc9.sh')
            else:
                os.startfile('startGPupSB5.sh')
                os.startfile('UpSB5.sh')
                os.startfile('startGPupSB6.sh')
                os.startfile('UpSB6.sh')

        if (gesture == 'DOWN'):
            if (button == 'True'):
                if (dataY >= 3.5 and dataY <= 7.0):
                    os.startfile('startGPDownSc7.sh')
                    os.startfile('DownSc7.sh')
                else:
                    os.startfile('startGPDownSc9.sh')
                    os.startfile('DownSc9.sh')
            else:
                os.startfile('startGPdownSB5.sh')
                os.startfile('DownSB5.sh')
                os.startfile('startGPdownSB6.sh')
                os.startfile('DownSB6.sh')



