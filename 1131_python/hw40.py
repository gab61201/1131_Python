def is_prime(n):
    if n <= 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

start = input()
end = input().split()
string = input()
gene = []
for g in string.split(start):
    for e in end:
        if e in g:
            if is_prime(len(g.split(e)[0])):
                gene.append(g.split(e)[0])
gene.sort(key=len)
if not gene:
    print('No gene')
    exit()
new_gene = []
for i in range(len(gene[-1])+1):
    new_gene.append(sorted([g for g in gene if len(g) == i]))
output = []
for g in new_gene:
    output += g
print('\n'.join(output))
