from sqlalchemy.orm import Session
import master.models as models


def create_user(db: Session, user_data: dict):
    user = models.User(**user_data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def update_user(db: Session, user_id: int, user_data: dict):
    db.query(models.User).filter(models.User.id == user_id).update(user_data)
    db.commit()
    return get_user(db, user_id)


def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if user:
        db.delete(user)
        db.commit()
        return user
    return None

# Similar functions can be defined for other models (e.g., Book, Club, Review)
