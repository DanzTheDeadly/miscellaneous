import os
from shutil import copyfile

def find(name, path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if name.lower() == os.path.splitext(file)[0].lower():
                return root, file

def copy(srcepath, destpath):
    copied = 0
    missing = 0
    missinglist = []
    
    for line in open(r'f:/images.prn'):
        article, dimensions = line.split()
        if dimensions not in os.listdir(srcepath):
            print('NOT FOUND', dimensions)
            continue
        try:
            root, file = find(article, destpath)
        except TypeError:
            missing += 1
            missinglist.append(article)
            continue
        srce = os.path.join(srcepath, dimensions)
        newname = os.path.splitext(file)[0] + '_2' + os.path.splitext(file)[1]
        if newname in os.listdir(root):
            newname = os.path.splitext(file)[0] + '_3' + os.path.splitext(file)[1]
        dest = os.path.join(root, newname)
        copyfile(srce, dest)
        print('COPIED', srce, dest)
        copied += 1
        #os.remove(os.path.join(srcepath, dimensions))
    print('{} files copied'.format(copied))
    print('Missing', missing, missinglist)

def check(path):
    found = 0
    missing = 0
    missinglist = []

    print('Performing check...')
    for article in open(r'f:\list.prn'):
        article = ''.join(article.split())
        if find(article, path):
            found += 1
        else:
            missing += 1
            missinglist.append(article)
    print('Found', found)
    print('Missing', missing, missinglist)
    
#copy(r'f:\test\srce', r'f:\test\dest')
check(r'f:\test\dest')
