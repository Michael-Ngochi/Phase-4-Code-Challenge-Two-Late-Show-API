from server.app import create_app, db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    guest = Guest(name="Trevor Noah", occupation="Comedian")
    episode = Episode(date="2023-06-21", number=101)
    appearance = Appearance(rating=5, guest=guest, episode=episode)

    db.session.add_all([guest, episode, appearance])
    db.session.commit()
