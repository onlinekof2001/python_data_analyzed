## https://wiki.postgresql.org/wiki/Python (Python drivers for PG)
#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="",user="", password="", host="", port="60901")
print "Connecting database successfully"

'''
# DDL operation
ddl_op = conn.cursor()
ddl_op.execute('''CREATE TABLE PY_TAB
(PY_ID INT PRIMARY KEY NOT NULL,
 NAME  CHAR(30) NOT NUL,
 AGE   INT2 NOT NULL,
 ADDRESS TEXT NOT NULL,
 SALARY REAL);
'''
print "Table created successfully"

conn.commit()
conn.close()
'''

'''
# DML INSERT operation
ddl_op = conn.cursor()

dml_op.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

dml_op.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

dml_op.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

dml_op.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.commit()

print "Records created successfully";
conn.close()

# DML UPDATE operation

dml_op.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
dml_op.execute("DELETE from COMPANY where ID=2")
conn.commit
print "Total number of rows deleted :", dml_op.rowcount
'''

'''
# DQL operation

dql_op = conn.cursor()

dql_op.execute("SELECT id, name, address, salary  from COMPANY")
rows = dql_op.fetchall()
for row in rows:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

print "Operation done successfully";
conn.close()  
'''

1

