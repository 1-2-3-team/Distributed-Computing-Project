'''
gruisu93@gmail.com
Copyright (c) 2022 Luis Yovanny Bedolla Galvan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.
'''

import csv
import subprocess
import os
from turtle import home
p = subprocess.Popen(["scp", "/data/team5/chart.png", "lbgalvan@132.247.186.67:/home/lbgalvan/public_html/img/"])
html =  subprocess.Popen(["scp", "-r", "/home/lbgalvan/git/Distributed-Computing-Project/public_html/", "lbgalvan@132.247.186.67:/home/lbgalvan/"])
r = subprocess.Popen(["rm", "/home/lbgalvan/result.csv"])
sts = os.waitpid(p.pid, 0)
sts1 = os.waitpid(r.pid, 0)
sts2 = os.waitpid(html.pid, 0)
