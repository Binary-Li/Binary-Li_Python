#coding=utf-8
def describe_pet(animal_type,pet_name):
	print("\nI have a "+ animal_type)
	print("My "+animal_type+"'s name is "+ pet_name)
describe_pet("hamster","harry")
#调用多次函数
describe_pet("dog","willie")
describe_pet("hello","dog")#形参和实参位置必须相同，否则会输出错误

#关键字实参--形参和实参绑定,.避免形参实参位置错误导致输出错误
describe_pet(pet_name="beibei",animal_type="cat")

