List = []
for x in range(10):
    if x%2 == 0:
        List.append(x)
        print(x)

List2 = ['1',2,3,45,'k']
List3  = [x for x in List2 if x!='1']
print(List3)
10 in List3
print(List3)