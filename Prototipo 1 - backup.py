# -*- coding: utf-8 -*-
"""
Created on Fri May 12 23:31:38 2017

@author: Samuel
"""

import pygame
import copy
import random

class Objeto:
    def __init__(self,arquivo,x,y):
        self.main=pygame.image.load(arquivo)
        self.x=x
        self.y=y
        self.m=1
        
        
        self.pontos=0
        
    def Mostra(self,x,y):
        gameDisplay.blit(self.main,(x,y))
        
    def Copy(self):
        return self
        
        
    def Recarrega(self, P):
        if P==0:
            self.main=pygame.image.load("homem1.png")
        elif P==1:
            self.main=pygame.image.load("homem2.png")
        elif P==2:
            self.main=pygame.image.load("homem3.png")
        else:
            self.main=pygame.image.load("homem4.png")
    
    def Pula(self):
        if self.v>0:
            self.y -= 1/2 * self.m * self.v**2
        else:
            self.y += 1/2 * self.m * self.v**2
    
        self.v -= 0.5
        
    def Colisao(self,objeto):
        
        a=pygame.Rect((self.x,self.y),(self.xi,self.yi))        
        b=pygame.Rect((objeto.x,objeto.y),(objeto.xi,objeto.yi))
        
        return a.colliderect(b)
    
        
    
    def Tamanho(self, x, y):
        
        self.main = pygame.transform.scale(self.main,(x,y))





pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Protótipo 1")
clock = pygame.time.Clock()


x = (display_width * 0.1)       #Posição Inicial do Personagem
y = (display_height * 0.7)


arquivo= "homem.png"
runner = Objeto(arquivo,x,y)

runner.xi = 100
runner.yi = 125

h_yi=int(runner.xi/2)

hamburguer = Objeto("hamburguer.png",display_width,runner.y + runner.yi - h_yi)
hamburguer.xi = int(runner.xi/2)
hamburguer.yi = h_yi
chao = Objeto("fundo.png",0,0)
chao.xi=int(pygame.Surface.get_width(chao.main))
chao.yi=int(pygame.Surface.get_height(chao.main))
chao.yi=display_height
chao.Tamanho(chao.xi,chao.yi)
chao2=copy.copy(chao)
chao2.x=chao2.x+chao2.xi
chao.x=0
chao.y=0
chao2.x=chao.x+chao2.xi

listarandom=range(int(display_width))
hamburguer.x=display_width+random.choice(listarandom)


runner.Tamanho(runner.xi,runner.yi)
hamburguer.Tamanho(hamburguer.xi,hamburguer.yi)

def descobreP(cnt):
    if cnt>=0 and cnt<15:
        return 0
    elif cnt>=15 and cnt<30:
        return 1
    elif cnt>=30 and cnt<45:
        return 2
    else:
        return 3

def Gameover():
    gameover = pygame.image.load("gameover.jpeg")
    gameover = pygame.transform.scale(gameover,(display_width,display_height))
    gameDisplay.blit(gameover,(0,0))
    
def Reiniciar():
    runner.x = (display_width * 0.1)       #Posição Inicial do Personagem
    runner.y = (display_height * 0.7)
    hamburguer.x = display_width
    hamburguer.y = runner.y + runner.yi - h_yi
    chao.x=0
    chao2.x=chao.x+chao2.xi
    
def Mostrav(lista):
    for i in range(len(lista)):
        lista[i].Mostra(display_width+random.choice(listarandom),lista[i].y)

def game_loop():           
    cnt=0
    cnth=0
    
    x_change = 8                       #Velocidade do objeto
    morto = 0
    pulando=0  
    runner_anda=0 
    runner_achata=0
    gameover=0
    listaf=[hamburguer]                

    while not morto:
        gameDisplay.fill((255,255,255))
        chao.Mostra(chao.x,chao.y)
        chao2.Mostra(chao2.x,chao2.y)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                morto=1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if runner.y==y and not pulando:
                        runner.v=8
                        pulando=1
                if event.key == pygame.K_LEFT:
                        runner_anda=-5
                if event.key == pygame.K_RIGHT:
                        runner_anda=+5
                if event.key == pygame.K_DOWN:
                        runner_achata=1
                        runner.yi=int(runner.yi/2)
                        runner.y=int(runner.y+runner.yi)
                        
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                        runner_anda=0
                if event.key == pygame.K_RIGHT:
                        runner_anda=0
                if event.key == pygame.K_DOWN:
                        runner_achata=0
                        runner.y=runner.y-runner.yi
                        runner.yi=int(runner.yi*2)
                        
                    
        
        if runner.x+runner_anda>0 and runner.x+runner_anda<display_width-runner.xi:
            runner.x+=runner_anda
                
        #if cnth==60:
            #listaf.append(copy.copy(hamburguer))
            #print("dw")
            #Mostrav(listaf)
        if hamburguer.x<-hamburguer.xi:
            hamburguer.x=display_width+random.choice(listarandom)
            
        if runner.Colisao(hamburguer):
            gameover=1
            
        if chao.x<-chao.xi:
            chao.x=chao2.x+chao2.xi
        if chao2.x<-chao2.xi:
            chao2.x=chao.x+chao.xi                        
               
        for i in range(len(listaf)):
            listaf[i].x -= x_change
        
        chao.x -= x_change
        chao2.x -= x_change
        
        P = descobreP(cnt)
        runner.Recarrega(P)
        runner.Tamanho(runner.xi,runner.yi)      
        
        if runner_achata:
            
            runner.Tamanho(runner.xi,runner.yi)
            runner.Mostra(runner.x,runner.y)
        else:
            runner.Mostra(runner.x,runner.y)
        
        hamburguer.Mostra(hamburguer.x,hamburguer.y)
        
        if pulando:
            runner.Pula()
            if runner.y+runner.yi>hamburguer.y+hamburguer.yi:
                runner.y=hamburguer.y+hamburguer.yi-runner.yi
                pulando=0
        
        if gameover==1:
            Gameover()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:                   
                    gameover=0
                    Reiniciar()
                    
            
        pygame.display.update()
        cnt+=3
        cnth+=1
        
        if cnt>60:
            cnt=0
        if cnth>60:
            cnth=0
        clock.tick(60)

game_loop()
pygame.quit()
quit()