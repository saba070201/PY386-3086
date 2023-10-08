# black_area='b'
# white_area='w'
# chess_field=[]
# for i in range(16):
#   middleware_array=[]
#   for j in range(16):
#     if (i + j) % 2 == 0: 
#       middleware_array.append('b')
#     else: 
#       middleware_array.append('w')
#   chess_field.append(middleware_array)
# print(chess_field)
# def create_chess_field(size,color1='b',color2='w'):
#   chess_field=[]
#   for i in range(size):
#     middleware_array=[]
#     for j in range(size):
#       if (i + j) % 2 == 0: 
#         middleware_array.append(color1)
#       else: 
#         middleware_array.append(color2)
#     chess_field.append(middleware_array)
#   return chess_field
# arr1=create_chess_field(8,'r','blue')
# arr2=create_chess_field(4,color2='orange')
# arr3=create_chess_field(2)
# print(arr1,arr2,arr3)
# # def hello_name(name):
#   print('Hello, '+str(name))

# hello_name('Misha')
# hello_name('Valerya')
# hello_name('Egor')
# import random 
# import math
# import colorama
# def calculator(value1,value2,operation_type='+'):
#   if operation_type=='+':
#     return value1 + value2
#   elif operation_type=='-':
#     return value1-value2
#   elif operation_type=='*':
#     return value1*value2
# result1=calculator(1,2)
# result2=calculator(10,calculator(10,5),'*')
# print(result1,result2)
# print(random.randint(1,100))
# print(colorama,'Hello world')
# import random 
# import colorama
# def generate_password(lenght,registr=False,special=False):
#   chars='qwertyuiopasdfghjklzxcvbnm'
#   registr_chars='QWERTYUIOOOOOOOPASDFGHJKLZXCVBNM'
#   special_chars='!@#$%^&*()_+{}[]'
#   password=''
#   if registr:
#     chars+=registr_chars
#   if special: 
#     chars+=special_chars
#   for i in range(lenght):
#     password+=random.choice(chars)
#   return password 
# password=generate_password(16,special=True,registr=True)
# print(colorama.Fore.RED,password)
# def find_indexes(l,k):
#   for i in range(len(l)-1):
#     for j in range(len(l)):
#       if l[i]+l[j] == k :
#         return i,j
#   return None
# print(find_indexes([1,2,3,4],6)[1])
# def replace(l,k,n):
#   midle_value=l[k]
#   l[k]=l[n]
#   l[n]=midle_value
#   l[k],l[n]= l[n],l[k]
# def custom_print(*words):
#   for i in words: 
#     print(i)
# custom_print(1,2,3)
# import random 
# def find_elems(l):
#   result_array=[]
#   for i in range(len(l)): 
#     if i%2==1 and l[i]%2==0:
#       result_array.append(l[i])
#   return result_array 
# l=[random.randint(1,1000) for i in range(100)]
# res=find_elems(l)
# print(res)
