#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 

"""
import os
import re
import json
import requests
import csv

base_dir = os.environ['HOME']+'/vinaya-comparison/vinaya/'
base_file = 'pli-tv-bi-pm'
output_csv_file = os.environ['HOME']+'/vinaya-comparison/vinaya_output/'+base_file+'.csv'

sortorder=['pli-tv-bi','pli-tv-bu','pli-tv-kd','lzh-mg-bi','lzh-mg-bu','san-mg-bi','san-mg-bu','san-lo-bi','san-lo-bu','lzh-mi-bi','lzh-mi-bu','lzh-dg-bi','lzh-dg-bu','pgd-dg-bi','pgd-dg-bu','lzh-sarv-bi','lzh-sarv-bu','san-sarv-bi','san-sarv-bu','san-sarv-sm','lzh-mu-bi','lzh-mu-bu','san-mu-bi','san-mu-bu','san-mu-kd','xct-mu-bi','xct-mu-bu','lzh-ka-bu','lzh-upp-bu','san-bu-pm','pgd-pm-bf13']

filelist = json.loads(open(base_dir+base_file+'-tree.json', 'r', encoding='utf8').read())

CsvOut = open(output_csv_file, 'w', newline='')
parallelwriter = csv.writer(CsvOut, delimiter=',')
parallelwriter.writerow(['Theravāda','Theravāda','Theravāda','Mahāsaṁghika','Mahāsaṁghika','Mahāsaṁghika','Mahāsaṁghika','Lokuttaravāda','Lokuttaravāda','Mahīśāsaka','Mahīśāsaka','Dharmaguptaka','Dharmaguptaka','Dharmaguptaka','Dharmaguptaka','Sarvāstivāda','Sarvāstivāda','Sarvāstivāda','Sarvāstivāda','Sarvāstivāda','Mūlasarvāstivāda','Mūlasarvāstivāda','Mūlasarvāstivāda','Mūlasarvāstivāda','Mūlasarvāstivāda','Mūlasarvāstivāda','Mūlasarvāstivāda','Kāśyapīya','Upāliparipṛcchā','Qizil','Bhikkhu Pātimokkha (unknown school)'])
parallelwriter.writerow(['Pali','Pali','Pali','Chinese','Chinese','Sanskrit','Sanskrit','Sanskrit','Sanskrit','Chinese','Chinese','Chinese','Chinese','Prakrit','Prakrit','Chinese','Chinese','Sanskrit','Sanskrit','Sanskrit','Chinese','Chinese','Sanskrit','Sanskrit','Sanskrit','Tibetan','Tibetan','Chinese','Sanskrit','Sanskrit','Prakrit'])
parallelwriter.writerow(['Bhikkhunī','Bhikkhu','Kandhaka','Bhikkhunī','Bhikkhu','Bhikkhunī','Bhikkhu','Bhikkhunī','Bhikkhu','Bhikkhunī','Bhikkhu','Bhikkhunī','Bhikkhu','Bhikkhunī','Bhikkhu','Bhikkhunī','Bhikkhu','Bhikkhunī','Bhikkhu','Śikṣamānā','Bhikkhunī','Bhikkhu','Bhikkhunī','Bhikkhu','Kandhaka','Bhikkhunī','Bhikkhu','Bhikkhu','Bhikkhu','Bhikkhu','Bhikkhu'])
parallelwriter.writerow(sortorder)
parallelwriter.writerow(['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''])
temp_list = []

def sortlist(parallelentrylist):
	newlist = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
	parallelcount = -1
	for item in parallelentrylist:
		if item.startswith('san-mu-mpt-bu'):
			sortcode = 'san-mu-bu'
		elif item.startswith('pli-tv-kd'):
			sortcode = 'pli-tv-kd'
		elif item.startswith('san-sarv-sm'):
			sortcode = 'san-sarv-sm'
		else:
			sortcode = "-".join(item.split("-", 3)[:3])

		if sortcode not in sortorder:
			print(item)
		else:
			if item.startswith('san-mu-mpt-bu'):
				parallelcode = re.sub('san-mu-mpt-bu-pm','pm-mpt',item)
			else:
				parallelcode = re.sub(sortcode,'',item).strip('-')
			if newlist[sortorder.index(sortcode)]:
				newlist[sortorder.index(sortcode)] += "; "+parallelcode
			else:
				newlist[sortorder.index(sortcode)] = parallelcode
				parallelcount += 1

	newlist[-1] = parallelcount

	return(newlist)

for categories in filelist[base_file]:
	for category in categories.values():
		for file in category:
			# print("https://suttacentral.net/api/parallels/"+file)
			response = requests.get("https://suttacentral.net/api/parallels/"+file)
			parallellist = response.json()[file]
			parallelentrylist = [file]
			for parallel in parallellist:
				if '-' in parallel['to']['to'] and not parallel['resembling']:
					parallelentrylist.append(parallel['to']['to'])
				elif '-' in parallel['to']['to'] and parallel['resembling']:
					parallelentrylist.append(parallel['to']['to']+'~')
			
			parallelwriter.writerow(sortlist(parallelentrylist))

CsvOut.close()


