def bubble_sort(list1):
    for i in range(1,len(list1)):
        for j in range(len(list1)-i):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]
    return list1
def Anagram(string1,string2):
    if len(string1)!=len(string2):
        return False
    list1=[]
    list2=[]
    for i in range(len(string1)):
        list1.append(string1[i])
        list2.append(string2[i])
    bubble_sort(list1)
    bubble_sort(list2)
    for i in range(len(string1)):
        if list1[i]!=list2[i]:
            return False 
    return True
n=int(input("Podaj ilość słów do porównania: "))
words=[]
print("Podaj słowa: ")
for i in range(n):
    words.append(input())
for i in range(n):
    for j in range(1,n-i):
        print(i,"i",i+j,Anagram(words[i],words[i+j]))


        
