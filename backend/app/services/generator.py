import random,json
from datetime import date,timedelta
FIRST=['John','Sarah','Ahmed','Maria','Mishal','Ali','Ayesha','David','Fatima','Omar']; LAST=['Smith','Khan','Raza','Garcia','Ijaz','Malik','Noor','Wilson','Patel','Ahmed']
def mask(v):
    s=str(v)
    if '@' in s: return s[0]+'***@'+s.split('@')[-1]
    if len(s)>8: return '***'+s[-4:]
    return s
def dt(days=1000): return str(date.today()-timedelta(days=random.randint(1,days)))
def mask_record(d):
    out=dict(d)
    for k,v in out.items():
        if any(x in k.lower() for x in ['email','phone','name','address','birth','account','patient']): out[k]=mask(v)
    return out
def make_record(dtype,i):
    first,last=random.choice(FIRST),random.choice(LAST); kind=dtype.lower()
    if 'order' in kind:
        qty=random.randint(1,5); price=round(random.uniform(20,500),2); raw={'order_id':f'ORD-{2000+i}','customer_id':f'CUST-{1000+i}','product_name':'Subscription','quantity':qty,'unit_price':price,'total_amount':round(qty*price,2),'order_status':random.choice(['Created','Shipped','Delivered']),'payment_status':random.choice(['Paid','Failed','Pending']),'order_date':dt(365),'shipping_address':f'{i} Commerce Ave'}; key=raw['order_id']; final='Orders'
    elif 'transaction' in kind or 'bank' in kind:
        raw={'transaction_id':f'TXN-{3000+i}','customer_id':f'CUST-{1000+i}','account_id':f'ACC-{random.randint(10000,99999)}','amount':round(random.uniform(10,5000),2),'currency':'USD','transaction_type':random.choice(['Card','ACH','Wire']),'merchant':'RetailCo','transaction_status':random.choice(['Success','Failed','Pending']),'risk_score':random.randint(1,100),'transaction_date':dt(365)}; key=raw['transaction_id']; final='Transactions'
    elif 'health' in kind or 'claim' in kind:
        raw={'patient_id':f'PAT-{4000+i}','patient_name':f'{first} {last}','date_of_birth':dt(25000),'gender':random.choice(['Male','Female']),'diagnosis_code':random.choice(['E11','I10','J45']),'diagnosis_description':'Synthetic diagnosis','provider_name':'Dr. Khan','appointment_date':dt(180),'claim_amount':round(random.uniform(100,8000),2),'claim_status':random.choice(['Submitted','Approved','Denied']),'insurance_plan':random.choice(['Basic','Premium'])}; key=raw['patient_id']; final='Healthcare'
    else:
        raw={'customer_id':f'CUST-{1000+i}','first_name':first,'last_name':last,'full_name':f'{first} {last}','email':f'{first.lower()}.{last.lower()}{i}@example.com','phone':f'555-{random.randint(100,999)}-{random.randint(1000,9999)}','date_of_birth':dt(15000),'address':f'{i} Main Street','city':'Lahore','country':'Pakistan','company':'DataWorks','customer_status':random.choice(['Active','Inactive','Trial']),'signup_date':dt(1200)}; key=raw['customer_id']; final='Customers'
    return {'dataset_type':final,'record_key':key,'raw_data':json.dumps(raw),'masked_data':json.dumps(mask_record(raw)),'validation_status':'Passed','has_pii':True}
def generate_records(dtype,count): return [make_record(dtype,i) for i in range(1,count+1)]
