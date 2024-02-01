List = [1,2,3,4,54,5,65,6,6,76,5,4,90]
truple = (2,3,4,5,6,78,8,6,5,4,12)
for x in List:
    print(x)
    List[0] = 67
    print(List[0])
    print(List[-1])

    print(truple[5])