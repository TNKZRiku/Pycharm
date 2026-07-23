#用于描述混合类型的注释
from typing import Union

mylist : list[int] = [1,2,3]
mylist2 : list[Union[int,str]] = [1,2,'zhoujielun']
mydict : dict[str, int] = {'a':1,'b':2,'c':3}
mydict2 :dict[Union[int,str],Union[int,str]] = {'a':1,2:'b','c':3}

def func(data:Union[int,str]) -> Union[int,str]:
    return data

func()
