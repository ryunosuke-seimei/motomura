from flask import Flask, request, render_template, redirect
import mysql.connector as db

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.cfg')


@app.route('/village/')
def index():
    # print(app.config["SERVER"])
    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                               database=app.config["DATABASES"])
    cursor = db_connection.cursor()
    cursor.execute(
        "select * from bought_list")
    bought_list = cursor.fetchall()
    return render_template("index.html", bought_list=bought_list)


@app.route('/village/insert/', methods=["POST"])
def data_insert():
    name = request.form["name"]
    count = request.form["count"]
    date = request.form["date"]

    join_point = ",".join([name, count, date])
    data_format = ",".join(["%s"] * 3)
    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                               database=app.config["DATABASES"])
    cursor = db_connection.cursor()
    cursor.execute(
        "INSERT INTO bought_list(name,count,day) values({})".format(
            data_format), tuple(join_point.split(",")))
    db_connection.commit()

    return redirect("/village/", code=302)


@app.route('/village/delete/', methods=["POST"])
def data_delete():
    ID = request.form["id"]
    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                               database=app.config["DATABASES"])
    cursor = db_connection.cursor()
    cursor.execute(
        "DELETE FROM bought_list WHERE id={}".format(ID)
    )
    db_connection.commit()

    return redirect("/village/", code=302)



if __name__ == '__main__':
    app.run()
