from datetime import date, datetime, timezone

from database import Engine, SessionLocal
from models.database.users.user import User
from models.database.city.city import City
from models.database.cinemas.cinema import Cinema
import utils.getId as getId


SEED_USERS = [
    {
        "first_name": "Aarav",
        "last_name": "Shah",
        "role": "USER",
        "phone": "9876543210",
        "email": "aarav@example.com",
        "dob": date(1995, 4, 12),
    },
    {
        "first_name": "Mira",
        "last_name": "Patel",
        "role": "USER",
        "phone": "8765432109",
        "email": "mira@example.com",
        "dob": date(1998, 9, 3),
    },
        {
        "first_name": "Ishaan",
        "last_name": "Mehta",
        "role": "USER",
        "phone": "7654321098",
        "email": "ishaan@example.com",
        "dob": date(1992, 1, 25),
    },
    {
        "first_name": "Anaya",
        "last_name": "Rao",
        "role": "USER",
        "phone": "6543210987",
        "email": "anaya@example.com",
        "dob": date(2000, 6, 8),
    },
    {
        "first_name": "Vivaan",
        "last_name": "Nair",
        "role": "USER",
        "phone": "9988776655",
        "email": "vivaan@example.com",
        "dob": date(1997, 11, 14),
    },
    {
        "first_name": "Diya",
        "last_name": "Kapoor",
        "role": "USER",
        "phone": "8877665544",
        "email": "diya@example.com",
        "dob": date(1999, 3, 19),
    },
    {
        "first_name": "Arjun",
        "last_name": "Desai",
        "role": "USER",
        "phone": "7766554433",
        "email": "arjun@example.com",
        "dob": date(1994, 7, 2),
    },
    {
        "first_name": "Sara",
        "last_name": "Iyer",
        "role": "USER",
        "phone": "6655443322",
        "email": "sara@example.com",
        "dob": date(2001, 12, 5),
    },
    {
        "first_name": "Kabir",
        "last_name": "Joshi",
        "role": "USER",
        "phone": "9988001122",
        "email": "kabir@example.com",
        "dob": date(1996, 5, 27),
    },
    {
        "first_name": "Tara",
        "last_name": "Menon",
        "role": "USER",
        "phone": "8877002211",
        "email": "tara@example.com",
        "dob": date(1993, 8, 16),
    },
    {
        "first_name": "Dev",
        "last_name": "Malhotra",
        "role": "ADMIN",
        "phone": "9123456780",
        "email": "dev.admin@example.com",
        "dob": date(1990, 2, 14),
    },
    {
        "first_name": "Riya",
        "last_name": "Sethi",
        "role": "SUPER_ADMIN",
        "phone": "9234567891",
        "email": "riya.superadmin@example.com",
        "dob": date(1988, 10, 21),
    },
]

SEED_CITIES = [
    {
        "id": 1,
        "name": "Bangalore",
        "added_by": "53b06452-ba13-4f50-bf0d-26d04b687be2"
    },
    {
        "id": 2,
        "name": "Mumbai",
        "added_by": "cd40f760-b87b-43e6-a652-6560b40a24e7"
    }

]

SEED_CINEMAS = [
    {
        "name": "Bangalore Central Cinema",
        "address": "Koramangala",
        "city": 1,
        "added_by": "53b06452-ba13-4f50-bf0d-26d04b687be2"
    },
    {
        "name": "Mumbai Ambience",
        "address": "Andheri",
        "city": 2,
        "added_by": "53b06452-ba13-4f50-bf0d-26d04b687be2"
    },
    {
        "name": "Forum Mall",
        "address": "HSR",
        "city": 1,
        "added_by": "cd40f760-b87b-43e6-a652-6560b40a24e7"
    },
    {
        "name": "Vega City",
        "address": "Juhu",
        "city": 2,
        "added_by": "cd40f760-b87b-43e6-a652-6560b40a24e7"
    }

]



def seed_users():
    User.metadata.create_all(bind=Engine)
    db = SessionLocal()

    try:
        now = datetime.now(timezone.utc)
        users = []

        for user_data in SEED_USERS:
            existing_user = (
                db.query(User)
                .filter(
                    (User.phone == user_data["phone"])
                    | (User.email == user_data["email"])
                )
                .first()
            )

            if existing_user is None:
                users.append(
                    User(
                        id=getId.getRandomId(),
                        **user_data,
                        created_at=now,
                        updated_at=now,
                    )
                )

        db.add_all(users)
        db.commit()
    except Exception:
        db.rollback()
        raise

    finally:
        db.close()

def seed_cities():
    City.metadata.create_all(bind=Engine)
    db = SessionLocal()

    try:
        now = datetime.now(timezone.utc)
        cities = []

        for city_data in SEED_CITIES:
            existing_city = (
                db.query(City)
                .filter(
                    (City.id == city_data["id"])
                )
                .first()
            )

            if existing_city is None:
                cities.append(
                    City(
                        **city_data,
                        created_at=now,
                        updated_at=now,
                    )
                )

        db.add_all(cities)
        db.commit()
    except Exception:
        db.rollback()
        raise

    finally:
        db.close()

def seed_cinemas():
    Cinema.metadata.create_all(bind=Engine)
    db = SessionLocal()

    try:
        now = datetime.now(timezone.utc)
        cinemas = []

        for cinema_data in SEED_CINEMAS:
            existing_cinema = (
                db.query(Cinema)
                .filter(
                    (Cinema.name == cinema_data["name"]),
                    (Cinema.city == cinema_data["city"])
                )
                .first()
            )

            if existing_cinema is None:
                cinemas.append(
                    Cinema(
                        id = getId.getRandomId(),
                        **cinema_data,
                        created_at=now,
                        updated_at=now,
                    )
                )

        db.add_all(cinemas)
        db.commit()
    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_users()
    seed_cities()
    seed_cinemas()