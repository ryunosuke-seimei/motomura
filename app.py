from flask import Flask, request, render_template, redirect, Response, jsonify
import mysql.connector as db
import json

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.cfg')


@app.route("/village/recipes", methods=["POST"])
def recipes_create():
    title = request.form["title"]
    making_time = request.form["making_time"]
    serves = request.form["serves"]
    ingredients = request.form["ingredients"]
    cost = request.form["cost"]

    join_point = ",".join([title, making_time, serves, ingredients, cost])
    data_format = ",".join(["%s"] * 5)

    try:
        db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                                   database=app.config["DATABASES"])
        cursor = db_connection.cursor()
        cursor.execute(
            "INSERT INTO recipes (title, making_time, serves, ingredients, cost) values({})".format(
                data_format), tuple(join_point.split(",")))
        db_connection.commit()
        message = {
            "message": "Recipe successfully created! "
        }
    except:
        message = {
            "message": "Recipe creation failed!",
            "required": "title, making_time, serves, ingredients, cost"
        }

    return jsonify(message)


@app.route("/village/recipes", methods=["GET"])
def recipes_get():
    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                                   database=app.config["DATABASES"])
    cursor = db_connection.cursor()
    cursor.execute(
        "select * from recipes")
    recipe_list = cursor.fetchall()

    for item in recipe_list:
        print(item)
    
    return jsonify(recipe_list)


@app.route("/village/recipes/<id>", methods=["GET"])
def recipes_get_item(id):
    db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
                               database=app.config["DATABASES"])
    cursor = db_connection.cursor()
    cursor.execute(
        "select * from recipes where id = {}".format(id))
    recipe_list = cursor.fetchall()

    for item in recipe_list:
        print(item)

    return jsonify(recipe_list)


@app.route("/village/recipes/<id>", methods=["PATCH"])
def recipes_patch_item(id):
    pass


@app.route("/village/recipes/<id>", methods=["DELETE"])
def recipes_delete_item(id):

    pass


# @app.route('/village/item/')
# def home_item():
#     db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
#                                database=app.config["DATABASES"])
#     cursor = db_connection.cursor()
#     cursor.execute(
#         "select * from item_list")
#     item_list = cursor.fetchall()
#     return render_template("index_item.html",item_list=item_list)
#
#
# @app.route('/village/item/insert/', methods=["POST"])
# def home_item_insert():
#     name = request.form["name"]
#     genre = request.form["genre"]
#     join_point = ",".join([name, genre])
#     data_format = ",".join(["%s"] * 2)
#     db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
#                                database=app.config["DATABASES"])
#     cursor = db_connection.cursor()
#     cursor.execute(
#         "INSERT INTO item_list(name,genre) values({})".format(
#             data_format), tuple(join_point.split(",")))
#     db_connection.commit()
#     return redirect("/village/item/", code=302)
#
#
# @app.route('/village/item/delete/', methods=["POST"])
# def home_item_delete():
#     ID = request.form["id"]
#     db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
#                                database=app.config["DATABASES"])
#     cursor = db_connection.cursor()
#     cursor.execute(
#         "DELETE FROM item_list WHERE id={}".format(ID)
#     )
#     db_connection.commit()
#     return redirect("/village/item/", code=302)
#
#
# @app.route('/village/bought/')
# def index():
#     # print(app.config["SERVER"])
#     db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
#                                database=app.config["DATABASES"])
#     cursor = db_connection.cursor()
#     cursor.execute(
#         "select * from bought_list join item_list on bought_list.item_id = item_list.id ")
#     bought_list = cursor.fetchall()
#
#     cursor.execute(
#         "select * from item_list")
#     item_list = cursor.fetchall()
#
#     return render_template("index.html", lists=[bought_list, item_list])
#
#
# @app.route('/village/bought/insert/', methods=["POST"])
# def data_insert():
#     item_id = request.form["item_id"]
#     count = request.form["count"]
#     date = request.form["date"]
#
#     join_point = ",".join([item_id, count, date])
#     data_format = ",".join(["%s"] * 3)
#     db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
#                                database=app.config["DATABASES"])
#     cursor = db_connection.cursor()
#     cursor.execute(
#         "INSERT INTO bought_list(item_id,count,day) values({})".format(
#             data_format), tuple(join_point.split(",")))
#     db_connection.commit()
#
#     return redirect("/village/bought/", code=302)
#
#
# @app.route('/village/bought/delete/', methods=["POST"])
# def data_delete():
#     ID = request.form["id"]
#     db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
#                                database=app.config["DATABASES"])
#     cursor = db_connection.cursor()
#     cursor.execute(
#         "DELETE FROM bought_list WHERE id={}".format(ID)
#     )
#     db_connection.commit()
#
#     return redirect("/village/bought/", code=302)
#
#
# @app.route('/village/recipe/')
# def index_recipe():
#     # print(app.config["SERVER"])
#     db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
#                                database=app.config["DATABASES"])
#     cursor = db_connection.cursor()
#     cursor.execute(
#         "select * from recipe_list")
#     recipe_list = cursor.fetchall()
#     return render_template("index_recipe.html", recipe_list=recipe_list)
#
#
# @app.route('/village/recipe/insert/', methods=["POST"])
# def data_recipe_insert():
#     name = request.form["name"]
#     genre1 = request.form["genre1"]
#     genre2 = request.form["genre2"]
#
#     join_point = ",".join([name, genre1, genre2])
#     data_format = ",".join(["%s"] * 3)
#     db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
#                                database=app.config["DATABASES"])
#     cursor = db_connection.cursor()
#     cursor.execute(
#         "INSERT INTO recipe_list(name,genre1,genre2) values({})".format(
#             data_format), tuple(join_point.split(",")))
#     db_connection.commit()
#
#     return redirect("/village/recipe/", code=302)
#
#
# @app.route('/village/recipe/delete/', methods=["POST"])
# def data_recipe_delete():
#     ID = request.form["id"]
#
#     db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
#                                database=app.config["DATABASES"])
#     cursor = db_connection.cursor()
#     cursor.execute(
#         "DELETE FROM recipe_list WHERE id={}".format(ID)
#     )
#     db_connection.commit()
#
#     return redirect("/village/recipe/", code=302)
#
#
# @app.route('/village/recipe/detail/<ID>/')
# def data_recipe_detail(ID):
#     print(ID)
#
#     db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
#                                database=app.config["DATABASES"])
#     cursor = db_connection.cursor()
#     cursor.execute(
#         "SELECT * FROM recipe_detail_list join item_list on recipe_detail_list.item_id = item_list.id WHERE recipe_id={}".format(ID))
#     recipe_list = cursor.fetchall()
#
#     cursor.execute(
#         "select * from item_list")
#     item_list = cursor.fetchall()
#
#     send_data = [ID, recipe_list, item_list]
#
#     return render_template("detail_recipe.html", send_data=send_data)
#
#
# @app.route('/village/recipe/detail/insert/', methods=["POST"])
# def data_recipe_detail_insert():
#     ID = request.form["id"]
#     item_id = request.form["item_id"]
#     count = request.form["count"]
#
#     join_point = ",".join([ID, item_id, count])
#     data_format = ",".join(["%s"] * 3)
#     db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
#                                database=app.config["DATABASES"])
#     cursor = db_connection.cursor()
#     cursor.execute(
#         "INSERT INTO recipe_detail_list(recipe_id,item_id,count) values({})".format(
#             data_format), tuple(join_point.split(",")))
#     db_connection.commit()
#
#     return redirect("/village/recipe/detail/{}/".format(ID), code=302)
#
#
# @app.route('/village/recipe/detail/delete/', methods=["POST"])
# def data_recipe_detail_delete():
#     ID = request.form["id"]
#     ex_id = request.form["ex_id"]
#     db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
#                                database=app.config["DATABASES"])
#     cursor = db_connection.cursor()
#     cursor.execute(
#         "DELETE FROM recipe_detail_list WHERE id={}".format(ID)
#     )
#     db_connection.commit()
#
#     return redirect("/village/recipe/detail/{}/".format(ex_id), code=302)
#
#
# @app.route('/village/recipe_check/', methods=["POST"])
# def data_recipe_check():
#     genre1 = request.form["genre1"]
#     genre2 = request.form["genre2"]
#     db_connection = db.connect(host=app.config["HOST"], user=app.config["USER"], password=app.config["PASSWORD"],
#                                database=app.config["DATABASES"])
#     cursor = db_connection.cursor()
#
#     cursor.execute(
#         "select DISTINCT id,item_id from bought_list"
#     )
#     item_list = cursor.fetchall()
#     item_id = []
#     for item in item_list:
#         item_id.append(item[1])
#
#     cursor.execute(
#         "select DISTINCT recipe_list.id, recipe_list.name from recipe_list "
#         "join recipe_detail_list on recipe_list.id=recipe_detail_list.recipe_id "
#         "join bought_list on recipe_detail_list.item_id=bought_list.item_id "
#         "where recipe_list.genre1={} and recipe_list.genre2={}".format(genre1, genre2)
#     )
#     result = cursor.fetchall()
#     list_child = []
#     for child in result:
#         child_id = child[0]
#         child_name = child[1]
#         print(child_id)
#         cursor.execute(
#             "select item_list.name, recipe_detail_list.count, item_list.id from recipe_detail_list join item_list on recipe_detail_list.item_id=item_list.id where recipe_id={}".format(child_id)
#         )
#         children = cursor.fetchall()
#         new_children = []
#         count = 0
#         for find_child in children:
#             temp_child = list(find_child)
#             flag = False
#             for item in item_id:
#                 if item == temp_child[2]:
#                     flag = True
#             if flag:
#                 count += 1
#                 temp_child.append(1)
#             else:
#                 temp_child.append(0)
#
#             new_children.append(temp_child)
#
#         new_children.insert(0, count)
#         new_children.insert(0, child_name)
#
#         list_child.append(new_children)
#
#     print(list_child)
#     list_child = sorted(list_child, key=lambda x: x[1],reverse=True)
#     print(list_child)
#
#     return Response(json.dumps(list_child),  mimetype='application/json')


if __name__ == '__main__':
    app.run()
