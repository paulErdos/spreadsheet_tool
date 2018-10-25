fname = 'Round 4 Origins Coding Matrix KN.csv'

with open(fname, 'r', encoding = 'ISO-8859-1') as i:
    data = [u.split(',') for u in i.readlines()]

# do stuff with data

# then rejoin
data = [','.join(data[i]) for i in range(len(data))]

with open('example_output.csv', 'w', encoding = 'ISO-8859-1') as o:
    o.write(data)
