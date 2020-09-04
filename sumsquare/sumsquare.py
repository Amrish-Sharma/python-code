import math

def take_inputs():
    is1 = input("Enter a list 1 elements separated by space ")
    is2 = input("Enter a list 2 elements separated by space ")
    print("\n")
    list1 = is1.split()
    list2 = is2.split()
  
    upperbound=int(input("Give the upperbound: "))
    lowerbound=int(input("Give the lowerbound: "))

    # Calculating the sum of input list elements
    count=0
    for num1 in list1:
        for num2 in list2:
            squaresum=math.pow(int(num1),2)+math.pow(int(num2),2)
            if upperbound < squaresum < lowerbound:
                count=count+1
    print(count)
    


take_inputs()


