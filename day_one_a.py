

with open('input.txt', 'r') as f:
    input = f.readlines()
def findmax():
    max = []
    total = 0
    for x in input:
        if x.strip() != '':
            total += int(x.strip())
        else:
            max.append(total)
            total = 0
    max.sort()
    print(sum(max[-3:]))

findmax()