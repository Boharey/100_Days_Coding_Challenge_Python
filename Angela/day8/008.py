# functions


#function definition ,user and times are parameters
def greet(user_name,times): 
  for i in range(times):
    print(f"hello, {user_name} ")

#function call , "utsav bohara" and 10 are arguments  
# greet("utsav bohara",2) 


#parameters are the values passed during function definition
#arguments are the actual values passed during function invoking/execution/calling


def hola(user,location):
  print(f"hello {user}")
  print(f"are you from {location}?\n")

# now understanding postional and keyword arguments
hola("kathmandu","pokhara") #positional
hola("pokhara","sabin") #positional
hola(location="pokhara",user="anish") #keyword





