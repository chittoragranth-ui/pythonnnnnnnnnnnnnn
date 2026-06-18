# Write code below 💖

height = int(input("Your height in cm:"))

credits = int(input("The number of credits you have:"))

if height > 137 and credits > 10:
  print("Enjoy the ride!")

elif height > 137 and credits < 10:
  print("You don't have enough credits.")

elif height < 137 and credits > 10:
  print("You are not tall enough to ride.")

else:
  print("You did not meet the reqired credentials")