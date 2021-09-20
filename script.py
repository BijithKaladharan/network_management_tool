import os


def ip_cmd():
    
    ip = input('Enter ip address to add on interface : ')
    if len(ip.split('.')) == 4:
        s = os.popen(
            'ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read()
        interfaces = s.split('\n')[:-2:2]
        print(interfaces)
        interface_choice = input("choose a interface: ")
        command = f'ip address add {ip} dev {interface_choice}'
        res = os.popen(command).read()
        print(res)
        print('Ip address assigned successfully')


def ip_cmd_del():
    # Delete Ip address
    ip = input('Enter ip address to delete from interface : ')
    if len(ip.split('.')) == 4:
        s = os.popen(
            'ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read()
        interfaces = s.split('\n')[:-2:2]
        print(interfaces)
        interface_choice = input("choose a interface: ")
        command = f'sudo ip address del {ip} dev {interface_choice}'
        res = os.popen(command).read()
        print(res)
        print('Ip address Deleted successfully')


def ip_display():
    # show ip address of all interfaces
    command = f'ip -c -br address'
    res = os.popen(command).read()
    print(res)


def display_all_interface():
    s = os.popen(
        'ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read()
    interfaces = s.split('\n')[:-2:2]
    command = 'ip l'
    res = os.popen(command).read()
    print(
        f'All interfaces name  => {interfaces}  Details => {res}')


def configure_routing():
    network_addr = input('Enter network Address with /mask : ')
    getway_ip = input('Enter Gateway ip address : ')
    if len(network_addr.split('.')) == 4 and len(getway_ip.split('.')) == 4:
        cmd = f'ip r add {network_addr} via {getway_ip}'
        res = os.popen(cmd).read()
        print(res,)
        print('Roting configuration completed !')


def on_off_interface():
    print('1.Turned off interface ')
    print('2.Turned on interface')
    choice = int(input("Enter your choice: "))

    s = os.popen(
        'ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read()
    interfaces = s.split('\n')[:-2:2]
    print(interfaces)
    interface_choice = input("choose a interface")

    if choice == 1:

        cmd = f'ip link set dev {interface_choice}  down'
        res = os.popen(cmd).read()
        
        print(
            f'{interface_choice} turned off ')

    elif choice == 2:
        cmd = f'ip link set dev {interface_choice}  up'
        res = os.popen(cmd).read()
        print(
            f'{interface_choice} turned on ')

    else:
        print('Wrong option choosed')


def add_ARP_entry():
    ip = input('Enter ip address  : ')
    if len(ip.split('.')) == 4:
        s = os.popen(
            'ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read()
        interfaces = s.split('\n')[:-2:2]
        print(interfaces)
        interface_choice = input("choose a interface")
        arp_cache = os.popen('ip n show | cut -d " " -f5').read()
        cmd = f'ip n add {ip} lladdr {arp_cache} dev {interface_choice} nud permanent'
        res = os.popen(cmd).read()
        print('ARP Entry added successfully ')


def del_arp_entry():
    ip = input('Enter ip address : ')
    if len(ip.split('.')) == 4:
        s = os.popen(
            'ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read()
        interfaces = s.split('\n')[:-2:2]
        print(interfaces)
        interface_choice = input("choose a interface")
        cmd = f'ip n del {ip} dev {interface_choice}'
        res = os.popen(cmd).read()
        print('ARP Entry deleted successfully ')


def restart_network():
    cmd = 'sudo systemctl restart networking'
    cmd2 = 'sudo systemctl status networking'
    os.popen(cmd).read()
    print('Network services restarted ')
    print(os.popen(cmd2).read())


def change_host_name():
    host_name = input("Enter new host name :")
    cmd = f'hostnamectl set-hostname {host_name}'
    os.popen(cmd).read()
    print(
        f'new host name {host_name} set successfully ')


def add_DNS_server():

    print('adding dns server')
    print('first : nameserver 8.8.8.8 write in this format')
    print('second : ctrl + d  to exit ')
    cmd = 'sudo cat  >> /etc/resolv.conf'
    print(os.popen(cmd).read())
    print('Nameserver added successfully  ')
