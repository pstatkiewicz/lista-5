def convert_to_HTML(x,y,z):
    if 0>x or 0>y or 0>z or x>255 or y>255 or z>255:
        return False
    return '#%02X%02X%02X'%(x,y,z)
n=int(input("Podaj ilość kolorów: "))
for i in range(n):
    print("Podaj 3 kolejne liczby: ")
    list1=[]
    for j in range(3):
        list1.append(int(input()))
    print(convert_to_HTML(list1[0],list1[1],list1[2]))
