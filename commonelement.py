#to find common elements of Dict1 and Dict2
# Common Elements i.e., having same key and values

Dict1 ={"Key1":[1,5,6],"Key2":[3,4],"Key3":[7,9]}
Dict2={"Key3":[7],"Key1":[1,6]}
Final_Dict={}

Keys=Dict1.keys()

for i in Keys:
    if i in Dict2:
        Final_Dict[i] = []
        for val in Dict1[i]:
            if val in Dict2[i]:
                Final_Dict[i].append(val)


print("Common Element in Dict1 and Dict2 are: "+str(Final_Dict))