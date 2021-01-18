def Palindrom(string):
    for i in range(int((len(string))/2)):
        if string[i]!=string[len(string)-i-1]:
            return False
    return True
word=input("Podaj słowo: ")
print(Palindrom(word))
