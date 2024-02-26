def Carpet(Number) :

    from random import choice

    list = ["🟥","🟧","🟨","🟩","🟦","🟪","🟫"]
    if Number % 2 != 0 :

        for i in range(Number) :
            for j in range(Number) :
                if j % 2 == 0: 
                    ch = choice(list)
                    print(ch,end="")
                else: 
                    ch = choice(list)
                    print(ch,end="") 
            print()
    else:
        print("Sorry , You Should Enter an Odd Number")
             
while True : Carpet(int(input("Please Enter a Odd Number : ")))
