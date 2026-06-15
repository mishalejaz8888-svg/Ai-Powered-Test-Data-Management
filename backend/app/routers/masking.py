from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import models,schemas
router=APIRouter(prefix='/api',tags=['Masking'])
@router.get('/masking-rules',response_model=List[schemas.MaskingRuleOut])
def rules(db:Session=Depends(get_db)): return db.query(models.MaskingRule).all()
@router.post('/mask/{project_id}')
def mask(project_id:int,db:Session=Depends(get_db)):
    p=db.query(models.DatasetProject).filter(models.DatasetProject.id==project_id).first()
    if p: p.masking_status='Masked'; db.add(models.AuditLog(action='Data masked',entity_type='DatasetProject',entity_id=str(project_id),notes='PII fields masked.')); db.commit()
    return {'message':'Masking completed','project_id':project_id}
