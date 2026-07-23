#在这里引用 就只会存在一个
from yuanwenjian import test1
test1 = test1
test2 = test1

print(test1)
print(test2)

#这个方法可以节省内存以及创建对象的开销