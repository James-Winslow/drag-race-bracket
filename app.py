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
        'pink': ['Jorgeous', 'Kerri Colby', 'Lydia B. Kollins', 'Mistress Isabelle Brooks', 'Nicole Paige Brooks', 'Tina Burner'],
        'orange': ['Aja', 'Bosco', 'DeJa Skye', 'Irene the Alien', 'Olivia Lux', 'Phoenix'],
        'purple': ['Acid Betty', 'Alyssa Hunter', 'Cynthia Lee Fontaine', 'Daya Betty', 'Denali', 'Ginger Minj']
    }
    return render_template('bracket_simple.html', queens=queens)

@app.route('/submitted')
def submitted():
    return render_template('submitted.html')

if __name__ == '__main__':
    app.run(debug=True)
