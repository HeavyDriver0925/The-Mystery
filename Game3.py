import pygame
import sys
import Menu2
import pickle
import TextWrap
import Story8Final
pygame.init()


# CURRENTLY WORKING ON SAVE SYSTEM

def GAME(savedstory=[]):
      
      screen = pygame.display.set_mode((1024,576))

      gameloop1 = True

      clock = pygame.time.Clock()

      font = pygame.font.Font(None,35)

      testimg = pygame.image.load('Test.png').convert()
      testimg = pygame.transform.scale(testimg,(1024,576))

      rect1 = pygame.Rect(20,500,800,40) # left top width height
      rect2 = pygame.Rect(825,500,30,40)
      rect3 = pygame.Rect(20,200,600,300) # 200 700 300

      SettingsRect = pygame.Rect(910,53,60,60)
      
      SettingsRect2 = pygame.Rect(362,163,300,250)

      SettingsRect3 = pygame.Rect(382,130,276,85)
      SettingsRect4 = pygame.Rect(382,230,276,85)
      SettingsRect5 = pygame.Rect(382,327,276,85)

      color = pygame.Color('white')
      color1 = pygame.Color('Red')

      b = []  # All Commands
      bsavelist = []
      a = ''  # TextBox Text 
      AllCom = [] # All Results From Commands
      
      counts = 0
      ScrollValue = 0 
      randomcount = 0 # DoubleInputs
      c1 = 0

      sx = 1
      sy = 1
      
      b1 = 1

      Settings1 = False

      while gameloop1:
            
            for i in pygame.event.get():
                  if i.type == pygame.QUIT:
                        gameloop1 = False
                              
                  if i.type == pygame.KEYDOWN:
                        if i.key == pygame.K_RETURN:
                              if a != ' ' and a != '':
                                    b.append(a)
                                    bsavelist.append(a)

                                    if len(savedstory) != 0:
                                          savedstory.append(a)

                              a = ''
                              counts = counts + 50
                        elif i.key == pygame.K_BACKSPACE:
                              a = a[:-1]
                        else:
                              a = a + i.unicode
                  if i.type == pygame.MOUSEBUTTONDOWN:
                        if i.button == 4 and ScrollValue > 0:
                              ScrollValue = ScrollValue - 20
                        elif i.button == 5 and ScrollValue < counts and len(b) > 5:
                              ScrollValue = ScrollValue + 20
                        if rect2.collidepoint(i.pos):
                              print('COLLIDED 1')
                              bl = not bl    
                        if SettingsRect.collidepoint(i.pos):
                              Settings1 = not Settings1
                              print('Collided')
                        if Settings1 == True:

                              if SettingsRect3.collidepoint(i.pos):
                                    Settings1 = False
                              if SettingsRect4.collidepoint(i.pos):
                                    print('GAME SAVED!')
                                    SaveFile = open('GameSave.dat','ab+')
                                    pickle.dump(bsavelist,SaveFile)
                                    SaveFile.close()
                              if SettingsRect5.collidepoint(i.pos):
                                    print('Gameloop Now False')
                                    Menu2.MENU()
                                    
            #z,y = pygame.mouse.get_pos()

            screen.blit(testimg,(0,0))
            
            textsurf = font.render(a,True,color) # Current Text 
                  
            #pygame.draw.rect(screen,color,rect1,3)  # Text Box # screen color rect border/fill

            ######## SETTINGS #########
            
            #pygame.draw.rect(screen,pygame.Color('red'),SettingsRect,4)


            if len(b) > b1:
                  b = b[::-1]
                  b1 = b1 + 1
            
            if len(b) != randomcount:
                  
                  TextList,sx,sy = Story8Final.Story(b[0],sx,sy)
                  
                  AllCom.extend(TextList)
                  
                  randomcount = randomcount + 1

            
            if 'TextList' in locals():
                  for i in TextList:
                        TextL = TextWrap.TextR(i)        
            else:
                  
                  TextL = TextWrap.TextR("You wake up in a small grey room on a cold hard floor, there's a door in front of you and a huge wooden table on your left")

            TextSpace = 0
                  
            if ScrollValue > 0:
                  texty = ScrollValue + 455
            else:
                  texty = 455

            if len(savedstory) == 0:
                  
                  if len(b) != 0:

                        for i in range(-1,-(len(AllCom))-1,-1):
                              
                              WrappedText = TextWrap.TextP(AllCom[i])
                              
                              for j in WrappedText:
                                    textsurf3 = font.render(j,True,color) # Text Print on Screen
                                    if texty > 50 and texty < 456:
                                          screen.blit(textsurf3,(30,texty))  # Text Log Print In Box
                                    texty = texty - 20 # Spacing for text box
                              texty = texty - 20
                              
                  else:
                        # TO PUT THE FIRST TEXT
                        
                        for i in range(len(TextL)):
                              textsurf3 = font.render(TextL[i],True,color)
                              screen.blit(textsurf3,(30,texty))
                              texty = texty - 20


            else:

                  # This is the part If the code has some text in it already

                  # put the returned coordinates here to fix the coordinates here to fix the issue

                  SavedTextList = []

                  SavedCo = []

                  sx,sy = 1,1

                  SavedTextList.extend(["You wake up in a small grey room on a cold hard floor, there's a door in front of you and a huge wooden table on your left"])

                  for i in savedstory:
                        
                        SavedTextList1,sx,sy = Story8Final.Story(i,sx,sy)

                        SavedTextList.extend(SavedTextList1)
                              
                  for i in range(-1,-(len(SavedTextList))-1,-1):

                        WrappedText = TextWrap.TextP(SavedTextList[i])
                        
                        for j in WrappedText:
                              
                              stextsurf = font.render(j,True,color)
                              screen.blit(stextsurf,(30,texty))
                              texty = texty - 20
                  
                        texty = texty - 20

            # TO PUT THE FIRST TEXT
            
            if c1 == 0:                  
                  AllCom.extend(["You wake up in a small grey room on a cold hard floor, there's a door in front of you and a huge wooden table on your left"])
            c1 = c1 + 1
            
            screen.blit(textsurf,(40,508)) # Text
                  
            clock.tick(50) # Maximum Frames Per Seconds
                        
            if Settings1 == True:


                  testimg1 = pygame.image.load('Test1.png').convert()

                  screen.blit(testimg1,(0,0))                  

            pygame.display.update() # Display Update

            
            if gameloop1 == False:
                  pygame.quit()
                  sys.exit()

