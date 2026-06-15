from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import models,schemas
router=APIRouter(prefix='/api/projects',tags=['Projects'])
@router.get('/',response_model=List[schemas.ProjectOut])
def list_projects(db:Session=Depends(get_db)): return db.query(models.DatasetProject).order_by(models.DatasetProject.id.desc()).all()
@router.post('/',response_model=schemas.ProjectOut)
def create_project(payload:schemas.ProjectCreate,db:Session=Depends(get_db)):
    item=models.DatasetProject(**payload.model_dump()); db.add(item); db.commit(); db.refresh(item); return item
