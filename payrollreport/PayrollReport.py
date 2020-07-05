
def input_empcode():
    while True:
        try:
            EID = int(input('Employee ID(0 to quit): '))
            if EID > 0:
                PrintDetails()
                break
            elif EID == 0:
                quit
            else:
                print('Invalid. Enter the number of testcases in range(1,10)')
        except:
            print('Invalid Number')



input_empcode()