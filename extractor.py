import os
import nltk
import re
from nltk.sem import extract_rels,rtuple
from relations import extract_relations

BASE_DIR = '15_docs'
IN = re.compile(r'.*\bin\b(?!\b.+ing)')

class doc():
	pass

def extract(file_name):
	# print(file_name)
	file_path = os.path.join(BASE_DIR, file_name)
	data_file = open(file_path, 'r')
	data = data_file.read().splitlines()

	has_comments = data[3].startswith('Comments:')

	info = {}
	# print(data[0].split())
	info['Link'] = data[0].split()[1]
	info['Title'] = data[1]
	info['Authors'] = [author.strip() for author in data[2].split(',')]
	info['Comments'] = data[3][10:] if has_comments else None
	info['Subjects'] = (data[4] if has_comments else data[3])[10:]
	info['Text'] = '\n'.join(data[5:] if has_comments else data[4:])
	info['Relations'] = extract_relations(info['Text'])

	return info



def main():
	files = [f for f in os.listdir(BASE_DIR) if f.endswith('.txt')]
	# extract(files[0])
	for f in files:
		extract(f)

if __name__ == '__main__':
	main()
