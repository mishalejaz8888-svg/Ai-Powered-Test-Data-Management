from fastapi import APIRouter
from .. import schemas
from ..services.ai_assistant import answer_question
router=APIRouter(prefix='/api/ai',tags=['AI'])
@router.post('/ask',response_model=schemas.AIAnswer)
def ask(payload:schemas.AIQuestion): return answer_question(payload.question)
