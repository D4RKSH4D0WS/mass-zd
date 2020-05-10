#Author D4RKSH4DOWS
G0 = "\033[0;32m"
G1 = "\033[1;32m"
C0 = "\033[0;36m"
C1 = "\033[1;36m"
P0 = "\033[0;35m"
P1 = "\033[1;35m"
W0 = "\033[0;37m"
W1 = "\033[1;37m"
B0 = "\033[0;34m"
B1 = "\033[1;34m"
R0 = "\033[0;31m"
R1 = "\033[1;31m"
Y1 = "\033[1;33m"
Y0 = "\033[0;33m"

import requests as r
import os,time,random,threading
from multiprocessing.dummy import Pool

os.system('clear')
print ('''
        [ Mass mirror zone-d ]
        [ Author D4RKSH4D0WS ]
''')
att=raw_input("\033[1;37m[\033[1;32m?\033[1;37m] \033[0;37mAttacker: ")
if att == '':
	exit('[!] Bye goblok')
def zd(sites):
	try:
		agent = r.get('https://pastebin.com/raw/ng1tPrfZ').text.split('\n')
		acak = random.choice(agent)
		site=r.post('https://zone-d.org/notify/action',headers={'cache-control': 'max-age=0','upgrade-insecure-requests': '1','save-data': 'on','user-agent': '{acak}','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3','referer': 'https://zone-d.org/notify','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data={'attacker':att,'poc':'social+engineering','url':sites}).text
		if 'Success' in site:
			print ('%s[ %sSuccess %s] %s'%(W0,G0,W0,sites))
		elif 'Already Defaced' in site:
			print ('%s[ %sAlready Defaced %s] %s'%(W0,R0,W0,sites))
		elif 'URL Not Defaced' in site:
			print ('%s[ %sNot Defaced %s] %s'%(W0,R0,W0,sites))
		else:
			print ('%s[ %sFailed %s] %s'%(W0,R0,W0,sites))
	except r.exceptions.ConnectionError:
		exit('[!] Koneksi internet tidak ada')

try:
	print ('%s[%s!%s] %sWeb harus pakai http atau https'%(W1,R1,W1,W0))
	sitelist=raw_input("\033[1;37m[\033[1;32m?\033[1;37m] \033[0;37mInput file: ")
	if sitelist == '':
		exit('[!] Bye goblok')
	sites = open(sitelist,"r").read().splitlines()
	pp = Pool(5) #gk usah di tambahin dah 5 aja !
	pr = pp.map(zd, sites)
except IOError:
	exit('[!] File tidak ada')
