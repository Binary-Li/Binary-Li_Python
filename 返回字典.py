def build_person(firstname,lastname,age=""):
	person={"first":firstname,"last":lastname}
	if age:
		person["age"]=age
	return person
musician=build_person("jimi","ajia",age=27)
print(musician)