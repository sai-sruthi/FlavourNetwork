
# coding: utf-8

# In[1]:

f1 = open("bengali.csv", 'r')
f2 = open("bengali2.txt", 'w')
for line in f1:
    f2.write(line.replace(',', ' '))
f1.close()
f2.close()

p1=0;p2=0;p3=0;p4=0;p5=0;p6=0;p7=0;p8=0;p9=0;p10=0
for line in open("bengali2.txt"):
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


# In[2]:

f1 = open("gujarati.csv", 'r')
f2 = open("gujarati2.txt", 'w')
for line in f1:
    f2.write(line.replace(',', ' '))
f1.close()
f2.close()

p1=0;p2=0;p3=0;p4=0;p5=0;p6=0;p7=0;p8=0;p9=0;p10=0
for line in open("gujarati2.txt"):
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


# In[3]:

f1 = open("jain.csv", 'r')
f2 = open("jain2.txt", 'w')
for line in f1:
    f2.write(line.replace(',', ' '))
f1.close()
f2.close()

p1=0;p2=0;p3=0;p4=0;p5=0;p6=0;p7=0;p8=0;p9=0;p10=0
for line in open("jain2.txt"):
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


# In[4]:

f1 = open("marathi.csv", 'r')
f2 = open("marathi2.txt", 'w')
for line in f1:
    f2.write(line.replace(',', ' '))
f1.close()
f2.close()

p1=0;p2=0;p3=0;p4=0;p5=0;p6=0;p7=0;p8=0;p9=0;p10=0
for line in open("marathi2.txt"):
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


# In[5]:

f1 = open("mughlai.csv", 'r')
f2 = open("mughlai2.txt", 'w')
for line in f1:
    f2.write(line.replace(',', ' '))
f1.close()
f2.close()

p1=0;p2=0;p3=0;p4=0;p5=0;p6=0;p7=0;p8=0;p9=0;p10=0
for line in open("mughlai2.txt"):
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


# In[6]:

f1 = open("punjabi.csv", 'r')
f2 = open("punjabi2.txt", 'w')
for line in f1:
    f2.write(line.replace(',', ' '))
f1.close()
f2.close()

p1=0;p2=0;p3=0;p4=0;p5=0;p6=0;p7=0;p8=0;p9=0;p10=0
for line in open("punjabi2.txt"):
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


# In[7]:

f1 = open("rajasthani.csv", 'r')
f2 = open("rajasthani2.txt", 'w')
for line in f1:
    f2.write(line.replace(',', ' '))
f1.close()
f2.close()

p1=0;p2=0;p3=0;p4=0;p5=0;p6=0;p7=0;p8=0;p9=0;p10=0
for line in open("rajasthani2.txt"):
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


# In[8]:

f1 = open("south_indian.csv", 'r')
f2 = open("south_indian2.txt", 'w')
for line in f1:
    f2.write(line.replace(',', ' '))
f1.close()
f2.close()

p1=0;p2=0;p3=0;p4=0;p5=0;p6=0;p7=0;p8=0;p9=0;p10=0
for line in open("south_indian2.txt"):
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


# In[ ]:



