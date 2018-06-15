
#coding:utf-8
D=['aa','bb','cc','dd','ee','ff','gg']
print(D[:])

for d in D:
	if d=='aa':    #注意“＝＝”号，为判断的意思，if else后面要有“：”
		print(d.upper())
	else:
		print(d.title())