from flask import Flask, render_template, request, redirect
from model import db, InventoryModel
import sqlite3
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        quanity = request.form['quantity']
        type = request.form['type']
        new_inventory = InventoryModel(name=name,quantity=quanity,type=type)
        try:
            db.session.add(new_inventory)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        inventory = InventoryModel.query.order_by(InventoryModel.id).all()
        return render_template('index.html', inventory=inventory)


@app.route('/delete/<int:id>')
def delete(id):
    items_to_delete = InventoryModel.query.get_or_404(id)

    try:
        db.session.delete(items_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that item'

@app.route('/update', methods=['GET', 'POST'])
def update():
    item = InventoryModel.query.get_or_404(request.form.get('id'))

    if request.method == 'POST':
        item.name = request.form['name']
        item.quanity = request.form['quantity']
        item.type = request.form['type']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an erroe while updating your item'

    else:
        return render_template('/')

@app.route('/export')
def export():
    conn = sqlite3.connect('test3.db', isolation_level=None,
                        detect_types=sqlite3.PARSE_COLNAMES)
    db_df = pd.read_sql_query("SELECT * FROM mytable", conn)
    db_df.to_csv('database.csv', index=False)
    return render_template('export.html')
    

if __name__ == "__main__":
    app.run(debug=True)
