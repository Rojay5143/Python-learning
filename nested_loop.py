# for i in range(1,6):
#     for j in range(1,4):
#         print(j, end= " ")
#     print()

# # print table of 2 using nasted loop 

# for i in range(1,2):
#     for j in range(1,2):
#         print(i*j, end= "\t")
#     print()

#printing grid star (*)
# rows = int(input("Enter number of Rows you want to print: "))
# for i in range(rows+1): # -1 in loop make go backword  or count down
#     for j in range(i): #range(start, stop, step)
#         print("*", end= " ")
#     print()
# #reverse the star
# for i in range(rows+1): # -1 in loop make go backword  or count down
#     for j in range(rows, i, -1): #range(start, stop, step)
#         print("*", end= " ")
#     print()

# #printing right aligned trangle
# for i in range(1,rows+1):
#     for j in range(rows+1,i,-1):
#         print(" ", end=" ")
#     for k in range(i):
#         print("*", end=" ")
#     print()

#Printing pyramid 
import time
rows = int(input("Enter number to make christmas tree: "))
for i in range(1,rows+1):
    for j in range(rows+1,i,-1): #print in reverse 
        print(" ", end="") # end="" doesnot seprate the * with space [this print space only]
    for k in range(i): # this print *
        print("*", end=" ")
    print()

#only printing in thired colum
for i in range (1, rows+1):
    for j in range(3):
        print(" ", end=" ")
    for k in range(1):
        print("*",end="")
    print()

message = "HAPPY CHRISTMAS TO ALL!"

for word in message:
    print(word, end=" ", flush= True)
    time.sleep(0.3)

