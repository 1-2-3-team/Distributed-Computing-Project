
import psycopg2
from datetime import datetime
import matplotlib as plt

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
#print(new_query)
positive = int(new_query[0])
wpositive = int(new_query[1])
spositive = int(new_query[2])
negative = int(new_query[3])
wnegative = int(new_query[4])
snegative = int(new_query[5])
neutral = int(new_query[6])

new_query = new_query.pop(7)
new_query = new_query.pop(8)

conn.close()
'''
def plotPieChart(self, positive, wpositive, spositive, negative, wnegative, snegative, neutral, searchTerm, noOfSearchTerms):
    labels = ['Positive [' + str(positive) + '%]', 'Weakly Positive [' + str(wpositive) + '%]','Strongly Positive [' + str(spositive) + '%]', 'Neutral [' + str(neutral) + '%]',
              'Negative [' + str(negative) + '%]', 'Weakly Negative [' + str(wnegative) + '%]', 'Strongly Negative [' + str(snegative) + '%]']
    sizes = [positive, wpositive, spositive, neutral, negative, wnegative, snegative]
    colors = ['yellowgreen','lightgreen','darkgreen', 'blue', 'red','lightsalmon','darkred']
    patches, texts = plt.pie(sizes, colors=colors, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.title('How people are reacting on ' + searchTerm + ' by analyzing ' + str(noOfSearchTerms) + ' Tweets.')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('chart.png')'''
    

#def percentage(self, part, whole):
#    temp = 100 * float(part) / float(whole)
#    return format(temp, '.2f')
#
#def plotPieChart(self, positive, wpositive, spositive, negative, wnegative, snegative, neutral, searchTerm, noOfSearchTerms):
#    labels = ['Positive [' + str(positive) + '%]', 'Weakly Positive [' + str(wpositive) + '%]','Strongly Positive [' + str(spositive) + '%]', 'Neutral [' + str(neutral) + '%]',
#            'Negative [' + str(negative) + '%]', 'Weakly Negative [' + str(wnegative) + '%]', 'Strongly Negative [' + str(snegative) + '%]']
#    sizes = [positive, wpositive, spositive, neutral, negative, wnegative, snegative]
#    colors = ['yellowgreen','lightgreen','darkgreen', 'blue', 'red','lightsalmon','darkred']
#    patches, texts = plt.pie(sizes, colors=colors, startangle=90)
#    plt.legend(patches, labels, loc="best")
#    plt.title('How people are reacting on ' + searchTerm + ' by analyzing ' + str(noOfSearchTerms) + ' Tweets.')
#    plt.axis('equal')
#    plt.tight_layout()
#    plt.savefig('chart.png')