from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bracket', methods=['GET', 'POST'])
def bracket():
    if request.method == 'POST':
        name = request.form['name']
        pink_top3 = request.form.getlist('pink')
        orange_top3 = request.form.getlist('orange')
        purple_top3 = request.form.getlist('purple')
        top9 = pink_top3 + orange_top3 + purple_top3

        with open('brackets.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name] + pink_top3 + orange_top3 + purple_top3)

        return redirect('/submitted')

    queens = {
        'pink': ['Aja', 'Bosco', 'Queen X', 'Queen A', 'Queen B', 'Queen C'],
        'orange': ['Jorgeous', 'Queen Y', 'Queen Z', 'Queen D', 'Queen E', 'Queen F'],
        'purple': ['Ginger Minj', 'Mistress Isabelle Brooks', 'Queen W', 'Queen G', 'Queen H', 'Queen I']
    }
    return render_template('bracket_simple.html', queens=queens)

@app.route('/submitted')
def submitted():
    return render_template('submitted.html')

if __name__ == '__main__':
    app.run(debug=True)
