
#By Christopher and Sherlyn
score =[]
#Import time so that we can count timer
import time
import sys
print("1.Start 2.Score 3.End")
def main_menu():
    x=input("Please input the number of your choice 1.Start 2.Score 3.End")
    if x == "1" :
        choices()
    elif x=="2":
        print(score)
        main_menu()
    elif x== "3":
        sys.exit()
    else:
        print("ERROR please input a valid option.")
        main_menu()


def choices():
    b=input("Please choose your difficulty. easy, medium, hard")
    if b =="easy":
        print("Hello World")
        start = time.time()
        w=input("Ready Go...!!!")
        if w=="Hello World":
            end = time.time()
            time_done= end - start
            print("You did it!",round(time_done, 2),"Seconds")
            score.append(round(time_done, 2))
            main_menu()
        else:
            print("ERROR. RESTARTING TO DIFFICULTY")
            choices()
    elif b =="medium":
        print("I'm going for a walk to the park")
        start = time.time()
        l=input("Ready Go...!!!")
        end = time.time()
        if l=="I'm going for a walk to the park":
            time_done= end - start
            print("You did it!",round(time_done, 2),"Seconds")
            score.append(round(time_done, 2))
            main_menu()
        else:
            print("ERROR. RESTARTING TO DIFFICULTY")
            choices()
    elif b =="Hard":
        print("One morning I shot an elephant in my pajamas. How he got into my pajamas I'll never know")
        start = time.time()
        z=input("Ready Go...!!!")
        end = time.time()
        if z=="One morning I shot an elephant in my pajamas. How he got into my pajamas I'll never know":
            time_done= end - start
            print("You did it!",round(time_done, 2),"Seconds")
            score.append(round(time_done, 2))
            main_menu()
        else:
            print("ERROR. RESTARTING TO DIFFICULTY")
            choices()
    else:
        "error please input valid choice"
        choices()
main_menu()
