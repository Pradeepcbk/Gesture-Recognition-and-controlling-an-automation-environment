import os

os.chdir('/home/pradeep/Documents/Project_Smart_Lab/Gesture-Recognition-and-controlling-an-automation-environment-master/Code/src/Task1/Pradeep_down4')

# Am I in the correct directory?
os.getcwd()

for f,i in zip(os.listdir(os.getcwd()),range(272,350)):
	f_name, f_ext = os.path.splitext(f)
	f_title, f_num = f_name.split('_')
	new_name = '{}_{}{}'.format(f_title, i, f_ext)
	print(i)
	os.rename(f, new_name)
	#print(f_title + str(' ') + str(i)+f_ext)
