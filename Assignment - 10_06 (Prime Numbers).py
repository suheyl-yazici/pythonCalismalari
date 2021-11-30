number = int(input("Give number : "))
list_a = set([])
for i in range(1,number + 1):
    for k in range(1,number + 1):
        if i%k == 0 and  i !=1 and  k !=1:
            list_a.add(k)
            break
list_a = list(list_a)
print(sorted(list_a))
