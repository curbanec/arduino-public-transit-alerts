#!/usr/bin/python

import serial
import webbrowser
import urllib
import time
import csv
from collections import Counter
import re
import sys


ser = serial.Serial("/dev/ttyACM2", 9600)
ser.write('1')# sends a number to the arduino(this is bytes, if arduino recieves bytes, light turns on)

#print ser
#Serial<id=0x7fe099176590, open=True>(port='/dev/ttyACM1', 
#	baudrate=9600, bytesize=8, parity='N', stopbits=1, 
#	timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)
#y=ser.readline()

#x=ser.read()# serial.read only returns a single byte by default
			# need to call it in a loop to see everything
#print y



# my lat 40.104364
# my lon -88.234171

# On my street, the busses travel north and south, this is why I am only concerned with the latitude 
#and longitude of my busses that I am tracking. I tracvk them to within one mile away, and a half mile away. 
# I would have tracked them to a quarter mile away, but the MTD API only updates every 1 minute, hence why I 
# made my program sleep for 1 minute. I found that information on thier website "https://developer.cumtd.com/".

def find_busses():
	busses_near_me=[]
	office_lat = 41.980262
	my_lat= 40.104364
	#my_lon= -88.234171

	#setting the coordinate range that will trigger the hardware
	my_lat_mile_positive= 40.118844
	my_lat_mile_negative= 40.089884

	my_lat_half_mile_positive= 40.111604
	my_lat_half_mile_negative= 40.097124
	

	from xml.etree.ElementTree import parse
	
	
	condition=True

	
	while condition == True:
		u = urllib.urlopen('https://developer.cumtd.com/api/v2.2/xml/GetVehiclesByRoute?key=1fc054a3aaec4cdfa6671c29dc5514d6&route_id=GREEN)'
		data = u.read()
		f = open('routes.xml', 'wb')
		
		f.write(data)
		f.close()
		print('Wrote routes.xml')
		doc = parse('routes.xml')

		# this is how you parse an XML tree
		for rsp in doc.findall('bus'):
			for vehicles:
				for vehicle:
					lat = float(bus.findtext('lat'))
					lon = float(bus.findtext('lon'))
					rounded_lat=("%.7f" % round(lat,7))# round off the lat for further analysis
					rounded_lon=("%.7f" % round(lon,7))# round off the lon for further analysis
					
					busid = bus.findtext('vehicle_id')
					direction = bus.findtext('direction')
					if direction.startswith('North') or direction.startswith('South'):
						busses_near_me.append(vehicle_id)
						busses_near_me.append(lat)
						busses_near_me.append(direction)
				
						


						if lat>= 40.089884 and lat<= 40.111604:
							print"This bus id:"+ busid+" is within 1 mile "
							ser.write('1')


							if lat>= 40.097124 and lat<= 40.118844:
								print"This bus id:"+ busid+" is within a half mile "

								ser.write('15')############################################
						
						
								googlemaps_url="https://maps.google.com/maps?q={0}N+40.668452W+(catch that bus!)&ll={1},-88.668452&spn=0.004250,0.011579&t=h&iwloc=A&hl=en".format(rounded_lat,rounded_lat)
						
								webbrowser.open(googlemaps_url)
								
								condition = False

										
			print busses_above_the_latitude	
			print"######################################################################"			
			time.sleep(60)


# create a command line tool to initiate the program, when I want to it to start looking for a bus to catch on campus
	
if __name__ == '__main__': 
	
	
	args = str(sys.argv)
	if "find_busses" in args:
		find_busses()



'''
usefull queries that I wrote to help understand how the API works and what data I can use
https://developer.cumtd.com/api/v2.2/json/GetTripsByBlock?block_id=4&key=1fc054a3aaec4cdfa6671c29dc5514d6

http://developer.cumtd.com/api/v2.2/json/GetDeparturesByStop?key=1fc054a3aaec4cdfa6671c29dc5514d6&stop_id=PLAZA&pt=60
https://developer.cumtd.com/api/v2.2/json/GetVehiclesByRoute?key=1fc054a3aaec4cdfa6671c29dc5514d6&route_id=GREEN
route_id="teal"&key=1fc054a3aaec4cdfa6671c29dc5514d6
http://developer.cumtd.com/api/v2.2/json/GetReroutes?key=1fc054a3aaec4cdfa6671c29dc5514d6
http://developer.cumtd.com/api/v2.2/json/GetVehicles?key=1fc054a3aaec4cdfa6671c29dc5514d6&vehicle_id="1166"
https://developer.cumtd.com/api/v2.2/json/GetRoute?key=1fc054a3aaec4cdfa6671c29dc5514d6&route_id=GREEN
http://www.linuxuser.co.uk/tutorials/arduino-programming-guide-part-1
'''