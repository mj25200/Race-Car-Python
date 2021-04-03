#-*- coding: utf-8 -*-
#Quem usar Python2 precisa de incluir isto... no Python3 não...  
#(tem a ver com a codificação do texto)
# O intrepretador de Python 2 assume que o programa está escrito em
# ASCII. Como em ASCII não existem os carateres acentuados do
# português todos os comentários escritos em português dão erro
# (caracter inválido). A forma de contornar isto em Python 2 é indicar
# que o programa está escrito em utf8 (é uma norma de codificação de
# caracteres Unicode. Os caracteres Unicode têm comprimento ilimitado
# e por isso acomodam totas as línguas presentes e futuras :-)). O
# intrepretador Python 3 já assume que o programa está escrito em
# Unicode/utf8 e por isso não é preciso fazer nada.


# Importar o módulo pygame
# se a execução deste import em Python3 ou Python2 der algum erro
# é porque o pygame não está bem instalado
import pygame, sys
from pygame.locals import *
from math import cos, sin, sqrt


# inicialização do módulo pygame
pygame.init()

# criação de uma janela
largura = 1098
altura  = 618
tamanho = (largura, altura)
janela  = pygame.display.set_mode(tamanho)
pygame.display.set_caption('Automobile on track') #nome da janela
#Nesta janela o ponto (0,0) é o canto superior esquerdo
#e (532-1,410-1) = (531,409) o canto inferior direito.

#ler um som de background
pygame.mixer.pre_init(44100,-16,2,2048)
som = pygame.mixer.Sound('carsound.ogg')
som.set_volume(0.1)


# número de imagens por segundo
frame_rate = 30

# relógio para controlo do frame rate
clock = pygame.time.Clock()

# ler uma imagem em formato bmp
pista = pygame.image.load("circuit.png")
carro = pygame.image.load("car.png")

    
#Inicializa o tempo
t=0.0


#########################
#Para escrever o tempo:
font_size = 25
font = pygame.font.Font(None, font_size) # fonte pré-definida
antialias = True # suavização
WHITE = (255, 255, 255)# cor (terno com os valores Red, Green, Blue entre 0 e 255)
#######################

#(A) Se descomentar aqui (e comentar B) vejo onde passou/ rasto da trajetória
# Pois neste caso só junta a pista uma vez,
#no outro caso está sempre a juntar/desenhar a pista
#janela.blit(pista, (0, 0))

  

##################################
##Exemplo ajustado à pista

def parametrizacao (t):
    if t==0:
        resultado=(650,129) #ponto incial
    if 0<t<=4.0:
        resultado=(650-307*t/5,129+77*t/5) #AB,reta1
    if 4.0<t<=6.9:
        resultado=(350-175*cos(-t+6),380-200*sin(-t+6))#Elipse
    if 6.9<t<=11:
        resultado=(356+500*(t-6.9)/4,563-98*(t-6.9)/4)#CD, reta2
    if 11.0<t<=14:
        resultado=(925-224*cos(-t+15)/2.1,369-177*sin(-t+15)/2.1)#Circunferência1
    if 14<t<=17:
        resultado=(928-172*(t-14)/4,280+95*(t-14)/4)#EF,reta3
    if 17<t<=19.5:
        resultado=(756-41*(t-17)/4,403-30*(t-17)/4)#FG,reta4
    if 19.5<t<=20.95:
        resultado=(715-66*(t-19.5)/4,411-25*(t-19.5)/4)#GH,reta5
    if 20.95<t<=22.5:
         resultado=(649-107*(t-20.95)/4,415-30*(t-20.95)/4)#HT,reta10
    if 22.5<t<=25.75:
        resultado=(542-98*(t-22.5)/4,380+45*(t-22.5)/4)#TU,reta11
    if 25.75<t<=28:
         resultado=(427+146*cos(t-30)/1.20,382+146*sin(t-30)/1.20)#Circunferência2
    if 28<t<=31:
       resultado=(410+278*(t-28)/3.9,303-74*(t-28)/3.9)#IJ,reta6
    if 31<t<=35.20:
       resultado=(688+372*(t-31)/3.75,249-98*(t-31)/3.75)#JM,reta7
    if 35.20<t<=39.10:
      resultado=(1060-372*(t-35.20)/3.55,171+98*(t-35.20)/3.55)#MJ,reta8
    if 39.10<t<=41.30:
      resultado= (688-38*(t-39.10)/3.20,249-220*(t-39.10)/3.20)#JA,reta9
    if 41.30<t:
      resultado=(650,129) #ponto inicial
    return resultado
    
    imagem = pygame.image.load('car.png')

def rodar_carro(t):
    global angulo

    if t ==0:
        angulo = 0
    if 0<t<=4.0:
        angulo = 0
    if 4.0<t<=4.3:
        angulo = 20
    if 4.3<t<=4.6:
        angulo = 40
    if 4.6<t<=4.9:
        angulo = 60
    if 4.9<t<=5.2:
        angulo = 80
    if 5.2<t<=5.5:
        angulo = 100
    if 5.5<t<=5.8:
        angulo = 120
    if 6.1<t<=6.4:
        angulo = 140
    if 6.4<t<=6.7:
        angulo = 160
    if 6.7<t<=7.0:
        angulo = 170
    if 7.0<t<=11.0:
        angulo = 180
    if 11.0<t<=11.3:
           angulo = 200
    if 11.3<t<=11.6:
        angulo = 220
    if 11.6<t<=11.9:
        angulo = 240
    if 11.9<t<=12.2:
        angulo = 260
    if 12.2<t<=12.5:
        angulo = 280
    if 12.5<t<=12.8:
        angulo = 300
    if 13.1<t<=13.4:
        angulo = 330
    if 13.4<t<=13.7:
        angulo = 350
    if 13.7<t<=14.0:
        angulo = 360
    if 14.0<t<=17.0:
        angulo = 0
    if 17.0<t<=19.5:
        angulo = -10
    if 19.5<t<=20.95:
        angulo = -20
    if 20.95<t<=22.5:
        angulo = -30
    if 22.5<t<=25.75:
        angulo = 20
    if 25.75<t<=26:
        angulo = -70
    if 26<t<=26.25:
        angulo = -90
    if 26.25<t<=26.50:
        angulo = -120
    if 26.75<t<=27:
        angulo = -140
    if 27.25<t<=27.50:
        angulo = -150
    if 27.50<t<=27.75:
        angulo = -160
    if 27.75<t<=28.0:
        angulo = -170
    if 28<t<=35.20:
        angulo = 180
    if 35.20<t<=39.0:
        angulo = 0
    if 39.10<t<=41.30:
         angulo = -90
    if 41.30<t:
        angulo = 0
 
    return angulo 

def angulo(t):
    if t == 0:
        angulo = 0
        carro2 = pygame.transform.rotate(image,angulo)
        
    if 0<t<=5.8:
        angulo = 360
        carro2 = pygame.transform.rotate(image,angulo)
    return angulo

        
def velocidade (t):
    if t == 0.0:
        velocidade = 0.0 # Velocidade inicial
    if 0.0 < t <= 4.0:
        velocidade = sqrt(((307)**2)+((98)**2))/5 # Velocidade em AB
    if 4.0 < t <= 6.9:
        velocidade = ( 175*(-1)*sin(-t+6)+200*cos(-t+6)) # Velocidade Elipse
    if 6.9 < t <= 11.0:
         velocidade = sqrt(((500)**2)+((98)**2))/4 # Velocidade em CD

    if 11.0<t<=14.0:
       velocidade = ( 224*(-1)*sin(-t+15)-177*cos(-t+15))/1.5  # Velocidade na Circunferência 1
    if 14.0<t<=17:
       velocidade = sqrt(((172)**2)+((95)**2))/4 # Velocidade  EF
    if 17<t<=19.5:
        velocidade = sqrt(((41)**2)+((30)**2))/4 # Velocidade FG
    if 19.5<t<=20.95:
        velocidade = sqrt(((66)**2)+((25)**2))/4 # Velocidade GH

    if 20.95<t<=22.5:
        velocidade = sqrt(((107)**2)+((30)**2))/4 # Velocidade HT

    if 22.5<t<=25.75:
        velocidade = sqrt(((98)**2)+((45)**2))/4 # Velocidade TU

    if  25.75<t<=28:
        velocidade = ( 146*(-1)*sin(t-30)+146*cos(t-30))/1.20 # Velocidade Circunferência 2         
    if 28<t<=31:
        velocidade = sqrt(((278)**2)+((74)**2))/3.9 # Velocidade IJ    
    if 31<t<=35.20:

        velocidade = sqrt(((372)**2)+ ((98)**2))/3.75 # Velocidade JM
    if 35.20<t<=39.10:
        velocidade = sqrt( ((372)**2) + ((98)**2))/3.55 # Velocidade MJ
    if 39.10<t<=41.30:
        velocidade = sqrt(((38)**2)+((220)**2))/3.20 # Velocidade  JA     
    if 41.30<t:
        velocidade = 0.0 # Velocidade Final 
    return velocidade
pygame.mixer.music.load('carsound.ogg')
pygame.mixer.music.play(-1)

#################################
#Ciclo principal do jogo
while True:
    angulo  = rodar_carro(t)
    carro2 = pygame.transform.rotate(carro,angulo)
    tempo= font.render("t="+str(t), antialias, WHITE)
    velocimetro = font.render("v="+str(velocidade(t)), antialias, WHITE)
    janela.blit(pista, (0, 0))  #(B) se descomentar aqui (e comentar (A)) vejo movimento
    janela.blit(carro2, parametrizacao(t))
    janela.blit(tempo, (10, 10))
    janela.blit(velocimetro,(10,50))
    pygame.display.update()
    clock.tick(frame_rate)
    t=t+0.1
    

    
    for event in pygame.event.get():
        #Para sair...
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #Ao clicar em qualquer local, o tempo recomeça com t=0
        # evento mouse click botão esquerdo (código = 1)
        #elif event.type== pygame.MOUSEBUTTONUP and event.button == 1:
        #    t = 0
                       

##        #Quando queremos saber as coordenadas de um ponto: 
##        # descomentar isto e comentar o "evento mouse click"...
##        #"clicar" nesse ponto... o python print as coordenadas.
##        # evento mouse click botão esquerdo (código = 1)
        elif event.type== pygame.MOUSEBUTTONUP and event.button == 1:
            (x, y) = event.pos
            localizacao="posicao=(" + str(x) + "," + str(y) + ")"
            print(localizacao)


##FAQs:
##            (1)
##            Quando parametrização (ou velocidade) não está definida
##            para algum valor de t, dá o erro:
##                "local variable "result/resultado" referenced before assignment"
##            
            




