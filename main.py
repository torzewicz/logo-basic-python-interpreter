from logo_parser import LogoParser

print("Type commands : ")
source = " "
P = LogoParser(source)
P.graphInit()
while True:
	source = input()
	if source == "exit" :
		break
	source = source + "  "
	P.reInit(source)
	P.parse()

print(P.history)
