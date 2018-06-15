motorcycles=["honda","yamaha","suzuki"]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

#使用方法pop（）删除列表数据
motorcycles.append("a") #列表末尾增加a
motorcycles.append("b") #列表末尾增加b
motorcycles.append("c") #列表末尾增加c
motorcycles.append("d") #列表末尾增加d
print(motorcycles)

motorcycles_a=motorcycles.pop()  #从motor...列表中删除最后一个值，并建立新变量
print(motorcycles)
print(motorcycles_a)


#使用pop（）删除列表任意位置的内容
motorcycles=['honda', 'suzuki', 'a', 'b', 'c',"d"]
print(motorcycles)

second=motorcycles.pop(1) #删除m..中第二个值，并给删除的第二个值写入second变量
print(second)   
print(motorcycles)

