while True:

    try:
        num_1 = int(input("Pick A Number: "))
        num_2 = (int(input("Pick A Second Number: ")))
    except ValueError:
        print("ERROR: Invalid Input")
        continue
    else:
        pass

    while True:
        operation = input("Please Pick One Of The Following Operations: +,-,*,/, Or Use Reset: ").lower()
        match operation:
            case "+":
                print(f"{num_1} + {num_2} = {num_1 + num_2}") 
            case "-":
                print(f"{num_1} - {num_2} = {num_1 - num_2}") 
            case "*":
                print(f"{num_1} * {num_2} = {num_1 * num_2}")
            case "/":
                print(f"{num_1} / {num_2} = {num_1 / num_2}")
            case "reset":
                break
            case _:
                print("Not A Valid Operation, Please Try Again") 