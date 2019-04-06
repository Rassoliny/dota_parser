import requests
import json
import time

def fill_skins_for_withrawal_list(skins_for_withdrawal):

	withrawal_file = open('../data/withdrawal_list.txt', 'r')

	skins_for_withrawal = []

	for lot in withrawal_file:
		skins_for_withrawal.append(lot)

	withrawal_file.close()

	return skins_for_withrawal


def change_parser():

	skins_old_json = requests.get('https://loot.farm/fullpriceDOTA.json')  
	skins_old_list = json.loads(skins_old_json.content)

	while True:
		
		time.sleep(60)

		skins_new_json = requests.get('https://loot.farm/fullpriceDOTA.json')
		skins_new_list = json.loads(skins_new_json.content)

		for old, new in zip(skins_old_list, skins_new_list):
			if old != new:
				print('Noticed a change!')
				print(old)
				print(new,'\n')

		skins_old_list = skins_new_list

def withrawal_parser(withrawal_list):

	skins_old_json = requests.get('https://loot.farm/fullpriceDOTA.json')  
	skins_old_list = json.loads(skins_old_json.content)

	while True:

		skins_json = requests.get('https://loot.farm/fullpriceDOTA.json')
		skins_list = json.loads(skins_json.content)

		for skin in skins_list:
			if (skin['name'] in withrawal_list) and (skin['have'] != 0):
				print('Noticed a desired skin!')
				print(skin,'\n')
				
		time.sleep(60)




withrawal_list = []
withrawal_list = fill_skins_for_withrawal_list(withrawal_list)
withrawal_parser(withrawal_list)



