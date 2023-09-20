import os, shutil


KEY_FOR_SEARCH = input('What find???\n')
PATH_FOR_COPY = input('What copy file??\n')
def search():
    for adress, dirs, files in os.walk(input('input path start\n')):
        for file in files:
            if file.endswith('.txt') and '$' not in file:
                yield os.path.join(adress, file)

def read_from_pathtxt(path):
    with open(path) as r:
        for i in r:
            if KEY_FOR_SEARCH in i:
                return copy(path)

def copy(path):
    file_name = path.split('\\')[-1]

    shutil.copyfile(path, os.path.join(PATH_FOR_COPY, file_name))
    print('file copy', file_name)


for i in search():
    try:
        read_from_pathtxt(i)
    except Exception as error:
        with open(os.path.join(PATH_FOR_COPY, 'errors.txt'), 'a') as r:
            r.write(str(error) + '\n' + i + '\n')

