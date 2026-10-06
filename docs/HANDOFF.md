# YandyTech HR SaaS Platform — Handoff Document

## What Are We Building?

A **secure, multi-tenant, configurable Human Resource Management SaaS platform** that:
- Supports multiple organizations (YandyTech Community is the first)
- Centralizes employee information, attendance, leave, payroll, performance, training, feedback, and more
- Protects sensitive HR data with field-level and document-level access control
- Audits all meaningful actions
- Remains configurable so each organization can customize HR policies without code changes

## Where Are We Now?

**Phase:** Foundation Setup (Phase 0)
**Completion:** ~15%

Both repositories created. Documentation framework established. Architecture decisions locked. No application code written yet.

## What Was Completed?

1. ✅ Repository setup (frontend + backend)
2. ✅ Documentation framework (BUILD_STATE, DECISIONS, REQUIREMENTS_DECISIONS, CHANGELOG, HANDOFF)
3. ✅ 10 architectural decisions documented (schema-per-tenant, Auth0, RBAC+ABAC, etc.)
4. ✅ 19 requirement decisions locked (multi-tenancy, privacy, audit, roles, features, scope)
5. ✅ Product scope clarified (V1 includes attendance, leave, payroll, appraisal, feedback, goals, training, documents, notifications, search, reports, audit)

## What Was Changed Recently?

- Initial session: Created repositories and documentation
- Locked all major architectural decisions before any code was written
- Established clear project state tracking

## What Decisions Are Locked?

### Technology
- Frontend: React + Vite + TanStack Query + React Hook Form + Zod + Shadcn UI
- Backend: Python + FastAPI + SQLAlchemy + Alembic
- Database: PostgreSQL
- Authentication: Auth0 (stateless resource server)
- Separate repositories (frontend/backend)

### Architecture
- Multi-tenancy: Schema-per-Tenant (tenant_* schemas in PostgreSQL)
- Authorization: RBAC + fine-grained ABAC
- Privacy: Field-level + document category + scope-based
- Audit: Immutable append-only logs with actor/effective user
- Backend organization: Domain-driven (modular monolith)
- Frontend organization: Feature-driven
- Tenant resolution: From Auth0 JWT claims (never trust client)

### Product
- Scope: V1 feature set (attendance, leave, payroll, appraisal, feedback, goals, training, documents, notifications, search, reports, audit)
- No: Forms, Competencies, full LMS
- Configurability: All org-specific rules in settings (no hard-coded YandyTech logic)
- YandyTech is first tenant, not product definition

## What Is Currently Broken?

Nothing. Application code not yet started.

## What Remains?

### Phase 1 — Foundation (Next)
- FastAPI app scaffolding
- PostgreSQL connection layer with tenant routing
- Auth0 JWT verification
- Alembic migrations
- Basic authorization framework
- Audit logging infrastructure

### Phase 2 — Core Organization
- Organizations, employees, departments, teams, office locations
- Profile management
- Org chart

### Phase 3 — Daily Operations
- Attendance (geofence check-in/check-out)
- Leave management
- Notifications

### Phase 4 — HR Operations
- Payroll
- Staff documents + organization documents
- Reports

### Phase 5 — Development & Performance
- Goals
- Training & learning path
- Appraisal cycles
- Feedback (formal + instant)
- Praise/recognition

### Phase 6 — Platform Experience
- Global search
- What's New
- Advanced reporting
- Bulk document generation
- Dashboard refinement

### Phase 7 — Hardening
- Security testing (tenant isolation, authorization, SQL injection, XSS)
- Performance testing
- Migration testing
- Accessibility checks
- Production readiness

## What Should I Do First?

1. **Read the docs:**
   - `docs/BUILD_STATE.md` — Current status
   - `docs/DECISIONS.md` — Why we made each choice
   - `docs/REQUIREMENTS_DECISIONS.md` — Product requirements locked
   - `docs/CHANGELOG.md` — What's been done
   - This file — Handoff orientation

2. **Review the repositories:**
   - `yandytech-hr-backend` — Will contain FastAPI app
   - `yandytech-hr-frontend` — Will contain React app

3. **Next task:**
   - Start backend foundation scaffolding (see "Phase 1" below)

## What Must I NOT Change?

- **Do NOT** deviate from locked architectural decisions without explicit approval
- **Do NOT** hard-code YandyTech-specific logic
- **Do NOT** trust client-supplied tenant IDs
- **Do NOT** disable authorization for convenience
- **Do NOT** merge frontend and backend repositories
- **Do NOT** remove field-level privacy protection
- **Do NOT** skip audit logging
- **Do NOT** expose raw stack traces in production errors
- **Do NOT** store JWT tokens in localStorage
- **Do NOT** use SQL string interpolation for dynamic schemas

## What Commands Should I Run?

### Backend
```bash
# Navigate to backend repo
cd yandytech-hr-backend

# Create Python venv
python3.11 -m venv venv
source venv/bin/activate  # or: venv\Scripts\activate on Windows

# Install dependencies (when requirements.txt exists)
pip install -r requirements.txt

# Run migrations (when migrations exist)
alembic upgrade head

# Start development server
uvicorn app.main:app --reload --port 8000
```

### Frontend
```bash
# Navigate to frontend repo
cd yandytech-hr-frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

## What Environment Variables Are Required?

### Backend
```bash
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/yandytech_hr

# Auth0
AUTH0_DOMAIN=your-tenant.auth0.com
AUTH0_CLIENT_ID=your-client-id
AUTH0_CLIENT_SECRET=your-client-secret
API_AUDIENCE=https://yandytech-hr-api

# Environment
ENVIRONMENT=development
DEBUG=True
```

### Frontend
```bash
# Auth0
VITE_AUTH0_DOMAIN=your-tenant.auth0.com
VITE_AUTH0_CLIENT_ID=your-client-id
VITE_API_URL=http://localhost:8000
VITE_API_AUDIENCE=https://yandytech-hr-api
```

## What Tests Should I Run?

When tests exist:

### Backend
```bash
pytest  # Run all tests
pytest --cov  # With coverage
pytest tests/test_tenant_isolation.py  # Tenant isolation tests (critical)
pytest tests/test_authorization.py  # Authorization tests (critical)
```

### Frontend
```bash
npm run test  # Run tests
npm run test:coverage  # With coverage
```

## What Known Risks Exist?

1. **Deadline:** October 10, 2026 (4 days from start)
   - Aggressive timeline
   - Must prioritize vertical slices over feature breadth
   - MVP must be secure and functional, even if not feature-complete

2. **Complexity:** HR systems are complex
   - Multi-tenancy adds complexity
   - Privacy/audit requirements are strict
   - Authorization logic is non-trivial
   - Must not rush security

3. **Team:** 11-person org, some roles unclear
   - Fatima Alhassan listed in two roles
   - Alamin Musa Magaga in management and tech
   - HR Associate name not provided
   - Verify actual team structure

4. **Auth0 Setup:** Requires external configuration
   - Must create Auth0 tenant
   - Must configure custom claims for tenant membership
   - Must set up API audience
   - Cannot proceed without this

5. **Database:** PostgreSQL required
   - Must be accessible from development environment
   - Schema-per-tenant requires careful setup
   - Migrations must handle multiple schemas
   - Test data seeding needed

## How Should Ongoing Work Be Tracked?

Maintain these documents:

1. **BUILD_STATE.md** — Update after each session
   - Current phase
   - Completed work
   - In-progress work
   - Blockers
   - Completion estimate

2. **CHANGELOG.md** — Add entry for each session
   - What was added/changed/fixed
   - Database changes
   - API changes
   - Frontend changes
   - Security changes

3. **HANDOFF.md** — Update at end of significant work
   - Summary of current state
   - What to do next
   - Known risks

## What If Something Goes Wrong?

1. **Database issues:** Check PostgreSQL connection, schema naming
2. **Auth0 issues:** Verify tenant config, JWT claims, API audience
3. **Authorization fails:** Check token claims, ABAC logic, database queries
4. **Tenant isolation fails:** CRITICAL — do not ship. Review schema routing, data filters, queries
5. **API not working:** Check CORS, error handling, request/response schemas
6. **Build fails:** Check dependencies, environment variables, Python/Node versions

## Key Dates

- **October 6, 2026:** Project started (today)
- **October 10, 2026:** Target MVP ready for YandyTech
- **4 days:** Full development window

## Next Agent/Developer

If taking over from here:

1. Read all docs
2. Inspect both repositories
3. Run tests and builds (if they exist)
4. Verify described state matches actual code state
5. If discrepancies exist, document them before proceeding
6. Start with the highest-value incomplete task
7. Update BUILD_STATE.md when beginning a new task
8. Update CHANGELOG.md when completing a task
9. Update this HANDOFF.md at the end of your session

---

**Last Updated:** 2026-10-06  
**By:** GitHub Copilot (autonomous build agent)  
**Next Session:** Backend Foundation Scaffolding
