from backend.models.category import Category
from scripts.seed_categories import DEFAULT_CATEGORIES, seed


def test_seed_creates_all_categories(db):
    seed(db)

    categories = db.query(Category).all()
    category_names = [c.name for c in categories]

    assert len(categories) == len(DEFAULT_CATEGORIES)
    for name in DEFAULT_CATEGORIES:
        assert name in category_names


def test_seed_marks_categories_as_system(db):
    seed(db)

    non_system = db.query(Category).filter_by(is_system=False).all()
    assert len(non_system) == 0


def test_seed_is_idempotent(db):
    seed(db)
    seed(db)

    categories = db.query(Category).all()
    assert len(categories) == len(DEFAULT_CATEGORIES)
