def convert_to_RGB(string):
    if string[0]!='#' or len(string)!=7:
        return False
    return int(string[1:3],16),int(string[3:5],16),int(string[5:],16)
n=int(input("Podaj ilość tekstów: "))
list1=[]
for i in range(n):
    list1.append(input("Podaj tekst: "))
    print(convert_to_RGB(list1[i]))

