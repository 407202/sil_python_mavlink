from dronekit import connect, VehicleMode, LocationGlobalRelative,APIException
import time
import socket
import APIException
import math
import argparse

/////////////////////////////////////

def connectMyCopter():
	parser = argparse.ArgumentParser(description='commands')
	parser.add_argument('--connect')
	args = parser.parse_args()

	connection_string = args.connect
	baud_rate = 921600

	vehicle = connect(connection_string,baud=baud_rate,wait_ready=True)
	return vehicle

def arm():
	while vehicle.is_armable==False:
		print("Waiting for vehicle to become armable..")
		time.sleep(1)
	print("Yoooooooo vehicle is now armable")
	print("")

	vehicle.armed=True
	while vehicle.armed==False:

		print("waiting for drone to become armed")
		time.sleep(1)

	print("Vehicle is now armed.")
	print("OMG props are spinning. Look out!!!!")

	return None		


vehicle = connectMyCopter()
arm()
print("End of..")
