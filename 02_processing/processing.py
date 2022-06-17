
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

import psycopg2
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

# Establish a connection to the database by creating a cursor object
# The PostgreSQL server must be accessed through the PostgreSQL APP or Terminal Shell

conn = psycopg2.connect(
   database="team5", user='team5', password='p3nt3c0st3s!', host='10.100.20.198', port= '5432'
)

# Create a cursor object
cur = conn.cursor()

# A sample query of all data from the "vendors" table in the "suppliers" database
cur.execute("""SELECT * FROM tweets""")
query_results = cur.fetchall()
new_query = query_results = query_results[-1]

def autopct_generator(limit):
    """Remove percent on small slices."""
    def inner_autopct(pct):
        return ('%.2f%%' % pct) if pct > limit else ''
    return inner_autopct

positive = int(new_query[0])
wpositive = int(new_query[1])
spositive = int(new_query[2])
negative = int(new_query[3])
wnegative = int(new_query[4])
snegative = int(new_query[5])
neutral = int(new_query[6])
searchTerm = str(new_query[8])
date = str(new_query[7])
time = str(new_query[9])

y = np.array([positive, wpositive, spositive,negative, wnegative, snegative, neutral])
labels = ['Positive', 'Weakly Positive','Strongly Positive', 'Neutral', 'Negative', 'Weakly Negative', 'Strongly Negative']
sizes = [positive, wpositive, spositive, neutral, negative, wnegative, snegative]
NUM_COLORS = len(sizes)
fig, ax = plt.subplots()
theme = plt.get_cmap('bwr')
ax.set_color_cycle([theme(
    1. * i / NUM_COLORS) for i in range(NUM_COLORS)])
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 1.3, box.height])
_, _, autotexts = ax.pie(
    sizes, autopct=autopct_generator(7), startangle=90, radius=1.8 * 1000)
for autotext in autotexts:
    autotext.set_weight('bold')
ax.axis('equal')
total = sum(sizes)
plt.legend(
    loc='upper left',
    labels=['%s, %1.1f%%' % (
        l, (float(s) / total) * 100) for l, s in zip(labels, sizes)],
    prop={'size': 12},
    bbox_to_anchor=(0.0, 1),
    bbox_transform=fig.transFigure
)
ax.set_title('Tweets analized')
ax.figure.savefig('/data/team5/chart.png')


conn.close()
