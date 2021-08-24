a = input("Insert Password here\n")

def view_p():
    with open('Password.txt','r') as f:
        for each_line in f.readlines():
            data = each_line.rstrip()
            user, passw = data.split("|")
            print("User:",user,", Password",passw)


def add_p():
    name = input("Insert account name | ")
    pwd = input("Insert password | ")

    with open("Password.txt",'a') as f:
        f.write(name + " | " + pwd + "\n")






while True:
    b = input(
    "Add new password or view existing one (add or view)\n")
    if b == "q":
        break
    
    if b == "view":
        view_p()
    elif b == "add":
        add_p()
    else:
        print("Invalid Input")
    continue
