from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/fortune', methods=['GET', 'POST'])
def fortune():
    if request.method == 'POST':
        user_name = request.form['user']
        color = request.form['color']
        number = request.form['number']
    
        fortunes = {
            'red': {
                '1': "You will have a great day ahead!",
                '2': "Beware of unexpected changes!",
                '3': "Success is coming your way.",
                '4': "You will meet someone important soon."
            },
            'yellow': {
                '1': "Good luck is on your side.",
                '2': "Prepare for new challenges.",
                '3': "A new adventure awaits you.",
                '4': "Keep an open mind; opportunities are near."
            },
            'blue': {
                '1': "Focus on your health and well-being.",
                '2': "Your creativity will shine today.",
                '3': "Financial gains are in your future.",
                '4': "Don't be afraid to take risks."
            },
            'green': {
                '1': "A journey will bring you new insights.",
                '2': "Stay positive and trust your instincts.",
                '3': "Peace and balance are coming into your life.",
                '4': "You'll achieve your goals sooner than expected."
            }
        }

        fortune_message = fortunes[color].get(number, "Your future is unclear, try again!")

        return render_template('fortune.html', user_name=user_name, color=color, number=number, fortune=fortune_message)

    return render_template('fortune_form.html')

if __name__ == '__main__':
    app.run(debug=True)