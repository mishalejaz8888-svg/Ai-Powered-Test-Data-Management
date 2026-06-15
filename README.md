# AI-Powered Test Data Management Platform

A full-stack platform that lets QA, automation, and data engineering teams generate realistic synthetic test data, mask sensitive PII, validate data quality, export datasets, and govern usage from a single executive dashboard.

---

## Project Overview

Engineering teams routinely burn days hand-crafting test data, and that data is often unrealistic, unmasked, or unsafe to copy from production. This platform removes that bottleneck by turning test data into a managed, auditable, and repeatable workflow.

**The problem it solves**

- Manual test data creation is slow, inconsistent, and rarely covers edge cases.
- Copying production data into QA environments exposes real PII and creates compliance risk.
- Teams lack visibility into where datasets came from, who used them, and whether they passed quality rules.

**Target users**

- QA and test automation engineers who need fresh, realistic datasets on demand.
- Data engineering teams standardizing test data across QA, UAT, Staging, and Performance environments.
- Regulated teams in healthcare, fintech, and e-commerce that must keep real PII out of non-production systems.

**Business value**

- Replaces days of manual data preparation with on-demand generation.
- Reduces compliance exposure by masking PII before any dataset leaves the platform.
- Provides a governed audit trail of every generation, masking, export, and usage event.

**Key differentiators**

- Domain-aware generators for Customers, Orders, Transactions, Healthcare, Insurance Claims, Banking, E-commerce, and SaaS Users.
- Built-in PII masking, data quality validation, and an audit trail rather than bolt-on afterthoughts.
- An executive analytics dashboard that frames test data as a measurable, governable asset.

---

## Demo

| Resource | Link |
| -------- | ---- |
| Live Demo | _Add deployment URL_ |
| GitHub Repository | _Add repository URL_ |
| Loom Video Walkthrough | _Add Loom URL_ |

---

## Key Features

| Feature | Description | Business Value |
| ------- | ----------- | -------------- |
| Executive Dashboard | Aggregated KPIs, data quality score, dataset breakdowns, masking coverage, and quality trends rendered as live charts. | Gives leadership a single view of test data health and coverage. |
| Synthetic Data Generator | Generates realistic records by dataset type, record count, environment, and complexity. | Eliminates manual data preparation and accelerates test cycles. |
| Domain-Aware Datasets | Purpose-built schemas for Customers, Orders, Transactions, Healthcare, Insurance Claims, Banking, E-commerce, and SaaS Users. | Produces data that mirrors real business entities, improving test relevance. |
| PII Masking Engine | Configurable masking rules (partial masking, initials, last-four, tokenization) applied across sensitive fields. | Keeps real PII out of non-production environments and reduces compliance risk. |
| Data Quality Validation | Rule-based validation with pass/fail counts, severity, and suggested fixes. | Catches invalid records before they pollute downstream tests. |
| Dataset Preview | Side-by-side view of raw and masked records before export. | Lets teams verify masking and structure before distribution. |
| Export Center | Tracks exported datasets across formats (CSV, JSON, SQL, Postman, API Mock) with record counts. | Centralizes distribution and creates a record of what left the platform. |
| Refresh Jobs | Generation job history with status, requested vs. generated counts, and failure reasons. | Provides operational visibility into data pipeline reliability. |
| Usage Tracking | Logs which teams used which datasets, in which environment, and for what purpose. | Surfaces dataset adoption and supports capacity planning. |
| Audit Trail | Chronological log of generation, masking, export, and validation events. | Supports governance, traceability, and compliance reporting. |
| AI Assistant | Generates dataset strategies, risk areas, quality findings, and recommended actions from a natural-language prompt. | Lowers the barrier for non-experts to design safe, high-quality datasets. |

---

## System Architecture

```
                          User (QA / Data Engineer)
                                     |
                                     v
              Frontend  -  React + Vite SPA (Dashboard, Generator, Audit)
                                     |  REST / Axios
                                     v
              API Layer  -  FastAPI Routers (11 resource modules)
                                     |
                                     v
              Business Logic  -  Generators, Masking, Validation, AI Assistant
                                     |  SQLAlchemy ORM
                                     v
              Database  -  SQLite (default)  /  PostgreSQL (production-ready)
```

**Layer responsibilities**

- **Frontend** — A single-page React application that renders the dashboard, dataset workflows, and analytics charts, communicating with the backend over REST.
- **API Layer** — FastAPI routers expose dedicated, versioned endpoints per resource (projects, generation, masking, quality, exports, jobs, usage, audit, AI), each documented automatically via OpenAPI/Swagger.
- **Business Logic** — Service modules encapsulate synthetic data generation, field-level PII masking, quality validation, and AI-assisted recommendations, keeping the API thin and testable.
- **Database** — SQLAlchemy models persist projects, records, masking rules, quality results, exports, jobs, usage, and audit logs. SQLite runs out of the box; a single environment variable switches to PostgreSQL.

---

## Technology Stack

| Layer | Technology |
| ----- | ---------- |
| Frontend | React, Vite, JavaScript (JSX) |
| Routing & Data Fetching | React Router, Axios |
| Data Visualization | Recharts, Lucide Icons |
| Backend | FastAPI, Python |
| ORM & Data Modeling | SQLAlchemy 2.0, Pydantic |
| Database | SQLite (default), PostgreSQL-ready (psycopg2) |
| API Documentation | OpenAPI / Swagger UI (auto-generated) |
| AI Services | Pluggable AI assistant service (extensible to OpenAI / Claude) |
| Configuration | python-dotenv environment-based configuration |
| Dev & Tooling | Uvicorn ASGI server, Vite dev server, CORS middleware |

---

## Core Workflows

**User Workflow**

1. Open the executive dashboard to review data quality score and dataset coverage.
2. Configure a dataset (type, record count, environment, complexity) in the generator.
3. Generate records, then preview raw vs. masked output.
4. Export the dataset in the required format and track it in the Export Center.

**Admin / Governance Workflow**

1. Review masking rules and confirm coverage across sensitive fields.
2. Run data quality validations and triage failures by severity.
3. Monitor refresh jobs for failures and inspect error messages.
4. Audit every generation, masking, and export event through the audit trail.

**Data Processing Workflow**

1. The generator produces domain-specific records based on the selected dataset type.
2. The masking engine applies field-level rules to protect PII.
3. Validation produces pass/fail counts with suggested fixes.
4. Results, jobs, and audit entries are persisted via SQLAlchemy.

**AI Workflow**

1. The user submits a natural-language question to the AI Assistant.
2. The assistant returns a dataset generation plan, risk areas, quality findings, and recommended actions.
3. The service interface is designed to be swapped for a hosted LLM provider without changing the API contract.

---

## Project Structure

```
ai-powered-test-data-management-platform/
├── backend/
│   ├── app/
│   │   ├── main.py            # FastAPI app, CORS, router registration
│   │   ├── database.py        # Engine, session, SQLite/PostgreSQL switch
│   │   ├── models.py          # SQLAlchemy models (8 domain tables)
│   │   ├── schemas.py         # Pydantic request/response schemas
│   │   ├── seed.py            # Deterministic seed data for demos
│   │   ├── routers/           # 11 resource routers (REST endpoints)
│   │   └── services/          # Generator, masking, AI assistant logic
│   └── requirements.txt
└── frontend/
    └── src/
        ├── App.jsx            # App shell, navigation, routing
        ├── pages/             # 11 feature pages (dashboard, generator, audit...)
        ├── components/        # Reusable UI components
        └── services/api.js    # Centralized Axios API client
```

- **backend/app/routers** — One router per business capability, keeping endpoints cohesive and easy to extend.
- **backend/app/services** — Pure business logic separated from transport, enabling unit testing and provider swaps.
- **frontend/src/pages** — Each platform capability is a self-contained page mapped to a route.
- **frontend/src/services/api.js** — A single API surface so endpoints are defined once and reused everywhere.

---

## Security & Performance

**Authentication & Authorization**

- The platform is structured for role-based access (QA, Automation, Data QA, Release QA are first-class concepts in the data model), providing a clear extension point for authentication and per-role authorization.

**Input Validation**

- All request and response payloads are validated through Pydantic schemas, rejecting malformed input before it reaches business logic.

**Data Protection**

- A field-level masking engine detects sensitive attributes (email, phone, name, address, date of birth, account, patient identifiers) and applies masking before records are previewed or exported.
- Synthetic generation means no production PII ever needs to enter non-production environments.

**Performance Optimizations**

- Record preview endpoints are bounded (capped result sets) to keep responses fast on large datasets.
- Analytics are aggregated server-side into a single summary payload, minimizing client round-trips.
- A lightweight SPA with on-demand data fetching keeps the frontend responsive.

**Scalability Considerations**

- The database layer is environment-driven: SQLite for local development, PostgreSQL for production with no code changes.
- The router-per-resource and service-per-capability layout supports horizontal growth of features and teams.
- CORS is explicitly scoped, and the stateless REST API is suitable for containerized, horizontally scaled deployment.

---

## Installation & Local Setup

**Backend**

```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
python -m app.seed
uvicorn app.main:app --reload
```

API: `http://127.0.0.1:8000` — Interactive docs: `http://127.0.0.1:8000/docs`

**Frontend**

```bash
cd frontend
npm install
npm run dev
```

App: `http://localhost:5173`

**Optional: PostgreSQL**

Create `backend/.env`:

```env
DATABASE_URL=postgresql+psycopg2://postgres:password@localhost:5432/test_data_management
```

---

## Deployment

The backend runs as a standard ASGI application (Uvicorn/Gunicorn) and is container-friendly for platforms such as Render, Railway, Fly.io, or any Docker host, backed by managed PostgreSQL in production. The frontend builds to static assets via `npm run build` and deploys to any static host or CDN (Vercel, Netlify, Cloudflare Pages). Environment variables drive both the database connection and the frontend API base URL, keeping configuration out of source control.

---

## Future Enhancements

- Authentication and role-based access control with JWT/SSO and per-environment permissions.
- Direct file download and streaming exports (CSV, JSON, SQL) from the Export Center.
- Integration with a hosted LLM provider for fully generative dataset design and validation.
- Schema-driven custom dataset builder so teams can define their own entities and fields.
- Scheduled and event-triggered refresh jobs with a background worker queue.
- Configurable, rule-based data quality engine with custom validation rules per dataset type.
- Data lineage and versioning to track dataset evolution across releases.
- Webhook and CI/CD integrations to provision test data automatically in pipelines.
- Multi-tenant workspaces with usage quotas and billing-ready metering.
- Observability layer with metrics, structured logging, and alerting on job failures.

---

## Why This Project Stands Out

- **Real-world business use case** — It targets a concrete, expensive problem: safe, realistic test data is a daily pain for QA and data teams across regulated industries.
- **Product thinking** — Features are framed around outcomes (governance, compliance, adoption) rather than raw CRUD, with an executive dashboard that communicates value to non-technical stakeholders.
- **Architecture decisions** — A clean separation between transport (routers), business logic (services), and persistence (models) keeps the codebase cohesive, testable, and easy to extend.
- **Scalability design** — Environment-driven configuration moves from SQLite to PostgreSQL with no code changes, and the stateless REST API is ready for containerized, horizontally scaled deployment.
- **Maintainability** — A single API client on the frontend, schema-validated contracts on the backend, and one router per capability make the system approachable for new contributors.
- **Production-readiness** — Auto-generated OpenAPI documentation, scoped CORS, validated I/O, seedable demo data, and a built-in audit trail reflect engineering practices expected of a real SaaS product.
