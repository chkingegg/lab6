#Ryan King

def encode(raw_data):
	encrypted_data = ""
	for c in raw_data:
		encrypted_data += str((int(c) + 3) % 10)
	return encrypted_data

def decode(encrypted_data):
	return ""

if __name__ == "__main__":
	password = ""
	while True:
		print("Menu")
		print("-------------")
		print("1. Encode")
		print("2. Decode")
		print("3. Quit\n")
		option = input("Please enter an option: ")
		if option == "1":
			password = encode(input("Please enter your password to encode: "))
			print("Your password has been encoded and stored!")
			print()
		elif option == "2":
			print(f"The encoded password is {password}, and the original password is {decode(password)}.")
			print()
		elif option == "3":
			break
