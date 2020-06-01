# WORK IN PROGRESS

I got tired of copying and pasting so I started writing a script

# Install
```
git clone https://github.com/devnull044/cb_search_generator.git
pip3 install -r requirements.txt
```
# Usage

```
 _                           ____               _                    ____   _               _    
| |      __ _  ____ _   _   / ___|  __ _  _ __ | |__    ___   _ __  | __ ) | |  __ _   ___ | | __
| |     / _` ||_  /| | | | | |     / _` || '__|| '_ \  / _ \ | '_ \ |  _ \ | | / _` | / __|| |/ /
| |___ | (_| | / / | |_| | | |___ | (_| || |   | |_) || (_) || | | || |_) || || (_| || (__ |   < 
|_____| \__,_|/___| \__, |  \____| \__,_||_|   |_.__/  \___/ |_| |_||____/ |_| \__,_| \___||_|\_\
                    |___/                                                                        
  ___                               ____                                  _                
 / _ \  _   _   ___  _ __  _   _   / ___|  ___  _ __    ___  _ __   __ _ | |_   ___   _ __ 
| | | || | | | / _ \| '__|| | | | | |  _  / _ \| '_ \  / _ \| '__| / _` || __| / _ \ | '__|
| |_| || |_| ||  __/| |   | |_| | | |_| ||  __/| | | ||  __/| |   | (_| || |_ | (_) || |   
 \__\_\ \__,_| \___||_|    \__, |  \____| \___||_| |_| \___||_|    \__,_| \__| \___/ |_|   
                           |___/                                                           

usage: da_generator.py [-h] -f IOC_FILE

	Easily create a CB search query using a list of IOCs.
	Ex. MD5, SHA256, Domain(s), IP(s), IP Ranges, etc.

optional arguments:
  -h, --help            show this help message and exit
  -f IOC_FILE, --filename IOC_FILE
                        the location of the file containing IOCs
```
## File Formart Example
```
8.8.8.8
-0e881e89ceab86856170e645369f20d3be37c0912ca74e35895dc36ff9af8f77
c65aeca861b188beaca0b161c5081a0c
google.com
```
