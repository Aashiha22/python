def find_missing(list1, size):
    a,b = (1,1)
    for i in range(1, size+1):
        a = a ^ i
    for val in list1:
        b = b ^ val
    return a^b


total = input()
for i in range(0,int(total)):
    size = int(input())
    list1 = []
    str1 = input()
    list1 = str1.split(" ")
    print(list1)
    for i in range(0,len(list1)):
        list1[i] = int(list1[i])
    #print(list1)
    print(find_missing(list1,size))
