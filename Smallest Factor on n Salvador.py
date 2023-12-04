while True:
    try:
        interger = int(input("Enter an Integer >= 2: "))
        if interger < 2:
            print("Invalid number, please enter an Integer >= 2")
        else:
            bababooie = False
            for i in range(2, interger):
                if interger % i == 0:
                    print(f"The smallest factor other than 1 for {interger} is {i}")
                    bababooie = True
                    break

            if not bababooie:
                print(f"{interger} is prime, it has no factor(s)")
            break

    except ValueError:
        print("INVALID INPUT, TRY AN ACTUAL NUMBER")

