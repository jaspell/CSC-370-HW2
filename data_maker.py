#!/usr/bin/env python

import random

with open("data_test.txt", 'w') as f:

	for i in range(100000):
		x = random.uniform(-10.0, 10.0)
		f.write(str(x) + " " + str((1/10.0)*(x**2) - x + 4) + "\n")

		if i % 100 == 0:
			print i