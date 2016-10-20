#!/usr/bin/python

import os
import numpy as np
import matplotlib.pyplot as plt
import time

def main():
	rootPath = os.path.join(os.sep, os.path.expanduser('~'), 'datasets', 'soc_gen_data')
	trainFilePath = os.path.join(rootPath, 'train.csv')
	testFilePath = os.path.join(rootPath, 'test.csv')

	f = open(trainFilePath, 'r')
	lines = f.readlines()
	f.close()

	rows = len(lines)-1
	cols = 0
	fields = lines[0].split(",")
	for field in fields:
		if field[0] == 'X':
			cols += 1

	X_train = np.zeros((rows, cols), dtype=np.float32)
	Y = np.zeros((rows), dtype=np.int8)

	for i in range(1, len(lines)):
		vals = lines[i].split(",")
		index = int(vals[0])-1

		for j in range(1,len(vals)-1):
			X_train[index,j-1] = vals[j]

		Y[index] = vals[len(vals)-1]

	fig = plt.figure()
	ax = fig.gca()
	fig.show()

	for i in range(cols):
		ax = fig.gca()
		fig.show()

		ax.plot(X_train[:,i])
		fig.canvas.draw()
		raw_input('pause : press any key ...')
		# fig.clear()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print "Pressed CNTRL+C"