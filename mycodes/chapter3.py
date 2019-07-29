print("A.")
#3-1姓名
names=["cxd","lxc","lyc"]
print(names[0])
print(names[1])
print(names[2])

#3-2问候语
s=", glad to see you!"
print(names[0]+s)
print(names[1]+s)
print(names[2]+s)

#3-3自己的列表
lis=["motorcycle","bike","car"]
print("I want to have a Porsche "+lis[-1]+".")

print("\nB.")
#3-4嘉宾名单
listname=["zkl","xxm","cxy","cx"]
print(listname[0]+", "+listname[1]+", "+listname[2]+", "\
+listname[3]+", welcome to have a dinner.")

#3-5修改嘉宾名单
print(listname[-1]+" can't come.")
listname[-1]="zkj"
print(listname[0]+", "+listname[1]+", "+listname[2]+", "\
+listname[3]+", welcome to have a dinner.")

#3-6添加嘉宾
print("I find a huge table.")
listname.insert(0,"zzl")
listname.insert(2,"qq")
listname.insert(-1,"xf")
print(listname[0]+", "+listname[1]+", "+listname[2]+", "\
+listname[3]+", "+listname[4]+", "+listname[5]+", "\
+listname[6]+", welcome to have a dinner.")

#3-7缩减名单
bqy="Sorry to say that only two person could come here."
print(bqy)
rm1=listname.pop()
print(rm1+", "+bqy)
rm2=listname.pop()
print(rm2+", "+bqy)
rm3=listname.pop()
print(rm3+", "+bqy)
rm4=listname.pop()
print(rm4+", "+bqy)
rm5=listname.pop()
print(rm5+", "+bqy)
print(listname[0]+", you're still invited.")
print(listname[1]+", you're still invited.")
del listname[0]
del listname[1]
print(listname)

print("\nC.")
#3-8放眼世界
position=["usa","japan","france","england","italy"]
print(position)
print(sorted(position))
print(position)
position.reverse()
print(position)
position.reverse()
print(position)
position.sort()
print(position)
position.sort(reverse=True)
print(position)

#3-9
len(position)

#3-10
#3-11
w=[]
print(w[-1])