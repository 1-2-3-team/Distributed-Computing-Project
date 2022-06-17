
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
explode = (0,0,0,0.1,0,0,0)
fig, ax = plt.subplots()
#colors = ['yellowgreen','lightgreen','darkgreen', 'grey', 'red','lightsalmon','darkred']
ax.pie(sizes, autopct='%.1f%%', shadow=True, startangle=90)
ax.legend(labels, loc='best')
ax.title('Tweets analized')
ax.set_aspect('equal')
#plt.tight_layout()
ax.savefig('/data/team5/chart.png')


conn.close()
