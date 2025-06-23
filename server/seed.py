from server.app import create_app, db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.models.user import User

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Users
    user1 = User(username="admin")
    user1.set_password("admin123")

    user2 = User(username="host")
    user2.set_password("hostpass")

    # Guests
    guest1 = Guest(name="Trevor Noah", occupation="Comedian")
    guest2 = Guest(name="Malala Yousafzai", occupation="Activist")
    guest3 = Guest(name="Simu Liu", occupation="Actor")

    # Episodes
    episode1 = Episode(date="2023-06-21", number=101)
    episode2 = Episode(date="2023-06-22", number=102)
    episode3 = Episode(date="2023-06-23", number=103)

    # Appearances
    appearance1 = Appearance(rating=5, guest=guest1, episode=episode1)
    appearance2 = Appearance(rating=4, guest=guest2, episode=episode1)
    appearance3 = Appearance(rating=3, guest=guest1, episode=episode2)
    appearance4 = Appearance(rating=2, guest=guest3, episode=episode3)

    db.session.add_all([
        user1, user2,
        guest1, guest2, guest3,
        episode1, episode2, episode3,
        appearance1, appearance2, appearance3, appearance4
    ])
    db.session.commit()

    print("Seeded the database with users, guests, episodes, and appearances.")
