# -*- coding: utf-8 -*-
"""
Created on Fri May 12 23:31:38 2017

@author: Samuel
"""

import pygame
import copy
import random
import json

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
        self.m=2.5
        self.pontos=0
        self.fisico="Normal"
        
    def Mostra(self,x,y):
        gameDisplay.blit(self.main,(x,y))
        
    def Copy(self):
        return self
        
    def Recarrega(self, P):
        if P==0:
            self.main=pygame.image.load("Bonecos/"+self.fisico+"/G(1).png")
        elif P==1:
            self.main=pygame.image.load("Bonecos/"+self.fisico+"/G(2).png")
        elif P==2:
            self.main=pygame.image.load("Bonecos/"+self.fisico+"/G(3).png")
        elif P==3:
            self.main=pygame.image.load("Bonecos/"+self.fisico+"/G(4).png")
        elif P==4:
            self.main=pygame.image.load("Bonecos/"+self.fisico+"/G(5).png")
        elif P==5:
            self.main=pygame.image.load("Bonecos/"+self.fisico+"/G(6).png")
        elif P==6:
            self.main=pygame.image.load("Bonecos/"+self.fisico+"/G(7).png")
        elif P==7:
            self.main=pygame.image.load("Bonecos/"+self.fisico+"/G(8).png")
        elif P==8:
            self.main=pygame.image.load("Bonecos/"+self.fisico+"/G(9).png")
        elif P==9:
            self.main=pygame.image.load("Bonecos/"+self.fisico+"/G(10).png")
        elif P==10:
            self.main=pygame.image.load("Bonecos/"+self.fisico+"/G(11).png")
        elif P==11:
            self.main=pygame.image.load("Bonecos/"+self.fisico+"/G(12).png")
        else:
            self.main=pygame.image.load("Bonecos/"+self.fisico+"/G(Deitado).png")
    
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
    
    def ColisaoMouse(self):
        mouse=pygame.mouse.get_pos()
        if mouse[0]>self.x and mouse[0]<self.x+self.xi and mouse[1]>self.y and mouse[1]<self.y+self.yi:
            return 1
    
    def Tamanho(self, x, y):
        
        self.main = pygame.transform.scale(self.main,(x,y))
        
    def MostraTexto(self):
        gameDisplay.blit(self.texto,self.recttxt)
        
    def Texto(self, texto,cor,tam):
        
        txtbotao = pygame.font.Font("freesansbold.ttf",tam)
        txtobj = txtbotao.render(texto, True, cor)
        self.texto=txtobj
        self.recttxt=(self.x+(self.xi/2)-(self.texto.get_rect()[2]/2), self.y-(self.texto.get_rect()[3]/2)+self.yi/2)
        
        
        
        
        
                       





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

myfont = pygame.font.SysFont("Arial", 25)

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
    if cnt>=0 and cnt<5:
        return 0
    elif cnt>=5 and cnt<10:
        return 1
    elif cnt>=10 and cnt<15:
        return 2
    elif cnt>=15 and cnt<20:
        return 3
    elif cnt>=20 and cnt<25:
        return 4
    elif cnt>=25 and cnt<30:
        return 5
    elif cnt>=30 and cnt<35:
        return 6
    elif cnt>=35 and cnt<40:
        return 7
    elif cnt>=40 and cnt<45:
        return 8
    elif cnt>=45 and cnt<50:
        return 9
    elif cnt>=50 and cnt<55:
        return 10
    else:
        return 11

def Score(pontuacao):
    p=str(pontuacao)
    score = pygame.image.load("energymold.png")
    score = pygame.transform.scale(score,(150,50))
    texto = myfont.render("Pontuação: ", 1, (130,30,0))
    pontos = myfont.render(p, 1, (130,30,0))
    gameDisplay.blit(texto, (20, 5))
    gameDisplay.blit(score,(20,30))
    gameDisplay.blit(pontos, (25, 50))

def Attpont(x):
    x=int(x)
    x=+50
    p=str(x)
    pontos = myfont.render(p, 1, (130,30,0))
    gameDisplay.blit(pontos, (25, 50))
    return x

def Gameover():
    gameover = pygame.image.load("gameover.jpeg")
    gameover = pygame.transform.scale(gameover,(display_width,display_height))
    gameDisplay.blit(gameover,(0,0))

def texto_objetos(texto,fonte):
    txtobj = fonte.render(texto, True, pygame.color.Color("black"))
    return txtobj, txtobj.get_rect()
    
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
        
def Menu():
    game=0
    botao1=Objeto("botaop.png",display_width/2,display_height/2,int(display_width/2),int(display_height/6))
    botao1.x=botao1.x-botao1.xi/2   
    botao1.Tamanho(botao1.xi,botao1.yi)
    
    botao2=copy.copy(botao1)
    botao2.y+=botao1.yi
    botao3=copy.copy(botao2)
    botao3.y+=botao2.yi
    
    botao1.Texto("Iniciar",pygame.color.Color("black"),40)
    botao2.Texto("Highscores",pygame.color.Color("black"),40)
    botao3.Texto("Opções",pygame.color.Color("black"),40)
    
    highscoretxt=Objeto("botaop.png",display_width/2,int(display_height/20),int(display_width/2),int(display_height/10))
    highscoretxt.x=highscoretxt.x-highscoretxt.xi/2   
    highscoretxt.Tamanho(highscoretxt.xi,highscoretxt.yi)
    highscoretxt.Texto("High scores",pygame.color.Color("black"),80)    
   
    while not game:
        chao.Mostra(chao.x,chao.y)
        botao1.Mostra(botao1.x,botao1.y)
        botao2.Mostra(botao2.x,botao2.y)
        botao3.Mostra(botao3.x,botao3.y)
        
        botao1.MostraTexto()
        botao2.MostraTexto()
        botao3.MostraTexto()
        
        botaovoltar=Objeto("botaop.png",int(display_width/18),int(display_height*0.8),int(display_width/6),int(display_height/6))
        botaovoltar.Tamanho(botaovoltar.xi,botaovoltar.yi)
        botaovoltar.Texto("Voltar",pygame.color.Color("black"),40)
                    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:     
                game=1
                
            if botao1.ColisaoMouse():
                botao1.Texto("Iniciar",pygame.color.Color("green"),40)
                if pygame.mouse.get_pressed()[0]:
                    game=1
                    game_loop()
            else:
                botao1.Texto("Iniciar",pygame.color.Color("black"),40)
            
            if botao2.ColisaoMouse():
                botao2.Texto("Highscores",pygame.color.Color("green"),40)
                
                if pygame.mouse.get_pressed()[0]:
                    highscores=1
                    
                    with open('score.json') as hs:    
                            lista_hs = json.load(hs)
                    
                    print(lista_hs)  
                    textohs = Objeto("botaop.png",0,0,0,0)
                    x=display_width/4
                    y=int(display_height/5)+20
                    
                    
                    
                    while highscores:
                        chao.Mostra(chao.x,chao.y)
                        pygame.draw.rect(gameDisplay, pygame.color.Color("white"), (int(display_width/2-(int(display_width*0.6)/2)),int(display_height/5) ,int(display_width*0.6) ,int(display_height*0.6 ))) 
                        highscoretxt.MostraTexto()  
                        
                        
                        botaovoltar.Mostra(botaovoltar.x,botaovoltar.y)
                        botaovoltar.MostraTexto()
            
                        #textohs.Texto(str([i["nome"] for i in lista_hs]),pygame.color.Color("black"),25)
                        
                        #textohs.MostraTexto()
                        textohs = pygame.font.Font("freesansbold.ttf",32)
                        
                        
                        
                        for i in range(len(lista_hs)):
                            if not i>=5:
                                gameDisplay.blit(texto_objetos(lista_hs[i]["nome"],textohs)[0],(x,(y+(i*70))))
                                gameDisplay.blit(texto_objetos(str(lista_hs[i]["pontos"]),textohs)[0],(x+300,(y+(i*70))))
                            
                           
                        
                        if botaovoltar.ColisaoMouse():
                            botaovoltar.Texto("Voltar",pygame.color.Color("green"),30)
                            if pygame.mouse.get_pressed()[0]:
                                highscores = 0
                        else:
                            botaovoltar.Texto("Voltar",pygame.color.Color("black"),30)
                            
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                highscores = 0
                                game=1
                                
                                
                        pygame.display.update()
                        clock.tick(30)
            else:
                botao2.Texto("Highscores",pygame.color.Color("black"),40)
                
                
                
                
                
            if botao3.ColisaoMouse():
                botao3.Texto("Opções",pygame.color.Color("green"),40)
                
                if pygame.mouse.get_pressed()[0]:
                    opcoes = 1
                    
                    
                    while opcoes:
                        chao.Mostra(chao.x,chao.y)
                        botaovoltar.Mostra(botaovoltar.x,botaovoltar.y)
                        botaovoltar.MostraTexto()        
        			        
                           
                        



                        if botaovoltar.ColisaoMouse():
                            botaovoltar.Texto("Voltar",pygame.color.Color("green"),30)
                            if pygame.mouse.get_pressed()[0]:
                                opcoes = 0
                        else:
                            botaovoltar.Texto("Voltar",pygame.color.Color("black"),30)
                            
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                highscores = 0
                                game=1

                        pygame.display.update()
                        clock.tick(30)    
                        
                        
                        
            else:
                botao3.Texto("Opções",pygame.color.Color("black"),40)
                    
                
                        
        pygame.display.update()  
        clock.tick(30)
    
def game_loop():           
    cnt=0                           
    cnth=0
    x_change = 10                                                   #Velocidade do objeto
    morto = 0
    pulando=0  
    runner_anda=0 
    gameover=0
    listaf=[hamburguer]
    pontuacao=0
    P=0
    while not morto:
        gameDisplay.fill((255,255,255))                             #Configurações iniciais
        chao.Mostra(chao.x,chao.y)                                 
        chao2.Mostra(chao2.x,chao2.y)
        pygame.fisico="Gorcddo"

        if runner.fisico=="Gordo" or runner.fisico=="Muito Gordo":
        	cor=pygame.color.Color("red")
        elif runner.fisico=="Forte" or runner.fisico=="Muito Forte":
        	cor=pygame.color.Color("blue")
        elif runner.fisico=="Normal":
        	cor=pygame.color.Color("green")
        else:
        	cor=pygame.color.Color("gray")

        pygame.draw.rect(gameDisplay,pygame.color.Color("black"),(display_width-250,50,200,20),5)	#moldura
        pygame.draw.rect(gameDisplay,cor,(display_width-248,52,195,15))		#barra vida


        #vidam.Mostra(vidam.x,vidam.y)
        #vida.Mostra(vida.x,vida.y)
        Score(pontuacao)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                morto=1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if runner.y==runner.yinit :
                        runner.v=6-x_change*0.01
                        pulando=1
                        P=11         
                            
                if event.key == pygame.K_DOWN and not pulando :
                        runner_anda=0
                        P = 12                              
                if event.key == pygame.K_LEFT:
                        runner_anda=-5
                        P=0
                if event.key == pygame.K_RIGHT:
                        runner_anda=+5
                        P=0
                if event.key == pygame.K_ESCAPE:        
                        gameover=1
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                        runner_anda=0
                if event.key == pygame.K_RIGHT:
                        runner_anda=0
                if event.key == pygame.K_DOWN:
                        P=0
        
        if runner.x+runner_anda>0 and runner.x+runner_anda<display_width-runner.xi:
            runner.x+=runner_anda                                   #Atualiza a posição do personagem
                
        if cnth==60:            
            hamb=copy.copy(hamburguer)                              #Cria um novo hamburguer
            hamb.x=display_width+random.choice(listarandom)         #Posição aleatória da comida
            listaf.append(copy.copy(hamb))                          #Adiciona a nova comida na lista                
            
        for i in range(len(listaf)):
            Mostrav(listaf)                                         #Display de todas as comidas
            if listaf[i].x<-listaf[i].xi:
                listaf.pop(i)                                       #Remove a comida não capturada
                pontuacao=Attpont(pontuacao)                
                break
            
        for i in range(len(listaf)):
            if runner.Colisao(listaf[i]):
                listaf.pop(i)                                       #Remove a comida da lista                 
                if not vida.xi-40<1:                                #Verifica se a vida não fica negativa
                    vida.xi-=40                                     #Remove 40 pixels de vida do personagem
                else:
                    gameover=1                                      #A vida ficaria negativa, logo, gameover                   
                vida.Tamanho(vida.xi,vida.yi)                       #Atualiza o tamanho da barra da vida
                break
                            
        if chao.x<-chao.xi:
            chao.x=chao2.x+chao2.xi
        if chao2.x<-chao2.xi:
            chao2.x=chao.x+chao.xi                        
               
        for i in range(len(listaf)):
                listaf[i].x -= x_change
                    
                  
        
        chao.x -= x_change                                          #Atualiza a posição de um dos backgrounds
        chao2.x -= x_change                                         #Atualiza a posição de um dos backgrounds
        
        if not P==12 and not pulando:
            P = descobreP(cnt)
        
        runner.Recarrega(P)                                         #Atualiza a imagem do personagem
        runner.Tamanho(runner.xi,runner.yi)                         #Atualiza o tamanho do personagem       
        runner.Mostra(runner.x,runner.y)                            #Display do personagem
        
        if runner_anda>0:                                           #Acelera o personagem se for pra frente
            cnt+=1.8
        elif runner_anda<0:                                         #Desacelera o personagem se for pra frente
            cnt-=1.3
               
        
        if pulando:                                                 #Função pula
            runner.Pula()                                           
            if runner.y+runner.yi>=runner.yinit+runner.yiinit:
                pulando=0                                           #Colisao com o "Chão"
                runner.y=runner.yinit+runner.yiinit-runner.yi
        
        if gameover==1:                                             #Testa se acabou o jogo
            Gameover()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:                   
                    gameover=0
                    Reiniciar()
                       
        pygame.display.update()                                     #Atualiza o display geral
        cnt+=3
        cnth+=1
        
        if cnt>60: #Contador utilizado para o movimento do personagem
            cnt=0
            x_change+=0.3

        if cnth>80: #Contador utilizado para a atualização dos objetos 
            cnth=0
        
        clock.tick(30)
        
Menu()
pygame.quit()
quit()