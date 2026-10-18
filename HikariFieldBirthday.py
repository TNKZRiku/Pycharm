#https://store.hikarifield.co.jp/characters/birthday/1
import pandas
import requests
from lxml import html

base_url = 'https://store.hikarifield.co.jp/characters/birthday/'

def get_name_list(url) -> list:
    name_list = []
    response = requests.get(url)
    data = html.fromstring(response.content)
    name = data.xpath('//*[@id="app"]/main/div[2]/div[4]/div/div/div/div/div[2]/div[1]/text()')
    for char in name:
        name_list.append(char.strip())
    return name_list

def get_birthday_list(url) -> list:
    birthday_list = []
    response = requests.get(url)
    data = html.fromstring(response.content)
    birthday = data.xpath('//*[@id="app"]/main/div[2]/div[4]/div/div/div/div/div[2]/div[2]/text()')
    for char in birthday:
        if len(char.strip()) > 1:
            birthday_list.append(char.strip())
    return birthday_list


def get_production_list(url) -> list:
    production_list = []
    response = requests.get(url)
    data = html.fromstring(response.content)
    production = data.xpath('//*[@id="app"]/main/div[2]/div[4]/div/div/div/div/div[2]/div[3]/small/text()')
    for char in production:
        production_list.append(char.strip())
    return production_list

def combine_list(name, birthday, production):
    combine_list = []
    for i in range(len(name)):
        combine_dict = {}
        combine_dict['角色名'] = name[i]
        combine_dict['生日'] = birthday[i]
        combine_dict['所属作品'] = production[i]
        combine_list.append(combine_dict)
    return combine_list

all_name_list = []
all_birthday_list = []
all_production_list = []

for num in range(1, 12+1):
    print(num)
    url = base_url + str(num)
    all_birthday_list.extend(get_birthday_list(url))
    all_production_list.extend(get_production_list(url))
    all_name_list.extend(get_name_list(url))
    l1st = combine_list(all_name_list, all_birthday_list, all_production_list)

res = sorted(l1st, key=lambda d: d["所属作品"])

data = pandas.DataFrame(res)
data.to_excel(
    'HikariFieldBirthday_sorted.xlsx',
              index=False
)








