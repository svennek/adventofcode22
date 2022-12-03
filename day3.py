
scores = {}
for i in range(97,97+26):
    scores[chr(i)] = i - 96
    
for i in range(65,65+26):
    scores[chr(i)] =  i - 38

#for k, v in scores.items(): print(k,v)

rucksacks1 = open('input').read().strip().split('\n')
#print(rucksacks1[:10])

def handle_rucksack1(r):
    l = int(len(r) / 2)
    a = [x for x in r[:l]]
    #print('a',len(a), a)
    b = [x for x in r[l:]]
    #print('b',len(b), b)
    return a,b

rucksacks2 = list(map(handle_rucksack1, rucksacks1) )

def handle_rucksack2(r):
    (a, b) = r
    t = None
    for x in a:
        if x in b:
            t = x
            break
    if not t:
        print("ERROR, found no common in {a} and {b}")
    return scores.get(t) 

rucksacks3 = list(map(handle_rucksack2, rucksacks2))
print('ANSWER1: sums', sum(rucksacks3))

def find_badge(rucksacks):
    candidates = list(scores.keys())
    for ru in rucksacks:
        nc = []
        rcom = ru[0] + ru[1]
        for c in candidates:
            if c in rcom: nc.append(c)
        candidates = nc

    if len(candidates) != 1: print('error')
    return candidates[0]

badges = []
for i in range(0, len(rucksacks2), 3):
    group = rucksacks2[i:i+3]
    badges.append(find_badge(group))
print(badges)
badgesum = sum(scores.get(x) for x in badges)
print('answer2: badgesum', badgesum)
