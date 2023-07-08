# a=19
# s=8
# d=38
# print(a,s,d)
# age=20
# name="waqas"
# print(f"my name is {name} my age is {age}")

# name=input("enter our name")
# print(f"your name is {name}")
# x=int(input("entre value 1"))
# y=int(input("entre value 2"))
# z=x+y
# print(f"total is{z}")
# x=(10>5)
# print(x)
# y='5463'
# print('6' in y)
# x="helo how are yuo"
# print(x[3:8])
# x="hello"
# y="waqas"
# z=x+' '+y
# print(z)
# 
# print(y*2)
# item="apple"
# qty=2
# price=10

# a="i want {} kg {} in {} dollars"
# print(a.format(qty,item,price))
# 
# a=" hello how are \"you\""
# print(a)
# 
# 
# x="he jhjjd"
# print(x.upper())

# x=43
# if x > 45:
    # print("ok")
    # print("ok")
# else:
    # print("notok")
# print("end")
# x=int(input("enter number"))

# if x % 2==0:
    # print(f"{x} is a even number")
# else:
    # print(f"{x} is a odd number")
# x=int(input("Enter your marks"))
# if x > 80:
    # print("grade A")
# elif x >= 60:
    # print("grade B")
# elif x >=40:
    # print('grade C')
# else:
    # print("fial")
     
# x =100
# if x >76:
    # pass
# else:
    # print("ok")

# x=20
# print("ok") if x >10 else print("not ok")
# 








# x =1
# while x<=6:
    # print(x)
    # x=x+1
# 
# x =2
# while x<=16:
    # print(x)
    # x=x*2

# 
# s1="python programming"

# l=len(s1)
# x=0
# while x<l:
    # print(s1[x])
    # x=x+1
# 
# s1="python programming"
# 
# l=len(s1)
# x=0
# while x<l:
    # if s1[x]!='y' and s1[x]!='g':
        # print(s1[x])
    # x=x+1
# x=2
# i=5
# while x<=i:
    # print(x)
    # x+=1



# x=2
# sum=0
# while x<=10:
    # sum=sum+x
    # x=x+1
# print(sum)    
# print(x)

# sum=0
# x=''
# while x!='n':
    # x=input('enter no')
    # if x !='n':
        # sum +=int(x) 
# print(sum)
# i=1
# while i<=5:
        # j=1
        # while j<=5:
                # print(j,end=" ")
                # j=j+1
        # print()
        # i=i+1        
# i=1
# while i<=5:
        # j=1
        # while j<=i:
                # print(j,end=" ")
                # j=j+1
        # print()
        # i=i+1        
    
 
# i="python programming"
# for x in i:
    # if x not in "aioue":
        # print(x)
# for i in range(1,11):
    # print(i)
# for i in range(2,11,2):
    # print(i)
# for i in range(1,6):
    # for j in range(1 ,i+1):
        # print(j,end=" ")
    # print()        

# i=1
# while i<=20:
    # print(i)
    # i=i*2
# x=2
# for i in range(x ,10):
    # print(i)
    # i=i+2
#i=1
#while i<=5:
#    if i ==3:
#        i+=1
#        continue
#    print(i)
#    i+=1
# 
# s="hello world"
# for x in s:
    # if x in'w':
        # break
    # print(x)
# 
# classlist=["waqas","ali",[1,2,3,4,4,'5',6,7,9],"awias","hassan","zab"]
# print(classlist[2])
# classlist[1]="ahmed"
# classlist.append("fazi")
# classlist.insert(2,"irfan")
# classlist.remove([1,2,3,4,4,'5',6,7,9])
# classlist.pop()
# del classlist[2]
# print(classlist)
# testlist=["tes",290,78.48,"true"]
# print(testlist)
# print(type(testlist))

# 
# marks=[90,92,85,69,75]
# max=marks[4]
# for m in marks:
    # if m>max:
        # max=m
# print(max)            
# for a in marks:
    # print(a)

# l=len(marks)
# x=0
# while x< l:
    # print(marks[x])
    # x+=1
# even=[]   
# marks=[90,92,85,69,75,23,67,86]
# 
# for a in marks:
    # if a % 2==0:
        # even.append(a)
# print(even)        
# marks=[90,92,85,69,75,23,67,86]
# even=[m for m in marks if m%2 ==0]
# print(even)
# print(marks*2)
# 
# x=10
# while x<=20:
    # print(x)
    # x+=1

#python sets

# country={"Pakistan","USA","Canaada"}
# print(country)
# print("india" in country)
# marks=set((43,43,45,75,67,56))
# print(marks)

# country.remove("Canaada")
# print(country)
# country.clear()
# print(marks)
# python dectionery

# person={
    # "name": "waqas",
    # "age": 19,
    # "work":"web developer"
# 
# }
# for x in person:
    # print(x, "=",person[x])



# print(person['age'])
# for x in person.items():
    # (a,b)=x
    # print("a=",a,"b=",b)
# functions of python

# def display():
    # print("hello")


# display()
# display()
# display()
# display()
# def argu(a):
    # print("a=",a)
# 
# argu(6+8)





# for loop lists

# my_list=[10,20,30,40,50,60]
# for i in range(len(my_list)):
    # print(i,my_list[i])


# for loop Dictionary

# my_dict={"brand":"frud","Model":"frudiya", "year":2022,}
# for val in my_dict.keys():
    # print(val)