#coding=utf-8
from email.MIMEText import MIMEText
from email.header import Header
message="hello world"

msg=MIMEText(message,"plain","utf-8")

msg["Subject"]=Header("自动化邮件")
msg["From"]=Header("lihaoz@qq.com")
msg["To"]=Header("receiver","utf-8")

from_addr="lihaoz@qqc.com"
password="lihaoz910326"
to_addr="iambinary@163.com"

smtp_server="smtp.qq.com"

try:
  server = smtplib.SMTP(smtp_server,25) #第二个参数为默认端口为25，有些邮件有特殊端口
  print('开始登录')
  server.login(from_addr,password) #登录邮箱
  print('登录成功')
  print("邮件开始发送")
  server.sendmail(from_addr,to_addr,msg.as_string())  #将msg转化成string发出
  server.quit()
  print("邮件发送成功")
except smtplib.SMTPException as e:
  print("邮件发送失败",e)
