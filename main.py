import argparse
import csv

parser = argparse.ArgumentParser()

parser.add_argument('size')
args = parser.parse_args()

f = open('file.csv')
csv_file = csv.reader(f)

result = []
file_name_prefix = 1
header = []
for index, row in enumerate(csv_file):
    if index == 0:
        header = row
        continue

    if index % int(args.size) == 0:
        f = open('file{0}.csv'.format(file_name_prefix), 'w', newline="")
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(result)
        file_name_prefix += 1
        result.clear()
    result.append(row)


