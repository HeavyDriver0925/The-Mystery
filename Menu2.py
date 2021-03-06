import pygame
import sys
import Game3
import pickle
import Story8Final
pygame.init()

def MENU():
      
      screen2 = pygame.display.set_mode((1024,576))

      caption = pygame.display.set_caption("The Mystery")

      treasure = pygame.image.load("chest.png")

      icon = pygame.display.set_icon(treasure)

      rect1 = pygame.Rect(320,189,383,37)

      rect2 = pygame.Rect(320,269,383,37)

      rect3 = pygame.Rect(320,349,383,37)

      font = pygame.font.Font(None,32)

      #text1 = font.render('New',True,pygame.Color('black'))
      #text2 = font.render('Continue Game',True,pygame.Color('black'))
      #text3 = font.render('Exit Game',True,pygame.Color('black'))

      gameloop = True

      rect1temp = False
      rect2temp = False
      rect3temp = False

      testimg = pygame.image.load('Menu.png').convert()

      while gameloop:
            for i in pygame.event.get():
                  if i.type == pygame.MOUSEBUTTONDOWN:
                        if rect1.collidepoint(i.pos):
                              print('COLLIDED NEW')
                              Game3.GAME()
                              
                        if rect2.collidepoint(i.pos):
                              
                              print('COLLIDED CONTINUE')

                              GameSave = open('GameSave.dat','rb')

                              while True:

                                    try:
                                          GameSaveText = pickle.load(GameSave)
                                          
                                    except:
                                          break

                        
                              Game3.GAME(GameSaveText)
                              
                        

                        if rect3.collidepoint(i.pos):
                              print('COLLIDED EXIT')
                              gameloop = False
                  if i.type == pygame.QUIT:
                        gameloop = False
                  if i.type == pygame.MOUSEMOTION:
                        if rect1.collidepoint(i.pos):
                              rect1temp = True
                        else:
                              rect1temp = False
                        if rect2.collidepoint(i.pos):
                              rect2temp = True
                        else:
                              rect2temp = False
                        if rect3.collidepoint(i.pos):
                              rect3temp = True
                        else:
                              rect3temp = False
                                                     
            if gameloop == False:
                  pygame.quit()
                  sys.exit()
                  break
            screen2.blit(testimg,(0,0))
            if rect1temp == True:
                  pygame.draw.rect(screen2,pygame.Color('Yellow'),rect1,6)
            else:
                  pygame.draw.rect(screen2,pygame.Color('White'),rect1,3)
            #screen2.blit(text1,(462,200))
            if rect2temp == True:
                  pygame.draw.rect(screen2,pygame.Color('Yellow'),rect2,6)
            else:
                  pygame.draw.rect(screen2,pygame.Color('White'),rect2,3)
            #screen2.blit(text2,(462,300))
            if rect3temp == True:
                  pygame.draw.rect(screen2,pygame.Color('Yellow'),rect3,6)
            else:
                  pygame.draw.rect(screen2,pygame.Color('White'),rect3,3)
            #screen2.blit(text3,(462,400))
            
            pygame.display.update()
MENU()

