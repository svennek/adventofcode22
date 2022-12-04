
lines = [ ((lambda x: x.split(','))(x)) for x in  open('input').read().strip().split('\n')]

def split(f):
    return [ (int(i[0]), int(i[1])) for i in [j.split("-") for j in f]]

sectionpairs = list(map(split, lines))

containcheck = zip(sectionpairs, map(lambda x: (x[0][0] <= x[1][0] and x[0][1] >= x[1][1]) or (x[0][0] >= x[1][0] and x[0][1] <= x[1][1]), sectionpairs))

contained = list(filter(lambda x: x[1], containcheck))

for pairs, cont in contained: 
    print(pairs, cont)

print('answer 1', len(contained))
overlapcheck = zip(sectionpairs, map(lambda x: (x[0][0] <= x[1][1] and x[0][1] >= x[1][0]), sectionpairs))

overlapped = list(filter(lambda x: x[1], overlapcheck))
print('answer 2', len(overlapped))
