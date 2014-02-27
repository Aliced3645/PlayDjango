#A naive way to connect to database

import MySQLdb;

db = MySQLdb.connect(user='shu', db='testdb', passwd='shu', host='localhost');

cursor = db.cursor();
cursor.execute('SELECT * from table1');
names = [row[0] for row in cursor.fetchall()];
print names;
db.close();