from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    email_id = db.Column(db.String(120), unique=True, nullable=False)
    phone_num = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.id}: {self.name}\t qty: {self.email_id}\tprice: {self.phone_num} \t'