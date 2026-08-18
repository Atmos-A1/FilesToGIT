for numbers in range(1,11):
    if numbers % 4 == 0:
        for count in range(0,5):   
            
            repeat = numbers ** count

            print(repeat, end = " ")
