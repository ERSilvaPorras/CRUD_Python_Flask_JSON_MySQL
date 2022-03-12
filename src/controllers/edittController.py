from flask.views import MethodView
from flask import render_template, redirect, request
from src.db import conn

class EdittController(MethodView):
    def get(self):
        return render_template('public/edit-form.html')
    def post(self):
        if request.form.get('actionButton') == "guardar":
            id_l = request.form.getlist('id')
            fullname_l = request.form.getlist('fullname')
            email_l = request.form.getlist('email')
            phone_l = request.form.getlist('phone')
            country_l = request.form.getlist('country')
            date_l = request.form.getlist('date')
            print(str(fullname_l))
            for i in range(0, len(id_l)):
                cur = conn.cursor()
                query = "UPDATE users SET fullname = %s, email = %s, phone = %s, country = %s, date = %s WHERE id = %s;"
                cur.execute(query, (fullname_l[i], email_l[i], phone_l[i], country_l[i], date_l[i], id_l[i]))
                cur.connection.commit()
                cur.close()
        return redirect('/')