#coding=utf-8
def describe_pet(animal_type,pet_name="hello"):#在编程中出现 non-default parameter follows default parameter 
                                                 #这种错误原因是将没有默认值的参数在定义时放在了有默认值的参数的后面,如写成annimal——tpye=xx，就会报错
	print("\nI have a "+ animal_type)
	print("My "+animal_type+"'s name is "+ pet_name)
#describe_pet(animal_type="dog")

describe_pet("dog")
