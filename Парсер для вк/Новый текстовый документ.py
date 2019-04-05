import pymorphy2
morph = pymorphy2.MorphAnalyzer()

file = open('main.txt','r')


members_dict = {'Янис Плевокас (': 0,
                'Дима Макаров (': 0,
                'Артур Мещеряков (': 0,
                'Арсений Оверчук (': 0,
                'Ян Иовлев (': 0,
                'Kostya Kokorev (': 0,
                'Иван Коваленко (': 0
           }
members_list = ['Янис Плевокас (',
                'Дима Макаров (',
                'Артур Мещеряков (',
                'Арсений Оверчук (',
                'Ян Иовлев (',
                'Kostya Kokorev (',
                'Иван Коваленко ('
           ]

forwarded_messages = 0
chars = 0
words = 0
data = {}
links = 0
wall_links = 0
video = 0
photo = 0
docs = 0

words_dict_1 = {}; alphabet_1 = 'абвгдеёжз' # а - з
words_dict_2 = {}; alphabet_2 = 'ийклмноп'  # и - п
words_dict_3 = {}; alphabet_3 = 'рстуфхцч'  # р - ч
words_dict_4 = {}; alphabet_4 = 'шщъыьэюя'  # ш - я


dict_0_1 = {}; dict_0_2 = {}; dict_0_3 = {}; dict_0_4 = {}
dict_1_1 = {}; dict_1_2 = {}; dict_1_3 = {}; dict_1_4 = {}
dict_2_1 = {}; dict_2_2 = {}; dict_2_3 = {}; dict_2_4 = {}
dict_3_1 = {}; dict_3_2 = {}; dict_3_3 = {}; dict_3_4 = {}
dict_4_1 = {}; dict_4_2 = {}; dict_4_3 = {}; dict_4_4 = {}
dict_5_1 = {}; dict_5_2 = {}; dict_5_3 = {}; dict_5_4 = {}
dict_6_1 = {}; dict_6_2 = {}; dict_6_3 = {}; dict_6_4 = {}


flag1 = False # Для пересланных сообщений
flag2 = False # Для вложений
flag3 = False # Для ссылок

last_name = 'Янис Плевокас ('

for line in file:

    if flag1 == True:
        flag1 = False
        continue
    
    if flag2 == True:
        if line.startswith('{"type":"wall"'):
            wall_links += 1
        if line.startswith('vk.com/video'):
            video += 1
        if line.startswith('vk.com/photo'):
            photo += 1
        if line.startswith('https://vk.com/doc'):
            docs += 1
        if line[0]==']':
            flag2 = False
            continue
        else:
            continue

    if flag3 == True:
        flag3 = False
        continue
        
    
    
    if line[1] != '	':
        
        if line[0] ==  '	' and line.endswith('):\n'):
            forwarded_messages += 1
            flag1 = True
            continue
        
        if line.startswith('Attachments:['):
            flag2 = True

            continue
        
        if line.startswith('http'):
            links += 1
            flag3 = True
            continue

        # Подсчет количества сообщений
        if line[0] != '	':
         

            for name in members_list:
        
                
                flag4 = False
                if line.startswith(name):
                    last_name = name
                    members_dict.update({name: members_dict[name] + 1})
                    data_one = line[-12:-2]
                    if data_one in data.keys():
                        data.update({data_one : data[data_one] + 1})
                    else:
                        data.update({data_one : 0})
                    flag4 = True
            
                str1 = name[0:-2] + ' пригласил'
                str2 = name[0:-2] + ' исключил'
        
                if (line.startswith(str1) or line.startswith(str2)) and flag4 == False:
                    members_dict.update({name: members_dict[name] - 1})
                    flag4 = True

                if flag4 == True:
                    break
                
            if flag4 == True:
                continue

            member_number = members_list.index(last_name)
            print()
            line = line.lower()
            chars += len(line) - line.count(' ')
            line = line.split()
            words += len(line)
            for word in line:
                while word.endswith('*') or word.endswith(',') or word.endswith(')') or \
                      word.endswith('(') or word.endswith('.') or word.endswith('!') or\
                      word.endswith('?'):
                    word = word[:-1]
                   
                normal_word = morph.parse(word)[0]
                word = normal_word.normal_form

               

                if len(word) >= 3:
                    if word[0] in alphabet_1:
                        word_dict_sort = words_dict_1
                        dic = 1
                    elif word[0] in alphabet_2:
                        word_dict_sort = words_dict_2
                        dic = 2
                    elif word[0] in alphabet_3:
                        word_dict_sort = words_dict_3
                        dic = 3
                    else:
                        word_dict_sort = words_dict_4
                        dic = 4
                        
                    if word in word_dict_sort.keys():
                        word_dict_sort.update({word : word_dict_sort[word] + 1})
                    else:
                        word_dict_sort.update({word : 1})

                    if dic == 1:
                        words_dict_1 = word_dict_sort

                        if member_number == 0:
                            if word in dict_0_1.keys():
                                dict_0_1.update({word : dict_0_1[word] + 1})
                            else:
                                dict_0_1.update({word : 1})
                               
                        elif member_number == 1:
                            if word in dict_1_1.keys():
                                dict_1_1.update({word : dict_1_1[word] + 1})
                            else:
                                dict_1_1.update({word : 1})
                        elif member_number == 2:
                            if word in dict_2_1.keys():
                                dict_2_1.update({word : dict_2_1[word] + 1})
                            else:
                                dict_2_1.update({word : 1})
                        elif member_number == 3:
                            if word in dict_3_1.keys():
                                dict_3_1.update({word : dict_3_1[word] + 1})
                            else:
                                dict_3_1.update({word : 1})
                        elif member_number == 4:
                            if word in dict_4_1.keys():
                                dict_4_1.update({word : dict_4_1[word] + 1})
                            else:
                                dict_4_1.update({word : 1})
                        elif member_number == 5:
                            if word in dict_5_1.keys():
                                dict_5_1.update({word : dict_5_1[word] + 1})
                            else:
                                dict_5_1.update({word : 1})
                        else:
                            if word in dict_6_1.keys():
                                dict_6_1.update({word : dict_6_1[word] + 1})
                            else:
                                dict_6_1.update({word : 1})        
                            
                        
                    elif dic == 2:
                        words_dict_2 = word_dict_sort

                        if member_number == 0:
                            if word in dict_0_2.keys():
                                dict_0_2.update({word : dict_0_2[word] + 1})
                            else:
                                dict_0_2.update({word : 1})
                        elif member_number == 1:
                            if word in dict_1_2.keys():
                                dict_1_2.update({word : dict_1_2[word] + 1})
                            else:
                                dict_1_2.update({word : 1})
                        elif member_number == 2:
                            if word in dict_2_2.keys():
                                dict_2_2.update({word : dict_2_2[word] + 1})
                            else:
                                dict_2_2.update({word : 1})
                        elif member_number == 3:
                            if word in dict_3_2.keys():
                                dict_3_2.update({word : dict_3_2[word] + 1})
                            else:
                                dict_3_2.update({word : 1})
                        elif member_number == 4:
                            if word in dict_4_2.keys():
                                dict_4_2.update({word : dict_4_2[word] + 1})
                            else:
                                dict_4_2.update({word : 1})
                        elif member_number == 5:
                            if word in dict_5_2.keys():
                                dict_5_2.update({word : dict_5_2[word] + 1})
                            else:
                                dict_5_2.update({word : 1})
                        else:
                            if word in dict_6_2.keys():
                                dict_6_2.update({word : dict_6_2[word] + 1})
                            else:
                                dict_6_2.update({word : 1})

                    elif dic == 3:
                        words_dict_3 = word_dict_sort
                        if member_number == 0:
                            if word in dict_0_3.keys():
                                dict_0_3.update({word : dict_0_3[word] + 1})
                            else:
                                dict_0_3.update({word : 1})
                        elif member_number == 1:
                            if word in dict_1_3.keys():
                                dict_1_3.update({word : dict_1_3[word] + 1})
                            else:
                                dict_1_3.update({word : 1})
                        elif member_number == 2:
                            if word in dict_2_3.keys():
                                dict_2_3.update({word : dict_2_3[word] + 1})
                            else:
                                dict_2_3.update({word : 1})
                        elif member_number == 3:
                            if word in dict_3_3.keys():
                                dict_3_3.update({word : dict_3_3[word] + 1})
                            else:
                                dict_3_3.update({word : 1})
                        elif member_number == 4:
                            if word in dict_4_3.keys():
                                dict_4_3.update({word : dict_4_3[word] + 1})
                            else:
                                dict_4_3.update({word : 1})
                        elif member_number == 5:
                            if word in dict_5_3.keys():
                                dict_5_3.update({word : dict_5_3[word] + 1})
                            else:
                                dict_5_3.update({word : 1})
                        else:
                            if word in dict_6_3.keys():
                                dict_6_3.update({word : dict_6_3[word] + 1})
                            else:
                                dict_6_3.update({word : 1})
                    else:
                        words_dict_4 = word_dict_sort
                        if member_number == 0:
                            if word in dict_0_4.keys():
                                dict_0_4.update({word : dict_0_4[word] + 1})
                            else:
                                dict_0_4.update({word : 1})
                        elif member_number == 1:
                            if word in dict_1_4.keys():
                                dict_1_4.update({word : dict_1_4[word] + 1})
                            else:
                                dict_1_4.update({word : 1})
                        elif member_number == 2:
                            if word in dict_2_4.keys():
                                dict_2_4.update({word : dict_2_4[word] + 1})
                            else:
                                dict_2_4.update({word : 1})
                        elif member_number == 3:
                            if word in dict_3_4.keys():
                                dict_3_4.update({word : dict_3_4[word] + 1})
                            else:
                                dict_3_4.update({word : 1})
                        elif member_number == 4:
                            if word in dict_4_4.keys():
                                dict_4_4.update({word : dict_4_4[word] + 1})
                            else:
                                dict_4_4.update({word : 1})
                        elif member_number == 5:
                            if word in dict_5_4.keys():
                                dict_5_4.update({word : dict_5_4[word] + 1})
                            else:
                                dict_5_4.update({word : 1})
                        else:
                            if word in dict_6_4.keys():
                                dict_6_4.update({word : dict_6_4[word] + 1})
                            else:
                                dict_6_4.update({word : 1})
                
print('Сообщений у каждого: ',members_dict)
members_list_for_print = sorted(members_dict.items(), key=lambda x: x[1])
i = 6
j = 1
messages = 0
while i >= 0:
    member = members_list_for_print[i]
    print(j,')',member[0], ' - ', member[1], sep='')
    messages += member[1]
    i -= 1
    j += 1
print('Всего сообщений: ', messages )

print('\n\nТоп слов у каждого:')
name_i = 0
print(members_list[name_i],':', sep='')
dict_0_1_list = sorted(dict_0_1.items(), key=lambda x: x[1])
dict_0_2_list = sorted(dict_0_2.items(), key=lambda x: x[1])
dict_0_3_list = sorted(dict_0_3.items(), key=lambda x: x[1])
dict_0_4_list = sorted(dict_0_4.items(), key=lambda x: x[1])
dict_0_top_list = []
for i in dict_0_1_list:
    dict_0_top_list.append(i)
for i in dict_0_2_list:
    dict_0_top_list.append(i)
for i in dict_0_3_list:
    dict_0_top_list.append(i)
for i in dict_0_4_list:
    dict_0_top_list.append(i)

dict_0_top_list = sorted(dict_0_top_list, key=lambda x: x[1])
print(len(dict_0_top_list))
i = -1
j = 1
while i >= -20:
    print(j,') ',dict_0_top_list[i][0],' - ',dict_0_top_list[i][1], sep='')
    i -= 1
    j += 1
name_i += 1


print(members_list[name_i],':', sep='')
dict_1_1_list = sorted(dict_1_1.items(), key=lambda x: x[1])
dict_1_2_list = sorted(dict_1_2.items(), key=lambda x: x[1])
dict_1_3_list = sorted(dict_1_3.items(), key=lambda x: x[1])
dict_1_4_list = sorted(dict_1_4.items(), key=lambda x: x[1])
dict_1_top_list = []
for i in dict_1_1_list:
    dict_1_top_list.append(i)
for i in dict_1_2_list:
    dict_1_top_list.append(i)
for i in dict_1_3_list:
    dict_1_top_list.append(i)
for i in dict_1_4_list:
    dict_1_top_list.append(i)

dict_1_top_list = sorted(dict_1_top_list, key=lambda x: x[1])
i = -1
j = 1
while i >= -20:
    print(j,') ',dict_1_top_list[i][0],' - ',dict_1_top_list[i][1], sep='')
    i -= 1
    j += 1
name_i += 1


print(members_list[name_i],':', sep='')
dict_2_1_list = sorted(dict_2_1.items(), key=lambda x: x[1])
dict_2_2_list = sorted(dict_2_2.items(), key=lambda x: x[1])
dict_2_3_list = sorted(dict_2_3.items(), key=lambda x: x[1])
dict_2_4_list = sorted(dict_2_4.items(), key=lambda x: x[1])
dict_2_top_list = []
for i in dict_2_1_list:
    dict_2_top_list.append(i)
for i in dict_2_2_list:
    dict_2_top_list.append(i)
for i in dict_2_3_list:
    dict_2_top_list.append(i)
for i in dict_2_4_list:
    dict_2_top_list.append(i)

dict_2_top_list = sorted(dict_2_top_list, key=lambda x: x[1])
i = -1
j = 1
while i >= -20:
    print(j,') ',dict_2_top_list[i][0],' - ',dict_2_top_list[i][1], sep='')
    i -= 1
    j += 1
name_i += 1


print(members_list[name_i],':', sep='')
dict_3_1_list = sorted(dict_3_1.items(), key=lambda x: x[1])
dict_3_2_list = sorted(dict_3_2.items(), key=lambda x: x[1])
dict_3_3_list = sorted(dict_3_3.items(), key=lambda x: x[1])
dict_3_4_list = sorted(dict_3_4.items(), key=lambda x: x[1])
dict_3_top_list = []
for i in dict_3_1_list:
    dict_3_top_list.append(i)
for i in dict_3_2_list:
    dict_3_top_list.append(i)
for i in dict_3_3_list:
    dict_3_top_list.append(i)
for i in dict_3_4_list:
    dict_3_top_list.append(i)

dict_3_top_list = sorted(dict_3_top_list, key=lambda x: x[1])
i = -1
j = 1
while i >= -20:
    print(j,') ',dict_3_top_list[i][0],' - ',dict_3_top_list[i][1], sep='')
    i -= 1
    j += 1
name_i += 1


print(members_list[name_i],':', sep='')
dict_4_1_list = sorted(dict_4_1.items(), key=lambda x: x[1])
dict_4_2_list = sorted(dict_4_2.items(), key=lambda x: x[1])
dict_4_3_list = sorted(dict_4_3.items(), key=lambda x: x[1])
dict_4_4_list = sorted(dict_4_4.items(), key=lambda x: x[1])
dict_4_top_list = []
for i in dict_4_1_list:
    dict_4_top_list.append(i)
for i in dict_4_2_list:
    dict_4_top_list.append(i)
for i in dict_4_3_list:
    dict_4_top_list.append(i)
for i in dict_4_4_list:
    dict_4_top_list.append(i)

dict_4_top_list = sorted(dict_4_top_list, key=lambda x: x[1])
i = -1
j = 1
while i >= -20:
    print(j,') ',dict_4_top_list[i][0],' - ',dict_4_top_list[i][1], sep='')
    i -= 1
    j += 1
name_i += 1


print(members_list[name_i],':', sep='')
dict_5_1_list = sorted(dict_5_1.items(), key=lambda x: x[1])
dict_5_2_list = sorted(dict_5_2.items(), key=lambda x: x[1])
dict_5_3_list = sorted(dict_5_3.items(), key=lambda x: x[1])
dict_5_4_list = sorted(dict_5_4.items(), key=lambda x: x[1])
dict_5_top_list = []
for i in dict_5_1_list:
    dict_5_top_list.append(i)
for i in dict_5_2_list:
    dict_5_top_list.append(i)
for i in dict_5_3_list:
    dict_5_top_list.append(i)
for i in dict_5_4_list:
    dict_5_top_list.append(i)

dict_5_top_list = sorted(dict_5_top_list, key=lambda x: x[1])
i = -1
j = 1
while i >= -20:
    print(j,') ',dict_5_top_list[i][0],' - ',dict_5_top_list[i][1], sep='')
    i -= 1
    j += 1
name_i += 1


print(members_list[name_i],':', sep='')
dict_6_1_list = sorted(dict_6_1.items(), key=lambda x: x[1])
dict_6_2_list = sorted(dict_6_2.items(), key=lambda x: x[1])
dict_6_3_list = sorted(dict_6_3.items(), key=lambda x: x[1])
dict_6_4_list = sorted(dict_6_4.items(), key=lambda x: x[1])
dict_6_top_list = []
for i in dict_6_1_list:
    dict_6_top_list.append(i)
for i in dict_6_2_list:
    dict_6_top_list.append(i)
for i in dict_6_3_list:
    dict_6_top_list.append(i)
for i in dict_6_4_list:
    dict_6_top_list.append(i)

dict_6_top_list = sorted(dict_6_top_list, key=lambda x: x[1])
i = -1
j = 1
while i >= -20:
    print(j,') ',dict_6_top_list[i][0],' - ',dict_6_top_list[i][1], sep='')
    i -= 1
    j += 1





print('\n\nВсего вложений:',links+wall_links+video +photo+docs)
print('Ссылок:', links)
print('Репостов:', wall_links)
print('Видео:', video)
print('Фотографий:', photo)
print('Документов:', docs)
print('\n\nПересланных сообщений: ',forwarded_messages)
print('Символов: ',chars)
print('Слов:',words)
print('\n\nТоп слов:')
word_list_for_print_1 = sorted(words_dict_1.items(), key=lambda x: x[1])
word_list_for_print_2 = sorted(words_dict_2.items(), key=lambda x: x[1])
word_list_for_print_3 = sorted(words_dict_3.items(), key=lambda x: x[1])
word_list_for_print_4 = sorted(words_dict_4.items(), key=lambda x: x[1])
top_list = []
for i in word_list_for_print_1:
    top_list.append(i)
for i in word_list_for_print_2:
    top_list.append(i)
for i in word_list_for_print_3:
    top_list.append(i)
for i in word_list_for_print_4:
    top_list.append(i)

top_list = sorted(top_list, key=lambda x: x[1])
i = -1
j = 1
while i >= -100:
    print(j,') ',top_list[i][0],' - ',top_list[i][1], sep='')
    i -= 1
    j += 1


data_list = sorted(data.items(), key=lambda x: x[1])
i = -1
j = 1
print('\n\nТоп популярных дат:')
while i >= -10:
    print(j,') ',data_list[i][0],' - ',data_list[i][1], sep='')
    i -= 1
    j += 1
a = input('Powered by IU7')

