#This is a single line comment

"""
This is
a Python
Multiline
Comment
"""

#variable_type : int,str,bool,float
my_name = "Utsav Bohara" # string type variable storing data "Utsav Bohara"
my_age = 21 #int type variable storing data 21
is_male = True #bool type variable
print("This is a simple print statement")



#Some inbuilt functions

#print
print("My name is",my_name) #automatically includes a space
print("My name is" + my_name) #we need to manually include a space 
#both are valid to join two strings


#type

print("type of my_name is : ",type(my_name))
print("type of my_age is : ",type(my_age))
print("type of is_male is : ",type(is_male))

#the actual format of print function is:
#  print(*objects, sep=' ', end='\n', file=None, flush=False)
