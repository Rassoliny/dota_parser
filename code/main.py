import requests
import json
import time
import os

def fill_skins_for_withdrawal_list(skins_for_withdrawal):

	withdrawal_file = open('../data/withdrawal_list.txt', 'r')

	skins_for_withdrawal = []

	for lot in withdrawal_file:
		skins_for_withdrawal.append(lot)

	withdrawal_file.close()

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
				print('Noticed a change!')
				print(old)
				print(new,'\n')

		skins_old_list = skins_new_list


def withdrawal_parser(withdrawal_list):

	skins_old_json = requests.get('https://loot.farm/fullpriceDOTA.json')  
	skins_old_list = json.loads(skins_old_json.text)
	ignore_list = []
	ignore_names = []

	while True:

		skins_json = requests.get('https://loot.farm/fullpriceDOTA.json')
		skins_list = json.loads(skins_json.text)

		for skin in skins_list:

			if ((skin['name'] + '\n') in withdrawal_list) and \
			   ((skin['name'] + '\n') not in ignore_names) and \
				(skin['have'] != 0):

				print('Noticed a desired skin!\n')
				print(skin,'\n'*4)
				ignore_list.append({'name' : skin['name'], 'time' : 5})
				ignore_names.append(skin['name'] + '\n')
				
				os.system('say "Noticed a desired skin"')

		time.sleep(60)
		
		for skin in ignore_list:
			if skin['time']:
				skin['time'] -= 1
			else:
				ignore_list.remove(skin)
				ignore_names.remove(skin['name'] + '\n')

		print(time.ctime(time.time()))




withdrawal_list = []
withdrawal_list = fill_skins_for_withdrawal_list(withdrawal_list)
withdrawal_parser(withdrawal_list)



