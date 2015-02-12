#!/usr/bin/env python

import subprocess
import numpy

with open("data1.txt", 'w') as f:

	for i in numpy.arange(-10, 10, 0.1):
		f.write(str(i) + " " + subprocess.check_output(["java", "-jar", "Generator1.jar", str(i)]))