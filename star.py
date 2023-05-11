import math
import pygame

"""
	Star class
"""
class Star ():
	"""
		Initialize the Star
	"""
	def __init__ (self, position):
		# Load the picture into a 'pygame surface'
		self.sprite = pygame.image.load("star.png").convert_alpha()

		# The start position of the star
		self.position = position
	
	"""
		This method will render the planet onto the game-screen
	"""
	def render (self, screen):
		screen.blit (self.sprite, (self.position[0] - (self.sprite.get_width () / 2.0), self.position[1] - (self.sprite.get_height () / 2.0)))
