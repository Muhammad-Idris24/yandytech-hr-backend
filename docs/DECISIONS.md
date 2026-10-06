# Architectural Decision Register (ADR)

## ADR-001 — Schema-per-Tenant PostgreSQL

**Status:** Accepted

**Decision:**

Use PostgreSQL schema-per-tenant multi-tenancy strategy.

**Reason:**

- Strong logical and physical tenant isolation
- Single PostgreSQL instance can serve multiple organizations
- Shared application code, isolated data
- Easier to implement tenant-specific customization later
- Migration tooling can apply updates across all tenant schemas uniformly
- Clear namespace isolation prevents accidental cross-tenant queries

**Consequences:**

- Tenant schema names must be validated/allowlisted (never interpolated from request)
- Migrations must support both platform and tenant schema updates
- New tenant onboarding requires schema provisioning
- Database connection pooling must handle schema selection
- Audit logs and tenant resolution must be precise

**Alternatives Considered:**

- Row-level security (RLS): Less explicit isolation, harder to reason about
- Separate databases: Operational complexity, harder to provision
- Shared schema with organization_id: Weaker isolation, easier for mistakes

---

## ADR-002 — Auth0 as Stateless Resource Server

**Status:** Accepted

**Decision:**

Backend is a stateless OAuth/OIDC resource server.
Backend independently verifies JWT access tokens.
No session state stored on backend.

**Reason:**

- Scalable: Stateless design allows horizontal scaling
- Secure: Token verification doesn't require backend state
- Standard: OAuth 2.0 + OIDC are industry standard
- Decoupled: Auth0 handles identity, backend handles authorization
- Frontend-agnostic: Any Auth0 client can authenticate

**Consequences:**

- Every request must include valid JWT
- Token expiration handled by Auth0 + frontend refresh logic
- Backend must validate token signature, issuer, audience, expiration
- Claims are the source of truth for tenant/user/roles

**Alternatives Considered:**

- Session-based auth: Requires server state, harder to scale
- Multiple identity providers: Complexity, defer to future

---

## ADR-003 — RBAC + Fine-Grained ABAC Authorization

**Status:** Accepted

**Decision:**

Role-Based Access Control (RBAC) provides baseline permissions.
Attribute-Based Access Control (ABAC) provides fine-grained enforcement.

Example:
```
Role: Manager
  permission: attendance.read
  scope: direct_reports
  
Attribute check:
  is_target_in_direct_reports(current_user, target_employee) ?
```

**Reason:**

- RBAC alone insufficient for HR domain complexity
- ABAC allows dynamic authorization based on user, resource, and context
- Can express: "manager can read direct report attendance" precisely
- Can express: "HR can read all payroll; managers cannot" precisely
- Field-level protection: "salary is sensitive; only HR + employee sees their own"

**Consequences:**

- Authorization logic not just role-based
- Must evaluate attributes at request time
- Authorization errors are possible (return 403)
- Testing must cover both role and attribute scenarios

**Alternatives Considered:**

- Pure RBAC: Too simplistic for HR, leads to over-permissioned roles
- Pure ABAC: No baseline, harder to reason about

---

## ADR-004 — Privacy Model: Least Privilege + Field-Level Protection

**Status:** Accepted

**Decision:**

Sensitive employee information protected at field level.
Users get only what they need.

Categories:
- **Public:** name, job title, department, manager (visible to organization)
- **Sensitive:** salary, payroll, address, personal contact, dates of birth (HR/self only)
- **Restricted:** disciplinary records, private appraisals, staff documents (category + permission based)

**Reason:**

- HR systems contain highly confidential information
- Legal/privacy compliance requires field-level access control
- Manager should not accidentally see unrelated employee salary
- Employee should see own payslip but not colleague's

**Consequences:**

- API responses must be filtered/serialized per user
- Cannot blindly return full employee record
- Requires permission checks at serialization layer
- Data models must tag sensitive fields

---

## ADR-005 — Immutable Audit Logs with Actor/Effective User Tracking

**Status:** Accepted

**Decision:**

Audit logs are append-only.
Every audit entry records:
- actual_actor (who made the change)
- effective_user (who the system acted as)
- action
- entity
- before/after state
- timestamp
- context (IP, user agent, etc.)

**Reason:**

- HR systems are legally sensitive; audit trail is compliance requirement
- Impersonation support requires distinguishing actual vs. effective actor
- Immutability prevents tampering
- Append-only ensures traceability

**Consequences:**

- Audit table grows quickly; requires retention/archival policy
- Sensitive data may appear in audit logs (salary changes); must be handled carefully
- Impersonation is auditable; not hidden

---

## ADR-006 — HR Impersonation is Supported and Fully Audited

**Status:** Accepted

**Decision:**

HR administrators can impersonate employees.
UI clearly shows impersonation state.
Audit trail records actual actor and impersonated user separately.

**Reason:**

- HR needs to troubleshoot employee issues
- Impersonation is better than giving HR full database access
- Audit trail makes impersonation transparent
- Controlled impersonation safer than other support mechanisms

**Consequences:**

- Impersonation is a powerful permission; must be granted carefully
- UI must prominently display impersonation status
- Audit logs must show impersonation clearly
- Testing must verify audit correctness

---

## ADR-007 — Modular Monolith Backend Architecture

**Status:** Accepted

**Decision:**

Backend is a single FastAPI application organized by domain/business capability.
Not separated into microservices unless operational requirements force it.

Structure:
```
app/
├── core/ (shared)
├── database/
├── modules/
│   ├── organization/
│   ├── employees/
│   ├── attendance/
│   ├── leave/
│   ├── payroll/
│   ├── feedback/
│   ├── etc./
└── shared/
```

**Reason:**

- Simpler to reason about and deploy
- Easier to enforce tenant isolation (all code in same process)
- Can evolve to microservices later if needed
- Typical SaaS MVP operates this way
- Clear module boundaries allow future separation

**Consequences:**

- All features share same database connection pool
- Tenant context must be consistently available
- Cannot independently scale modules
- Code organization is critical

---

## ADR-008 — Feature-Driven Frontend Architecture

**Status:** Accepted

**Decision:**

React app organized by feature/domain, not by technical layer.

Structure:
```
src/
├── app/ (shell, main layout)
├── features/
│   ├── attendance/
│   ├── employees/
│   ├── organization/
│   ├── leave/
│   ├── payroll/
│   ├── feedback/
│   ├── etc./
├── auth/
├── hooks/
├── components/ (shared)
├── lib/
├── types/
└── main.tsx
```

**Reason:**

- Mirrors backend domain structure
- Easier to locate code for a feature
- Scales better as app grows
- Team can own features end-to-end

**Consequences:**

- More directories, but clearer organization
- Shared components live in common folder
- Feature isolation reduces accidental cross-feature coupling

---

## ADR-009 — Tenant Resolution from Auth0 JWT Claims

**Status:** Accepted

**Decision:**

Current tenant is derived from Auth0 JWT claims.
Never trust client-supplied tenant ID.

**Reason:**

- Auth0 token is cryptographically verified
- Claims are source of truth for user identity
- Prevents client-side privilege escalation
- Tenant membership must be server-verified

**Consequences:**

- Auth0 custom claims must include tenant identifier
- Backend must look up tenant from claims
- Invalid claims result in 401/403

---

## ADR-010 — No Shared Frontend State for Tenant

**Status:** Accepted

**Decision:**

Do not store tenant ID in React state, localStorage, or sessionStorage.
Derive it from Auth0 user claims or backend context.

**Reason:**

- Frontend state is not trustworthy
- Tenant membership is server-verified
- XSS or state manipulation cannot escalate privileges

**Consequences:**

- Tenant ID passed in API requests but derived server-side
- Frontend cannot unilaterally change tenant
- Increases security

---
