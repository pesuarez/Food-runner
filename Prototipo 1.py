# -*- coding: utf-8 -*-
"""
Created on Fri May 12 23:31:38 2017

@author: Samuel
"""

import pygame
import copy
import random

class Objeto:
    def __init__(self,arquivo,x,y,xi,yi):
        self.main=pygame.image.load(arquivo)
        self.x=x
        self.xinit=x
        self.yinit=y
        self.yi=yi
        self.xi=xi
        self.yiinit=yi
        self.xiinit=xi
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

altura_inicial=display_height * 0.7


x = (display_width * 0.1)       #Posição Inicial do Personagem
y = (altura_inicial)


arquivo= "homem.png"
runner = Objeto(arquivo,x,y,100,130)
if runner.yiinit%2==1:
    runner.yiinit+=1
nomedofundo="fundo.png"


h_yi=int(runner.xi/2)
chaoaux=pygame.image.load(nomedofundo)
hamburguer = Objeto("hamburguer.png",display_width,runner.y + runner.yi - h_yi,int(runner.xi/2),h_yi)
chao = Objeto(nomedofundo,0,0,int(pygame.Surface.get_width(chaoaux)),int(pygame.Surface.get_height(chaoaux)))
chao.yi=display_height
chao.Tamanho(chao.xi,chao.yi)
chao2=copy.copy(chao)
chao2.x=chao2.x+chao2.xi
chao.x=0
chao.y=0
chao2.x=chao.x+chao2.xi
vida=Objeto("energy.png",display_width-250,20,230,40)
vidam=Objeto("energymold.png",display_width-256,15,241,50)
vida.Tamanho(vida.xi,vida.yi)
vidam.Tamanho(vidam.xi,vidam.yi)

listarandom=range(int(display_width),int(display_width)*2)
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
    runner.y = (altura_inicial)
    hamburguer.x = display_width
    hamburguer.y = runner.y + runner.yi - h_yi
    chao.x=0
    chao2.x=chao.x+chao2.xi
    vida.xi=vida.xiinit
    vida.Tamanho(vida.xiinit,vida.yi)
    
def Mostrav(lista):
    for i in range(len(lista)):
        lista[i].Mostra(lista[i].x,lista[i].y)

def game_loop():           
    cnt=0
    cnth=0
    
    x_change = 10                       #Velocidade do objeto
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
        vidam.Mostra(vidam.x,vidam.y)
        vida.Mostra(vida.x,vida.y)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                morto=1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if runner.y==runner.yinit and not pulando:
                        runner.v=8
                        pulando=1
                    else:
                        print(runner.y)
                        print(runner.yinit)
                    
                        
                if event.key == pygame.K_LEFT:
                        runner_anda=-5
                if event.key == pygame.K_RIGHT:
                        runner_anda=+5
                if event.key == pygame.K_DOWN:
                        runner_achata=1
                        runner.yi=int(runner.yi/2)
                        runner.y=runner.y+runner.yi
                if event.key == pygame.K_ESCAPE:        
                        gameover=1
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                        runner_anda=0
                if event.key == pygame.K_RIGHT:
                        runner_anda=0
                if event.key == pygame.K_DOWN:
                        runner_achata=0
                        runner.y-=runner.yi
                        
                        runner.yi=runner.yiinit
                        
                        
                        
                    
        if vida.xi<1:
            gameover=1
        if runner.x+runner_anda>0 and runner.x+runner_anda<display_width-runner.xi:
            runner.x+=runner_anda
                
        if cnth==60:
            
            hamb=copy.copy(hamburguer)
            hamb.x=display_width+random.choice(listarandom)
            listaf.append(copy.copy(hamb))
        
        
            
        for i in range(len(listaf)):
            Mostrav(listaf)
            if listaf[i].x<-listaf[i].xi:
                listaf.pop(i)
                print("Esqueceu de pegar hamburguer")
                break
        for i in range(len(listaf)):
            if runner.Colisao(listaf[i]):
                listaf.pop(i)
                print("Pegou hamburguer")
                if not vida.xi-40<1:
                    vida.xi-=40
                else:
                    gameover=1
                vida.Tamanho(vida.xi,vida.yi)
                break
                
            
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
        
        if runner_anda>0:
            cnt+=1.8
        elif runner_anda<0:
            cnt-=1.3
        
        
        
        if pulando:    
            runner.Pula()
            if runner.y+runner.yi>=runner.yinit+runner.yiinit:
                pulando=0
                runner.y=runner.yinit+runner.yiinit-runner.yi
        
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
        if cnth>80:
            cnth=0
        clock.tick(60)

game_loop()
pygame.quit()
quit()