from game_data import data
from random import randint
from art import logo,vs
# data is a list of dictionaries

# for A
indA = randint(0,len(data)-1)
A = data[indA]
# print(indA)
# print(A)

# for B
indB = randint(0,len(data)-1)
B = data[indB]
# print(indB)
# print(B)


user_guess = ""
result = ""
score = 0
won = bool 
# print(won)
#1
print(logo)
# ask question

# compare A and B
# def compare():
#   print(f"compare A :",A["follower_count"],A)
#   print(vs)
#   print(f"compare B : ",B["follower_count"],B)
#   user_guess = input("Who has more Followers 'A' or 'B' ? Type A or B ")
#     # changing of A and Selection of new B
#   if(A["follower_count"] > B["follower_count"]):
#     result = "A"
#   else:
#     result = "B"
      
#   if(result == user_guess):
#     score =score + 1
#     print(f"you won score : {score}")
#     A = B
#     rand = randint(0,len(data)-1)
#     B = data[rand]
#     won = True 
#   else:
#     print(f"You lost score : {score}")
#     won = False
  

while(won != False):
  print(f"compare A :",A["follower_count"],A)
  print(vs)
  print(f"compare B : ",B["follower_count"],B)
  user_guess = input("Who has more Followers 'A' or 'B' ? Type A or B ")
    # changing of A and Selection of new B
  if(A["follower_count"] > B["follower_count"]):
    result = "A"
  else:
    result = "B"
      
  if(result == user_guess):
    score =score + 1
    print(f"you won score : {score}")
    A = B
    rand = randint(0,len(data)-1)
    B = data[rand]
    won = True 
  else:
    print(f"You lost score : {score}")
    won = False
  
print("game over")
  #compare 
# gives value of result





# final logic

      
    # score += increment 

   #increase score 


    