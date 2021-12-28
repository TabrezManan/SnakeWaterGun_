import random
loop = 1
while(loop<=9):
	list = random.choice([1,2,3])
	var = int(input("type 1 for snake , 2 for water , 3 for gun as you choice \n"))

	if var==int(1) and list==int(2):
		print("you won")

	elif var==int(1) and list==int(3):
		print("you lose")

	elif var==int(2) and list==int(1):
		print("you lose")

	elif var==int(2) and list==int(3):
		print("you won")

	elif var==int(3) and list==int(1):
		print("you won")

	elif var==int(3) and list==int(2):
		print("you lose")

	else:
		print("draw")