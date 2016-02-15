Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:45:13) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pygame
>>> window = pygame.display.set_mode((400, 400))
>>> pygame.display.set_caption("Hello pygame")
>>> 
>>> screen = pygame.surface((400, 400))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    screen = pygame.surface((400, 400))
TypeError: 'module' object is not callable
>>> screen = pygame.Surface((400, 400))
>>> 
>>> done = True
>>> while done:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			done = False
	window.blit(screen, (0, 0))
	pygame.display.flip()
	
