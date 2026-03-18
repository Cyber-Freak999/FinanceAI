from backend.core.database import SessionLocal
from backend.models.category import Category

DEFAULT_CATEGORIES = [
    "Food & Dining",
    "Transport",
    "Housing & Utilities",
    "Entertainment",
    "Healthcare",
    "Shopping",
    "Savings & Investment",
    "Income",
    "Other",
]


def seed():
    db = SessionLocal()
    for name in DEFAULT_CATEGORIES:
        exists = db.query(Category).filter_by(name=name).first()
        if not exists:
            db.add(Category(name=name, is_system=True))
    db.commit()
    db.close()
    print("Categories seeded.")


if __name__ == "__main__":
    seed()
