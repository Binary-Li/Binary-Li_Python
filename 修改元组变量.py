#coding:utf-8
#不能修改元组中的元素，但是可以重新定义整个元组，修改元组的尺寸和元素
D=(200,50,20)
print(D)
print(D[0])

#重新定义D元组
D=(100,200,300)
for d in D:
	print(d)