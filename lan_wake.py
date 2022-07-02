import time
import os
#Pinging phone ip address to see if it's connected
#saving output to file to then read and check if it's alive
def wake_lan():
	while True:
		os.system("ping -c 1 " + phone_address + " > file")
		with open("file", "r") as file:
			reading = file.read()
		if "64 bytes from " + phone_address +": icmp_seq=" in reading:
			print('Phone is nearby.....TURNING PC ON...')
			os.system("wakeonlan " + pc_mac)
			reset()
		else:
			print("No one is home :(")
			time.sleep(60)

#Pinging pc to see if it's alive and if not then repeat until it's down and then go to wake_lan()
#saving output as in wake_lan()
def reset():
	while True:
		os.system("ping -c 1 " + pc_address + " > file")
		with open("file", "r") as file:
			reading = f.read()
		if "64 bytes from " + pc_address + ": icmp_seq=" in reading:
			print("PC is online")
			time.sleep(60)
		elif "Destination Host Unreachable" in reading:
			print("PC is offline, reseting and activating wake on lan...")
			wake_lan()

#Checks if file2 exists and if not it will ask you for ip's and mac address
if os.path.isfile('file2'):
	print ("File exist")
	with open("file2") as file:
		info = f.readlines()
	pc_address = info[0]
	phone_address = info[1]
	pc_mac = info[2]
else:
	pc_address = input("Enter your pc's ip address: ")
	phone_address = input("Enter phone's ip address: ")
	pc_mac = input("Enter your pc's mac address: ")
	with open("file2", "w") as file:
		file.write(pc_address + "\n" + phone_address + "\n" + pc_mac)
wake_lan()