#coding:utf-8
########检查特殊元素＃＃＃＃
A=["a","b","c","d","e"]
for a in A:
	print("Adding"+a+".")

print("Finish")

#########for 循环中添加if语句
A=["a","b","c","d","e"]
for a in A:
	if a=="b":
		print("sorry")
	else:
		print(a+"Finish")
###########确定列表不是空白＃＃＃＃＃
B=["1","2","3"]
if B:
	for b in B:
		print(b)
else:
	print("no character here")

##########使用多个列表＃＃＃＃＃＃
characters1=["a","b","c","d","e"]
numbers2=["a","c","d","v","m"]
for characters11 in characters1:
	if characters11 in numbers2:
		print(characters11+" is double")
	else:
		print(characters11+" is single")
