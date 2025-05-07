from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")

# --- DATABASE SETUP ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Song {self.title}>"

def init_db():
    with app.app_context():
        db.create_all()
        if Song.query.count() == 0:
            songs = [
                Song(title="Shape of You", artist="Ed Sheeran", genre="Pop", year=2017),
                Song(title="Blinding Lights", artist="The Weeknd", genre="Pop", year=2019),
                Song(title="Smells Like Teen Spirit", artist="Nirvana", genre="Rock", year=1991),
                Song(title="Bad Guy", artist="Billie Eilish", genre="Pop", year=2019),
            ]
            db.session.bulk_save_objects(songs)
            db.session.commit()

# --- ROUTES ---

@app.route('/')
def home():
    return render_template('home.html', app_name="My Flask App")

@app.route('/songs')
def song_list():
    songs = Song.query.all()
    return render_template('songs.html', songs=songs)

@app.route('/song/<int:song_id>')
def song_detail(song_id):
    song = Song.query.get_or_404(song_id)
    return render_template('song_detail.html', song=song)

@app.route('/fortune', methods=['GET', 'POST'])
def fortune():
    if request.method == 'POST':
        user_name = request.form.get('user', '').strip()
        color = request.form.get('color', '').lower().strip()
        number = request.form.get('number', '').strip()
        fortunes = {
            'red':    {'1': "You will have a great day ahead!",
                       '2': "Beware of unexpected changes!",
                       '3': "Success is coming your way.",
                       '4': "You will meet someone important soon."},
            'yellow': {'1': "Good luck is on your side.",
                       '2': "Prepare for new challenges.",
                       '3': "A new adventure awaits you.",
                       '4': "Keep an open mind; opportunities are near."},
            'blue':   {'1': "Focus on your health and well-being.",
                       '2': "Your creativity will shine today.",
                       '3': "Financial gains are in your future.",
                       '4': "Don't be afraid to take risks."},
            'green':  {'1': "A journey will bring you new insights.",
                       '2': "Stay positive and trust your instincts.",
                       '3': "Peace and balance are coming into your life.",
                       '4': "You'll achieve your goals sooner than expected."},
        }
        fortune_message = fortunes.get(color, {}).get(number, "Your future is unclear, try again!")
        return render_template('fortune.html',
                               user_name=user_name,
                               color=color,
                               number=number,
                               fortune=fortune_message)
    return render_template('fortune_form.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)