from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import models,schemas
router=APIRouter(prefix='/api/audit-logs',tags=['Audit'])
@router.get('/',response_model=List[schemas.AuditOut])
def list_audit(db:Session=Depends(get_db)): return db.query(models.AuditLog).order_by(models.AuditLog.timestamp.desc()).all()
