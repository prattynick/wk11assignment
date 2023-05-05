from flask import Flask, render_template, request
import sqlite3
import mysql.connector as sql

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
	if request.method == 'POST':
		EmpID = request.form['EmpID']
		EmpName = request.form['EmpName']
		EmpGender = request.form['EmpGender']
		EmpPhone = request.form['EmpPhone']
		EmpBdate = request.form['EmpBdate']

		conn = sqlite3.connect('employee.db')
		cur = conn.cursor()
		cur.execute('''INSERT INTO employee (EmpID, EmpName, EmpGender, EmpPhone, EmpBdate) VALUES (?, ?, ?, ?, ?)''', (EmpID, EmpName, EmpGender, EmpPhone, EmpBdate))
		conn.commit()
		return 'Registered Successfully'
		conn.close()
	else:
		return render_template('registration.html')
		conn.close()

@app.route('/information')
def information():
	conn = sqlite3.connect('employee.db')
	conn.row_factory = sqlite3.Row
	c = conn.cursor()
	c.execute('''SELECT * FROM employee''')
	employee = c.fetchall()
	conn.close()
	return render_template('information.html', employee=employee)

with sql.connect(host="localhost", \
		 user="flask", \
		 password="buddy710", \
		 database="employee_db") as con:
   cur = con.cursor()



if __name__ == '__main__':
	app.run(debug=True)
