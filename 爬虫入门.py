import requests
from lxml import html

url = 'https://www.tiobe.com/tiobe-index/'
response = requests.get(url)
document = html.fromstring(response.content)

#解析表头
res1 = document.xpath('//table[@id="top20"]/thead/tr/th/text()')
#<table id="top20" class="table table-striped table-top20">
    # <thead>
    #     <tr>
    #         <th style="width: 15%">Aug 2026</th>
    #         <th style="width: 15%">Aug 2025</th>
    #         <th title="Difference compared to last year" style="width: 15%">Change</th>
    #         <th style="width: 25%" colspan="2">Programming Language</th>
    #         <th style="width: 15%">Ratings</th>
    #         <th title="Difference compared to last year" style="width: 15%">Change</th>
    #     </tr>
    # </thead>
    #id代表唯一标识
print(res1)

#解析表格
res2 = document.xpath('//table[@id="top20"]/tbody/tr')
for list in res2:
    td_list = list.xpath('./td/text()')
    print(td_list)

