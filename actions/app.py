
# from flask import Flask, jsonify
# import mysql.connector as c

# app = Flask(__name__)

# # Database connection details
# config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': 'root',
#     'database': 'nsedata'
# }

# # Helper function to connect to the database
# def get_db_connection():
#     con = c.connect(**config)
#     return con

# @app.route('/')
# def index():
#     return "Welcome to the Employees Database API"

# @app.route('/tables', methods=['GET'])
# def get_tables():
#     con = get_db_connection()
#     cursor = con.cursor()
#     cursor.execute("SHOW TABLES")
#     tables = cursor.fetchall()
#     cursor.close()
#     con.close()
#     return jsonify(tables=[table[0] for table in tables])

# @app.route('/employees', methods=['GET'])
# def get_employees():
#     con = get_db_connection()
#     cursor = con.cursor()
#     cursor.execute("SELECT * FROM employees")
#     rows = cursor.fetchall()
#     cursor.close()
#     con.close()
#     return jsonify(employees=rows)

# @app.route('/employees/etl', methods=['GET'])
# def get_etl_employees():
#     con = get_db_connection()
#     cursor = con.cursor()
#     cursor.execute("SELECT id, name, dept FROM employees WHERE dept = 'ETL'")
#     rows = cursor.fetchall()
#     cursor.close()
#     con.close()
#     return jsonify(etl_employees=rows)

# @app.route('/employees/datawarehouse', methods=['GET'])
# def get_datawarehouse_employees():
#     con = get_db_connection()
#     cursor = con.cursor()
#     cursor.execute("SELECT id, name, dept FROM employees WHERE dept = 'Datawarehouse'")
#     rows = cursor.fetchall()
#     cursor.close()
#     con.close()
#     return jsonify(datawarehouse_employees=rows)

# @app.route('/employees/count', methods=['GET'])
# def get_employee_counts():
#     con = get_db_connection()
#     cursor = con.cursor()
#     cursor.execute("SELECT dept, COUNT(*) FROM employees GROUP BY dept")
#     rows = cursor.fetchall()
#     cursor.close()
#     con.close()
#     return jsonify(employee_counts={dept: count for dept, count in rows})

# if __name__ == '__main__':
#     app.run(port=5001, debug=True)
