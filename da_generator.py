#!/usr/bin/python3

#twit me @dev_nu1l
#git me @devnull044

import sys
import os
import validators
from art import *
import argparse

tprint("Lazy CarbonBlack\nQuery Generator")
query = ''
def parse_iocs(ioc):
	#check ioc and prepend appropriate tag
	if validators.ipv4(ioc.strip):
		query += ' ',ioc
parser = argparse.ArgumentParser(description="""
	Easily create a CB search query using a list of IOCs.
	Ex. MD5, SHA256, Domain(s), IP(s), IP Ranges, etc.
""", formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument("-f","--filename",
					required=True,
					dest="ioc_files",
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




