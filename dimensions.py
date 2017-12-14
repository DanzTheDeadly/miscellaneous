def dimensions():
    result_file = open(r'f:/dimensions.txt', 'w')
    for line in open(r'f:\размеры.txt'):
        newline = line.rstrip()
        if 'x' in line:
            if not r'/' in line:
                newline = newline + ';' + newline.split('x')[0] + "cm" + ';' + newline.split('x')[1] + "cm"
        elif r'/' in line:
            newline = newline + ';' + '-'.join(newline.split(r'/')) + "cm"
        print(newline)
        print(newline, file=result_file)
        
dimensions()
