import pygame

ROJO = (255, 0, 0) #closelist
VERDE = (0, 255, 0) #openlist
AZUL = (64, 224, 208) #inicio/final
NEGRO = (0, 0, 0) #muro
BLANCO = (255, 255, 255) #background
PURPLE = (128, 0, 128)
NARANJA = (255, 128,0)
class Nodo:
	def __init__(self, row, col, width, total_rows, type = '0'):

		self.row = col
		self.col = row
		self.x = row * width
		self.y = col * width
		self.width = width
		self.total_rows = total_rows
		self.color = BLANCO
		self.f = 0
		self.h = 0
		self.g = 0
		self.parent = None
		self.type = type
		self.direccion = ""

	def get_pos(self):
		return self.row, self.col
	def get_parent(self):
		return self.parent

	def set_h(self, end):
		x1, y1 = self.row, self.col
		x2, y2 = end.get_pos()
		self.h = abs(x1 - x2)*10 + abs(y1 - y2)*10
		return self.h

	def set_parent(self, parent):
		self.parent = parent

	def set_fn(self, fn):
		self.fn = fn

	def is_closed(self):
		return self.color == ROJO

	def is_open(self):
		return self.color == VERDE

	def is_barrier(self):
		return self.color == NEGRO

	def is_start(self):
		if self.color == AZUL:
			return True
		else: return False

	def is_end(self):
		if self.color == NARANJA:
			return True
		else: return False

	def reset(self):
		self.color = BLANCO

	def make_start(self):
		self.color = AZUL

	def make_closed(self):
		self.color = ROJO
		pygame.display.update()

	def make_open(self):
		self.color = VERDE
		pygame.display.update()

	def make_barrier(self):
		self.color = NEGRO

	def make_end(self):
		self.color = NARANJA

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

	def make_path(self):
		self.color = PURPLE



