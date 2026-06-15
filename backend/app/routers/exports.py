from datetime import datetime
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import models,schemas
router=APIRouter(prefix='/api/exports',tags=['Exports'])
@router.get('/',response_model=List[schemas.ExportOut])
def list_exports(db:Session=Depends(get_db)): return db.query(models.ExportFile).order_by(models.ExportFile.exported_at.desc()).all()
@router.post('/generate/{project_id}')
def export(project_id:int,db:Session=Depends(get_db)):
    c=db.query(models.GeneratedRecord).filter(models.GeneratedRecord.project_id==project_id).count(); db.add(models.ExportFile(project_id=project_id,file_name=f'project_{project_id}_export.json',format='JSON',exported_by='QA Lead',exported_at=datetime.utcnow(),record_count=c)); db.commit(); return {'message':'Export generated','records':c}
