import time

while True:
    name = input("Name: ")
    date = input("Date: " + time.strftime("%d.%m.%Y") + " [y|n]: ")

    if date == "y":
        realdate = time.strftime("%d.%m.%Y")
    else:
        realdate = input("Enter Date: ")

    time = input("Time: ")

    file = open("todos.txt", "a")
    file.write(realdate + " | " + time + " | " + name + "\n")
    file.close()

    new = input("New Entry? [y|n]: ")

    if new == "n":
        break
