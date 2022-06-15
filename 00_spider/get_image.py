import subprocess
import os
p = subprocess.Popen(["scp", "/data/team5/chart.png", "lbgalvan@132.247.186.67:/home/lbgalvan/public_html/static/images/"])
html =  subprocess.Popen(["scp", "-r", "/home/lbgalvan/git/Distributed-Computing-Project/public_html/", "lbgalvan@132.247.186.67:/home/lbgalvan/"])
sts = os.waitpid(p.pid, 0)
