#!/usr/bin/env python
# Python script that changes the MAC address

# calling modules

import subprocess
import optparse

# creating an object

parser = optparse.OptionParser()

parser.add_option("-i","--interface ",dest="Interface", help=("Interface to change its MAC Address"))
parser.add_option("-m","--MAC", dest="MAC", help=("New MAC Address"))
(options, arguments) = parser.parse_args()

# initializing a variable
Interface = input("Enter Interface > ")
MAC = input("Enter MAC address > ")

subprocess.call(["ifconfig", Interface, "down"])
subprocess.call(["ifconfig", Interface, "hw", "ether", MAC])
subprocess.call(["ifconfig", Interface, "hw", "ether", MAC])
subprocess.call(["ifconfig", Interface, "up"])

print("[+] Successfully changed MAC Address")