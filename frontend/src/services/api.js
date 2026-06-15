import axios from 'axios'
const API_BASE=import.meta.env.VITE_API_BASE||'http://127.0.0.1:8000'
export const api=axios.create({baseURL:API_BASE})
export const analyticsApi={summary:()=>api.get('/api/analytics/summary')}
export const projectApi={list:()=>api.get('/api/projects/'),create:p=>api.post('/api/projects/',p)}
export const recordApi={list:()=>api.get('/api/records/')}
export const generatorApi={generate:p=>api.post('/api/generate/',p)}
export const maskingApi={rules:()=>api.get('/api/masking-rules'),mask:id=>api.post(`/api/mask/${id}`)}
export const qualityApi={list:()=>api.get('/api/data-quality/'),run:id=>api.post(`/api/data-quality/run/${id}`)}
export const exportApi={list:()=>api.get('/api/exports/'),generate:id=>api.post(`/api/exports/generate/${id}`)}
export const jobApi={list:()=>api.get('/api/jobs/')}
export const usageApi={list:()=>api.get('/api/usage/')}
export const auditApi={list:()=>api.get('/api/audit-logs/')}
export const aiApi={ask:q=>api.post('/api/ai/ask',{question:q})}
