import pygame
class Inventory:
	inv = list()
	def __init__(self, items = []):
		self.inv = items
	def openChest(self, newItem):
		self.inv.append(newItem)
	