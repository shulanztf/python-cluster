# b.py
from a import run, data

data[0] = 5  # 类似赋值，b里面的data和a里面的data指向同一个对象，这么做对两者都有影响
print(data)  # 输出[5,2,3]
run()  # 输出[5,2,3]

data = 100  # 由于直接改变了data的指向，所以不会影响源模块a
print(data)  # 输出100
run()  # 输出[5,2,3]