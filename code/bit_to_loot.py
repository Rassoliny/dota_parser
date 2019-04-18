import requests
import json
import pyotp
from constants import SECRET, API_KEY

class Skin(object):

    def __init__(self, skin):

        if len(skin) == 5:                          # => loot.farm skin

            self.name = skin['name']
            self.loot_price = skin['price']
            self.bit_price = 'None'
            self.on_loot = skin['have']
            self.on_bit = 'None'
            self.max_loot = skin['max']

        else:                                       # => bitskins skin

            self.name = skin['market_hash_name']
            self.loot_price = 'None'
            self.bit_price = int(float(skin['lowest_price']) * 100)
            self.on_loot = 'None'
            self.on_bit = skin['total_items']
            self.max_loot = 'None'

    def profit_bit_to_loot(self):
        
        if self.loot_price != 'None' and self.bit_price != 'None':
            profit = ((self.loot_price * 0.97) - self.bit_price) / (self.loot_price * 0.97)
            return profit
        else:
            return 1


def get_totp():

    totp = pyotp.TOTP(SECRET)
    code = str(totp.now())

    return code


def get_lootfarm_list():

    MIN_PRICE = 2000

    lootfarm_list = []

    skins_json = requests.get('https://loot.farm/fullpriceDOTA.json')
    skins_list = json.loads(skins_json.text)

    lootfarm_data = open('../data/lootfarm_data.txt', 'w')
    lootfarm_names = open('../data/lootfarm_names.txt', 'w')

    skins_loot_info_list = []

    for skin in skins_list:

        skin = Skin(skin)

        # Фильтр ненужных скинов
        if (skin.on_loot >= skin.max_loot) or (skin.loot_price <= MIN_PRICE):
            continue

        lootfarm_names.write(skin.name + '\n')

        lootfarm_list.append(skin)

        # Заполнение списка нужных скинов
        name = skin.name
        price = str(skin.loot_price)
        bots_have = str(skin.on_loot)
        bots_can_have = str(skin.max_loot)
        skin_loot_info = {'name': name, 'price': price, 'have': bots_have, 'max': bots_can_have}
        skins_loot_info_list.append(skin_loot_info)

    lootfarm_list = sorted(lootfarm_list, key=lambda x: x.name)

    lootfarm_names_list = []
    for skin_loot_info in skins_loot_info_list:
        lootfarm_data.write(str(skin_loot_info) + '\n')
        lootfarm_names_list.append(skin_loot_info['name'])

    lootfarm_names.close()
    lootfarm_data.close()

    return lootfarm_list, lootfarm_names_list


def get_bitskins_price_list():

    bitskins_list = []
    bitskins_names = []

    MAIN_URL = 'https://bitskins.com'
    URL_ENDPOINT = '/api/v1/get_price_data_for_items_on_sale'
    CODE = get_totp()
    PAGE = 'PAGE'
    APP_ID = '570'
    JSON_URL = MAIN_URL + URL_ENDPOINT + '/?api_key=' + API_KEY + '&code=' + CODE + '&app_id=' + APP_ID

    skins_json = requests.get(JSON_URL)
    skins_json = json.loads(skins_json.text)
    skins_list = skins_json['data']['items']

    bitskins_data = open('../data/bitskins_data.txt', 'w')
    bitskins_names_file = open('../data/bitskins_names.txt', 'w')
    lootfarm_names_file = open('../data/lootfarm_names.txt', 'r')

    lootfarm_names = []
    for name in lootfarm_names_file:
        lootfarm_names.append(name)

    for skin in skins_list:

        skin = Skin(skin)

        if skin.name + '\n' not in lootfarm_names:
            continue

        bitskins_list.append(skin)
        name = skin.name
        bitskins_names_file.write(name + '\n')
        bitskins_names.append(name)
        price = str(int(float(skin.bit_price) * 100))
        skin_price = str({'name': name, 'price': price}) + '\n'
        bitskins_data.write(skin_price)

    bitskins_data.close()
    bitskins_names_file.close()

    bitskins_list = sorted(bitskins_list, key=lambda x: x.name)

    return bitskins_list, bitskins_names


def get_parsing_skins(lootfarm_list, bitskins_list, bitskins_names):
    # Отбрасывание скинов, которых нет на битскинс
    i = 0
    while i < len(bitskins_list):
        skin = lootfarm_list[i]
        if skin.name not in bitskins_names:
            lootfarm_list.remove(skin)
            i -= 1
        else:
            i += 1

    parsing_list = lootfarm_list

    for i in range(len(bitskins_list)):
        parsing_list[i].bit_price = bitskins_list[i].bit_price
        parsing_list[i].on_bit = bitskins_list[i].on_bit


        skin = parsing_list[i]
    '''
        print('name', skin.name)
        print('on_bit', skin.on_bit)
        print('bit_price',skin.bit_price)
        print('loot_price', skin.loot_price)
        print('on_loot', skin.on_loot)
        print('max_loot', skin.max_loot)
        print('\n'*3)
    '''


    return parsing_list


def get_profit_bit_to_loot(skin_list):

    for skin in skin_list:
        profit = skin.profit_bit_to_loot()
        if profit > 0.47 and profit != 1:

            print('name', skin.name)
            print('bit_price', skin.bit_price)
            print('loot_price', skin.loot_price)
            print('profit', profit)

            print('\n' * 3)


if __name__ == '__main__':

    while True:
        lootfarm_skins, lootfarm_names = get_lootfarm_list()
        bitskins_skins, bitskins_names = get_bitskins_price_list()

        parsing_skins = get_parsing_skins(lootfarm_skins, bitskins_skins, bitskins_names)

        get_profit_bit_to_loot(parsing_skins)
