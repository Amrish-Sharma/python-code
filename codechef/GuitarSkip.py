

def type_input():
    while True:
        try:
            T = int(input('Enter Number of Test Cases: '))
            if 1 <= T <= 10:
                take_testcase()
                break
            else:
                print('Invalid. Enter the number of testcases in range(1,10)')
        except:
            print('Invalid Number')

n = []
i = 0
 
def take_testcase():
    while True:
        try:
            while (i < T):
                n[i]  = int(input())
                if 2 <= n[i] <= 10 ^ 5:
                    i=i+1
                else:
                    print('Invalid. Enter the number of testcases in range(1,10)')
        except:
            exit()


type_input()