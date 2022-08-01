from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    text = db.Column(db.Text, nullable=False)


@app.route('/')
@app.route('/home')
def index():
    # items = Item.querry.order_by(Item.price).all()
    return render_template('index.html')


# @app.route('/order', methods=['POST', 'GET'])
# def order():
#     if request.method == "POST":
#         title = request.form['title']
#         price = request.form['price']
#         item = Item(title=title, price=price)
#         try:
#             db.session.add(item)
#             db.session.commit()
#         except:
#             return "Произошла ошибка. Попробуйте снова."
#     else:
#         return render_template('order.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)