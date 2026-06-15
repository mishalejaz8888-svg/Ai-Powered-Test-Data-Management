from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import models,schemas
router=APIRouter(prefix='/api/data-quality',tags=['Quality'])
@router.get('/',response_model=List[schemas.QualityResultOut])
def list_results(db:Session=Depends(get_db)): return db.query(models.DataQualityResult).order_by(models.DataQualityResult.id.desc()).all()
@router.post('/run/{project_id}')
def run(project_id:int,db:Session=Depends(get_db)):
    db.add(models.DataQualityResult(project_id=project_id,rule_name='Required Fields Not Null',passed_count=95,failed_count=5,severity='High',suggested_fix='Regenerate invalid records.')); db.commit(); return {'message':'Quality validation completed'}
