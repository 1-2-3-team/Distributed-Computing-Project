import subprocess
import os
p = subprocess.Popen(["scp", "/data/team5/chart.png", "lbgalvan@132.247.186.67:/home/lbgalvan/public_html/static/images/"])
sts = os.waitpid(p.pid, 0)