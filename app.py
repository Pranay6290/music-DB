from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret_key'  # For flashing messages
db = SQLAlchemy(app)

# Models
class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_song', methods=['GET', 'POST'])
def add_song():
    if request.method == 'POST':
        title = request.form['title']
        artist = request.form['artist']
        if title and artist:
            new_song = Song(title=title, artist=artist)
            db.session.add(new_song)
            db.session.commit()
            flash('Song added successfully!')
            return redirect(url_for('add_song'))
        else:
            flash('Both title and artist are required.')
    return render_template('add_song.html')

@app.route('/view_songs')
def view_songs():
    songs = Song.query.all()
    return render_template('view_songs.html', songs=songs)

@app.route('/create_playlist', methods=['GET', 'POST'])
def create_playlist():
    if request.method == 'POST':
        name = request.form.get('name')
        song_ids = request.form.get('song_ids', '')

        if not name:
            flash('Playlist name is required', 'error')
            return render_template('create_playlist.html')

        # Process song IDs
        song_ids_list = song_ids.split(',') if song_ids else []
        
        # Assuming 'songs' is a valid attribute in your Playlist model
        new_playlist = Playlist(name=name, songs=','.join(song_ids_list))
        db.session.add(new_playlist)
        db.session.commit()

        flash('Playlist created successfully!', 'success')
        return redirect(url_for('view_playlists'))
    
    return render_template('create_playlist.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)
name = request.form.get('name')

from your_app import db, Song  # Import your app's db instance and Song model

# Example songs to add
example_songs = [
    Song(id=1, title="Song of Freedom"),
    Song(id=2, title="Journey of Time"),
    Song(id=3, title="Echoes of Eternity"),
    Song(id=4, title="Melody of Light"),
    Song(id=5, title="Whispers of the Wind"),
]

# Adding and committing songs to the database
for song in example_songs:
    db.session.add(song)
db.session.commit()
song_ids_list = ['1', '2', '3']
new_playlist = Playlist(name="My Favorite Tunes", song_ids=','.join(song_ids_list))

# Adding and committing the new playlist
db.session.add(new_playlist)
db.session.commit()
