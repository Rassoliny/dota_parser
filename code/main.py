import requests
import json
import time

def fill_skins_for_withdrawal_list(skins_for_withdrawal):

	withrawal_file = open('../data/withdrawal_list.txt', 'r')
	for lot in withrawal_file:
		skins_for_withdrawal.append(lot)

	return skins_for_withdrawal


def change_parser():

	skins_old_json = requests.get('https://loot.farm/fullpriceDOTA.json')  
	skins_old_list = json.loads(skins_old_json.content)

	while True:
		
		time.sleep(60)

		skins_new_json = requests.get('https://loot.farm/fullpriceDOTA.json')
		skins_new_list = json.loads(skins_new_json.content)

		for old, new in zip(skins_old_list, skins_new_list):
			if old != new:
				print('ЗАМЕЧЕНО ИЗМЕНЕНИЕ')
				print(old)
				print(new)
				print()

		skins_old_list = skins_new_list

withdrawal_list = []
withdrawal_list = fill_skins_for_withdrawal_list(withdrawal_list)



