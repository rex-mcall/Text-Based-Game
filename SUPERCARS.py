#from (filename) import (a specific class)
#use = (specific class).(function inside class)

import scenes #data source
from sys import exit

def runProgram():	
	scenes.opening_scene.intro()

	scenes.CarSelection()

	scenes.Daytona()

	scenes.Annapolis()

	scenes.LosAngeles()	
	
def runAgain():
	again = input("Would you like to play again? (y/n)\n> ")
	if again == "y" or again == "yes" or again == "Y" or again == "Yes":
		runProgram()
	elif again == "n" or again == "no" or again == "N" or again == "no":
		exit(0)
	else:
		print("Input not recognized, please try again.")
		runAgain()

runProgram()	
runAgain()