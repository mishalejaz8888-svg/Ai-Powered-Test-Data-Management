from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import models,schemas
router=APIRouter(prefix='/api/usage',tags=['Usage'])
@router.get('/',response_model=List[schemas.UsageOut])
def list_usage(db:Session=Depends(get_db)): return db.query(models.DatasetUsage).order_by(models.DatasetUsage.last_used_at.desc()).all()
