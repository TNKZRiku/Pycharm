from lxml import html
import requests
import re
import pandas

url = "https://store.hikarifield.co.jp/shops"

def get_all_urls(url):
    response = requests.get(url)
    restext = response.text
    res = html.fromstring(restext)
    galgameurls: list = res.xpath('//*[@id="app"]/main/div[2]/div[2]/div/div/div/a/@href')
    return galgameurls

def get_galgame(galgameurl):
    response = requests.get(galgameurl)
    restext = response.text
    res = html.fromstring(restext)
    return res

def get_price(res):
    a = res.xpath('/html/body/div[1]/main/div[2]/div[3]/div/div[1]/section[1]/div/div/div[2]/div[1]/span[3]/text()')
    if a:
        try:
            return re.findall(r'(\d+)', a[0])
        except:
            print(res.text)
    else:
        return None

def get_name(res):
    a = res.xpath('//h1[@class="col-12 col-xl"]/text()')
    return a[0].strip()

def get_bound(res):
    a = res.xpath('//th[text()="游戏品牌"]/following-sibling::td[1]/text()')
    return a[0]

def get_date(res):
    a = res.xpath('//th[text()="发售日期"]/following-sibling::td[1]/text()')
    return a[0]

def get_detail(res):
    try:
        a = res.xpath('//section[@class="introduction mt-5 mb-3"]//p/text()')
        return a[0].strip()
    except:
        return None

def get_detail2(res):
    a = res.xpath('//section[contains(@class,"introduction")]//p//text()')
    return a[0].strip()

def get_detail3(res):
    a = res.xpath('//section[contains(@class,"introduction")]//div[@class="wrap"]//p//text()')
    return a[0].strip()


def normalize_date(raw_str):
    if len(raw_str) > 7:
        print(raw_str)
        pat = pat = re.compile(r'(\d{4})(?:[‑/. ]|年|-|/|\\)\s*(\d{1,2})(?:[‑/. ]|月|-|/|\\)\s*(\d{1,2})(?:[‑/. ]|日|-|/|\\)?')
        match = pat.search(raw_str)
        y = match.group(1)
        m = match.group(2).zfill(2)
        d = match.group(3).zfill(2)
        return f"{y}-{m}-{d}"
    else:
        return raw_str



###################################################

urls = get_all_urls(url)

galgames = []
count = 1
for galgameurl in urls:
    print(count,end='')
    galgames_dict = {}
    galgame = get_galgame(galgameurl)
    price = get_price(galgame)[0] if get_price(galgame) else '免费或暂未发售'
    name = get_name(galgame)
    bound = get_bound(galgame)
    date = get_date(galgame)
    detailtest1 = get_detail(galgame)
    detailtest2 = get_detail2(galgame)
    detailtest3 = get_detail3(galgame)
    if detailtest1 and len(detailtest1)>10:
        detail = detailtest1
    elif detailtest2 and len(detailtest2)>10:
        detail = detailtest2
    else:
        detail = detailtest3
    galgames_dict['游戏名'] = name
    galgames_dict['售价'] = price
    galgames_dict['厂商'] = bound
    galgames_dict['发行日期'] = normalize_date(date)
    galgames_dict['游戏简介'] = detail
    galgames.append(galgames_dict)
    count += 1
    print(name)

data = pandas.DataFrame(galgames)
data.to_excel('HikariField.xlsx', index=False)



