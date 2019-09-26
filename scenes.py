from sys import exit

username = input("Please enter a username.\n> ")
choice = input("Would you like a McLaren 720s or a Chevrolet Camaro? (Options: McLaren or Camaro) \n> ")
name = username
result = choice
money_left = 350,000

def CarSelection():
	if choice == "McLaren":
		cars.McLaren()
	elif choice == "Camaro":
		cars.Camaro()
	else:
		print("Choice not registered in system.")
		CarSelection()

class opening_scene():
	def intro():
		speech = f"""Welcome to SUPERCARS. In this game you will be driving your {result} at breakneck speeds through various tracks. 
Your decisions will affect the outcome of this game.\n"""
		print("\n\n" + "-" * 180 + "\n" + "-" * 180 + "\n\n")
		print(f"\nHello, {username}.", speech)
	

class cars():
	def McLaren():
		info_or_race = input(f"Would you like to race or receive info on your {result}? (Options: 'info' & 'race')\n>")
		if info_or_race == "Info" or info_or_race == "info":
			print("\n\n" + "-" * 180 + "\n" + "-" * 180 + "\n\n")
#info is pulled from wikipedia page
			print("""
The McLaren 720S is a British sports car designed and manufactured by McLaren Automotive. It is the second all-new car in the McLaren Super Series, replacing the 650S beginning in May 2017.

The 720S was launched at the Geneva Motor Show on 7 March 2017 and is built on a modified carbon chassis, which is lighter and stiffer in contrast to the 650S.
Overview:

Manufacturer:	McLaren Automotive
Production:	2017–present
Assembly:	Woking, Surrey, England
Designer:	Robert Melville

Body and chassis:

Class:	Sports car (S)
Body style:	2-door coupe
Layout:	Rear mid-engine, rear-wheel drive
Related:	McLaren F1, McLaren Senna

Powertrain:

Engine:	4.0 L M840T twin-turbocharged V8
Power output:	530 kW (710 hp; 720 PS)
Transmission:	7-speed dual-clutch

Dimensions:

Wheelbase:	2,670 mm (105 in)
Length:	4,543 mm (179 in)
Width:	2,161 mm (85 in)
Height:	1,196 mm (47 in)
Kerb weight	1,283 kg (2,829 lb) (dry)                                                                                                                                                                     
1,419 kg (3,128 lb) (curb)

Chronology:

Predecessor:	McLaren 650S\n""")
			
		else:
			pass
	def Camaro():
		info_or_race = input(f"Would you like to race or receive info on your {result}? (Options: 'info' & 'race')\n>")
		if info_or_race == "Info" or info_or_race == "info":
			print("\n\n" + "-" * 180 + "\n" + "-" * 180 + "\n\n")
#info is pulled from wikipedia page
			print("""
The Chevrolet Camaro is an American automobile manufactured by Chevrolet, classified as a pony car and some versions also as a muscle car.
It went on sale on September 29, 1966, for the 1967 model year and was designed as a competing model to the Ford Mustang.
The car shared its platform and major components with the Pontiac Firebird, also introduced for 1967.

Four distinct generations of the Camaro were developed before production ended in 2002.
The nameplate was revived on a concept car that evolved into the fifth-generation Camaro; production started on March 16, 2009.

Overview:

Manufacturer:	General Motors

Production:

1966–2002
2009–present

Model years:
	
1967–2002
2010–present

Body and chassis:

Class:	
Pony car
Muscle car

Body style:	

2-door coupe
2-door convertible

Layout:	FR layout

Platform:

F-body (1967–2002)
Zeta platform (2010–2015)
Alpha platform (2016–present)

Chronology:

Predecessor:	Chevrolet Corvair\n""")
			
		else:
			pass
			
def death(why):
	print("\n\n" + "-" * 180 + "\n" + "-" * 180 + "\n\n")
	print(f"Your choice cost you your life.", why, "Game over man! Game over!")
	print("\n\n" + "-" * 180 + "\n" + "-" * 180 + "\n\n")
	exit(0)
	
def Daytona():
	def fuel():
		FUEL = input("Do you make a pit stop for fuel or try to squeeze in an extra lap? (Options are: fuel or continue)\n> ")
		
		if FUEL == "fuel":
			print("You have an excellent pit crew, and you only dropped three places. It is now the final lap, let's make it count!")
		elif FUEL == "continue":
			print("You just barely made it, but you have an extra lap under your belt. It's the final lap now; make it count!")
		else:
			print("Input not recognized, try again.")
			fuel()
			
	def doyoupass():
		PASS = input("Do you attempt to pass on the left or right?\n> ")
		
		if PASS == "Left" or PASS == "left":
		
			print("Good Job! You are now in the lead again!")
			
		elif PASS == "Right" or PASS == "right":
		
			death("As you attempted to pass him, he swerved violently and sent your car into the wall. The car behind you was unable to stop and proceeded to run your car over, crushing you. Good Job!")
		else:
			print("Choice not recognized, try again.")
			doyoupass()
	
	print("\n\n" + "-" * 180 + "\n" + "-" * 180 + "\n\n")
	print("Welcome to the Daytona International Speedway in Daytona Beach, Florida, USA.")
	
	print(f"Your {result} is ready! It's a beautiful yet powerful car... let us hope it's driver is skilled enough to use it's full potential.")
	
	print("4\n3\n2\n1\nGO!")
	
	print("Wow! Your car was first off the line! Bad news: a Bugatti just passed you on the left. Good news: The driver is inexperienced, and you have an opportunity to regain your position in the front.")
	doyoupass()
			
	print("You have now made it through a few laps, and you stayed in the lead since you passed the Bugatti. Unfortunately, you are low on fuel.")
	fuel()
	
	
	print("You're approaching the finish line quickly! If you earned a special code from the last race, enter it now. Otherwise, just hit ENTER.")
	code = input("> ")
	if code == "1024":
		print(f"Good job, {name}! You won the race! Congratulations!")
	else:
		print(f"Good job, {name}. Unfortunately, as you were about to cross the finish line, another car passed you. You ended up in third place. Lucky for you, you've won this prize (1024). Type that number in next time and see what happens!")
		
		
def Annapolis():
	print("\n\n" + "-" * 180 + "\n" + "-" * 180 + "\n\n")
	print("Now that you've completed Daytona, you can be included in a street race through Annapolis. The starting line is at the intersection of Green Street and Main Street, facing Church Circle.\n")
	print("The finish line is at St. Mary's.\n")
	print("Through this level, your options are 'forward', 'left', or 'right', unless otherwise specified. Enter your choice when you see the '>'.\n ")
	
	ready = input("Ready? (y/n)\n> ")
	if ready == "y":
		pass
	else:
		print("Too bad. The race isn't waiting for you!")
	
	print("4\n3\n2\n1\nGO!")
	
	def finishLine(a):
		if a == True:
			pass
		else:
			c5 = input("> ")
			if c5 == "right":
				print(f"Good job again, {name}! You win! Time for a final race.")
			else:
				death("Tsk, tsk tsk. So close. So dead.")
	
	
	def raceEnding():
			print("You're now at the top of Duke of Gloucester street (You are on Duke of Gloucester, not on the circle) , and also still in first place. Make your decision!")
			c4 = input("> ")
			if c4 == "forward":
				print("You're now outside the gates of St. Mary's.")
				finishLine()
			else:
				death("You crash into buildings on the side of the road.")
	
	def ChurchCircle():		
		c3 = input("> ")
		if c3 == "forward":
			death("You just crashed into the governor's mansion.")
		elif c3 == "left":
			print("Good choice! You have now made it around the traffic circle and are at the top of Duke of Gloucester street.")
			raceEnding()
		elif c3 == "right":
			print("You are now on State Circle, and you are so far behind that you quit the race. You didn't die though...")
			LosAngeles()
		else:
			print("Input not recognized, try again.")
			ChurchCircle()
			
	def raceContinue():
		print("You're now at the top of Main Street. DO you go left, right, or forward?")
		c2 = input("> ")
		if c2 == "forward":
			death("What were you thinking??? Your car is now in pieces because you rammed St. Anne's Church!")
		elif c2 == "left":
			death("Nice try making a u-turn... but this is a traffic circle. You have to turn right.")
		elif c2 == "right":
			print("You are now on Church Circle, facing the governor's mansion. Forward, Left, or Right?")
			ChurchCircle()
		else:
			print("Input not recognized, try again.")
			raceContinue()
			
	def startLine():		
		c1 = input("> ")
		
		if c1 == "forward":
			print("Once again, you're fast off the starting line. Halfway up Main Street, you remember there is a Starbucks. Would you like to stop and place an order? (y/n)")
			starbucks = input("\n> ")
			if starbucks == "y":
				print("All the other drivers see you, and they also decide to stop and order something.")
			else:
				print("Good! You learned from the tortoise and the hare!")
				raceContinue()
					
		elif c1 == "left":
			def elseif():
				print("To everyone's surprise, you turn and go the wrong way up Green Street! It was a risky move; if the streets weren't closed you would have it oncoming traffic.\nThis shortcut allows you to end up right outside of St. Mary's. Make your final choice:")
				c1 = input("> ")
				if c1 == "forward":
					print("You've won the race, thanks to your knowledge of Annapolis and your choice of the shortcut! Congratulations.")
					finishLine(True)
				elif c1 == "left":
					death("You obviously do not know where you're going, and you end up crashing into the yacht club and setting it on fire again. I think you made the turn up Green Street by mistake and did not actually know it was a shortcut.")
				elif c1 == "right":
					death("You end up crashing into oncoming race cars because of your incompetence. I think you made the turn up Green Street by mistake and did not actually know it was a shortcut.")
				else:
					print("Input not recognized, try again.")
					elseif()
			elseif()
				
		elif c1 == "right":
			print("Wrong way! Luckily, a futuristic version of Tesla autopilot was installed in your car, and it put you back on track.")
			raceContinue()
		else:
			print("Input not recognized.")
			startLine()
	startLine()
def	LosAngeles():
	print("\n\n" + "-" * 180 + "\n" + "-" * 180 + "\n\n")
	print("Here we are, at the Los Angeles International Motor Speedway. Welcome to the race for the Piston Cup!\n\n")
	print("The race begins. Since the track is an oval, and you don't have much choice, I'll choose for you.\n\n") 
	print("Left\n" * 20)
	print(f"\n\nYou win! Nice Job! You receive the Piston Cup, and the game ends. Well done, {name}.\n\n\n\n")