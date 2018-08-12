def get_formatted_name(first_name,last_name,middle_name=""):
	if middle_name:
		full_name=first_name+" "+middle_name+" "+last_name
	else:
		full_name=first_name+" "+last_name
	return full_name.title()  #return 函数最终的结果

musician=get_formatted_name("jimi","hend")
print(musician)

musician=get_formatted_name("hello","hg","acv")
print(musician)

