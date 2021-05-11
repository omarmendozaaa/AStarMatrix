import pygame as pygame
from AStartAlgorithm import AStartAlgorithm
from Table import Table
from Nodo import Nodo

WIDTH = 960
ROWS = 24
WINDOWN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Algorithm")

ROJO = (255, 0, 0) #close
VERDE = (0, 255, 0) #openlist
BLUE = (0, 255, 0) #inicio/final
NEGRO = (0, 0, 0) #muro
BLANCO = (255, 255, 255) #background
GRIS = (128, 128, 128) #grid

def createTable(width,height):
    table =  Table(width,height)
    return table

def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, GRIS, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, GRIS, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
	win.fill(BLANCO)

	for row in grid.board:
		for spot in row:
			spot.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()


def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap

	return row, col
		
def main(win,width):
	grid = createTable(WIDTH,ROWS)
	algoritmo = AStartAlgorithm(grid)
	start = None
	end = None
	run = True
	while run:
		draw(WINDOWN,grid,ROWS,WIDTH)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			#Crear inicio, final, barrera
			if pygame.mouse.get_pressed()[0]: #LEFT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, WIDTH)
				nodo = grid.get_nodo(row,col)
				if not start and nodo != end:
					start = nodo
					start.make_start()
				elif not end and nodo != start:
					end = nodo
					end.make_end()
				elif nodo != end and nodo != start:
					nodo.make_barrier()
			#Borrar inicio, final, barrera
			elif pygame.mouse.get_pressed()[2]: # RIGHT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, WIDTH)
				nodo = grid.get_nodo(row,col)
				nodo.reset()
				if nodo == start:
					start = None
				elif nodo == end:
					end = None
			#Iniciar el algoritmo
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					algoritmo.findPath(start,end)
					start.make_start()
					end.make_end()
				if event.key == pygame.K_c:
					grid = createTable(WIDTH,ROWS)
					algoritmo = AStartAlgorithm(grid)
					start = None
					end = None
					run = True

main(WINDOWN,WIDTH)



