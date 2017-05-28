import os
from extractor import extract

BASE_DIR = 'docs'
infos = []
files = [f for f in os.listdir(BASE_DIR) if f.endswith('.txt')]
for f in files:
    infos.append(extract(f))

for info in infos:
    print("=" * 30)
    print("Authors: {}".format(', '.join(info['Authors'])))
    print("Title: {}".format(info['Title']))
    if info['Subjects'] : print("Subjects: {}".format(info['Subjects']))
    if info['Comments'] : print("Comments: {}".format(info['Comments']))
    print("Link: {}".format(info['Link']))
    print("Relations: {}".format(', '.join(info['Relations'])))
