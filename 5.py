import os

def CombineLists():
    list_1=[]
    list_2=[]
    combinedList =[]
    
    print("Enter number of element of list 1:", end = " ")
    n1 = int(input())
    print('Enter the elements')
    for i in range(0, n1):
        element = input()
        list_1.append(element)

    print("Enter number of element of list 2:", end = " ")
    n2 = int(input())
    print('Enter the elements')
    for i in range(0, n2):
        element = input()
        list_2.append(element)

    if (n1 > n2) or (n1 == n2):
        n_bigest = n1
    else:
        n_bigest = n2


    for i in range(n_bigest):
        try:
            combinedList.append(list_1[i])
        except:
            pass
    
        try:
            combinedList.append(list_2[i])
        except:
            pass
    return(combinedList)

print('The combined list: ', CombineLists())

os.system('pause')