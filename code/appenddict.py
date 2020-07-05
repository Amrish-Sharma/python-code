# To append the Dict2 elements at the end of Dict1

Dict1 ={"Key1":[1,5,6],"Key2":[3,4],"Key3":[7,9]}
Dict2 = {"Key4": [9], "Key5": [11, 2]}


Keys = Dict2.keys()

for i in Keys:
    Dict1.update({i : Dict2[i]})
print(Dict1)