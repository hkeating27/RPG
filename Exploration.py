class Exploration:

	def __init__(self, playerPositionX=0, playerPositionY=0):
		self.playerPositionX = 0
		self.playerPositionY = 0
	
	#Moves the player across the overworld, using checkPositionValidity() to ensure they stay in-bounds
	#Was originally made using a case statement in Java
	def moveOverworld(self, direction):
		#North
		if (direction == 'n'):
			#North sends you down and south up. Must be Australia.
			if (checkPositionValidity(self.playerPositionX, self.playerPositionY-1)):
				print("Moving north...")
				self.playerPositionY-=1
			else:
				print("You can't go that far north.")
		#South			
		elif (direction == 's'):
			if (checkPositionValidity(self.playerPositionX, self.playerPositionY+1)):
				print("Moving south...")
				self.playerPositionY+=1
			else: 
				print("You can't go that far south.")
		#East			
		elif (direction == 'e'):
			if (checkPositionValidity(self.playerPositionX+1, self.playerPositionY)):
				print("Moving east...")
				self.playerPositionX+=1
			else:
				print("You can't go that far east.")
		#West			
		elif (direction == 'w'): 
			if (checkPositionValidity(self.playerPositionX-1, self.playerPositionY)):
				print("Moving west...")
				self.playerPositionX-=1
								
			else:
				print("You can't go that far west.")
		#This default is an input statement for all other inputs
		else: 
			print("You can't go that way." + str(direction) );
	
		print("You are at location " + str(self.playerPositionX) + "," + str(self.playerPositionY) )
