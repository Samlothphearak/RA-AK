import os

shutdown = input("Do you want to Shutdown your pc ? (yes / no): ")

if shutdown == 'yes':
	exit()
else:
	os.system("shutdown /s /t 1")
n