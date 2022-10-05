import email
from unicodedata import name
from flask import *
import sqlite3

app = Flask(__name__)

@app.route('/')
def flaskWork():
    return render_template('home.html')

@app.route('/bookings')
def bookings():
    return render_template('bookings.html')

@app.route('/savedetails', methods= ["POST", "GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            address = request.form["address"]
            phone = request.form["phone"]
            email = request.form["email"]
            date = request.form["date"]
            time = request.form["time"]

            with sqlite3.connect("clients.db") as con:
                curp = con.cursor()
                curp.execute("INSERT into Clients (name, address, phone, email, date, time ) values (?,?,?,?,?,?)", (name, address, phone, email, date, time))
                con.commit()
                msg = "Your Booking was Successful"

        except:
            con.rollback()
            msg = "Sorry Your Booking was Unsuccessful"
        finally:
            return render_template("success.html", msg = msg)
            con.close()

@app.route('/<name>')
def view(name):
    if name == 'damilola':
        con = sqlite3.connect("clients.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select * from Clients")
        rows = cur.fetchall()
        return render_template("view.html", rows = rows )

@app.route('/delete')
def delete():
    return render_template("delete.html")

@app.route('/deleterecord', methods = ["POST"])
def deleterecord():
    id = request.form["id"]
    with sqlite3.connect("clients.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from Clients where id = ?", id)
            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return render_template("delete_record.html", msg = msg)

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')
if __name__ == '__main__':
    app.run(debug=True)