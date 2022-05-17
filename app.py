from flask import Flask, redirect, flash, render_template, request, url_for
from flask_sqlalchemy import Model

import model
from model import db, Employee

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# To get the Table in database created
with app.app_context():
    db.create_all()


# This is the default route of the application Where Welcome is displayed
@app.route("/", methods=['GET', 'POST'])
def home_page():
    return render_template('page.html', title='Employee Database', message='Welcome to Employee DB!')


# This is the about route where about of the page is displayed
@app.route("/about")
def about():
    return render_template('page.html', title='About',
                           message='This is our Employee Database where you can view all the employee details or Get a particular Employee Details')


# This Route is used to get all the details of the employees
@app.route("/employee_table")
def employee_details():
    data = Employee.query.all()
    return render_template('employee_table.html', title='Our Employee Database', employees=data)


# This Route is used to get all the details of the employee with an ID
@app.route("/show_user_by_id", methods=['GET', 'POST'])
def show_user_by_id():
    if request.method == 'GET':
        return render_template('search_by_id.html', title='Show Employee by ID')
    else:
        ID = request.form['max']
        data = Employee.query.filter(int(ID) == Employee.id).all()
        return render_template('employee_table.html', title='Search results', employees=data)


# This Route is used to get all the users with Same email company
@app.route("/show_user_by_similar_email", methods=['GET', 'POST'])
def show_employee_with_similar_email():
    if request.method == 'GET':
        return render_template('search_by_name.html', title='Show Employee who Use Same Mail Company Services')
    else:
        name = request.form['max1']
        search = "%{}%".format(name)
        data = Employee.query.filter(Employee.email_id.like(search)).all()
        return render_template('employee_table.html', title='Search results', employees=data)


# This Route to add an employee to the table
@app.route("/add", methods=['GET', 'POST'])
def add_employee():
    if request.method == 'GET':
        return render_template('add_employee.html', title='Add an Employee')

    else:
        f_name = request.form['name']
        f_mail_id = request.form['mail_id']
        f_ph_num = request.form['ph_num']
        to_add = Employee(name=f_name, email_id=f_mail_id, phone_num=f_ph_num)
        db.session.add(to_add)
        db.session.commit()
        return redirect(url_for('employee_details'))


if __name__ == '__main__':
    app.run(debug='True')
