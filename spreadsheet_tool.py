from sys import argv
from random import shuffle

def read_csv(filename):
    '''Read a csv into a list of lines'''

    with open(filename, 'r', encoding='ISO-8859-1') as i:
        return [u.strip('\n').split(',') for u in i.readlines()]


def combine_filenames(f1, f2):
    '''f1 = 'Round 4 Origins Coding Matrix KN.csv'
       f2 = 'Round 4 Origins Coding Matrix RC.csv'
       combine_filenames(f1, f2)
       'Round 4 Origins Combined Coding Matrix KN RC.csv'

       also adds some random numbers at the end to avoid filename collisions
    '''

    tokens = f1.split(' ')
    prefix = tokens[:3] # word number word
    prefix.append('Combined') # word number word combined
    prefix.extend(tokens[3:5])

    prefix.append(f1.split(' ')[-1].split('.')[0])
    prefix.append(f2.split(' ')[-1].split('.')[0])

    random_numbers = [str(u) for u in list(range(10))]
    shuffle(random_numbers)
    random_numbers = ''.join(random_numbers)
    prefix.append(random_numbers)

    result = ' '.join(prefix)

    return result + '.csv'


def write_csv(data, filename):
    '''Write a list of lists of strings to csv, where the filename was
       generated using combine_filenames
    '''

    data = '\n'.join([','.join(data[i]) for i in range(len(data))])
    with open(filename, 'w', encoding = 'ISO-8859-1') as o:
        o.write(data)


def sanity_check(s1, s2):
    '''Make sure the input files have matching numbers of rows and cols'''

    if len(s1) != len(s2) or len(s1[0]) != len(s2[0]):
        raise Exception("Sanity check failed: number of rows or number of "
                        "columns unequal! Check files and retry.")
        exit(1)

    if len(set([len(u) for u in s1])) > 1:
        raise Exception("It appears file 1 has commas in its rownames. "
                        "Check file, edit if necessary, and retry.")
        exit(1)

    if len(set([len(u) for u in s2])) > 1:
        raise Exception("It appears file 2 has commas in its rownames. "
                        "Check file, edit if necessary, and retry.")
        exit(1)


def combine(filename1, filename2):
    s1 = read_csv(filename1)
    s2 = read_csv(filename2)

    sanity_check(s1, s2)

    colnames = s1[0][:]
    rownames = [s1[rownumber][0] for rownumber in range(len(s1))]

    new_colnames = []
    new_colnames.append(colnames[0])
    for name in colnames[1:]:
        new_colnames.append(name)
        new_colnames.append(name)

    s3 = []
    s3.append(new_colnames)

    for i in range(1, len(s1)): # rows
        new_row = []
        new_row.append(rownames[i])
        for j in range(1, len(s1[0])): # columns
            new_row.append(s1[i][j])
            new_row.append(s2[i][j])

        s3.append(new_row)

    combined_filename = combine_filenames(filename1, filename2)

    write_csv(s3, combined_filename)


if __name__ == '__main__':
    if len(argv) != 3:
        raise Exception('Usage: python3 file1.csv file2.csv')
        exit(1)

    f1 = argv[1]
    f2 = argv[2]
    combine(f1, f2)


