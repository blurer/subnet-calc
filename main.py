#!/usr/bin/env python3

import netaddr
import ipaddress
import subprocess
from subprocess import call
import os

# define clear function
def clear():
	# check and make call for specific operating system
	_ = call('clear' if os.name =='posix' else 'cls')
	
clear()
print("#"*45)
print("                  Subnet Calc")
print("#"*45)
print("1: Is host valid in subnet?")
print("2: Hosts in subnet")

print("#"*45)
choice = input("Select Number (q to quit) ")

while choice != 'q':
	if choice == '0':
		clear()
		print("#"*45)
		print("    ")
		print("#"*45)
		choice = input("Select Number (q to quit) ")
	if choice == '1':
		clear()
		print("#"*45)
		print('Is host a valid IP address within subnt A?')
		host = input('Host: ')
		subnet_a = input('Subnet A: ')
		print(ipaddress.IPv4Address(host) in ipaddress.IPv4Network(subnet_a))
		print("#"*45)
	elif choice == '2':
		clear()
		print("#"*45)
		subnet = input("Subnet/Mask: ")
		print('------------------------------')
		for x in (ipaddress.IPv4Network(subnet).hosts()):
			print(x)
		print("#"*45)
	else:
		clear()
		print("#"*45)
		print("That is not a valid input.")
		print("#"*45)
	choice = input("Press q to quit, 0 for menu) ")