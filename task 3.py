print("Welcome to the birthday game")
print("Set 1: 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31")
print("Set 2: 2 3 6 7 10 11 14 15 18 19 22 23 26 27 30 31")
print("Set 3: 4 5 6 7 12 13 14 15 20 21 22 23 28 29 30 31")
print("Set 4: 8 9 10 11 12 13 14 15 24 25 26 27 28 29 30 31")
print("Set 5: 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31")

step=1
total=0
for i in range(0,5):
    answer=input(f"Your birthday in {i+1}? add 1 for yes and 0 for no")
    if answer=="1":
        total=total+step
    step=step*2

print(f"Your birthday is{total}")