import ipaddress

#creating empty list// ip_list
ip_list =[]

n = int(input("Enter the number of IPs you want to enter: "))

for i in range(0, n):
    ip = input()
    ip_list.append(ip)  #adding the IPs to the list
    
sorted_list=[]
sorted_list=ip_list.sort()

print(ip_list)

print(sorted_list)


    

