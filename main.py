from logo_parser import LogoParser

if __name__ == '__main__':
	print("Type commands : ")
	interpreter = LogoParser()
	while True:
		user_input = input().lower()
		if user_input == "exit":
			break
		interpreter.apply_user_input(user_input + " ")
