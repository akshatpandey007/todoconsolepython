from datetime import datetime
from os import path
import os


userdb = "Userdb.txt"
state = "savestate.txt"
if not(path.exists(userdb)):
    u = open(userdb, "w")
    u.close()


def add_task(f_name, f_count):
    now = datetime.now()
    if path.exists(f_name):
        fileObj = open(f_name, "a")
        fileCount = open(f_count, "r")
        count = int(fileCount.read())
        count += 1
        fileCount.close()
        fileCount = open(f_count, "w")
        fileCount.write(str(count))
        data = input("Enter task\n")
        fileObj.write(
            data+"                          ..........."+str(now)+"\n")
        fileCount.close()
    else:
        fileObj = open(f_name, "w")
        fileCount = open(f_count, "w")
        data = input("Enter task\n")
        fileObj.write(
            data+"                          ..........."+str(now)+"\n")
        fileCount.write("1")
        fileCount.close()
    fileObj.close()


def noTasks(f_name, f_count):
    if path.exists(f_count):
        fileCount = open(f_count, "r")
        count = fileCount.read()
        print(count)
        fileCount.close()
    else:
        print("0")


def deleteTask(f_name, f_count):
    if path.exists(f_name):
        number = int(input("Enter task number to be deleted\n"))
        fileCount = open(f_count, "r")
        count = int(fileCount.read())
        count -= 1
        fileCount.close()
        fileCount = open(f_count, "w")
        fileCount.write(str(count))
        tem = 1
        fileObj = open(f_name, "r")
        fileTemp = open("temp.txt", "w")
        f1 = fileObj.readlines()
        for i in f1:
            if tem != number:
                fileTemp.write(i)
            tem += 1
        fileObj.close()
        fileTemp.close()
        os.remove(f_name)
        os.rename("temp.txt", f_name)
    else:
        print("Empty List!!!")


def ShowMenu():
    print("Menu")
    print("N) Add a new task")
    print("P) Show the number of tasks")
    print("D) Delete a task by number")
    print("S) Print a task by number")
    print("M) Print menu list")
    print("L) Show all the taks")
    print("R) Reset List")
    print("Q) Quit")
    print("O)Log out")


def show_Task_number(f_name, f_count):
    if path.exists(f_name):
        number = int(input("Enter task number to be deleted\n"))
        fileObj = open(f_name, "r")
        f1 = fileObj.readlines()
        tem = 1
        for i in f1:
            if tem == number:
                print(i)
            tem += 1
        fileObj.close()
    else:
        print("Empty list!!")


def ShowTasks(f_name, f_count):
    if path.exists(f_name):
        fileObj = open(f_name, "r")
        f1 = fileObj.readlines()
        tem = 1
        for i in f1:
            print(str(tem)+"> "+i)
            tem += 1
        fileObj.close()
    else:
        print("Empty tasks!!")


def reset(f_name, f_count):
    if path.exists(f_name):
        print("Reset!!")
        os.remove(f_name)
        os.remove(f_count)


def todo(f_name, f_count):
    while(True):
        op = input("Choose an option , or press m/M for menu\n")
        if op == "N" or op == "n":
            add_task(f_name, f_count)
        elif op == "P" or op == "p":
            noTasks(f_name, f_count)
        elif op == "D" or op == "d":
            deleteTask(f_name, f_count)
        elif op == "S" or op == "s":
            show_Task_number(f_name, f_count)
        elif op == "M" or op == "m":
            ShowMenu()
        elif op == "L" or op == "l":
            ShowTasks(f_name, f_count)
        elif op == "R" or op == "r":
            reset(f_name, f_count)
        elif op == "Q" or op == "q":
            exit(1)
        elif op == "O" or op == "o"or op == "0":
            os.remove(state)
            user()
        else:
            print("wrong input")


def user():
    log = True
    while(log):
        print("1>LogIn")
        print("2>SignUp")
        print("3>EXIT")
        ch = int(input("Enter choice\n"))
        if ch == 1:
            u = open(userdb, "r")
            userid = input("Enter username\n")
            userpassword = input("Enter password\n")
            u1 = u.readlines()
            for i in u1:
                id = i.split('@,@')
                if userid == id[1]:
                    if userpassword == id[2]:
                        print("Login Succesful\n")
                        log = False
                        st = open(state, "w")
                        st.write(i)
                        st.close()
                        f_name = id[1]+id[2]+"list.txt"
                        f_count = id[1]+id[2]+"count.txt"
                        todo(f_name, f_count)
                    else:
                        print("Invalid Password\n")
                else:
                    print("User not found!!")

        elif ch == 2:
            u = open(userdb, "r")
            name = input("Enter full name\n")
            userid = input("Enter username\n")
            u1 = u.readlines()
            flag = 0
            for i in u1:
                id = i.split('@,@')
                if userid == id[1]:
                    flag = 1
                    print("User id already taken")
            u.close()
            u = open(userdb, "a")
            if flag == 0:
                userpassword = input("Enter password\n")
                user = name+"@,@"+userid+"@,@"+userpassword+"@,@"
                u.write(user+"\n")
            u.close()
        elif(ch == 3):
            os.remove(state)
            exit(1)
        else:
            print("very wrong choice")


def main():
    if not(path.exists(state)):
        user()
    else:
        st = open(state, "r")
        ss = st.readlines()[0]
        id = ss.split('@,@')
        f_name = id[1]+id[2]+"list.txt"
        f_count = id[1]+id[2]+"count.txt"
        st.close()
        todo(f_name, f_count)


if __name__ == "__main__":
    main()
