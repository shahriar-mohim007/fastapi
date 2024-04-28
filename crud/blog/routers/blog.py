from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from .. import models, schemas, database
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)