import random #dont forget of import random at frist 
print(random.random())
print(random.randint(1,10))

names = ["hari", "kali", "rati", "gori"] # 0, 1, 2, 3 
lucky_name = random.randint(0,len(names)-1) #storing value in variable and (len is used to count length and it is function)
 #(-1 at last is for last value )
print(names[lucky_name])

random.shuffle(names)
print(names)

#create a pythongame that gentrate number  50 - 100 
# You have 5 friends at canteen, you need to generator one person name to pay the bill. 
