from flask import Flask,request,jsonify
import sqlite3
from flask_cors import CORS

def init_sqlite_db():

    con = sqlite3.connect('users.db')
    print("Created Database successfully")

    con.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, surname TEXT, email TEXT, pin TEXT)')
    print("Users Table created successfully")

    con.execute('CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY AUTOINCREMENT, productname TEXT, pro_description TEXT, price TEXT, brand TEXT, picture TEXT)')
    print("Products table created successfully")

    mycursor = con.cursor()
    mycursor.execute("SELECT * FROM users")
    print(mycursor.fetchall())

    con.close()

init_sqlite_db()

app = Flask (__name__)
CORS(app)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/')
@app.route('/add-new-user/', methods=['POST'])
def add_new_user():
    if request.method == "POST":
        msg= None
        try:
            #post_data = request.get_json()
            name = request.form['name']
            surname = request.form['surname']
            email = request.form['email']
            password = request.form['pin']

            with sqlite3.connect('users.db') as conn:
                cur = conn.cursor()
                conn.row_factory = dict_factory
                cur.execute("INSERT INTO users(username, surname, email, pin) VALUES(?,?,?,?)", (name, surname, email, password))
                conn.commit()
                msg = "Record added successfully"

        except Exception as e:
            msg = 'error'+ str(e)

        finally:
            return {'msg': msg}

@app.route('/list-users/', methods=['GET'])
def list():
    try:
        with sqlite3.connect('users.db') as conn:
                conn.row_factory = dict_factory
                cur = conn.cursor()
                cur.execute("SELECT * FROM users")
                rows = cur.fetchall()
    except Exception as e:
        print("Something went wrong" + str(e))
    return jsonify(rows)

@app.route('/add-products', methods=['POST'])
def add_prod():

   with sqlite3.connect('users.db') as conn:
        cur = conn.cursor()
        conn.row_factory = dict_factory
        cur.execute("INSERT INTO products(productname, pro_description, price, brand, picture) VALUES (?, ?, ?, ?, ?)",('Oval Silver Ring', 'Category 1', 'R 1573', 'rings', 'https://i.postimg.cc/CLv4bG0V/Silver-Fancy-Oval-Claw-Cluster-Cubic-Zirconia-Ring.jpg'))
        cur.execute("INSERT INTO products(productname, pro_description, price, brand, picture) VALUES (?, ?, ?, ?, ?)", ('9ct Gold & Silver Ring', 'Category 1', 'R 1500', 'rings', 'https://i.postimg.cc/T3pvcPvK/9ct-Gold-Silver-Diamond-Tripset-Wedding-Ring.jpg'))
        cur.execute("INSERT INTO products(productname, pro_description, price, brand, picture) VALUES (?, ?, ?, ?, ?)", ('Mens Wedding Band ', 'Category 1', 'R 1800', 'rings', 'https://i.postimg.cc/cLL0bNPn/broad.jpg'))
        cur.execute("INSERT INTO products(productname, pro_description, price, brand, picture) VALUES (?, ?, ?, ?, ?)", ('Morganite CZ Cluster Ring', 'Category 1', 'R 4000', 'rings', 'rsz-silver-round-cz-single-solitaire-morganite-cz-cluster-ring-removebg-preview.jpg'))
        cur.execute("INSERT INTO products(productname, pro_description, price, brand, picture) VALUES (?, ?, ?, ?, ?)", ('Golden Swirl Earings', 'Category 2', 'R 1000', 'Earings', 'https://i.postimg.cc/vB0ZBZRb/12.jpg'))
        cur.execute("INSERT INTO products(productname, pro_description, price, brand, picture) VALUES (?, ?, ?, ?, ?)", ('Hoop Earings', 'Category 2', 'R 800', 'Earings', 'https://i.postimg.cc/LXtsM3DY/Silver-Oval-Twisted-Hoop-Earrings.jpg'))
        cur.execute("INSERT INTO products(productname, pro_description, price, brand, picture) VALUES (?, ?, ?, ?, ?)", ('Diamante Earings ', 'Category 2', 'R 900', 'Earings', 'https://i.postimg.cc/h4N2Y8wb/9.jpg'))
        cur.execute("INSERT INTO products(productname, pro_description, price, brand, picture) VALUES (?, ?, ?, ?, ?)", ('Gold Rose Earings', 'Category 2', 'R 600', 'Earings', '9ct-Rose-Gold-Fancy-Round-Circle-Black-Diamond-Earrings.jpg'))
        cur.execute("INSERT INTO products(productname, pro_description, price, brand, picture) VALUES (?, ?, ?, ?, ?)", ('Mens Pendant  Classic', 'Category 3 ', 'R 950', 'Necklaces', 'TSAR-Stainless-Steel-Gents-Fleur-De-Lis-Cross-Pendant.jpg'))
        cur.execute("INSERT INTO products(productname, pro_description, price, brand, picture) VALUES (?, ?, ?, ?, ?)", ('Zion Collection Set', 'Category 3', 'R 2500', 'Necklaces', 'https://i.postimg.cc/MKnZtwBr/8.jpg'))
        cur.execute("INSERT INTO products(productname, pro_description, price, brand, picture) VALUES (?, ?, ?, ?, ?)", ('Tanzanite and Diamond Set', 'Category 3', 'R 3000', 'Necklaces', 'https://i.postimg.cc/s2ynfV9n/Silver-Tanzanite-and-Diamond-Square-Pendant-and-Earring-Set.jpg'))
        cur.execute("INSERT INTO products(productname, pro_description, price, brand, picture) VALUES (?, ?, ?, ?, ?)", ('Silver Charm Bracelet', 'Category 4', 'R 7000', 'Bracelet', 'https://i.postimg.cc/yd1rjVDJ/Silver-Charm-Bracelet-with-Free-Cubic-Zirconia-Charm.jpg'))
        cur.execute("INSERT INTO products(productname, pro_description, price, brand, picture) VALUES (?, ?, ?, ?, ?)", ('Mens Bracelet', 'Category 4', 'R 250', 'Necklaces', 'https://i.postimg.cc/NMGBXvYD/rsz-mensbra-removebg-preview.jpg'))
        cur.execute("INSERT INTO products(productname, pro_description, price, brand, picture) VALUES (?, ?, ?, ?, ?)", ('9 Crt Belcher Bracelet', 'Category 4 ', 'R 5000', 'Bracelet', 'https://i.postimg.cc/d3t3JTLq/rsz-9ct-gold-19cm-belcher-bracelet-with-senoretti-clasp-removebg-preview.jpg'))
        cur.execute("INSERT INTO products(productname, pro_description, price, brand, picture) VALUES (?, ?, ?, ?, ?)", ('Silver Jane Bangle', 'Category 4', 'R 8000', 'Bracelet', 'https://i.postimg.cc/cH3Mf2mK/rsz-balnd-removebg-preview.jpg'))

add_prod()


@app.route('/list-prod/', methods=['GET'])
def list_prod():
    data = []
    try:
        with sqlite3.connect('users.db') as conn:
                conn.row_factory = dict_factory
                cur = conn.cursor()
                cur.execute("SELECT * FROM products")
                data = cur.fetchall()
    except Exception as e:
        conn.rollback()
        print("Something went wrong" + str(e))
    finally:
        conn.close()
        return jsonify(data)

@app.route('/login-user/' , methods=["GET"])
def login_user():
    if request.method == 'GET':
        response = []
        msg= None
        try:
            #get_data = request.get_json()
            username = request.form['email']
            password = request.form['pin']

            with sqlite3.connect('users.db') as conn:
                conn.row_factory = dict_factory
                cur = conn.cursor()
                sql_stmnt = ('SELECT * FROM users')
                cur.execute(sql_stmnt)
                users = cur.fetchall()
                conn.commit()
                msg = username + "Successfully Logged In " 

        except Exception as e:
            conn.rollback()
            msg = "error " + str(e)

        finally:
            return jsonify(msg = msg)


if __name__ == '__main__':
    app.run()
            