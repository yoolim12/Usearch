with open('temp.txt') as f:
    lines = f.read().splitlines()

new_lines = list()

for line in lines:
    split = line.split(',')
    new_date = ["'" + '-'.join(split[4:7]) + "'"]
    new_line = split[0:4] + new_date +split[7:]
    new_line = ','.join(new_line)

    new_lines.append(new_line)

with open('new.txt', 'w') as f:
    for nl in new_lines:
        f.write(nl+'\n')