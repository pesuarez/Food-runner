# -*- coding: utf-8 -*-
"""
Created on Fri May 12 23:31:38 2017

@author: Samuel
"""

import pygame
import copy
import random
import json
from operator import itemgetter

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
        self.x_change=10
        self.vida=0
        self.vidan=195
        self.vidam=195
        self.file=arquivo
        
    def Mostra(self,x,y):
        gameDisplay.blit(self.main,(x,y))
        
    def Copy(self):
        return self
        
    def Recarrega(self, P):
        if not P==12:
            self.main=pygame.image.load("Bonecos/"+self.fisico+"/G("+str(P+1)+").png")        
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
        gameDisplay.blit(self.texto,(self.x+(self.xi/2)-(self.texto.get_rect()[2]/2), self.y-(self.texto.get_rect()[3]/2)+self.yi/2))
        
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



h_yi=int(runner.xi/2)
chaoaux=pygame.image.load(nomedofundo)
hamburguer = Objeto("hamburguer.png",display_width,runner.y + runner.yi - h_yi,int(runner.xi/2),h_yi)
alface = Objeto("alface.png",display_width,runner.y + runner.yi - h_yi,int(runner.xi/2),h_yi)

chao = Objeto(nomedofundo,0,0,int(pygame.Surface.get_width(chaoaux)),int(pygame.Surface.get_height(chaoaux)))
chao.yi=display_height
chao.Tamanho(chao.xi,chao.yi)
chao2=copy.copy(chao)
chao2.x=chao2.x+chao2.xi
chao.x=0
chao.y=0
chao2.x=chao.x+chao2.xi





listarandom=range(int(display_width),int(display_width)*2)
hamburguer.x=display_width+random.choice(listarandom)

runner.Tamanho(runner.xi,runner.yi)
hamburguer.Tamanho(hamburguer.xi,hamburguer.yi)
alface.Tamanho(alface.xi,alface.yi)

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

def Score(pontuacao,i):
    p=str(int(pontuacao))
    #pygame.draw.rect(gameDisplay,pygame.color.Color("black"),(50,50,100,50),5)
    
    score=Objeto("botaop.png",display_width/2,int(display_height/20),int(display_width/2),int(display_height/10))
    
    score.y=-5
    score.x=-115
    
    if i:
        score.Texto("Pontuação",pygame.color.Color("white"),20) 
    else:
        score.Texto("Pontuação",pygame.color.Color("black"),20) 
    score.MostraTexto()
    
    score.y=35
    if i:
        score.Texto(p,pygame.color.Color("white"),30)
    else:
        score.Texto(p,pygame.color.Color("black"),30)    
    
    score.MostraTexto()

   

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
    
    runner.x_change=10
    runner.fisico="Normal"
    runner.vida=0
    runner.vidam=195
    runner.vidan=185
    
    
    

    
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
                    while not botao1.y>display_height:
                        chao.Mostra(chao.x,chao.y)
                        botao1.y+=15
                        botao2.y+=15
                        botao3.y+=15
                        
                        botao1.Mostra(botao1.x,botao1.y)
                        botao1.MostraTexto()
                        botao2.Mostra(botao2.x,botao2.y)
                        botao2.MostraTexto()
                        botao3.Mostra(botao3.x,botao3.y)
                        botao3.MostraTexto()
                        
                        
                        
                        
                        pygame.display.update()
                        clock.tick(50)
                        
                    game_loop()
                    
            else:
                botao1.Texto("Iniciar",pygame.color.Color("black"),40)
            
            if botao2.ColisaoMouse():
                botao2.Texto("Highscores",pygame.color.Color("green"),40)
                
                if pygame.mouse.get_pressed()[0]:
                    highscores=1
                    
                    with open('score.json') as hs:    
                            lista_hs = json.load(hs)                    
                      
                    textohs = Objeto("botaop.png",0,0,0,0)
                    x=display_width/4
                    y=int(display_height/5)+20                
                    
                    while highscores:
                        chao.Mostra(chao.x,chao.y)
                        pygame.draw.rect(gameDisplay, pygame.color.Color("white"), (int(display_width/2-(int(display_width*0.6)/2)),int(display_height/5) ,int(display_width*0.6) ,int(display_height*0.6 ))) 
                        highscoretxt.MostraTexto()                          
                        
                        botaovoltar.Mostra(botaovoltar.x,botaovoltar.y)
                        botaovoltar.MostraTexto()
                                    
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
                                pygame.quit()
                                exit()
                                
                                
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
                        
                        botaoautores=Objeto("botaop.png",int(display_width/2-int(display_width/4)),int(display_height/2),int(display_width/2),int(display_height/6))
                        botaoautores.Tamanho(botaoautores.xi,botaoautores.yi)
                        botaoautores.Mostra(botaoautores.x,botaoautores.y)
                        
                        botaoautores.Texto("Autores",pygame.color.Color("black"),30)
                        botaoautores.MostraTexto()

                        if botaovoltar.ColisaoMouse():
                            botaovoltar.Texto("Voltar",pygame.color.Color("green"),30)
                            if pygame.mouse.get_pressed()[0]:
                                opcoes = 0
                        else:
                            botaovoltar.Texto("Voltar",pygame.color.Color("black"),30)
                            
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:                               
                                game=1
                                opcoes=0

                        pygame.display.update()
                        clock.tick(30)    
                        
                        
                        
            else:
                botao3.Texto("Opções",pygame.color.Color("black"),40)
                    
                
                        
        pygame.display.update()  
        clock.tick(30)
    
def game_loop():           
    cnt=0                           
    cnth=0
    runner.x_change = 10                                                   #Velocidade do objeto
    morto = 0
    pulando=0  
    runner_anda=0 
    gameover=0
    listaf=[hamburguer]
    pontuacao=0
    P=0
    
    fisicor=Objeto("botaop.png",display_width/2,int(display_height/20),int(display_width/2),int(display_height/10))
    fisicor.x=fisicor.x-fisicor.xi/2   
    fisicor.Tamanho(fisicor.xi,fisicor.yi)
     
    
    
    while not morto:
        gameDisplay.fill((255,255,255))                             #Configurações iniciais
        chao.Mostra(chao.x,chao.y)                                 
        chao2.Mostra(chao2.x,chao2.y)        

        pygame.draw.rect(gameDisplay,pygame.color.Color("black"),(display_width-250,50,200,20),5)	#moldura
        pygame.draw.rect(gameDisplay,pygame.color.Color("gray"),(display_width-248,52,runner.vidam,15)) #vida magro
        pygame.draw.rect(gameDisplay,pygame.color.Color("green"),(display_width-248,52,runner.vidan,15))                         #vida normal
        
        if runner.fisico=="Gordo" or runner.fisico=="Muito Gordo":   
            cor=pygame.color.Color("red")
            pygame.draw.rect(gameDisplay,cor,(display_width-248,52,runner.vida,15))
            fisicor.Texto(runner.fisico,cor,40)
            fisicor.MostraTexto()
            
        elif runner.fisico=="Forte" or runner.fisico=="Muito Forte":
            cor=pygame.color.Color("blue")
            pygame.draw.rect(gameDisplay,cor,(display_width-248,52,runner.vida,15))
            fisicor.Texto(runner.fisico,cor,40)
            fisicor.MostraTexto()
            
        elif runner.fisico=="Normal":
            cor=pygame.color.Color("green")
            fisicor.Texto(runner.fisico,cor,40)
            fisicor.MostraTexto()
        else:
            cor=pygame.color.Color("gray")
            fisicor.Texto(runner.fisico,cor,40)
            fisicor.MostraTexto()
        
        if runner.fisico=="Muito Gordo":
            runner.m=1
            pontuacao-=2
        elif runner.fisico=="Gordo":
            runner.m=1.5
            pontuacao-=1
        elif runner.fisico=="Normal":
            runner.m=2.5
            pontuacao+=0.5
        elif runner.fisico=="Magro":
            runner.m=3
            pontuacao-=1
        elif runner.fisico=="Muito Magro:":
            runner.m=4
            pontuacao-=1
        elif runner.fisico=="Forte":
            pontuacao+=1
            runner.m=2.5
        else:
            pontuacao+=2
            runner.m=2.5
        Score(pontuacao,0)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                morto=1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if runner.y==runner.yinit :
                        runner.v=6-runner.x_change*0.01
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
                
        if cnth==60 or cnth==30:            
            if random.choice([0,1]):                
                hamb=copy.copy(hamburguer)                              #Cria um novo hamburguer
                hamb.x=display_width+random.choice(listarandom)         #Posição aleatória da comida
                listaf.append(hamb)                                     #Adiciona a nova comida na lista
            else:
                alfac=copy.copy(alface)                              #Cria um novo hamburguer
                alface.x=display_width+random.choice(listarandom)         #Posição aleatória da comida
                
                listaf.append(alfac)
                
            
        for i in range(len(listaf)):
            Mostrav(listaf)                                         #Display de todas as comidas
            if listaf[i].x<-listaf[i].xi:
                listaf.pop(i)                                       #Remove a comida não capturada                                
                break
            
        for i in range(len(listaf)):
            if runner.Colisao(listaf[i]):
                if listaf[i].file=="alface.png":
                    if runner.fisico=="Gordo" or runner.fisico=="Muito Gordo":
                        if runner.vida-20<1:
                            runner.fisico="Forte"
                            runner.vida=abs(runner.vida-40)
                        else:
                            if runner.vida-20<120:
                                runner.fisico="Gordo"
                            runner.vida-=20
                            
                    elif runner.fisico=="Magro" or runner.fisico=="Muito Magro":
                        if runner.vidam+40>195:
                            runner.fisico="Normal"
                            runner.vidam=195
                            runner.vidan=10
                        else:
                            if runner.vidam+40>120:
                                runner.fisico="Magro"
                            runner.vidam+=40
                            
                    elif runner.fisico=="Forte" or runner.fisico=="Muito Forte":
                            if runner.vida+20>195:
                                runner.vida=195
                            else:
                                if runner.vida+40>120:
                                    runner.fisico="Muito Forte"
                                runner.vida+=20
                    else:
                            if runner.vidan+40>=195:
                                runner.fisico="Forte"
                                runner.vidan=195
                                runner.vida=10
                            else:
                                runner.vidan+=40
                  
                                

                                                                            
                if listaf[i].file=="hamburguer.png":                                    #Caso a comida pega seja hamburguer
                
                    if runner.fisico=="Gordo" or runner.fisico=="Muito Gordo":
                        if runner.vida+80>195:
                            runner.vida=195
                            gameover=1
                            print("explodiu")
                        else:
                            if runner.vida+80>120:
                                runner.fisico="Muito Gordo"
                            runner.vida+=80
                            
                    elif runner.fisico=="Magro" or runner.fisico=="Muito Magro":
                        if runner.vidam+40>195:
                            runner.fisico="Normal"
                            runner.vidam=195
                            runner.vidan=10
                        else:
                            if runner.vidam+40>120:
                                runner.fisico="Normal"
                            runner.vidam+=40
                            
                    elif runner.fisico=="Forte" or runner.fisico=="Muito Forte":
                            if runner.vida-80<1:
                                runner.vida=abs(runner.vida-40)
                                runner.fisico="Gordo"
                                
                            else:
                                if runner.vida-80<120:
                                    runner.fisico="Forte"
                                runner.vida-=80
                                
                    else:
                            if runner.vidan+40>=195:
                                runner.fisico="Gordo"
                                runner.vidan=195
                                runner.vida=10
                            else:
                                runner.vidan+=40
                    
                listaf.pop(i)                                           #Remove o alface da lista                                                                  
                
                break
                            
        if chao.x<-chao.xi:
            chao.x=chao2.x+chao2.xi
        if chao2.x<-chao2.xi:
            chao2.x=chao.x+chao.xi                        
               
        for i in range(len(listaf)):
                listaf[i].x -= runner.x_change                                      
        
        chao.x -= runner.x_change                                          #Atualiza a posição de um dos backgrounds
        chao2.x -= runner.x_change                                         #Atualiza a posição de um dos backgrounds
        
        if not P==12 and not pulando:
            P = descobreP(cnt)
        
        runner.Recarrega(P)                                         #Atualiza a imagem do personagem
        runner.Tamanho(runner.xi,runner.yi)                         #Atualiza o tamanho do personagem       
        runner.Mostra(runner.x,runner.y)                            #Display do personagem
        
        if runner_anda>0:                                           #Acelera o personagem se for pra frente
            cnt+=1.8
        elif runner_anda<0:                                         #Desacelera o personagem se for pra frente
            cnt-=1.3
               
        #gameover=1
        if pulando:                                                 #Função pula
            runner.Pula()                                           
            if runner.y+runner.yi>=runner.yinit+runner.yiinit:
                pulando=0                                           #Colisao com o "Chão"
                runner.y=runner.yinit+runner.yiinit-runner.yi
        
        if gameover:
            inputbox=Objeto("botaop.png",display_width/2-int(display_width/5),int(display_height-100),int(display_width/10),int(display_height/10))
            inputbox.x=display_width/2-45
            inputbox.Texto("Digite seu nome para salvar a pontuação:",pygame.color.Color("white"),20)
            inpute=1
            inputtxt=copy.copy(inputbox)
            inputtxt.y+=50
            
        while gameover:                                             #Testa se acabou o jogo
            gameovert = pygame.image.load("gameover.jpeg")
            gameovert = pygame.transform.scale(gameovert,(display_width,display_height))
            gameDisplay.blit(gameovert,(0,0))

            pygame.draw.rect(gameDisplay,pygame.color.Color("white"),(display_width/2-100,display_height-50,200,40),5)
            inputbox.MostraTexto()
            

            name=""   
            Score(pontuacao,1)
            pygame.display.update()
            clock.tick(30) 
            while inpute: 
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                            morto=1
                            gameover=0
                            inpute=0
                            pygame.quit()
                            exit()

                    if event.type == pygame.KEYDOWN:                   

                        if event.key == pygame.K_r:                   
                            gameover=0                       
                            Reiniciar()
                            P=1
                    
                        if event.unicode.isalpha():
                            name += event.unicode

                        elif event.key == pygame.K_BACKSPACE:
                            name = name[:-1]

                        elif event.key == pygame.K_ESCAPE:
                            gameover=0
                            inpute=0
                            Reiniciar()
                            Menu()

                        elif event.key == pygame.K_RETURN:
                            gameover=0
                            inpute=0
                            morto=1

                            with open('score.json') as hs:    
                                lista_hs = json.load(hs)


                            with open('score.json', 'w') as arquivo:
                                dictionary={"nome":name, "pontos":pontuacao}
                                
                                lista_hs.append(dictionary)
                                print(lista_hs)
                                lista_hs=sorted(lista_hs, key=lambda d: d['pontos'], reverse=True)
                                
                                json.dump(lista_hs, arquivo, indent=4)
                                
    
                            Reiniciar()
                            Menu()

                        
                        if inpute:

                            gameDisplay.blit(gameovert,(0,0))
                            pygame.draw.rect(gameDisplay,pygame.color.Color("white"),(display_width/2-100,display_height-50,200,40),5)
                            inputbox.MostraTexto()
                            inputtxt.Texto(name,pygame.color.Color("white"),15)
                            inputtxt.MostraTexto()
                            Score(pontuacao,1)
                            pygame.display.update()
                            clock.tick(30)
                       
        pygame.display.update()                                     #Atualiza o display geral
        cnt+=3
        cnth+=1      
        
        if cnt>60: #Contador utilizado para o movimento do personagem
            cnt=0
            runner.x_change+=0.3

        if cnth%5==0:    
            if runner.fisico=="Gordo" or runner.fisico=="Muito Gordo" or runner.fisico=="Forte" or runner.fisico=="Muito Forte":
                runner.vida-=1
                
                if runner.vida<2:
                    runner.fisico="Normal"
                    runner.vidan=195
                elif runner.vida==118:
                    runner.fisico==runner.fisico.replace("Muito ","")
                
                    
                
            elif runner.fisico=="Normal":
                runner.vidan-=2
                if runner.vidan<2:
                    runner.fisico="Magro"
                    runner.vidam=195
                    runner.vidan=0
                
            elif runner.fisico=="Magro" or runner.fisico=="Muito Magro":
                runner.vidam-=2
                if runner.vidam<2:
                    gameover=1
                elif runner.vidam<120:
                    runner.fisico="Muito Magro"                
                    
        if cnth>80: #Contador utilizado para a atualização dos objetos 
            cnth=0
        
        clock.tick(30)
        
Menu()
pygame.quit()
quit()