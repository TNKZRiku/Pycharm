#match从头
#search任意位置
#findall全部找到
import re
s = '我的手机号14451441919，,14511441919,qq号191981000,666'

#span:匹配的位置
#group:匹配的文本


# res1 = re.match(r'1[3-9]\d{9}',s)
# print(res1.group())

res2 = re.search(r'1[3-9]\d{9}',s)
print(res2.group())
print(res2.span())

res3 = re.findall(r'1[3-9]\d{9}',s)
print(res3)
