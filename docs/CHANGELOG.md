# YandyTech HR SaaS Platform — Changelog

## [2026-10-06] — Session 1 — Foundation Setup

### Added
- Frontend repository: `yandytech-hr-frontend`
- Backend repository: `yandytech-hr-backend`
- Documentation framework:
  - BUILD_STATE.md
  - DECISIONS.md (10 ADRs)
  - REQUIREMENTS_DECISIONS.md (19 requirement decisions)
  - CHANGELOG.md (this file)
  - HANDOFF.md
- Initial project state tracking
- Architecture decisions locked (Schema-per-Tenant, Auth0, RBAC+ABAC, etc.)
- Requirements clarified and documented

### Notes
- Project deadline: October 10, 2026 (4 days)
- Team: 11 members across technology, HR, finance, operations, communication
- YandyTech is first tenant, not product definition
- Product must be reusable for other organizations

---

## Upcoming Sessions

### Session 2 — Backend Foundation Scaffolding
- FastAPI app structure
- PostgreSQL connection layer
- Auth0 JWT verification
- Database tenant routing
- Alembic migrations setup
- Initial models and schemas

### Session 3 — Backend Core Modules
- Organization module
- Employees module
- Departments/Teams
- Authorization framework
- Audit logging implementation

### Session 4 — Frontend Scaffolding & Auth
- React + Vite setup
- Auth0 provider integration
- API client with token refresh
- Protected routes
- Dashboard shell

### Session 5 — Attendance Module (Vertical Slice)
- Backend: models, API, location verification
- Frontend: UI, geofence, check-in/check-out
- Database: migrations
- Tests and validation

### Session 6 — Leave Module (Vertical Slice)
- Backend: models, approval workflow, notifications
- Frontend: leave request, approvals, balance view
- Database: migrations
- Tests

### Session 7 — Payroll Foundation
- Backend: salary structures, payslips
- Frontend: employee payslip view, HR payroll management
- Database: migrations
- Tests

### Session 8 — Documents & Staff Folders
- Backend: document models, ACLs, versioning
- Frontend: upload, download, permissions
- Database: migrations
- Tests

### Session 9 — Appraisal & Feedback
- Backend: workflow, permissions
- Frontend: self-assessment, manager review, publication
- Database: migrations
- Tests

### Session 10+ — Platform Experience, Testing, Refinement

---
