from typing import List, Dict
import simplejson as json
from flask import Flask, request, Response, redirect
from flask import render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'zillowData'
mysql.init_app(app)


@app.route('/', methods=['GET'])
def index():
    user = {'username': 'Zillow Project'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblZillowImport')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, zillow=result)


@app.route('/view/<int:ID>', methods=['GET'])
def record_view(ID):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblZillowImport WHERE id=%s', ID)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', property=result[0])


@app.route('/edit/<int:ID>', methods=['GET'])
def form_edit_get(ID):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblZillowImport WHERE id=%s', ID)
    result = cursor.fetchall()
    return render_template('edit.html', title='Edit Form', property=result[0])


@app.route('/edit/<int:ID>', methods=['POST'])
def form_update_post(ID):
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('house'), request.form.get('Car_Garage'), request.form.get('Living_Space_sq_ft'),
                 request.form.get('Beds'), request.form.get('Baths'),
                 request.form.get('Zip'), request.form.get('Year'), request.form.get('List_price'), ID)
    sql_update_query = """UPDATE tblZillowImport t SET t.house = %s, t.Car_Garage = %s, t.Living_Space_sq_ft = %s, t.Beds = 
    %s, t.Baths = %s, t.Zip = %s, t.Year = %s, t.List_Price = %s WHERE t.ID = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/zillow/new', methods=['GET'])
def form_insert_get():
    return render_template('new.html', title='New Property Form')


@app.route('/zillow/new', methods=['POST'])
def form_insert_post():
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('house'), request.form.get('Car_Garage'), request.form.get('Living_Space_sq_ft'),
                 request.form.get('Beds'), request.form.get('Baths'), request.form.get('Zip'),
                 request.form.get('Year'), request.form.get('List_Price'))
    sql_insert_query = """INSERT INTO tblZillowImport (house,Car_Garage,Living_Space_sq_ft,Beds,Baths,Zip,Year,List_Price) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/delete/<int:ID>', methods=['POST'])
def form_delete_post(ID):
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM tblZillowImport WHERE id = %s """
    cursor.execute(sql_delete_query, ID)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/api/v1/zillow', methods=['GET'])
def api_browse() -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblZillowImport')
    result = cursor.fetchall()
    json_result = json.dumps(result)
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/zillow/<int:ID>', methods=['GET'])
def api_retrieve(ID) -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblZillowImport WHERE id=%s', ID)
    result = cursor.fetchall()
    json_result = json.dumps(result)
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/zillow/', methods=['POST'])
def api_add() -> str:
    resp = Response(status=201, mimetype='application/json')
    return resp


@app.route('/api/v1/zillow/<int:ID>', methods=['PUT'])
def api_edit(ID) -> str:
    resp = Response(status=201, mimetype='application/json')
    return resp


@app.route('/api/zillow/<int:ID>', methods=['DELETE'])
def api_delete(ID) -> str:
    resp = Response(status=210, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
