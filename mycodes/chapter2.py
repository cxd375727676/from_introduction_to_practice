#2-1简单消息
message1="Hello, world!"
print(message1)

#2-2多条简单消息
print(message1)
message1=message1+" I'll learn python."
print(message1)

#2-3个性化消息
name="eric"
a="Hello "
b=", would you like to learn some Python today?"
s=a+name.title()+b
print(s)

#2-4调整名字的大小写
name1=name.title()
name2=name.upper()
name3=name.lower()
Name=name1+" "+name2+" "+name3
print(Name)

#2-5名言
print('Albert Einstein once said,"A person who never \
made a mistake never tried anything new."')

#2-6名言2
famous_person="Albert Einstein"
message=famous_person+' once said,"A person who never \
made a mistake never tried anything new."'
print(message)
 
 #2-7剔除人名中的空白
myname="  cxd  "
print(myname)
print("\t"+myname.lstrip()+"\n\t"+myname.rstrip()+"\n\t"+myname.strip())

#2-8数字8
print(5+3)
print(10-2)
print(2*4)
print(24/3)

#2-9最喜欢的数字
number=9
Message="My favorite number is "+str(number)+"."
print(Message)

#2-10添加注释

#2-11Python之禅：键入import this查看编写原则