from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException,status


def create(request: schemas.Blog,db: Session):
    new_blog = models.Blog(title=request.title, body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog