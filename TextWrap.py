
def TextW(b):
      c = []
      d = 0
      e = 70
      w = True
      
      if len(b) > 70:
            for i in range((len(b)//70)+1):
                  cd1 = b[d:e]
                  for j in range(-1,-len(cd1),-1):
                        if cd1[j] == ' ':
                              de = j
                              break
                  cd = b[d:e+de]
                  d = e + de + 1
                  e = e + 70
                  c.append(cd)
      c = c[::-1]

      print(c)
      return c


def TextS(b):
      a = []
      c = []
      for i in b:
            a.append(i)
      d = 0
      e = ''
      #print(b.split(' ',2))
      #print(len(b))
      for i in a:
            e = e + i
            if i == ' ':
                  print(e)
                  c.append(e)
                  e = ''
            d = d + 1
      print(c)

def TextR(a):
      e = 0 # Starting Position Of Line
      c = 0 # Counter Of Gaps Not Needed
      d = 0 # Counter Of Lines Not Needed
      f = 0 # Position Of Gaps 
      b = []
      #print(a[0:70])
      #print(len(a))
      for i in range(0,len(a)):
            if a[i] == ' ':
                  c = c + 1
                  f = i
            if i % 70 == 0 and i != 0:
                  b.append(a[e:f+1])
                  e = f
                  d = d + 1
                  
            elif i > 70 * (len(a) // 70):
                  b.append(a[e:])
                  break
      return b[::-1]

def TextP(a):
      e = 0 # Starting Position Of Line
      c = 0 # Counter Of Gaps Not Needed
      d = 0 # Counter Of Lines Not Needed
      f = 0 # Position Of Gaps 
      b = []
      #print(a[0:70])
      #print(len(a))
      for i in range(0,len(a)):
            if a[i] == ' ':
                  c = c + 1
                  f = i
            if i % 70 == 0 and i != 0:
                  b.append(a[e:f+1])
                  e = f
                  d = d + 1
                  
            elif i > 70 * (len(a) // 70):
                  b.append(a[e:])
                  break
      return b[::-1]






#print(TextP("You wake up in a small grey room on a cold hard floor, there's a door in front of you and a huge wooden table on your left "))
