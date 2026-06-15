from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from collections import Counter
from ..database import get_db
from .. import models
router=APIRouter(prefix='/api/analytics',tags=['Analytics'])
@router.get('/summary')
def summary(db:Session=Depends(get_db)):
    p=db.query(models.DatasetProject).all(); r=db.query(models.GeneratedRecord).all(); q=db.query(models.DataQualityResult).all(); u=db.query(models.DatasetUsage).all(); jobs=db.query(models.GenerationJob).order_by(models.GenerationJob.started_at.desc()).limit(5).all()
    score=max(0,round(100-(sum(x.failed_count for x in q)/(sum(x.failed_count+x.passed_count for x in q) or 1)*100),1))
    return {'total_datasets':len(p),'generated_records':len(r),'masked_records':len([x for x in r if x.masked_data]),'pii_fields_protected':len(r)*4,'data_quality_score':score,'failed_validation_rules':len([x for x in q if x.failed_count>0]),'dataset_usage_count':len(u),'recent_generation_jobs':[{'job_key':j.job_key,'status':j.status,'records':j.records_generated} for j in jobs],'dataset_type_breakdown':[{'name':k,'value':v} for k,v in Counter(x.dataset_type for x in p).items()],'masking_coverage_chart':[{'name':k,'value':v} for k,v in Counter(x.masking_status for x in p).items()],'data_quality_trend':[{'name':x.name[:14],'score':x.quality_score} for x in p]}
