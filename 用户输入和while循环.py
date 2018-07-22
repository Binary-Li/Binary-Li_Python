#coding:utf-8

####函数input（）的原理
#message=input("please input a letter:")
#print(message)


#######编写清晰的程序＃＃＃＃
#name=input("Plese enter your name:")
#print("Hello "+name+" !" )

##通过变量存储字符串,再通过用户输入存储在变量中，进行输出＃＃＃＃＃
#promot="If you tell us who you are,we can personalize the message you see"
#promot+="/nWhat is your first name?"
#name=input(promot)
#print("Hello "+name)



#使用int()来获取数值输入，input()将用户输入解读为字符串
#age=input("how old are you ?")
#print(age)
#age>=18     ####input会把数字解读为字符串，可以print输出，但无法使用数值大小比较

#正确写法
#age=input("how old are you ?")
#age=int(age) #必需先使用input让用户输入，再转格式，int只是格式，不是让用户输入的命令
#print(age)
#age>=18    ###此时会返回true 和false的结果

#input(),int()转换
#height=input("How tall are you,in inches?")
#height=int(height)     #int格式转换

#if height>=36:
#	print("your tall is enough")
#else:
#	print("you are too short to ride") #将数值用于比较和计算是，必需将其转换为数值表示



	#求模运算符“％”－－求余数，可用来判断奇偶
#	4%3
#	5%3
#	6%3
#	7%3


#while循环
number=1
while number<=5:
	print(number)
	number+=1


#让用户选择何时退出
A="Enter ‘quit’ to end the program"
message=""
while message!="quit":
	message=input(A)
	print(message)



