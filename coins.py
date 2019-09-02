## Write a program that will prompt you for how many coins you want. Initially you have no coins. 
## It will ask you if you want a coin? If you type "yes", it will give you one coin, 
## and print out the current tally. If you type no, it will stop the program

count = 0
answer = input("Type yes for a coin, type no to stay broke: ")

while answer == "yes":
    count = count + 1
    print("You have " + str(count) + " coins!")
    answer = input("Would you like another? ")
    
print("Okay")