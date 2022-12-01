sections = open('input').read().strip().split("\n\n")
sums = []

for sec in sections:
    sums.append(sum(int(x) for x in sec.split("\n")))
sums = sorted(sums, reverse=True)

#print(f'len {len(sums)}')
#print(sums)

# answer 1
print(f'max {sums[0]}')

# answer 2
top3 = sum(sums[:3])
print(f'top3 {top3}')
