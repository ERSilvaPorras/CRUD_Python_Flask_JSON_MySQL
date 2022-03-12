from flask.views import MethodView
from flask import flash, render_template, request, redirect 
from src.db import conn
from fpdf import FPDF
import os

class IndexController(MethodView):
    def get(self):
        cur = conn.cursor()
        query = "SELECT * FROM users;"
        cur.execute(query)
        users_t = cur.fetchall()
        users_l = list(users_t)
        return render_template('public/index.html', users = users_l)
        
    def post(self):
        options_l = request.form.getlist("op")
        options_t = tuple(options_l)
        #print(str(options_l))
        match request.form.get('actionButton'):
            case "editar":
                cur = conn.cursor()
                users_l=list()
                match len(options_l):
                    case 0:
                        flash("No selecciono ningun registro.", "warning")
                        return redirect('/')
                    case 1:
                        query = "SELECT * FROM  users WHERE id = %s;"
                        cur.execute(query, (options_l[0]))
                        users_t = cur.fetchone()
                        users_l = []
                        users_l.append(users_t)
                        #print(str(users_l))
                        return render_template('public/edit-form.html', users = users_l)
                    case _:
                        query = " SELECT * FROM users WHERE id IN %s;"
                        cur.execute(query, (options_t,))
                        users_l = cur.fetchall()
                        #print(str(users_l))
                        return render_template('public/edit-form.html', users = users_l)
            case "compartir":
                cur = conn.cursor()
                query = "SELECT * FROM users;"
                cur.execute(query)
                users_t = cur.fetchall()
                # CREATE JSON
                dir_file = "C:/Users/richa/Desktop/flask-app/src/static/json"
                file_json = open(os.path.join(dir_file, "users.json"), mode='w+')
                user_list_json = []
                for user in users_t:
                    user_dict =  {}
                    user_dict["id"] = user[0]
                    user_dict["fullname"] = user[1]
                    user_dict["email"] = user[2]
                    user_dict["phone"] = user[3]
                    user_dict["country"] = user[4]
                    user_dict["date"] = user[5]
                    user_list_json.append(user_dict)
                print(str(users_t))
                string_users = str(user_list_json)
                file_json.write(string_users)
                file_json.close()
                # CREATE PDF
                # dir_file = "C:/Users/richa/Desktop/flask-app/src/static/PDF"
                # pdf = FPDF()
                # pdf.add_page()
                # pdf.set_font("Times", size=10)
                # line_height = pdf.font_size * 2.5
                # col_width = pdf.epw / 6
                # for row in users_t:
                #     for datum in row:
                #         pdf.multi_cell(col_width, line_height, datum, border=1, ln=3, max_line_height=pdf.font_size)
                #     pdf.ln(line_height)
                # pdf.output(dir_file + 'users.pdf')
                return ('', 204)
            case "eliminar":
                cur = conn.cursor()
                match len(options_l):
                    case 0:
                        flash("No selecciono ningun registro.", "warning")
                    case 1:
                        query = "DELETE FROM users WHERE id = %s;"
                        cur.execute(query, (options_l[0]))
                        cur.connection.commit()
                    case _:
                        query = "DELETE FROM users WHERE id IN %s;"
                        cur.execute(query, (options_t,))
                        cur.connection.commit()
                return redirect('/')
        #print(options_l)
        #return redirect('/')