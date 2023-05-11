import math
import pygame

from star import Star
from planet import Planet

"""
	Game Class
"""
class Game ():
	"""
		Initialize all the game stuff.
		Including the gamewindow (pygame)
	"""
	def __init__ (self):
		# Start pygame
		pygame.init ()
		
		# Make the gamewindow
		self.screen = pygame.display.set_mode ((300, 300), flags = pygame.SCALED)
		# Set the Title of the window
		pygame.display.set_caption ("Planets Simulation")
		
		# Create a Star object, at position = []
		self.star = Star (position = [150, 150])

		# Create a Planet object
		self.planet = Planet ()
		#self.planet2 = Planet (image = "planet2.png", radians = 3.14, radius = 150.0, speed = 0.1)
		
		# We need to track time, with a clock
		self.clock = pygame.time.Clock ()
		# Set the framerate (FPS) to 60 fps
		self.clock.tick (60)

	"""
		Start the gameloop
	"""
	def run (self):
		# The game will run if run_flag == True
		self.run_flag = True

		# This is the game loop
		while self.run_flag == True:
			# This checks keyboard inputs
			self.events ()

			# Update the game logic and physics
			self.update ()

			# Render all the visuals/pictures
			self.render ()

			# A frame has passed, tick the clock
			self.clock.tick (60)

		# Cleanup afterwards
		pygame.quit ()
		quit ()

	"""
		Check for game inputs/events
	"""
	def events (self):
		# Loop through every event that has happened
		for event in pygame.event.get ():
			# Did we click EXIT?
			if event.type == pygame.QUIT:
				self.run_flag = False

			# A Key was pressed
			elif event.type == pygame.KEYDOWN:
				# Which keycode was pressed?
				#print (f"Keydown: {event.key}")
				
				# 113 == 'Q' for quit
				if event.key == 113:
					self.run_flag = False

	
	"""
		Update the gamelogic
	"""
	def update (self):
		# Update the planet
		self.planet.update (self.clock, self.star)
		#self.planet2.update (self.clock, self.star)

	"""
		Render the graphics
	"""
	def render (self):
		# Fill the screen with color DARK_GREY
		DARK_GREY = (25, 25, 25)
		self.screen.fill (DARK_GREY)

		# Render the star
		self.star.render (self.screen)

		# Render the planet
		self.planet.render (self.screen)
		#self.planet2.render (self.screen)

		# Flip the table
		# This will actually display the pictures
		pygame.display.flip ()

"""
	This will run when you enter the program
"""
if __name__ == "__main__":
	# Creat a new Game object
	game = Game ()

	# Let's start the game
	game.run ()
else:
	print ("ERROR! You need to run main.py as the main file!")
	quit ()