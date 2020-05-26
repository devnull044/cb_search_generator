#!/usr/bin/python3

#twit me @dev_nu1l
#git me @devnull044

import sys
import os
import validators
from art import *
import argparse
import re

tprint("Lazy CarbonBlack\nQuery Generator")
query = ''
q_tab = []
def parse_iocs(ioc):
	#check ioc and prepend appropriate tag
	#print(ioc)
	if ioc.strip()[0] == '-':
		if validators.ip_address.ipv4(ioc.strip()[1:len(ioc)]): #ip
			tmp = ioc.strip()[:1]+'ipaddr:'+ioc.strip()[1:]
			return tmp
		elif re.match(r'([a-fA-F\d]{32})', ioc.strip()[1:len(ioc)]): #md5
			tmp = ioc.strip()[:1]+'md5:'+ioc.strip()[1:]
			return tmp
	else:
		if validators.ip_address.ipv4(ioc.strip()): #ip
			tmp = 'ipaddr:'+ioc.strip()
			return tmp
		elif re.match(r'([a-fA-F\d]{32})', ioc.strip()): #md5
			tmp = 'md5:'+ioc.strip()
			return tmp


parser = argparse.ArgumentParser(description="""
	Easily create a CB search query using a list of IOCs.
	Ex. MD5, SHA256, Domain(s), IP(s), IP Ranges, etc.
""", formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument("-f","--filename",
					required=True,
					dest="ioc_file",
					action="store",
					help="the location of the file containing IOCs")
args = parser.parse_args()

ioc_list = []
try:
	with open(args.ioc_files, "r") as iocs:
		for each in iocs:
			ioc_list.append(each)
except (ValueError, FileNotFoundError, NameError) as e:
	print(e)

for ioc in ioc_list:
	if ioc != ioc_list[-1]:
		query += parse_iocs(ioc) + ' OR '
	else:
		query += parse_iocs(ioc)
print(query)



