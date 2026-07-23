import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import re

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Referer': 'http://www.tianqihoubao.com/'
}
url = 'https://www.tianqihoubao.com/lishi/xinxiang/month/202606.html'

dates = []
high_temps = []
low_temps = []

soup = BeautifulSoup(requests.get(url, headers=headers, timeout=30).text, 'html.parser')

tab = soup.find_all('table')[0]
tab2 = tab.find_all('tr')[1:]

for row in tab2:
    cells = row.find_all('td')
    if len(cells) < 3:
        continue
    day = re.search(r'06月(\d{2})日', cells[0].text)
    temps = re.findall(r'(\d+)℃', cells[2].text)
    if day and len(temps) >= 2:
        dates.append(int(day.group(1)))
        high_temps.append(int(temps[0]))
        low_temps.append(int(temps[1]))

plt.figure(figsize=(14,6),dpi=100)
plt.plot(
    dates,high_temps,color = '#e74c3c',
    marker = 's',
    linewidth = 2,
    label = '最高气温'
)

plt.plot(
    dates,low_temps,color = 'blue',
    marker = 's',
    linewidth = 2,
    label = '最低气温'
)

plt.title('郑州市2026年6月气温走势图',fontsize = 16)
plt.xlabel('日期')
plt.ylabel('气温（℃）')
plt.legend(loc='upper right')
plt.grid(alpha=0.3,linestyle='--')
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig('郑州市气温走势图')
plt.show()


