#Printing all positive numbers in a list

#Initialising empty list
num_list = [];

#Number of elements you want to enter in a list
n = int(input("Enter no. of elements: "))

#Adding elements one by one
for i in range(0, n): 
    element = int(input())
    num_list.append(element)
    
#Checking & print all positive numbers
print("All positive numbers: ", end="")
for i in range(0, n):
    if num_list[i] >= 0:
        print (num_list[i], end=" ");