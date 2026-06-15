from datetime import datetime
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models,schemas
from ..services.generator import generate_records
router=APIRouter(prefix='/api/generate',tags=['Generator'])
@router.post('/')
def generate(payload:schemas.GenerateRequest,db:Session=Depends(get_db)):
    p=models.DatasetProject(name=f'{payload.dataset_type} Dataset - {payload.environment}',dataset_type=payload.dataset_type,owner=payload.owner,environment=payload.environment,record_count=payload.record_count,generation_status='Completed',masking_status='Masked',quality_score=92); db.add(p); db.commit(); db.refresh(p)
    for rec in generate_records(payload.dataset_type,payload.record_count): db.add(models.GeneratedRecord(project_id=p.id,**rec))
    db.add(models.GenerationJob(job_key=f'JOB-{p.id:04d}',project_id=p.id,dataset_type=payload.dataset_type,records_requested=payload.record_count,records_generated=payload.record_count,status='Completed',completed_at=datetime.utcnow(),generated_by=payload.owner)); db.add(models.AuditLog(user=payload.owner,action='Dataset generated',entity_type='DatasetProject',entity_id=str(p.id),notes=f'Generated {payload.record_count} records.')); db.commit(); return {'message':'Dataset generated','project_id':p.id,'records':payload.record_count}
