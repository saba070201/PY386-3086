# message= 'Good bye world'
# f=open('test.txt','w')
# f.write(message)
# f.close()
# arr=[]
# with open('test.txt','r') as f:
#   for i in f: 
#     arr.append(int(i))

# print(arr)
import random 
def write_to_file(arr,path_to_file):
  with open(path_to_file,'a+') as f:
    for i in arr: 
      f.write(str(i)+'\n')
PATH_TO_FILE='test.txt'
write_to_file([random.randint(1,1000) for i in range(100)],PATH_TO_FILE)
