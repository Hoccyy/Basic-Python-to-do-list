

stopper = 0
while stopper != 990:
    if stopper != 990:
        todo_ = input("What do you need to do?")
        #
        with open ("todo.txt", 'a', encoding="utf-8") as f:
            f.write(todo_ + "\n\n")
    #
    stopper = int(input("\nStop? enter 990 to stop"))

