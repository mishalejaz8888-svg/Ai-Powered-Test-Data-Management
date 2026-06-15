from datetime import datetime,timedelta
from .database import Base,engine,SessionLocal
from .models import *
from .services.generator import generate_records
Base.metadata.create_all(bind=engine); db=SessionLocal(); now=datetime.utcnow()
if db.query(DatasetProject).count()==0:
    types=['Customers','Orders','Transactions','Healthcare','Insurance Claims','Banking','E-commerce','SaaS Users']; envs=['QA','UAT','Staging','Performance']; projects=[]
    for i,t in enumerate(types,1):
        p=DatasetProject(name=f'{t} Test Dataset',dataset_type=t,owner=['QA Team','Automation Team','Data QA','Healthcare QA'][i%4],environment=envs[i%4],record_count=13,generation_status='Completed',masking_status='Masked' if i%3 else 'Partial',quality_score=90-(i%5)*3,created_at=now-timedelta(days=i),last_generated_at=now-timedelta(hours=i*3)); db.add(p); db.commit(); db.refresh(p); projects.append(p)
        for r in generate_records(t,13): db.add(GeneratedRecord(project_id=p.id,**r))
    for field,typ,method,ex in [('email','Email','Partial Masking','j***@example.com'),('phone','Phone','Partial Masking','555-***-****'),('full_name','Name','Initials','J. S.'),('date_of_birth','DOB','Date Masking','1989-XX-XX'),('address','Address','Synthetic Replacement','*** Main St'),('account_id','Account','Last Four','****1234'),('card_number','Card','Last Four','****-1234'),('patient_id','Healthcare Identifier','Tokenization','TOKEN-001')]: db.add(MaskingRule(field_name=field,pii_type=typ,masking_method=method,example=ex))
    rules=[('Required Fields Not Null','High'),('Valid Email Format','High'),('Positive Transaction Amount','High'),('Order Total Validation','Medium'),('No Future Dates','Medium'),('Duplicate ID Detection','High'),('Healthcare Claim Amount Positive','High'),('Patient DOB Realistic','High'),('Masking Coverage Complete','Critical'),('Valid Status Values','Medium')]
    for i in range(15): db.add(DataQualityResult(project_id=projects[i%len(projects)].id,rule_name=rules[i%len(rules)][0],passed_count=90+i,failed_count=i%6,severity=rules[i%len(rules)][1],suggested_fix='Review failed records and regenerate invalid fields.'))
    formats=['CSV','JSON','SQL','Postman','API Mock']
    for i,p in enumerate(projects): db.add(ExportFile(project_id=p.id,file_name=f'{p.dataset_type.lower()}_export.{formats[i%5].lower()}',format=formats[i%5],exported_by='QA Lead',exported_at=now-timedelta(hours=i),record_count=p.record_count))
    for i in range(10): db.add(GenerationJob(job_key=f'JOB-{1000+i}',project_id=projects[i%len(projects)].id,dataset_type=projects[i%len(projects)].dataset_type,records_requested=13,records_generated=13 if i!=3 else 11,status='Completed' if i!=3 else 'Failed',started_at=now-timedelta(hours=i+1),completed_at=now-timedelta(hours=i),error_message='' if i!=3 else 'Duplicate ID validation failed.',generated_by='QA Engineer'))
    purposes=['Regression Test','UAT Session','Performance Test','API Testing','Manual QA']
    for i in range(10): db.add(DatasetUsage(project_id=projects[i%len(projects)].id,used_by=f'user{i+1}@company.com',team=['QA','Automation','Data QA','Release QA'][i%4],test_environment=envs[i%4],purpose=purposes[i%5],last_used_at=now-timedelta(days=i)))
    actions=['Dataset generated','Data masked','Export created','Quality validation failed','Dataset refreshed','Dataset usage logged']
    for i in range(20): db.add(AuditLog(user=f'user{i%5+1}@company.com',action=actions[i%len(actions)],entity_type=['DatasetProject','GeneratedRecord','ExportFile','DataQualityResult'][i%4],entity_id=str(i+1),timestamp=now-timedelta(hours=i),notes='System audit event captured.'))
    db.commit()
db.close(); print('Database seeded successfully.')
