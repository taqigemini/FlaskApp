from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

items = []

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        item = request.form['item']
        items.append(item)
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/update/<int:item_id>', methods=['GET', 'POST'])
def update(item_id):
    if request.method == 'POST':
        items[item_id] = request.form['item']
        return redirect(url_for('index'))
    return render_template('update.html', item=items[item_id], item_id=item_id)

@app.route('/delete/<int:item_id>', methods=['GET', 'POST'])
def delete(item_id):
    if request.method == 'POST':
        items.pop(item_id)
        return redirect(url_for('index'))
    return render_template('delete.html', item=items[item_id], item_id=item_id)

if __name__ == '__main__':
    app.run(debug=True)
