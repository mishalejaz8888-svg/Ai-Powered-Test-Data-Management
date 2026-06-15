from pydantic import BaseModel
from datetime import datetime
from typing import Optional,List
class ProjectCreate(BaseModel):
    name:str; dataset_type:str; owner:str='QA Team'; environment:str='QA'; record_count:int=0; generation_status:str='Completed'; masking_status:str='Masked'; quality_score:float=90
class ProjectOut(ProjectCreate):
    id:int; created_at:datetime; last_generated_at:datetime
    class Config: from_attributes=True
class GenerateRequest(BaseModel):
    dataset_type:str='Customers'; record_count:int=10; environment:str='QA'; complexity:str='Realistic'; include_invalid_records:bool=False; include_edge_cases:bool=True; include_null_values:bool=False; include_duplicates:bool=False; owner:str='QA Team'
class RecordOut(BaseModel):
    id:int; project_id:int; dataset_type:str; record_key:str; raw_data:str; masked_data:str; validation_status:str; has_pii:bool; created_at:datetime
    class Config: from_attributes=True
class MaskingRuleOut(BaseModel):
    id:int; field_name:str; pii_type:str; masking_method:str; enabled:bool; example:str
    class Config: from_attributes=True
class QualityResultOut(BaseModel):
    id:int; project_id:int; rule_name:str; passed_count:int; failed_count:int; severity:str; suggested_fix:str; created_at:datetime
    class Config: from_attributes=True
class ExportOut(BaseModel):
    id:int; project_id:int; file_name:str; format:str; exported_by:str; exported_at:datetime; record_count:int
    class Config: from_attributes=True
class JobOut(BaseModel):
    id:int; job_key:str; project_id:int; dataset_type:str; records_requested:int; records_generated:int; status:str; started_at:datetime; completed_at:Optional[datetime]; error_message:str; generated_by:str
    class Config: from_attributes=True
class UsageOut(BaseModel):
    id:int; project_id:int; used_by:str; team:str; test_environment:str; purpose:str; last_used_at:datetime
    class Config: from_attributes=True
class AuditOut(BaseModel):
    id:int; user:str; action:str; entity_type:str; entity_id:str; timestamp:datetime; notes:str
    class Config: from_attributes=True
class AIQuestion(BaseModel): question:str
class AIAnswer(BaseModel):
    summary:str; dataset_generation_plan:str; risk_areas:List[str]; data_quality_findings:List[str]; recommended_actions:List[str]; example_generated_records:List[str]
