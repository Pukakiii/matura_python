# INPUT PRACTISE / STRING FUNCTIONALITY / ARYTHMETIC OPERATIONS / LOOPS / TUPLES / DICTIONARIES / CLASS and other functionality

"""
name=input('name: ')
color=input('color: ')
print(name+' and '+color)
"""
""" 
birth_year=input('year: ')
age=2025-int(birth_year)
print(age)
 
weight=input('kg: ')
age=1000*int(weight)
print(age, 'g')
"""

# multi_line_string="""Hi
# my
#      neightor 
#  """
# print(multi_line_string)

""" 
course='python for beginners'
print(course[-1])
print(course[0:3])
print(course[1:])
print(course[:5])
copy=course[:]
print(copy)
print(course[1:-1])
"""
""" 
course1='python for beginners'
formated_string=f'is it {course1}?'
# formated_string.upper() - not updating
print(len(formated_string))
print(formated_string.upper())
print(formated_string.title())
print(formated_string.find('o')) # - case sensitive
print(formated_string.find('beginners'))
print(formated_string.replace('beginners', 'pros'))
print('pros' in formated_string)
"""
""" 
print(5//2)
print(5%2)
print(abs(-2.4))
print(round(-2.4))
print(round(-2.6))
"""
""" 
name1='long Naaaame'
if len(name1)<3:
  print(name1)
elif len(name1)>12:
  print(f'yes {name1}') 
else: print('nothing')
"""
""" 
inp_w=int(input("waga: "))
inp_m=input("jednostki 'Kg' czy 'g': ")
if inp_m.capitalize() == 'Kg':
  print(inp_w*1000,'g')
elif inp_m.lower() == 'g':
  print(inp_w/1000,'Kg')
"""
""" 
i=0
while i<=5:
  print(i*'^')
  i+=1
print('Done')
"""
"""
g_count=0
g_num=5
g_guess=0
while g_count<3:
  g_guess=int(input('guess a num: '))
  if g_guess==g_num:
    print('win')
    break
  g_count+=1
else: 
  print('lost')
"""
""" 
for item in range(5, 10, 2):
  print(item)
"""
# numbers=[5,2,5,2,2]
# for num in numbers: I
#   print('x'*num)
# 
# i=0
# for num in numbers: II
#   output=''
#   while i<num:
#     output+='x'
#     i+=1
#   i=0
#   print(output)
# 
# for num in numbers: III
#   output=''
#   for c in range(num):
#     output+='x'
#   print(output)
# list=[3,1,4.4,3,5]
# list.sort()
# list.reverse()
# list.remove(4.4)
# print(list)
""" 
tuple_ = (1, 2, 4) # - usefull for keeping immutable data
x,y,z=tuple_
print(tuple_[0])
print(x,z,y)
print(tuple_.count(4))
print(tuple_.index(4)) 
"""
""" 
dictionary={
    "name": 'John Smith',
    "age": 30,
    "is_certified": False,
}
print(dictionary.get("age"))
print(dictionary.get("birthday", "Jan 1 1982")) 
"""
""" 
def greet_user (first_name,last_name):
print(f'Hi {first_name} {last_name}!')
print('Welcome aboard')
print("Start")
greet_user (last_name="Smith", first_name="Joe")
print("Finish")
"""
""" 
class Point: 
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def move(self):
        print('move')
    def draw(self):
        print('draw')
point1=Point(1,2)
point1.x=10
point1.y=20
print(point1.x)
point1.draw()

point2=Point(15,20)
print(point2) 
"""