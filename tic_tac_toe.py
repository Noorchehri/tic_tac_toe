x_score = 0
o_score = 0

# 3 set
for dast in range(3) :
    print("------------------------------")
    print("********** SET : ", dast + 1, "**********")
    print("------------------------------")

    c1 = "1"
    c2 = "2"
    c3 = "3"
    c4 = "4"
    c5 = "5"
    c6 = "6"
    c7 = "7"
    c8 = "8"
    c9 = "9"

    player = "x"
    winner = ""

    print(c1,"|",c2,"|",c3)
    print("----------")
    print(c4,"|",c5,"|",c6)
    print("----------")
    print(c7,"|",c8,"|",c9)

    for dooz in range(9) :
        print("------------------------------")
        print ("************************ TURN: ", player)
        print("------------------------------")
        choice = input(" khane ra entekhab konid (1-9) : ")
        print("------------------------------")

        if choice == "1" and c1 == "1" :
            c1 = player
        elif choice == "2" and c2 == "2" :
            c2 = player
        elif choice == "3" and c3 == "3" :
            c3 = player
        elif choice == "4" and c4 == "4" :
            c4 = player
        elif choice == "5" and c5 == "5" :
            c5 = player
        elif choice == "6" and c6 == "6" :
            c6 = player
        elif choice == "7" and c7 == "7" :
            c7 = player
        elif choice == "8" and c8 == "8" :
            c8 = player
        elif choice == "9" and c9 == "9" :
            c9 = player
        print(c1,"|",c2,"|",c3)
        print("----------")
        print(c4,"|",c5,"|",c6)
        print("----------")
        print(c7,"|",c8,"|",c9)


        if c1 == "x" and c2 == "x" and c3 == "x" :
            winner = "x"
        elif c4 == "x" and c5 == "x" and c6 == "x" :
            winner = "x"
        elif c7 == "x" and c8 == "x" and c9 == "x" :
            winner = "x"
        elif c1 == "x" and c4 == "x" and c7 == "x" :
            winner = "x"
        elif c2 == "x" and c5 == "x" and c8 == "x" :
            winner = "x"
        elif c3 == "x" and c6 == "x" and c9 == "x" :
            winner = "x"
        elif c1 == "x" and c5 == "x" and c9 == "x" :
            winner = "x"
        elif c3 == "x" and c5 == "x" and c7 == "x" :
            winner = "x"



        elif c1 == "o" and c2 == "o" and c3 == "o" :
            winner = "o"
        elif c4 == "o" and c5 == "o" and c6 == "o" :
            winner = "o"
        elif c7 == "o" and c8 == "o" and c9 == "o" :
            winner = "o"
        elif c1 == "o" and c4 == "o" and c7 == "o" :
            winner = "o"
        elif c2 == "o" and c5 == "o" and c8 == "o" :
            winner = "o"
        elif c3 == "o" and c6 == "o" and c9 == "o" :
            winner = "o"
        elif c1 == "o" and c5 == "o" and c9 == "o" :
            winner = "o"
        elif c3 == "o" and c5 == "o" and c7 == "o" :
            winner = "o"
        if winner != "" :
            break



        if player == "x" :
            player = "o"
        else :
            player = "x"


    if winner == "x" :
        print("----------- SET : ", dast + 1)
        print("----------- XXX ")
        x_score += 1
    elif winner == "o" :
        print("----------- SET : ", dast + 1)
        print("----------- OOO")
        o_score += 1
    else :
        print("----------- SET : ", dast + 1)
        print("----------- MOSAVI")


if x_score > o_score :
    print("----------- WIN : X")
elif o_score > x_score :
    print("----------- WIN : O")
else :
    print("----------- EQUAL")
