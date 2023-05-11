import math
import pygame

"""
	Planet class
"""
class Planet ():
	"""
		Initialize the Planet
		image = "planet.png"
		radians = 0.0
		radius = 50.0
		speed = 1.5
	"""
	def __init__ (self, image = "planet.png", radians = 0.0, radius = 50.0, speed = 1.5):
		# Image to be used as a planet
		self.sprite = pygame.image.load("planet.png").convert_alpha()
		self.sprite = pygame.image.load(image).convert_alpha()

		# The start angle measured in radians
		self.radians = 0.0
		self.radians = radians

		# Radius of the circle
		self.radius = 50.0
		self.radius = radius

		# Speed of the planet
		self.speed = 1.5
		self.speed = speed

	"""
		This method is called every frame.
		Update the gamephysics (gamelogic) on the planet
		clock: pygame clock object. This has the delta_time
	"""
	def update (self, clock, star):
		# Update the angle of the planet
		self.radians += self.speed * (clock.get_time () / 1000.0)
		
		# We can reset the rotation because "mathematics". Angle = Angle +- 2*pi
		if self.radians > 2*math.pi:
			self.radians -= 2*math.pi
		elif self.radians < 0.0:
			self.radians += 2*math.pi

		# Update the position based on the angle.
		# This is Trigonometry (Mathematics)
		# x**2 + y**2 = r**2, where r is the radius of the circle.
		self.position = [star.position[0] + self.radius * math.cos (self.radians), star.position[1] - self.radius * math.sin (self.radians)]

	"""
		This method will render the planet onto the game-screen
	"""
	def render (self, screen):
		screen.blit (self.sprite, (self.position[0] - (self.sprite.get_width () / 2.0), self.position[1] - (self.sprite.get_height () / 2.0)))
