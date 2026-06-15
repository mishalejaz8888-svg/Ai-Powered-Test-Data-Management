from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import models,schemas
router=APIRouter(prefix='/api/records',tags=['Records'])
@router.get('/',response_model=List[schemas.RecordOut])
def list_records(db:Session=Depends(get_db)): return db.query(models.GeneratedRecord).order_by(models.GeneratedRecord.id.desc()).limit(300).all()
