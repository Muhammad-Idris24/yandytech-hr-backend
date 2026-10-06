# YandyTech HR SaaS Platform — Build State

## Current Phase

**PHASE 0: DISCOVERY & FOUNDATION**

---

## Current Objective

Establish secure multi-tenant architecture foundation with Auth0 integration and database schema-per-tenant strategy. Build authentication, authorization, audit, and core organization/employee modules.

---

## Overall Completion Estimate

- **Phase 0 (Foundation):** 15%
- **Phase 1 (Organization Core):** 0%
- **Phase 2 (Attendance + Leave):** 0%
- **Phase 3 (Payroll + Documents):** 0%
- **Phase 4 (Development + Performance):** 0%
- **Phase 5 (Platform Experience):** 0%
- **Phase 6 (Hardening):** 0%

**MVP Overall:** ~15%

---

## Completed

### Repository Setup
- ✅ Frontend repository created: `yandytech-hr-frontend`
- ✅ Backend repository created: `yandytech-hr-backend`
- ✅ Documentation framework initialized
- ✅ Decision registers created
- ✅ Changelog established

### Architecture Decisions
- ✅ Tech stack locked: React/Vite + FastAPI + PostgreSQL + Auth0
- ✅ Multi-tenancy strategy locked: Schema-per-Tenant
- ✅ Authorization model locked: RBAC + Fine-grained ABAC
- ✅ Security philosophy locked: Least privilege + field-level protection
- ✅ Product scope locked: V1 feature set defined

---

## In Progress

- Backend foundation scaffolding (starting now)
  - FastAPI app structure
  - PostgreSQL connection layer
  - Auth0 JWT verification
  - Tenant database routing
  - RBAC/ABAC foundation
  - Audit logging base

---

## Blocked

None at this time.

---

## Known Bugs

None at this time.

---

## Technical Debt

None at this time.

---

## Current Architecture

### Backend Stack
- **Framework:** FastAPI
- **Database:** PostgreSQL with schema-per-tenant
- **Authentication:** Auth0 OAuth/OIDC
- **Authorization:** RBAC baseline + ABAC fine-grained
- **Logging:** Structlog
- **ORM:** SQLAlchemy
- **Migrations:** Alembic

### Frontend Stack
- **Framework:** React 18+
- **Build Tool:** Vite (SPA mode)
- **State:** TanStack Query
- **Forms:** React Hook Form + Zod
- **UI:** Shadcn UI + Tailwind CSS
- **Auth:** Auth0 React SDK

### Multi-Tenancy
- **Strategy:** PostgreSQL schema-per-tenant
- **Tenant Identification:** From Auth0 JWT claims
- **Tenant Isolation:** Server-side enforcement at all layers

---

## Current Database State

### Platform (public schema)
```
Not yet implemented.
```

### Tenant Schema Template (tenant_*)
```
Not yet implemented.
```

---

## Current API State

Not yet implemented. Will follow OpenAPI-first design with Pydantic schemas.

---

## Current Frontend State

Not yet implemented. Will scaffold React app with Auth0 provider.

---

## Security State

### Implemented
- Decision: Schema-per-tenant isolation strategy
- Decision: Least privilege authorization
- Decision: Field-level sensitive data protection

### Planned
- Auth0 JWT verification
- RBAC/ABAC implementation
- Audit logging
- SQL injection protection
- CORS security
- Tenant isolation testing
- Authorization testing

---

## Tests

None at this time. Test framework will be established in Phase 1.

---

## Environment Requirements

### Backend
- Python 3.11+
- PostgreSQL 14+
- Auth0 tenant configured
- Environment variables:
  - `DATABASE_URL`
  - `AUTH0_DOMAIN`
  - `AUTH0_CLIENT_ID`
  - `AUTH0_CLIENT_SECRET`
  - `API_AUDIENCE`

### Frontend
- Node.js 18+
- Environment variables:
  - `VITE_AUTH0_DOMAIN`
  - `VITE_AUTH0_CLIENT_ID`
  - `VITE_API_URL`
  - `VITE_API_AUDIENCE`

---

## Next Recommended Task

1. ✅ Initialize documentation (this)
2. **→ Backend FastAPI app scaffolding**
3. Database connection layer
4. Auth0 JWT verification
5. Tenant context resolution
6. Organization module (models + API)
7. Employees module (models + API)
8. Authorization framework
9. Audit logging
10. Frontend React/Vite scaffolding
11. Auth0 provider integration
12. API client hook
13. Protected routes
14. Dashboard shell

---

## Last Updated

2026-10-06 — Initial setup

## Last Agent/Developer

GitHub Copilot (autonomous build agent)

---

## Key Decisions Locked

1. **Multi-tenancy:** Schema-per-Tenant in PostgreSQL
2. **Authentication:** Auth0 stateless resource server
3. **Authorization:** RBAC + ABAC
4. **Privacy:** Field-level + document category + scope-based
5. **Audit:** Immutable append-only logs with actor/effective user tracking
6. **Impersonation:** Supported with full audit trail
7. **Product Scope:** V1 feature set (not Forms, Competencies)
8. **Repositories:** Separate frontend/backend
9. **Architecture:** Modular monolith with domain-driven structure

---
