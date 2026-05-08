for i in range(5):
   print(f"number:{i}")


   numbers = [10,20,30,40,50]
   for number in numbers:
        print(f"number:{number}")


count = 0
while count < 5:
    print(f"count:{count}")
    count += 1


numbers = [10,20,30,40,50]
for number in numbers:
    if number == 20:
        print("found 20!stopping the loop.")
        break 
    print(number)


age = 25
if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")
    