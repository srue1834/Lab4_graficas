import random
import pygame

class Life(object):
	def __init__(self, screen, pixel):
		self.screen = screen
		self.pixel = pixel

	def clear(self):
		self.screen.fill((0,0,0))

	def draw(self, pixel):
		for i in range(len(pixel)):
			for j in range(len(pixel)):

				if pixel[i][j] == 1:
					pygame.draw.rect(self.screen, (236,255,0), [j * 5, i * 5, 4, 4])

	def render(self, pixel):

		alive = [[0 for x in range(100)] for y in range(100)] 
		
		for i in range(len(pixel)):
			for j in range(len(pixel)):

				if i ==0 or i == len(pixel) - 1 or j == 0 or j == len(pixel) - 1:
					alive [i][j] = pixel[i][j]
				else:

					alive[i][j] = pixel[i][j]

					count = 0

					for k in range(-1, 2):
						for l in range(-1, 2):
							count += pixel[i + k][j + l]

					neighbors = count - pixel[i][j]

					status = pixel[i][j]

					if status == 0 and neighbors == 3:
						alive[i][j] = 1

					elif status == 1 and (neighbors < 2 or neighbors > 3):
						alive[i][j] = 0

					else:
						alive[i][j] = status 
		return alive


pygame.init()
screen = pygame.display.set_mode((500, 500))



pixel = [[random.randint(0, 1) for x in range(100)] for y in range(100)] 
r = Life(screen, pixel)

running = True

while running:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			running = False

	r.clear()
	
	r.draw(pixel)	


	pygame.display.flip()
	pixel = r.render(pixel)
	
