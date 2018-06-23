#coding=utf-8
##promt="\nplease enter a letter"
##while True:
	##letter=input(promt)

	##if letter=="A":
		##break
	##else:
		##print("there is no A here")



######在循环中使用continue
current_number=0
while current_number<10:
	current_number+=1
	if current_number%2==0:
		continue
	else:
		print("hello world")




######使用while循环处理列表和字典

#####在列表之间移动元素

###创建待验证用户列表，和用于存储已验证用户的空列表

#unconfirm_users=["alice","brian","candace"]
#confirmed_users=[]
#while unconfirm_users:
#	current_user=unconfirm_users.pop() #pop（）方法：删除列表末尾
#	print("Verify User"+" "+current_user.title())
#	confirmed_users.append(current_user)
#print("the following users are confirmed:")
#for confirmed_user in confirmed_users:
#	print(confirmed_user.title())

######删除包含特定值的所有列表元素
#letter=["A","B","C","D","E","F","AA","BB","Abc"]
#while "A" in letter:
#	letter.remove("A") #只删除了A的那一项
#print(letter)



#####使用用户输入填充字典
responses={}
polling_active=True #设置标注指出调查是否继续
while polling_active:
	name=input("\nWhat is your name")
	response=input("\nWhat mountain would you lile to climb?")
	#将答案存储在字典中
	responses[name]=response
	#查看是否还有人要参与调查
	repeat=input("would you like to let another person response?(yes/no)")
	if repeat=="no":
		polling_active=False
print("\n------Poll Result")
for name,response in responses.items():
	print(name+response)