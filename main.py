
from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = "3781204262Bb"
app.config['MYSQL_DATABASE_DB'] = "Microlocations"

mysql = MySQL()
mysql.init_app(app)


@app.route("/")
def hello_world():
    return "hello_world"#primera ruta


@app.route("/locations")
def get_locations():
    cursor = mysql.get_db().cursor()#lo que nos une a la bd     

    cursor.execute("""
        SELECT * 
        FROM Locations 
    """)
    locations = cursor.fetchall()
    
    # cursor.fetchall() ir a leer datos
    # mysql.get_db().commit() \\ Para crear una nueva entrada de datos

    print (locations)
    return "locations"

if __name__=="__main__":
    app.run(port=3000)

#crud de localizaciones 
#crud de trips




##Running on http://127.0.0.1:3000