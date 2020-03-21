import os
import json
from time import sleep
from shutil import move
from pathlib import Path
import sys

class App:
	def __init__(self):
		self.path_folder = 'resources/folder'
		self.path_json = 'resources/data.json'
		with open(self.path_folder, 'r') as f:
			a = f.read()
			self.folder = Path(a) if a != '' else ''
			f.close()

		with open(self.path_json, 'r') as f:
			self.data = json.load(f)
			f.close()

	def loop(self):
		while True:
			if self.folder != '':
				self.organize(self.folder)
			sleep(5)

	def organize(self, folder):
		files = os.listdir(folder)
		if len(files) != 0:
			for file in files:
				ex = file.split('.')[-1]
				for i in self.data:
					if ex in i['ext']:
						try:
							move(folder / file, folder / f'{i["name"]}/{file}')
						except FileNotFoundError:
							os.mkdir(folder / i['name'])
							move(folder / file, folder / f'{i["name"]}/{file}')
						break

if __name__ == '__main__':
	App()