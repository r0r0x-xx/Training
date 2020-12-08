#!/usr/bin/env python3
print ("# #########################################")
print ("#  Fuzz TRUN instruction | Vulnserver   ####")
print ("#     PWNEDCR \x03  | Exploit Dev      ####")
print ("#           Exploit By r0r0x_xxx       ####")
print ("#           Date: 5-12-2020 	       ####")
print ("#       Simple Buffer Overflow   	   ####")
print ("###########################################")

#Banner

print (" _    _                         _    _            _    _             ")
print ("| |  | |                       | |  | |          | |  (_)            ")
print ("| |__| | __ _ _ __  _ __  _   _| |__| | __ _  ___| | ___ _ __   __ _ ")
print ("|  __  |/ _` | '_ \| '_ \| | | |  __  |/ _` |/ __| |/ / | '_ \ / _` |")
print ("| |  | | (_| | |_) | |_) | |_| | |  | | (_| | (__|   <| | | | | (_| |")
print ("|_|  |_|\__,_| .__/| .__/ \__, |_|  |_|\__,_|\___|_|\_\_|_| |_|\__, |")
print ("             | |   | |     __/ |                                __/ |")
print ("             |_|   |_|    |___/                                |___/ ")

from boofuzz import *
import time 


def get_banner (target, my_logger, session, *args, **kwargs):
	banner_template= b"Welcome to Vulnerable Server! Enter HELP for help."
	try: 
		banner = target.recv(10000)	
	except:
		print ("Unable to Connect, the target is down. Check this")	
		exit(1)

	my_logger.log_check("Receiving Banner...")
	if banner_template in banner:
		my_logger.log_pass("Banner recieved")
	else:
		my_logger.log_fail("No banner recieved")
		print ("No banner recieved, exiting")
		exit(1)

#Socket

def main():

	session = Session (
		sleep_time = 1, # Seconds
		target = Target(
			connection = SocketConnection ("10.0.2.5", 9999, proto = 'tcp')
		),
	)

#Setup

	s_initialize(name="Request")
	with s_block("Host_Line"):
		s_static("TRUN", name='command name')
		s_delim(" ")
		s_string("FUZZ", name = 'trun varialble contect')
		s_delim("\r\n")




#Fuzzing 

	session.connect(s_get("Request"), callback= get_banner)
	session.fuzz()

if __name__ == "__main__":
	main()	




