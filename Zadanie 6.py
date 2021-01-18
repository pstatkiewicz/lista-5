def bubble_sort(list1):
    for i in range(1,len(list1)):
        for j in range(len(list1)-i):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]
    return list1
def issorted(list1):
    list2=[]
    for i in range(len(list1)):
        list2.append(list1[i])
    bubble_sort(list2)
    if list1==list2:
        return True
    return False
n=int(input("Podaj ilość argumentów w liście: "))
list1=[]
for i in range(n):
    list1.append(input())
print(issorted(list1))


    
    
