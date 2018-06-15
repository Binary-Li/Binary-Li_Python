range(1,7)
print(range(1,7))  #range()不能直接包含在print中

for value in range(1,7):
	print(value)     #range()只指定的第一个数值开始，到达第二个数值后停止，所以输出的实际是1~6


	#使用list（）和range（）创建数值列表
numbers=list(range(1,7))
print(numbers)

#使用range（）指定步长 range（）的第三位为步长,range（）的步长必须为整数
numbers1=list(range(1,7,2))
print(numbers1)

# **2表示平方  **3不表示次方 **不表示平方

squares=[]  #创建空的列表
for value in range(1,11): #value为1到11
	square=value**2 #square为value的平方
	squares.append(square)  #把square添加到squares列表的最后一位
print(squares)

#不使用临时变量square
A=[]
for x in range(1,10):
	A.append(x**2)

print()
	
