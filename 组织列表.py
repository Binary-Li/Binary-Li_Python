#使用方法sort（）对列表永久性排序
cars=["bmw","audi",'toyota','subaru']
print(cars)

cars.sort()  #首字母从a到z自动排序
print(cars)

cars.sort(reverse=True) #倒序排列，reverse=True，T必须大写
print(cars)

#用sorted（）进行临时排序
cars=["bmw","audi",'toyota','subaru']
print("The original list is:" )
print(cars)

print("The sorted list is:")
print(sorted(cars))

print("the original list is:")
print(cars)

