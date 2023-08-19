n_lst = set(range(1, 10001))
r_lst = set()
for i in n_lst:
    for j in str(i):
        i += int(j)
    r_lst.add(i)
self_num = sorted(n_lst - r_lst)
print(*self_num, sep='\n')