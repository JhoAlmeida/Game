import os
import pygame
pygame.init()
os.system("cls")
print ("Comecando o Jogo de Futebol")

largura = 500
altura = 300
tamanho = (largura,altura) #tupla - imutavel -> nao pode alterar os valores
display = pygame.display.set_mode (tamanho)
pygame.display.set_caption ("Jogo de Futebol")

branco = (255, 255, 255)
#looping para ficar rodando o jogo
while True:
    display.fill(branco)
