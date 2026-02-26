from flask import Flask,render_template

app = Flask(__name__)


@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)

@app.route("/get-data",methods=["GET"])
def get_data():
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="portfolio"
    )
    cursor=db.cursor()
    cursor.execute("SELECT * FROM projects")
    data=cursor.fetchall()
    return render_template("project.html",data=data)