from flask.views import MethodView
from flask import render_template, request, redirect
from src.db import conn

class CreateController(MethodView):
    def get(self):
        return render_template('public/create-form.html')
    
    def post(self):
        fullname = request.form.get('fullname')
        email =  request.form.get('email')
        phone = request.form.get('phone')
        country = request.form.get('country')
        date = request.form.get('date')
        print("Resultado:" + str(fullname) + str(email) + str(phone) + str(country) + str(date))
        cur = conn.cursor()
        query = "INSERT INTO users(fullname, email, phone, country, date) VALUES(%s, %s, %s, %s, %s);"
        cur.execute(query, (fullname, email, phone, country, date))
        cur.connection.commit()

     
        return redirect('/')