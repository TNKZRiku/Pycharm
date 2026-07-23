import json

#json可以是字典 也可以是字典的列表

data = [{'name':'张三','age':'18'},{'name':'李四','age':'15'},{'name':'王五','age':'21'}]
json_str = json.dumps(data,ensure_ascii=False)
print(type(json_str))
print(json_str)

#dumps用来把字典转化为JSON
#其中 JSON类型为字符串

#第六行的第二个参数意味着不把中文字符转化为ASCII码

##########################################

#loads用来把字符串（JSON）转化回字典或字典列表

str = '[{"name":"张三","age":"18"},{"name":"李四","age":"15"},{"name":"王五","age":"21"}]'
l = json.loads(str)
print(type(l))
print(l)

#这里l是字典列表解出来的 是列表形式



