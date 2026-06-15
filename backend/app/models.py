from sqlalchemy import Column,Integer,String,Float,Text,DateTime,Boolean,ForeignKey
from datetime import datetime
from .database import Base
class DatasetProject(Base):
    __tablename__='dataset_projects'; id=Column(Integer,primary_key=True,index=True); name=Column(String(180)); dataset_type=Column(String(80)); owner=Column(String(120),default='QA Team'); environment=Column(String(80),default='QA'); record_count=Column(Integer,default=0); generation_status=Column(String(60),default='Completed'); masking_status=Column(String(60),default='Masked'); quality_score=Column(Float,default=90); created_at=Column(DateTime,default=datetime.utcnow); last_generated_at=Column(DateTime,default=datetime.utcnow)
class GeneratedRecord(Base):
    __tablename__='generated_records'; id=Column(Integer,primary_key=True,index=True); project_id=Column(Integer,ForeignKey('dataset_projects.id')); dataset_type=Column(String(80)); record_key=Column(String(120)); raw_data=Column(Text); masked_data=Column(Text); validation_status=Column(String(60),default='Passed'); has_pii=Column(Boolean,default=True); created_at=Column(DateTime,default=datetime.utcnow)
class MaskingRule(Base):
    __tablename__='masking_rules'; id=Column(Integer,primary_key=True,index=True); field_name=Column(String(120)); pii_type=Column(String(80)); masking_method=Column(String(80)); enabled=Column(Boolean,default=True); example=Column(String(200),default='')
class DataQualityResult(Base):
    __tablename__='data_quality_results'; id=Column(Integer,primary_key=True,index=True); project_id=Column(Integer,ForeignKey('dataset_projects.id')); rule_name=Column(String(180)); passed_count=Column(Integer,default=0); failed_count=Column(Integer,default=0); severity=Column(String(60),default='Medium'); suggested_fix=Column(Text,default=''); created_at=Column(DateTime,default=datetime.utcnow)
class ExportFile(Base):
    __tablename__='export_files'; id=Column(Integer,primary_key=True,index=True); project_id=Column(Integer,ForeignKey('dataset_projects.id')); file_name=Column(String(180)); format=Column(String(60)); exported_by=Column(String(120)); exported_at=Column(DateTime,default=datetime.utcnow); record_count=Column(Integer,default=0)
class GenerationJob(Base):
    __tablename__='generation_jobs'; id=Column(Integer,primary_key=True,index=True); job_key=Column(String(120)); project_id=Column(Integer,ForeignKey('dataset_projects.id')); dataset_type=Column(String(80)); records_requested=Column(Integer); records_generated=Column(Integer); status=Column(String(60)); started_at=Column(DateTime,default=datetime.utcnow); completed_at=Column(DateTime,nullable=True); error_message=Column(Text,default=''); generated_by=Column(String(120),default='QA Engineer')
class DatasetUsage(Base):
    __tablename__='dataset_usage'; id=Column(Integer,primary_key=True,index=True); project_id=Column(Integer,ForeignKey('dataset_projects.id')); used_by=Column(String(120)); team=Column(String(120)); test_environment=Column(String(80)); purpose=Column(String(180)); last_used_at=Column(DateTime,default=datetime.utcnow)
class AuditLog(Base):
    __tablename__='audit_logs'; id=Column(Integer,primary_key=True,index=True); user=Column(String(120),default='system'); action=Column(String(180)); entity_type=Column(String(80)); entity_id=Column(String(80)); timestamp=Column(DateTime,default=datetime.utcnow); notes=Column(Text,default='')
