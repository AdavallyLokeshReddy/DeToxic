from sqlalchemy.orm import Session
from ..models import user, submission, prediction
from ..auth.security import get_password_hash

# CRUD functions (stubs)

def create_submission(db: Session, comment_text: str, user_id: int | None = None):
    db_sub = submission.Submission(comment_text=comment_text, user_id=user_id)
    db.add(db_sub)
    db.commit()
    db.refresh(db_sub)
    return db_sub


def get_submission(db: Session, submission_id: int):
    return db.query(submission.Submission).filter(submission.Submission.id == submission_id).first()


def list_submissions(db: Session, limit: int = 100):
    return db.query(submission.Submission).limit(limit).all()

# User CRUD

def get_user_by_username(db: Session, username: str):
    return db.query(user.User).filter(user.User.username == username).first()


def create_user(db: Session, username: str, email: str, password: str, full_name: str | None = None):
    hashed = get_password_hash(password)
    db_user = user.User(username=username, email=email, password_hash=hashed, full_name=full_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
