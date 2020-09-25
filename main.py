import pygame
import random
import numpy as np

run = True

win = pygame.display.set_mode((288, 512))

bgImg = pygame.image.load('res/bg.png')
baseImg = pygame.image.load('res/base.png')
pipeImg = pygame.image.load('res/pipe.png')
pipe2Img = pygame.image.load('res/pipe2.png')

pipex=340
pipey=random.randrange(-250,-20,1)

rin = random.random()
rin2 = random.random()

birdImg = []
birdx = []
birdy = []
birdVel = []
colission = []
fit = []
maxx = []
val = []
gen = 0

dedBird = 0

def jump(birdy,pipey,i):
	if birdy[i] > (pipey+390):
		return True
	else:
		return False

def jump2():
	num = random.randrange(-1,110)
	if num < 0:
		return True
	else:
		return False

def jump3():
	global run
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				return True
			else:
				return False


def bg():
	win.blit(bgImg,(0,0))

def base():
	win.blit(baseImg,(0,400))

def bird(birdNum,birdx,birdy,birdVel):
	global pipey
	global pipex
	global dedBird
	global gen


	for i in range(birdNum):
		colission.append(False)
		birdx.append(64)
		birdy.append(144)
		birdVel.append(0.5)
		birdImg.append(pygame.image.load('res/bird1.png'))
		fit.append(10)

		if not colission[i]:
			rImg = pygame.transform.rotate(birdImg[i],birdVel[i]*-10)
			win.blit(rImg, (birdx[i], birdy[i]))

			if birdy[i] < pipey+320 and birdx[i]+34 > pipex or birdy[i]+24 > pipey+420 and birdx[i]+34 > pipex :
				if not birdx[i] > pipex+52 :
					colission[i]=True
					dedBird+=1

			if birdy[i] < 0:
				birdy[i] = 0

			if birdy[i] > 400-24:
				birdy[i]=400-25

			birdy[i]+=birdVel[i]
			birdVel[i]+=0.05

			if jump(birdy,pipey,i):
				birdVel[i]=-2.6

			fit[i]+=1

		if dedBird == birdNum:
			gen += 1
			maxx.append((max(fit)))
			print(str(gen) + " : " + str(max(maxx)))
			del birdImg[:]
			del birdx[:]
			del birdy[:]
			del colission[:]
			del birdVel[:]
			del fit[:]
			pipex=340
			pipey=random.randrange(-250,-20,1)
			dedBird = 0
			game()


def pipe():
    global pipex
    global pipey
    win.blit(pipeImg,(pipex, pipey))
    win.blit(pipe2Img,(pipex, pipey+420))
    pipex-=1
    if pipex < -52:
        pipex = 340
        pipey = random.randrange(-300,-20,1)

def game():
	global run
	while run:
		pygame.time.delay(0)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		bg()
		bird(1,birdx,birdy,birdVel)
		pipe()
		base()

		pygame.display.update()



game()
