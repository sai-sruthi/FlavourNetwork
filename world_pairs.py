f1 = open("african.txt", 'r')
f2 = open("african2.txt", 'w')
for line in f1:
    f2.write(line.replace(',', ' '))
f1.close()
f2.close()

p1=0;p2=0;p3=0;p4=0;p5=0;p6=0;p7=0;p8=0;p9=0;p10=0
for line in open("african2.txt"):
        m=0;f=0;b=0;bm=0;chi=0;o=0;l=0;melo=0;ses=0;y=0;
        s = line.split()
        for item in s:
            if item =="milk": m=1
            if item =="banana": b=1
            if item =="fish": f=1
            if item =="buttermilk": bm=1
            if item =="chicken": chi=1
            if item =="orange": o=1
            if item =="lemon": l=1
            if item =="melon": melo=1
            if item =="sesame_seed": ses=1
            if item =="yogurt": y=1
            if (m,f)==(1,1): p1=p1+1
            if (m,b)==(1,1): p2=p2+1
            if (m,melo)==(1,1): p3=p3+1
            if (m,o)==(1,1): p4=p4+1
            if (m,l)==(1,1): p5=p5+1
            if (m,chi)==(1,1): p6=p6+1 
            if (y,b)==(1,1): p7=p7+1 
            if (bm,b)==(1,1): p8=p8+1
            if (chi,ses)==(1,1): p9=p9+1 
            if (f,ses)==(1,1): p10=p10+1      
                
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)
print(p9)
print(p10)


f1 = open("east_asain.txt", 'r')
f2 = open("east_asian2.txt", 'w')
for line in f1:
    f2.write(line.replace(',', ' '))
f1.close()
f2.close()

p1=0;p2=0;p3=0;p4=0;p5=0;p6=0;p7=0;p8=0;p9=0;p10=0
for line in open("east_asian2.txt"):
        m=0;f=0;b=0;bm=0;chi=0;o=0;l=0;melo=0;ses=0;y=0;
        s = line.split()
        for item in s:
            if item =="milk": m=1
            if item =="banana": b=1
            if item =="fish": f=1
            if item =="buttermilk": bm=1
            if item =="chicken": chi=1
            if item =="orange": o=1
            if item =="lemon": l=1
            if item =="melon": melo=1
            if item =="sesame_seed": ses=1
            if item =="yogurt": y=1
            if (m,f)==(1,1): p1=p1+1
            if (m,b)==(1,1): p2=p2+1
            if (m,melo)==(1,1): p3=p3+1
            if (m,o)==(1,1): p4=p4+1
            if (m,l)==(1,1): p5=p5+1
            if (m,chi)==(1,1): p6=p6+1 
            if (y,b)==(1,1): p7=p7+1 
            if (bm,b)==(1,1): p8=p8+1
            if (chi,ses)==(1,1): p9=p9+1 
            if (f,ses)==(1,1): p10=p10+1      
                
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)
print(p9)
print(p10)

f1 = open("latin_american.txt", 'r')
f2 = open("latin_american2.txt", 'w')
for line in f1:
    f2.write(line.replace(',', ' '))
f1.close()
f2.close()

p1=0;p2=0;p3=0;p4=0;p5=0;p6=0;p7=0;p8=0;p9=0;p10=0
for line in open("latin_american2.txt"):
        m=0;f=0;b=0;bm=0;chi=0;o=0;l=0;melo=0;ses=0;y=0;
        s = line.split()
        for item in s:
            if item =="milk": m=1
            if item =="banana": b=1
            if item =="fish": f=1
            if item =="buttermilk": bm=1
            if item =="chicken": chi=1
            if item =="orange": o=1
            if item =="lemon": l=1
            if item =="melon": melo=1
            if item =="sesame_seed": ses=1
            if item =="yogurt": y=1
            if (m,f)==(1,1): p1=p1+1
            if (m,b)==(1,1): p2=p2+1
            if (m,melo)==(1,1): p3=p3+1
            if (m,o)==(1,1): p4=p4+1
            if (m,l)==(1,1): p5=p5+1
            if (m,chi)==(1,1): p6=p6+1 
            if (y,b)==(1,1): p7=p7+1 
            if (bm,b)==(1,1): p8=p8+1
            if (chi,ses)==(1,1): p9=p9+1 
            if (f,ses)==(1,1): p10=p10+1      
                
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)
print(p9)
print(p10)


f1 = open("north_american.txt", 'r')
f2 = open("north_american2.txt", 'w')
for line in f1:
    f2.write(line.replace(',', ' '))
f1.close()
f2.close()

p1=0;p2=0;p3=0;p4=0;p5=0;p6=0;p7=0;p8=0;p9=0;p10=0
for line in open("north_american2.txt"):
        m=0;f=0;b=0;bm=0;chi=0;o=0;l=0;melo=0;ses=0;y=0;
        s = line.split()
        for item in s:
            if item =="milk": m=1
            if item =="banana": b=1
            if item =="fish": f=1
            if item =="buttermilk": bm=1
            if item =="chicken": chi=1
            if item =="orange": o=1
            if item =="lemon": l=1
            if item =="melon": melo=1
            if item =="sesame_seed": ses=1
            if item =="yogurt": y=1
            if (m,f)==(1,1): p1=p1+1
            if (m,b)==(1,1): p2=p2+1
            if (m,melo)==(1,1): p3=p3+1
            if (m,o)==(1,1): p4=p4+1
            if (m,l)==(1,1): p5=p5+1
            if (m,chi)==(1,1): p6=p6+1 
            if (y,b)==(1,1): p7=p7+1 
            if (bm,b)==(1,1): p8=p8+1
            if (chi,ses)==(1,1): p9=p9+1 
            if (f,ses)==(1,1): p10=p10+1      
                
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)
print(p9)
print(p10)


f1 = open("west_europe.txt", 'r')
f2 = open("west_europe2.txt", 'w')
for line in f1:
    f2.write(line.replace(',', ' '))
f1.close()
f2.close()

p1=0;p2=0;p3=0;p4=0;p5=0;p6=0;p7=0;p8=0;p9=0;p10=0
for line in open("west_europe2.txt"):
        m=0;f=0;b=0;bm=0;chi=0;o=0;l=0;melo=0;ses=0;y=0;
        s = line.split()
        for item in s:
            if item =="milk": m=1
            if item =="banana": b=1
            if item =="fish": f=1
            if item =="buttermilk": bm=1
            if item =="chicken": chi=1
            if item =="orange": o=1
            if item =="lemon": l=1
            if item =="melon": melo=1
            if item =="sesame_seed": ses=1
            if item =="yogurt": y=1
            if (m,f)==(1,1): p1=p1+1
            if (m,b)==(1,1): p2=p2+1
            if (m,melo)==(1,1): p3=p3+1
            if (m,o)==(1,1): p4=p4+1
            if (m,l)==(1,1): p5=p5+1
            if (m,chi)==(1,1): p6=p6+1 
            if (y,b)==(1,1): p7=p7+1 
            if (bm,b)==(1,1): p8=p8+1
            if (chi,ses)==(1,1): p9=p9+1 
            if (f,ses)==(1,1): p10=p10+1      
                
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)
print(p9)
print(p10)


# In[40]:

f1 = open("south_europe.txt", 'r')
f2 = open("south_europe2.txt", 'w')
for line in f1:
    f2.write(line.replace(',', ' '))
f1.close()
f2.close()

p1=0;p2=0;p3=0;p4=0;p5=0;p6=0;p7=0;p8=0;p9=0;p10=0
for line in open("south_europe2.txt"):
        m=0;f=0;b=0;bm=0;chi=0;o=0;l=0;melo=0;ses=0;y=0;
        s = line.split()
        for item in s:
            if item =="milk": m=1
            if item =="banana": b=1
            if item =="fish": f=1
            if item =="buttermilk": bm=1
            if item =="chicken": chi=1
            if item =="orange": o=1
            if item =="lemon": l=1
            if item =="melon": melo=1
            if item =="sesame_seed": ses=1
            if item =="yogurt": y=1
            if (m,f)==(1,1): p1=p1+1
            if (m,b)==(1,1): p2=p2+1
            if (m,melo)==(1,1): p3=p3+1
            if (m,o)==(1,1): p4=p4+1
            if (m,l)==(1,1): p5=p5+1
            if (m,chi)==(1,1): p6=p6+1 
            if (y,b)==(1,1): p7=p7+1 
            if (bm,b)==(1,1): p8=p8+1
            if (chi,ses)==(1,1): p9=p9+1 
            if (f,ses)==(1,1): p10=p10+1      
                
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)
print(p9)
print(p10)


# In[41]:

f1 = open("northern_europe.txt", 'r')
f2 = open("northern_europe2.txt", 'w')
for line in f1:
    f2.write(line.replace(',', ' '))
f1.close()
f2.close()

p1=0;p2=0;p3=0;p4=0;p5=0;p6=0;p7=0;p8=0;p9=0;p10=0
for line in open("northern_europe2.txt"):
        m=0;f=0;b=0;bm=0;chi=0;o=0;l=0;melo=0;ses=0;y=0;
        s = line.split()
        for item in s:
            if item =="milk": m=1
            if item =="banana": b=1
            if item =="fish": f=1
            if item =="buttermilk": bm=1
            if item =="chicken": chi=1
            if item =="orange": o=1
            if item =="lemon": l=1
            if item =="melon": melo=1
            if item =="sesame_seed": ses=1
            if item =="yogurt": y=1
            if (m,f)==(1,1): p1=p1+1
            if (m,b)==(1,1): p2=p2+1
            if (m,melo)==(1,1): p3=p3+1
            if (m,o)==(1,1): p4=p4+1
            if (m,l)==(1,1): p5=p5+1
            if (m,chi)==(1,1): p6=p6+1 
            if (y,b)==(1,1): p7=p7+1 
            if (bm,b)==(1,1): p8=p8+1
            if (chi,ses)==(1,1): p9=p9+1 
            if (f,ses)==(1,1): p10=p10+1      
                
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)
print(p9)
print(p10)


# In[42]:

f1 = open("southasian.txt", 'r')
f2 = open("southasian2.txt", 'w')
for line in f1:
    f2.write(line.replace(',', ' '))
f1.close()
f2.close()

p1=0;p2=0;p3=0;p4=0;p5=0;p6=0;p7=0;p8=0;p9=0;p10=0
for line in open("southasian2.txt"):
        m=0;f=0;b=0;bm=0;chi=0;o=0;l=0;melo=0;ses=0;y=0;
        s = line.split()
        for item in s:
            if item =="milk": m=1
            if item =="banana": b=1
            if item =="fish": f=1
            if item =="buttermilk": bm=1
            if item =="chicken": chi=1
            if item =="orange": o=1
            if item =="lemon": l=1
            if item =="melon": melo=1
            if item =="sesame_seed": ses=1
            if item =="yogurt": y=1
            if (m,f)==(1,1): p1=p1+1
            if (m,b)==(1,1): p2=p2+1
            if (m,melo)==(1,1): p3=p3+1
            if (m,o)==(1,1): p4=p4+1
            if (m,l)==(1,1): p5=p5+1
            if (m,chi)==(1,1): p6=p6+1 
            if (y,b)==(1,1): p7=p7+1 
            if (bm,b)==(1,1): p8=p8+1
            if (chi,ses)==(1,1): p9=p9+1 
            if (f,ses)==(1,1): p10=p10+1      
                
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)
print(p9)
print(p10)


# In[44]:

f1 = open("Middle_easter.txt", 'r')
f2 = open("Middle_eastern2.txt", 'w')
for line in f1:
    f2.write(line.replace(',', ' '))
f1.close()
f2.close()

p1=0;p2=0;p3=0;p4=0;p5=0;p6=0;p7=0;p8=0;p9=0;p10=0
for line in open("Middle_eastern2.txt"):
        m=0;f=0;b=0;bm=0;chi=0;o=0;l=0;melo=0;ses=0;y=0;
        s = line.split()
        for item in s:
            if item =="milk": m=1
            if item =="banana": b=1
            if item =="fish": f=1
            if item =="buttermilk": bm=1
            if item =="chicken": chi=1
            if item =="orange": o=1
            if item =="lemon": l=1
            if item =="melon": melo=1
            if item =="sesame_seed": ses=1
            if item =="yogurt": y=1
            if (m,f)==(1,1): p1=p1+1
            if (m,b)==(1,1): p2=p2+1
            if (m,melo)==(1,1): p3=p3+1
            if (m,o)==(1,1): p4=p4+1
            if (m,l)==(1,1): p5=p5+1
            if (m,chi)==(1,1): p6=p6+1 
            if (y,b)==(1,1): p7=p7+1 
            if (bm,b)==(1,1): p8=p8+1
            if (chi,ses)==(1,1): p9=p9+1 
            if (f,ses)==(1,1): p10=p10+1      
                
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)
print(p9)
print(p10)


# In[45]:

f1 = open("south_east_asia.txt", 'r')
f2 = open("south_east_asia2.txt", 'w')
for line in f1:
    f2.write(line.replace(',', ' '))
f1.close()
f2.close()

p1=0;p2=0;p3=0;p4=0;p5=0;p6=0;p7=0;p8=0;p9=0;p10=0
for line in open("south_east_asia2.txt"):
        m=0;f=0;b=0;bm=0;chi=0;o=0;l=0;melo=0;ses=0;y=0;
        s = line.split()
        for item in s:
            if item =="milk": m=1
            if item =="banana": b=1
            if item =="fish": f=1
            if item =="buttermilk": bm=1
            if item =="chicken": chi=1
            if item =="orange": o=1
            if item =="lemon": l=1
            if item =="melon": melo=1
            if item =="sesame_seed": ses=1
            if item =="yogurt": y=1
            if (m,f)==(1,1): p1=p1+1
            if (m,b)==(1,1): p2=p2+1
            if (m,melo)==(1,1): p3=p3+1
            if (m,o)==(1,1): p4=p4+1
            if (m,l)==(1,1): p5=p5+1
            if (m,chi)==(1,1): p6=p6+1 
            if (y,b)==(1,1): p7=p7+1 
            if (bm,b)==(1,1): p8=p8+1
            if (chi,ses)==(1,1): p9=p9+1 
            if (f,ses)==(1,1): p10=p10+1      
                
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)
print(p9)
print(p10)


# In[46]:

f1 = open("East_europian.txt", 'r')
f2 = open("East_europian.txt", 'w')
for line in f1:
    f2.write(line.replace(',', ' '))
f1.close()
f2.close()

p1=0;p2=0;p3=0;p4=0;p5=0;p6=0;p7=0;p8=0;p9=0;p10=0
for line in open("East_europian.txt"):
        m=0;f=0;b=0;bm=0;chi=0;o=0;l=0;melo=0;ses=0;y=0;
        s = line.split()
        for item in s:
            if item =="milk": m=1
            if item =="banana": b=1
            if item =="fish": f=1
            if item =="buttermilk": bm=1
            if item =="chicken": chi=1
            if item =="orange": o=1
            if item =="lemon": l=1
            if item =="melon": melo=1
            if item =="sesame_seed": ses=1
            if item =="yogurt": y=1
            if (m,f)==(1,1): p1=p1+1
            if (m,b)==(1,1): p2=p2+1
            if (m,melo)==(1,1): p3=p3+1
            if (m,o)==(1,1): p4=p4+1
            if (m,l)==(1,1): p5=p5+1
            if (m,chi)==(1,1): p6=p6+1 
            if (y,b)==(1,1): p7=p7+1 
            if (bm,b)==(1,1): p8=p8+1
            if (chi,ses)==(1,1): p9=p9+1 
            if (f,ses)==(1,1): p10=p10+1      
                
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)
print(p9)
print(p10)


# In[52]:

lines=[2869, 3249]
f1 = open("all.txt", 'r')
f2 = open("all2.txt", 'w')
for line in f1:
    f2.write(line.replace(',', ' '))
f1.close()
f2.close()
i=1
p1=0;p2=0;p3=0;p4=0;p5=0;p6=0;p7=0;p8=0;p9=0;p10=0
for line in open("all2.txt"):
    if i in lines:
        m=0;f=0;b=0;bm=0;chi=0;o=0;l=0;melo=0;ses=0;y=0;
        s = line.split()
        for item in s:
            if item =="milk": m=1
            if item =="banana": b=1
            if item =="fish": f=1
            if item =="buttermilk": bm=1
            if item =="chicken": chi=1
            if item =="orange": o=1
            if item =="lemon": l=1
            if item =="melon": melo=1
            if item =="sesame_seed": ses=1
            if item =="yogurt": y=1
            if (m,f)==(1,1): p1=p1+1
            if (m,b)==(1,1): p2=p2+1
            if (m,melo)==(1,1): p3=p3+1
            if (m,o)==(1,1): p4=p4+1
            if (m,l)==(1,1): p5=p5+1
            if (m,chi)==(1,1): p6=p6+1 
            if (y,b)==(1,1): p7=p7+1 
            if (bm,b)==(1,1): p8=p8+1
            if (chi,ses)==(1,1): p9=p9+1 
            if (f,ses)==(1,1): p10=p10+1      
    i=i+1         
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)
print(p9)
print(p10)


# In[ ]:



