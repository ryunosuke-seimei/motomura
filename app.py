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


@app.route('/village/recipe/')
def index_recipe():
    # print(app.config["SERVER"])
    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                               database=app.config["DATABASES"])
    cursor = db_connection.cursor()
    cursor.execute(
        "select * from recipe_list")
    recipe_list = cursor.fetchall()
    return render_template("index_recipe.html", recipe_list=recipe_list)


@app.route('/village/recipe/insert/', methods=["POST"])
def data_recipe_insert():
    name = request.form["name"]
    genre1 = request.form["genre1"]
    genre2 = request.form["genre2"]

    join_point = ",".join([name, genre1, genre2])
    data_format = ",".join(["%s"] * 3)
    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                               database=app.config["DATABASES"])
    cursor = db_connection.cursor()
    cursor.execute(
        "INSERT INTO recipe_list(name,genre1,genre2) values({})".format(
            data_format), tuple(join_point.split(",")))
    db_connection.commit()

    return redirect("/village/recipe/", code=302)


@app.route('/village/recipe/delete/', methods=["POST"])
def data_recipe_delete():
    ID = request.form["id"]

    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                               database=app.config["DATABASES"])
    cursor = db_connection.cursor()
    cursor.execute(
        "DELETE FROM recipe_list WHERE id={}".format(ID)
    )
    db_connection.commit()

    return redirect("/village/recipe/", code=302)


@app.route('/village/recipe/detail/<ID>/')
def data_recipe_detail(ID):
    print(ID)

    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                               database=app.config["DATABASES"])
    cursor = db_connection.cursor()
    cursor.execute(
        "SELECT * FROM recipe_detail_list WHERE recipe_id={}".format(ID))
    recipe_list = cursor.fetchall()
    send_data = [ID, recipe_list]

    return render_template("detail_recipe.html", send_data=send_data)


@app.route('/village/recipe/detail/insert/', methods=["POST"])
def data_recipe_detail_insert():
    ID = request.form["id"]
    name = request.form["name"]
    count = request.form["count"]

    join_point = ",".join([ID, name, count])
    data_format = ",".join(["%s"] * 3)
    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                               database=app.config["DATABASES"])
    cursor = db_connection.cursor()
    cursor.execute(
        "INSERT INTO recipe_detail_list(recipe_id,sozai,count) values({})".format(
            data_format), tuple(join_point.split(",")))
    db_connection.commit()

    return redirect("/village/recipe/detail/{}/".format(ID), code=302)


@app.route('/village/recipe/detail/delete/', methods=["POST"])
def data_recipe_detail_delete():
    ID = request.form["id"]
    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                               database=app.config["DATABASES"])
    cursor = db_connection.cursor()
    cursor.execute(
        "DELETE FROM recipe_detail_list WHERE id={}".format(ID)
    )
    db_connection.commit()

    return redirect("/village/recipe/detail/{}/".format(ID), code=302)


if __name__ == '__main__':
    app.run()
