from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import models,schemas
router=APIRouter(prefix='/api/jobs',tags=['Jobs'])
@router.get('/',response_model=List[schemas.JobOut])
def list_jobs(db:Session=Depends(get_db)): return db.query(models.GenerationJob).order_by(models.GenerationJob.started_at.desc()).all()
