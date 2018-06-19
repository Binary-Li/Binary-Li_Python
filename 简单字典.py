#coding:utf-8

alien={"coler":"green","point":"5"}  #字典使用｛ ｝
print(alien["coler"])
print(alien["point"])

#访问字典中的值
alien={"coler":"green","point":"5"} 
A=alien["coler"]
B=alien["point"]
print("bbb"+A)
print("aaa"+B)


#添加键－值对
alien={"coler":"green","point":"5"}  #字典使用｛ ｝
print(alien["coler"])
print(alien["point"])
alien["x_positon"]=15
alien["y_position"]=0
print(alien)



######创建空字典
alien={}
alien["coler"]="red"  #添加非数字必需使用引号
alien["point"]=10
alien["x_positon"]=55
alien["y_position"]=90
print(alien)


#########修改字典中的值＃＃＃＃＃
alien["coler"]="grey"
print(alien)

###########s删除键值对＃＃＃＃

