#code
num = input()
for i in range(0, int(num)):
    str1 = input()
    str2 = ""
    list1 = str1.split(".")
    list1.reverse()
    for i in range(0, len(list1)-1):
        str2 += list1[i]
        str2 += "."
    str2 += list1[len(list1)-1]
    print(str2)
