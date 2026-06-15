from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base,engine
from .routers import analytics,projects,records,generate,masking,quality,exports,jobs,usage,audit,ai
Base.metadata.create_all(bind=engine)
app=FastAPI(title='AI-Powered Test Data Management Platform',description='Synthetic test data generation, PII masking, validation, exports, usage tracking, and AI assistance.',version='1.0.0')
app.add_middleware(CORSMiddleware,allow_origins=['http://localhost:5173','http://127.0.0.1:5173'],allow_credentials=True,allow_methods=['*'],allow_headers=['*'])
for r in [analytics.router,projects.router,records.router,generate.router,masking.router,quality.router,exports.router,jobs.router,usage.router,audit.router,ai.router]: app.include_router(r)
@app.get('/')
def health_check(): return {'status':'ok','message':'AI-Powered Test Data Management API is running'}
