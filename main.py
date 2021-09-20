#!/usr/bin/python3

import os
from script import *


def main_menu():
	print('1.Assign ip Address')
	print('2.Delete ip Address')
	print('3.Display ip Address')
	print('4.Display all interfaces')
	print('5.Configure Routing')
	print('6.Turn ON/OFF Interface')
	print('7.Add ARP entry')
	print('8.Delete ARP entry')
	print('9.Restart Network')
	print('10.Change hostname')
	print('11.Add DNS server entry')
	print('12.Exit')

while True:
	main_menu()
	ch = int(input('Enter choice : '))
	if ch == 1:
		ip_cmd()
	elif ch == 2:
		ip_cmd_del()
	elif ch == 3:
		ip_display()
	elif ch == 4:
		display_all_interface()
	elif ch == 5:
		configure_routing()
	elif ch == 6:
		on_off_interface()
	elif ch == 7:
		add_ARP_entry()
	elif ch == 8:
		del_ARP_entry()
	elif ch == 9:
		restart_network()
	elif ch == 10:
		change_host_name()
	elif ch == 11:
		add_DNS_server()
	elif ch == 12:
		break
	else:
		print("wrong choice")
		
