# -*- coding: utf-8 -*-
"""
Created on Fri May 12 23:31:38 2017

@author: Samuel
"""

import pygame

class Objeto:
    def __init__(self,arquivo,x,y):
        self.main=pygame.image.load(arquivo)
        self.x=x
        self.y=y
        self.m=1
        self.pontos=0
        
    def Mostra(self, x, y):
        gameDisplay.blit(self.main,(x,y))
        
        
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
        print(self.v)
    
    def Tamanho(self, x, y):
        
        self.main = pygame.transform.scale(self.main,(x,y))





pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Protótipo 1")
clock = pygame.time.Clock()

x = (display_width * 0.1)       #Posição Inicial do Personagem
y = (display_height * 0.5)


arquivo= "homem.png"
runner = Objeto(arquivo,x,y)

runner.xi = 100
runner.yi = 125

h_yi=int(runner.xi/2)

hamburguer = Objeto("hamburguer.png",display_width,runner.y + runner.yi - h_yi)
hamburguer.xi = int(runner.xi/2)
hamburguer.yi = h_yi


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

    

def game_loop():    

    
    chao=pygame.image.load("chao.png")
        
    cnt=0
    
    x_change = 8                       #Velocidade do objeto
    morto = 0
    pulando=0  
    runner_anda=0 
    runner_achata=0                    

    while not morto:
        
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
                        
                        
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                        runner_anda=0
                if event.key == pygame.K_RIGHT:
                        runner_anda=0
                if event.key == pygame.K_DOWN:
                        runner_achata=0
                        
                    
        if pulando:
            runner.Pula()
            if runner.y>y:
                runner.y=y
                pulando=0
        
        if runner.x+runner_anda>0 and runner.x+runner_anda<display_width-runner.xi:
            runner.x+=runner_anda
                
        if hamburguer.x<-hamburguer.xi:
            hamburguer.x=display_width+hamburguer.xi
                
        hamburguer.x -= x_change
        gameDisplay.fill((255,255,255))
        gameDisplay.blit(chao,(0,-200))
        P= descobreP(cnt)
        runner.Recarrega(P)
        
        runner.Tamanho(runner.xi,runner.yi)
        
        if runner_achata:
            
            runner.Tamanho(runner.xi,int(runner.yi/2))
            runner.Mostra(runner.x,int(runner.y+runner.yi/2))
        else:
            runner.Mostra(runner.x,runner.y)
        
        hamburguer.Mostra(hamburguer.x,hamburguer.y)

        
    
        
        pygame.display.update()
        cnt+=3
        
        if cnt>60:
            cnt=0
        clock.tick(60)
        
game_loop()
pygame.quit()
quit()