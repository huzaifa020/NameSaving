#program that take your name or after entering your it give option to view your name.
import pyttsx3
sell = pyttsx3.init()
sell.say("Make a program that take your name or after entering your it give option to view your name.")
sell.runAndWait()
data = dict()
while True:
    print("Welcome to another awsome program.")
    print("Press 1 for entering any person name.")
    print("press 2 for viewing the data of any person.")
    print("Press Q for exist the program.")
    #This condition took name or save it.
    ans = input('Enter a number:')
    if ans == "1":
        name = input("Enter name :")
        temp = []
        while True:
            likes = input("Enter anything that you like or press q for exist")
            if likes == "Q" or likes == "q":
                break
            else:
                temp.append(likes)
                data[name] = temp
                print(data)
    #This condition show names.
    if ans == "2":
        name = input("Enter name :")
        if name in list(data.keys()):
            for d in data[name]:
                print(d) 
        else:
            print("Data not found")
    #This function quit from program.
    if ans == "Q" or ans == "q":
        print("Goodbye")   
        break    