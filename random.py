import random
n = random.randint(1, 100)
while True:
    x = int(input("Guess The Number: "))
    if x < n:
     print("Oh! Too Low")
    elif x > n:
     print("Oh! Too High")
    else:
     print("Wow! You Got The Number")
     break
