import pygame
from pygame import *
import random
from random import *
import sys
from pygame.locals import *


pygame.init()


display_width = 702
display_height = 532

screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Farm Factory Flee')

black = (0,0,0)
white = (255,255,255)
grey= (128, 128, 128)
blue = (70,130,180)
darkBlue = (25,25,112)
darkOrange = (255,140,0)
orange = (255,165,0)
cute_blue=(203,222,239)
lavender=(168,161,218)
pastel_pink=(222,165,164)

clock = pygame.time.Clock()
started = False
home = pygame.image.load('bg.jpg')
left = False
right = False
font = pygame.font.Font(None, 25)

# raise the USEREVENT every 1000ms
pygame.time.set_timer(pygame.USEREVENT, 200)
 
# make a list of text
listText = ["THE ", " HARSH ", " TRUTH "]


x =  (display_width * 0.45)
y = (display_height * 0.8)

yHay = (display_height * -0.2)
yFarmer = (display_height * -0.2)
yPitchfork = (display_height * -0.2)
piggy_width = 53

def mainPage(x,y):
    screen.blit(home, (x,y))		
def pig(x,y):
	pigphoto = pygame.image.load("pig1.png")
	screen.blit(pigphoto, (x,y))

def gameover():
	# display_width = 716
	# display_height = 557
	gameover = pygame.image.load('GameOver.png')
	screen.blit(gameover, (0,0))
	pygame.display.flip()
	pygame.time.delay(1000)
	


def text_generator(text):
    tmp = ''
    for letter in text:
        tmp += letter
        # don't pause for spaces
        if letter != ' ':
            yield tmp
def update():
	message.update()
	message1.update()
	message2.update()
	message3.update()
	message4.update()
	message5.update()
	message6.update()
	message7.update()
	message8.update()
	message9.update()
	message10.update()
	message11.update()
def draw():
	message.draw(screen)
	message1.draw(screen)
	message2.draw(screen)
	message3.draw(screen)
	message4.draw(screen)
	message5.draw(screen)
	message6.draw(screen)
	message7.draw(screen)
	message8.draw(screen)
	message9.draw(screen)
	message10.draw(screen)
	message11.draw(screen)

# a simple class that uses the generator
# and can tell if it is done
class DynamicText(object):
	def __init__(self, font, text, pos, autoreset=False):
		self.done = False
		self.font = font
		self.text = text
		self._gen = text_generator(self.text)
		self.pos = pos
		self.autoreset = autoreset
		self.update()

	def reset(self):
		self._gen = text_generator(self.text)
		self.done = False
		self.update()

	def update(self):
		if not self.done:
			try: self.rendered = self.font.render(next(self._gen), True, (254, 254, 250))
			except StopIteration: 
				self.done = True
				if self.autoreset: self.reset()

	def draw(self, screen):
		screen.blit(self.rendered, self.pos)

class hay():
	"""docstring for hay"""
	def __init__(self,x, y ):
		self.image = pygame.image.load("hay.png")
		self.xHay = x
		self.yHay = y
	def move (self):
		self.yHay += 5
	def showHay (self):
		screen.blit(self.image, (self.xHay, self.yHay))
		
class farmer():
	"""docstring for farmer"""
	def __init__(self,x, y ):
		self.image = pygame.image.load("farmer.png")
		self.xfarmer = x
		self.yfarmer = y

	def move (self):
		self.yfarmer += 5
	def showFarmer (self):
		screen.blit(self.image, (self.xfarmer, self.yfarmer))

class pitchfork():
	"""docstring for pitchfork"""
	def __init__(self,x, y ):
		self.image = pygame.image.load("pitchfork.png")
		self.xpitchfork = x
		self.ypitchfork = y

	def move (self):
		self.ypitchfork += 5
	def showPitchfork (self):
		screen.blit(self.image, (self.xpitchfork, self.ypitchfork))

msg = "9 billion animals are killed for meat each year."
msg2 =" Because of the cruel practices used in factory farming,"
msg3="these animals live lives of pain and suffering."
msg4= "In a farm factory, Peter the  Pig would have been born"
msg5="in a small crate and separated from his mother."
msg6="He would have been castrated with metal cutters, had "
msg7=" his tail clipped without anesthesia, and been raised without"
msg8="ever seeing the sunlight or the outdoors. "
msg9="If humans continue to eat meat in such large quantities,"
msg10="animals will continue to be obliterated."
msg11 ="It is time for us to stand up against cruelty."

# update draw method to iterate over list and print out each line
#message = DynamicText(font, "Animals never see the sun, touch the Earth, or taste the grass.", (100, 167), autoreset=True)

message = DynamicText(font, listText, (100, 67), autoreset=False)
message1 = DynamicText(font, msg, (52, 100), autoreset=False)
message2 = DynamicText(font, msg2, (46,120 ), autoreset=False)
message3 = DynamicText(font, msg3, (52, 140), autoreset=False)
message4= DynamicText(font, msg4, (52, 160), autoreset=False)
message5= DynamicText(font, msg5, (52, 180), autoreset=False)
message6= DynamicText(font, msg6, (52, 200), autoreset=False)
message7= DynamicText(font, msg7, (46, 220), autoreset=False)
message8= DynamicText(font, msg8, (50, 240), autoreset=False)
message9= DynamicText(font, msg9, (50, 300), autoreset=False)
message10 = DynamicText(font, msg10, (50, 320), autoreset=False)
message11 = DynamicText(font, msg11, (50, 360), autoreset=False)
game = False
obstacle = []
crash = False
selectedChar = False


while game == False:
	
#-------------CHECKING FOR EVENTS----------------------
	if (not started):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				started = True
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					left = True
				elif event.key == pygame.K_RIGHT:
					right = True	

		screen.fill(white)
		mainPage(0,0)
#*----------*********** BUTTON***************--------------------*
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()     

		if 73+142 > mouse[0] > 73 and 382+70 > mouse[1] > 382:
			pygame.draw.rect(screen, orange ,(73,382,142,70))
#*-------------**************** WHEN CLICKED NEXT SCREEN ******************--------------------*
			if click[0] == 1:
				started = True		
		else:
		 	pygame.draw.rect(screen,darkOrange,(73,382,142,70))
		
		font = pygame.font.Font(None,36)
		text = font.render("ESCAPE!!!", 1, (250,250,250))
		screen.blit (text, (85,403))

	elif crash == True:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				started = True
				pygame.quit()
			if event.type == pygame.USEREVENT: 
				update()

		else:
			# gameover()
			pygame.display.flip()
			pygame.time.delay(700)
			update()
			screen.fill(pastel_pink)
			draw()
			pygame.display.flip()
			clock.tick(25)
			pygame.time.delay(1000)
			# continue

	elif selectedChar == False:
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
		mouse = pygame.mouse.get_pos()
		character_click = pygame.image.load("farm.jpg")
		screen.blit(character_click, (0,0))
		
		# Hover over Chad
		if 171+120 > mouse[0] > 171 and 475+45 > mouse[1] > 475:
			pygame.draw.rect(screen, cute_blue ,(171,475,120,45))
			if click[0] == 1:
				selectedChar = True
		else:
		 	pygame.draw.rect(screen,lavender,(171,475,120,45))	

		font = pygame.font.Font(None,36)
		text = font.render("Chad", 1, (250,250,250))
		screen.blit (text, (189,487))

		# Hover over Timothy
		if 397+120 > mouse[0] > 397 and 475+45 > mouse[1] > 475:
			pygame.draw.rect(screen, cute_blue ,(397,475,120,45))
			if click[0] == 1:
				selectedChar = True
		else:
		 	pygame.draw.rect(screen,lavender,(397,475,120,45))
			#pygame.draw.rect(screen, cute_blue ,(397,475,120,45))
		font = pygame.font.Font(None,36)
		text = font.render("Timothy", 1, (250,250,250))
		screen.blit (text, (402,482))

		# Hover over Candice
		if 32+120 > mouse[0] > 32 and 264+45 > mouse[1] > 264:
			pygame.draw.rect(screen, cute_blue ,(32,265,120,45))
			if click[0] == 1:
				selectedChar = True
		else:
		 	pygame.draw.rect(screen,lavender,(32,265,120,45))
			#pygame.draw.rect(screen, cute_blue ,(32,265,120,45))
		font = pygame.font.Font(None,36)
		text = font.render("Candice", 1, (250,250,250))
		screen.blit (text, (38,271))

		# Hover over Peter
		if 289+120 > mouse[0] > 289 and 264+45 > mouse[1] > 264:
			pygame.draw.rect(screen, cute_blue ,(289,264,120,45))
			# Game Over
			if click[0] == 1:
				selectedChar = True
		else:
		 	pygame.draw.rect(screen,lavender,(289,264,120,45))
		 	#pygame.draw.rect(screen, cute_blue ,(289,264,120,45))

		font = pygame.font.Font(None,36)
		text = font.render("Peter", 1, (250,250,250))
		screen.blit (text, (309,272))

		# Hover over Peter
		if 521+120 > mouse[0] > 521 and 264+45 > mouse[1] > 264:
			pygame.draw.rect(screen, cute_blue ,(521,264,120,45))
			if click[0] == 1:
				selectedChar = True
		else:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					quit()
			pygame.draw.rect(screen,lavender,(521,264,120,45))
			#pygame.draw.rect(screen, cute_blue ,(521,264,120,45))

		font = pygame.font.Font(None,36)
		text = font.render("Sally", 1, (250,250,250))
		screen.blit (text, (539,269))


	else:

#------------------CHECKING FOR EVENTS---------------------
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				started = True
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					left = True
				elif event.key == pygame.K_RIGHT:
					right = True	
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					left = False
				elif event.key == pygame.K_RIGHT:
					right = False	
#-------------GAME BACKGROUND---------------
		x_change = 0 
		screen.fill(grey)
		pig (x,y)
		time = pygame.time.get_ticks()
		
		if time % 180 == 0:
			xPitchfork = (display_width * uniform(0.0,0.8))
			pitchforks = pitchfork(xPitchfork, yPitchfork)
			obstacle.append(pitchforks)

		elif time % 210 == 0:
			xHay =  (display_width * uniform(0.0,0.8))
			hayy = hay(xHay,yHay)
			obstacle.append(hayy)		

		elif time % 240 == 0:
			xFarmer =  (display_width * uniform(0.0,0.8))
			farmers = farmer(xFarmer,yFarmer)
			obstacle.append(farmers)
		
		for elem in obstacle:
			if type (elem) == hay:
				elem.showHay()
				elem.move()
			elif type(elem) == farmer:
				elem.showFarmer()
				elem.move()
			elif type(elem) == pitchfork:
				elem.showPitchfork()
				elem.move()
#---------------MOVEMENT WITH ARROWS---------------------
		if left == True: 
			x_change = -5
		elif right == True:
			x_change = 5
		else:
			x_change = 0
#--------------BOUNDARIES-------------------------
		if x > display_width - piggy_width :
			x_change = -1	
		if x < 0:
			x_change = 1
#----------ADDING TO X VALUE----------------------------------
		x += x_change
#-------------DETECTING IF TOUCHING PITCHFORK OBSTACLE------------
		for elem in obstacle:
			if type(elem) == pitchfork:
				if y <= elem.ypitchfork and elem.ypitchfork + 80 < 532 :
					if x <= elem.xpitchfork + 58 and x + piggy_width >= elem.xpitchfork:
						gameover()
						crash = True
			elif type(elem) == farmer:
				if y <= elem.yfarmer and elem.yfarmer + 97 < 532 :
					if x <= elem.xfarmer + 100 and x + piggy_width >= elem.xfarmer:
						gameover()
						print("the screen has changed")
						crash = True
						
			elif type(elem) == hay:
				if y <= elem.yHay and elem.yHay + 128 < 600:
					if x <= elem.xHay + 128 and x + piggy_width >= elem.xHay:
						gameover()
						print("the screen has changed")
						crash = True



	pygame.display.update()
	clock.tick(60)

pygame.display.update()
pygame.quit()
quit()