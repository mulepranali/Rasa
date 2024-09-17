# import mysql.connector as c 

# # Establish the connection
# con = c.connect(host='localhost', user='root', password='root', database='nsedata')
# if con.is_connected():
#     print("Connection successful")

# # Create a cursor object
# cursor = con.cursor()
 
# # Fetch and print the list of tables in the database
# cursor.execute("SHOW TABLES")
# tables = cursor.fetchall()
# print("Tables in nsedata database:")
# for table in tables:
#     print(table[0])

# # Fetch and print the data from the 'data' table
# cursor.execute("SELECT * FROM data")
# rows = cursor.fetchall()
# print("\nData in 'data' table:")
# for row in rows:
#     print(row)

# # fetch the data by dept
# cursor.execute("Select id,name , dept from data where dept='etl'")
# etl_rows = cursor.fetchall()
# print("\n Data by ETL department")
# for row in etl_rows:
#     print(row)

# # fetch the data by dept datawarehouse
# cursor.execute("Select id,name , dept from data where dept='data warehouse'")
# datawarehouse_rows = cursor.fetchall()
# print("\n Data by Datawarehouse department")
# for row in datawarehouse_rows:
#     print(row)

# #count of employee
# cursor.execute("SELECT dept, COUNT(*) FROM data GROUP BY dept")
# dept_counts = cursor.fetchall()
# print("\nCount of each department:")
# for dept, count in dept_counts:
#     print(f"{dept}: {count}")



# # Close the cursor and connection
# cursor.close()
# con.close()
