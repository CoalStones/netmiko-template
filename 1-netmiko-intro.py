#!/usr/bin/python3

from netmiko import ConnectHandler
from getpass import getpass # used for password input as to not store the password in plain text
from getpass import getuser # used to get the username of the current user

# 1. create a device dictionary to store all the device information
# 2. create a netmiko_device object from netmiko ConnectHandler
if __name__ == "__main__":
    # Define the device to connect to
    # keys matter how they are spelled
    device_dict = {
        "device_type": "cisco_ios",
        "host": "cisco3.last",
        "username": getuser(),
        "password": getpass()
    }

    netmiko_device = ConnectHandler(**device_dict)
    # print(netmiko_device.find_prompt())
    # print(netmiko_device.send_command("show version | include Version"))
    # print(dir(netmiko_device))
    netmiko_device.disconnect()