# move []

# e = Empty Slot
# l = Locked Slot
# d = Door
# p = Player
# ke = Key
# ta = Table
iv = []

def Story(a,x=1,y=1):
      global iv
      gamed = {'north':'You moved north',
               'east':'You moved east',
               'west':'You moved west',
               'south':'You moved south',
               'door':'You walk closer to the door, you try to open it but it appears to be locked. It requires a key',
               'door2':'You walk closer to the door',
               'inspdoor':"It's an old wooden door.",
               'inspkey':"It's a key with a triangular shaped end, mabye you can use it to open the door ",
               'table':'You walk closer to the huge wooden table. You think of inspecting it.',
               'insptable':'You try to inspect the table closely. It seems that the table is very clean and placed in the center of the wall. You look under the table There is a key neatly placed in the centre. You pick up the key.',
               'win':'You use your key to unlock the door, the Door opens.',
               'org':'Back to original position.',
               'na1':'You cannot go there',
               'na2':'You cannot use it here',
               'na3':'You dont have an item named Key in inventory',
               'temp1':'This is a temp string',
               'na4':'No item here to inspect'}


      d = gamed['door']
      l = gamed['na1']
      ta = gamed['table']
      insptable = gamed['insptable']
      inspdoor = gamed['inspdoor']
      inspkey = gamed['inspkey']
      usekey = gamed['win']
      e = gamed['org']
      temp = gamed['temp1']
      ree = []
      n = gamed['north']
      s = gamed['south']
      e1 = gamed['east']
      w = gamed['west']
      b = a.split()

      c = [[l,d,l],
           [l,e,ta,l],
           [l,l,l]]

      # c[x][y]
      # c[0][1] Door
      # c[1][1] Player
      # c[0][2] Empty
      # c[1][2] Table
      # c[2][1] Locked Slot Player South
      # c[1][0] Locked Slot Player West
 
      if b[0] == 'move':
            if b[1] == 'north':
                  x = x - 1
                  ree.append(n + ' ' +c[x][y])
                  if c[x][y] == l or x < 0:
                        x = x + 1
                  
            elif b[1] == 'south':
                  x = x + 1
                  ree.append(s + ' ' + c[x][y])
                  if c[x][y] == l or x < 0:
                        x = x - 1
                  
            elif b[1] == 'east':
                  y = y + 1
                  try:
                        ree.append(e1 + ' '+ c[x][y])
                  except:
                        y = y - 1
                  if c[x][y] == l:
                        y = y - 1            
            elif b[1] == 'west':
                  y = y - 1
                  ree.append(w + ' ' +c[x][y])
                  if c[x][y] == l or y < 0:
                        y = y + 1
            else:
                  
                  ree.append('Please enter a valid direction')
      
      elif b[0] == 'inspect':
            if b[1] == 'table':
                  if x == 1 and y == 2:
                        ree.append(insptable)
                        iv.append('key')
                  else:
                        ree.append('Nothing to inspect here')
                  
            elif b[1] == 'door':
                  if x == 0 and y == 1:
                        ree.append(inspdoor)
                  else:
                        ree.append('Nothing to inspect here')

            elif b[1] == 'key':
                  for i in iv:
                        if i == 'key':
                              ree.append(inspkey)
                              break
                  else:
                        ree.append('Nothing to inspect here')
            
      elif b[0] == 'use':
            if x == 0 and y == 1:
                  for i in iv:
                        if i == 'key':
                              ree.append(usekey)
                              ree.append('You escaped the room. You Win! ')
                              break
                  else:
                        ree.append('You dont have the item')
            else:
                  ree.append('Cannot use it here')

      else:
            
            ree.append('Please enter a valid command.')
            
      return ree,x,y

def StoryRepeat(a):
      # A is the list of commands
      b = []
      for i in a:
           b.append(Story(i))

      return b
