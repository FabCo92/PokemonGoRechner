

w = 0.63
ww = 0.63
s = 1.6

#Matrix für Angreifer gemäß Tabelle
effektMat = [[1,1,1,1,1,1,1,1,1,1,1,1,w,ww,1,1,w,1], #Normal
             [1,w,w,s,1,s,1,1,1,1,1,s,w,1,w,1,s,1], #Feuer
             [1,s,w,w,1,1,1,1,s,1,1,1,s,1,w,1,1,1], #Wasser
             [1,2,s,w,1,1,1,w,s,w,1,w,s,1,w,1,w,1], #Pflanze
             [1,1,s,w,w,1,1,1,ww,s,1,1,1,1,w,1,1,1], #Elektro
             [1,w,w,s,1,w,1,1,s,s,1,1,1,1,s,1,w,1], #Eis
             [s,1,1,1,1,s,1,w,1,w,w,w,s,ww,1,s,s,w], #Kampf
             [1,1,1,s,1,1,1,w,w,1,1,1,w,w,1,1,ww,s], #Gift
             [1,s,1,w,s,1,1,s,1,ww,1,w,s,1,1,1,s,1], #Boden
             [1,1,1,s,w,1,s,1,1,1,1,s,w,1,1,1,w,1], #Flug
             [1,1,1,1,1,1,s,s,1,1,w,1,1,1,1,ww,w,1], #Psycho
             [1,w,1,s,1,1,w,w,1,w,s,1,1,w,1,s,w,w], #Käfer
             [1,s,1,1,1,s,w,1,w,s,1,s,1,1,1,1,w,1], #Gestein
             [w,1,1,1,1,1,1,1,1,1,s,1,1,s,1,w,1,1], #Geist
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1,s,1,w,ww], #Drache
             [1,1,1,1,1,1,w,1,1,1,s,1,1,s,1,w,1,w], #Unlicht
             [1,w,w,1,w,s,1,1,1,1,1,1,s,1,1,1,w,s], #Stahl
             [1,w,1,1,1,1,s,w,1,1,1,1,1,1,s,s,w,1], #Fee  
             ] 

#transponierte Matrix für Verteidiger
effektVMat = [list(x) for x in zip(*effektMat)]

types = ["Normal","Feuer", "Wasser", "Pflanze", "Elektro", "Eis", "Kampf",
         "Gift", "Boden", "Flug", "Psycho", "Käfer", "Gestein", "Geist", 
         "Drache", "Unlicht", "Stahl", "Fee"]

typeEffekt = {}

#füllt das Dictonary typeEffekt
for i in range(len(effektMat)):
    typeEffekt[types[i]]=effektMat[i]

typeEffektV = {}

#füllt das Dictonary typeEffekt
for i in range(len(effektVMat)):
    typeEffektV[types[i]] = effektVMat[i]

def effektivAng(x):
    output = ()
    for i in range(len(x)):
       effekt = typeEffekt.get(x[i])
       j = 0
       
       while (j < len(effekt)):
            if(effekt[j] == s):
               if types[j] not in output:
                  output += tuple([types[j]])
            j += 1
    #print(output)
    return output

def uneffektivAng(x):
    output = ()
    for i in range(len(x)):
       effekt = typeEffekt.get(x[i])
       j = 0
       
       while (j < len(effekt)):
            if(effekt[j] == w or effekt[j] == ww):

               if types[j] not in output:
                  output += tuple([types[j]])
            j += 1
    #print(output)
    return output

def vertPlus(x):
   output = ()

   for i in range(len(x)):
      effekt = typeEffektV.get(x[i])
      j = 0

      
      while(j < len(effekt)):
         multi = 1
         if(effekt[j] == w):
            multi *= w
         elif(effekt[j] == ww):
            multi *= ww
         elif(effekt[j] == s):
            multi *= s
         if(multi < 1):
            output += tuple([types[j]])
         j += 1
   #print(output)
   return output


def verMinus(x):
   output = ()

   for i in range(len(x)):
      effekt = typeEffektV.get(x[i])
      j = 0

      while(j < len(effekt)):
         multi = 1
         if(effekt[j] == w):
            multi *= w
         elif(effekt[j] == ww):
            multi *= ww
         elif(effekt[j] == s):
            multi *= s
         if(multi > 1 and types[j] not in output):
            output += tuple([types[j]])
         elif(multi < 1 and types[j] in output):
            outputList = list(output)
            outputList.remove(types[j])
            output = tuple(outputList)
         j += 1
   #print(output)
   return output

def analyzeTeam(x):
   print("Das Team hat einen Konter gegen folgende Typen(Verteidigung):",vertPlus(x))
   print("Das Team hat folgende Schwächen:", verMinus(x))

   
