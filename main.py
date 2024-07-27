#TASK 2
from numpy import random

attempts = 0
n = random.randint(100)
print(n)

while attempts < 5:
  
        guess = int(input("Enter an integer from 1 to 99: "))
        attempts=attempts+1

        if guess == n:
                 print("WELL DONE!! YOU GUESSED IT RIGHT!")
                 break
        if guess < n:
                 print("the number you entered is lower than the actual number")

        if guess > n:
                 print("the number you entered is higher than the actual number")
        
  

 
  
    