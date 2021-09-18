import time

def current_task():
    out = ""

    file = open("todos.txt", "r")

    for line in file.readlines():
        sp = line.strip("\n").split(" | ")

        if sp[0] == time.strftime("%d.%m.%Y"):
            sp_time = sp[1].split(":")

            if sp_time[0] == time.strftime("%H"):
                if int(sp_time[1]) >= int(time.strftime("%M")):
                    out = sp[1] + " | " + sp[2]
                    break
    
    return out

def next_task():
    out = ""

    file = open("todos.txt", "r")

    count = 0

    for line in file.readlines():
        sp = line.strip("\n").split(" | ")

        if sp[0] == time.strftime("%d.%m.%Y"):
            sp_time = sp[1].split(":")

            if sp_time[0] == time.strftime("%H"):
                if int(sp_time[1]) >= int(time.strftime("%M")):
                    
                    if count == 1:
                        out = sp[1] + " | " + sp[2]
                        break
                    else:
                        out = ""
                        count += 1
                    
    
    return out