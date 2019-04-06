import requests
import json
import time

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

