from flask import Flask, render_template, request, redirect, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "inventory_secret_key"


# MySQL Configuration
app.config.from_object("config.Config")


mysql = MySQL(app)



@app.route("/")
def home():
    return render_template("index.html")



@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        cursor = mysql.connection.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=%s AND password=%s",
            (username, password)
        )

        user = cursor.fetchone()

        cursor.close()

        if user:
            session["user"] = username
            return redirect("/dashboard")
        else:
            return "Invalid Username or Password"

    return render_template("login.html")



@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/login")

    cursor = mysql.connection.cursor()

    # Total Products
    cursor.execute("SELECT COUNT(*) FROM products")
    total_products = cursor.fetchone()[0]

    # Total Quantity
    cursor.execute("SELECT SUM(quantity) FROM products")
    total_quantity = cursor.fetchone()[0] or 0

    # Inventory Value
    cursor.execute("SELECT SUM(price * quantity) FROM products")
    inventory_value = cursor.fetchone()[0] or 0

    cursor.close()

    return render_template(
        "dashboard.html",
        user=session["user"],
        total_products=total_products,
        total_quantity=total_quantity,
        inventory_value=inventory_value
    )



@app.route("/products")
def products():

    if "user" not in session:
        return redirect("/login")

    cursor = mysql.connection.cursor()

    cursor.execute("SELECT * FROM products")

    product_list = cursor.fetchall()

    cursor.close()

    return render_template(
        "products.html",
        products=product_list
    )


@app.route("/add_product", methods=["GET", "POST"])
def add_product():

    # Check if user is logged in
    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":

        name = request.form["name"]
        price = request.form["price"]
        quantity = request.form["quantity"]

        cursor = mysql.connection.cursor()

        cursor.execute(
            """
            INSERT INTO products (name, price, quantity)
            VALUES (%s, %s, %s)
            """,
            (name, price, quantity)
        )

        mysql.connection.commit()
        cursor.close()

        return redirect("/products")

    return render_template("add_product.html")

@app.route("/edit_product/<int:id>", methods=["GET", "POST"])
def edit_product(id):

    if "user" not in session:
     return redirect("/login")

    cursor = mysql.connection.cursor()

    if request.method == "POST":

        name = request.form["name"]
        price = request.form["price"]
        quantity = request.form["quantity"]

        cursor.execute("""
            UPDATE products
            SET name=%s, price=%s, quantity=%s
            WHERE id=%s
        """, (name, price, quantity, id))

        mysql.connection.commit()

        cursor.close()

        return redirect("/products")

    cursor.execute("SELECT * FROM products WHERE id=%s", (id,))

    product = cursor.fetchone()

    cursor.close()

    return render_template("edit_product.html", product=product)

@app.route("/delete_product/<int:id>")
def delete_product(id):
    if "user" not in session:
     return redirect("/login")

    cursor = mysql.connection.cursor()

    cursor.execute("DELETE FROM products WHERE id=%s", (id,))

    mysql.connection.commit()

    cursor.close()

    return redirect("/products")

@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect("/login")

@app.route("/test")
def test():
    return "Flask is running the correct app!"


if __name__ == "__main__":
    app.run(debug=True)


