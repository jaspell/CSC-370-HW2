#!/usr/bin/env python

import subprocess
import random

with open("data1_small.txt", 'w') as f:

	for i in range(500):
		print i
		x = random.uniform(0, 5.0)
		f.write(str(x) + " " + str(subprocess.check_output(["java", "-jar", "Generator1.jar", str(x)])))