
# size=1000.6
# temperature=36.7
# # result=size*temperature
# # print(result)
# # print('hello, world!')
# word='Python'
# print(word+word)
# flag=True
# notflag=False
# print(flag*notflag)
# none_value=None
# a=10
# b=20
# c=a+b
# c=a-b
# c=a*b
# c=a/b
# c=b%a
# c=b//a
# a=10
# b=50
# c=2
# word='hello'
# d=(a*(b**2)*c)/(c*a)
# # print(d)
# # print(type(word))
# # print(id(a),id(b))
# word=input('введите значение переменной word')
# print(word)
# age=int(input())
# if age >= 65: 
#   print('Вы пенсионер!!!')
# elif 0 <= age < 18 or age == 66:
#   print('вы ребенок')
# else: 
#   print('сработало условие')
# if age >= 65: 
#   print('Вы пенсионер!!!')
# if 0 <= age < 18 or age == 66:
#   print('вы ребенок')
# age=int(input())
# discount_card=bool(input())
# male_or_female=str(input())
# pension_age=None
# discount=0
# if male_or_female=='male':
#   pension_age=65
# elif male_or_female=='female':
#   pension_age=60
#   discount+=5
# if age >= pension_age: 
#   discount=20
# elif 18 <= pension_age <=65: 
#   discount=15 
# else: 
#   discount=10 
# if discount_card:
#   discount+=10
# print(discount)
# k=1
# n=10
# # while k<=n: 
# #   print(k)
# #   k+=1

# while True:
#   print(k)
#   k+=1
#   if k==n+1:
#     break 

# while True:
#   a=int(input())
#   b=int(input())
#   if (a<=10 or a >= 0) and (b<= 10 or b >= 0):
#     c=a*b
#     print(c)
#     break 
#   else: 
#     print('Числа не входят в допустимый диапозон') 

# k=1
# n=10
# sum=0
# while k<=n:
#   if k%2==0:
#       sum+=k
#   k+=1
# print(sum)
# word='Hello'
# l=[1,True,3,4,'Misha',[6,7,8,[9,10,11]]]
# for i in l:
#   print(i)
# for j in l[5]:
#   print(j)
# i=0
# while i < len(l):
#   print(l[i])
#   i+=1
# l=[1,2,3]
# l
# l.append(4)
# print(l)
# l1=[1,2,3]
# l2=l1.copy()
# l2[1]=7
# print(id(l1),id(l2))
# l=[1,2,4,5]
# sum=0
# for i in l: 
#   sum+=i
# # print(sum)
# range_object=list(range(10))
# print(range_object)
# for i in range(len(l)):
#   print(l[i])
# l1=[10,15,1,7,5,8,4,3,2]
# l2=[]
# for i in range(len(l1)):
#   if l1[i]> 5: 
#     l2.append(i)
# print(l2)
# l1=[[1,2,3],
#     [7,8,9],
#     [4,5,6],
#   ]
# max_value=sum(l1[0])
# index=0
# for i in range(len(l1)):
#   if sum(l1[i])>max_value:
#     print(i)
#     max_value=sum(l1[i])
#     index=i
# print(max_value,index)
# l=[1,0,-1,-2,5,0,0]
# pozitive_numbers=[]
# zero_numbers=[]
# negative_numbers=[]
# for i in l:
#   if i > 0:
#     pozitive_numbers.append(i)
#   elif i < 0:
#     negative_numbers.append(i)
#   else: 
#     zero_numbers.append(i)
# print(pozitive_numbers,negative_numbers,zero_numbers)
about_Misha={'name':'Misha','age':22}
print(d['age'])
