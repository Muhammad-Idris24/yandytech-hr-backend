# Requirements & Implementation Decisions

## R1 — Multi-Tenancy

**Status:** LOCKED

**Decision:**

One shared application instance serves multiple organizations (tenants).
Each tenant's data is completely isolated in PostgreSQL schema.
Tenant A must never access Tenant B's data.

**Resolution:**
Schema-per-Tenant + Auth0 claims + server-side verification.

---

## R2 — Configurability

**Status:** LOCKED

**Decision:**

Organizations have different HR policies and rules.
These must be configurable, not hard-coded.

Examples:
- Attendance geofence radius (YandyTech: 20m, others: 100m)
- Leave types (YandyTech: Annual/Sick/Emergency; others: Annual/Casual/Study/Maternity)
- Payroll rules and percentages
- Office locations and working hours
- Appraisal cycles

**Resolution:**
Organization settings table.
Feature flags/configuration per feature.
No YandyTech-specific rules in application code.

---

## R3 — Privacy & Least Privilege

**Status:** LOCKED

**Decision:**

Sensitive HR information protected.
Users see only what they need.

Sensitive fields:
- Salary and payroll information
- Home address and personal contact
- Date of birth
- Emergency contacts
- Disciplinary records
- Private appraisal data
- Confidential staff documents

**Resolution:**
Field-level access control + document category ACLs + scope-based visibility.

---

## R4 — Audit & Accountability

**Status:** LOCKED

**Decision:**

Every meaningful action is logged and traceable.
Audit trail shows who did what, when, and why.

Critical audit events:
- Authentication/login
- Employee data changes
- Salary/payroll changes
- Payroll publication
- Leave approvals
- Document uploads/deletions
- Role/permission changes
- Impersonation
- Security events

**Resolution:**
Immutable append-only audit_logs table.
Structured logging with actor/effective user.

---

## R5 — Attendance with Geofence

**Status:** LOCKED

**Decision:**

Employees check in/out when physically at office.
System verifies location via geofence (coordinates + radius).

Supported:
- Multiple office locations
- Check-in / check-out with location verification
- Late detection
- Missed checkout detection
- Configurable radius per location

YandyTech requirement: 20-meter radius for initial office.

**Resolution:**
Attendance module with location verification.
Office location table with coordinates.
Configuration table for geofence radius.

---

## R6 — Leave Management

**Status:** LOCKED

**Decision:**

Employees request leave digitally.
Manager approves/rejects.
System updates leave balance.
Notifications sent.

Configurable:
- Leave types
- Annual entitlements
- Carry-over rules
- Approval workflow
- Holidays
- Half-days

**Resolution:**
Leave module with request/approval workflow.
Leave configuration per organization.

---

## R7 — Payroll

**Status:** LOCKED

**Decision:**

Payroll is a sensitive HR domain.
Employees see their payslips.
HR manages payroll.
Rules are configurable and effective-dated.

Supported:
- Salary structures
- Earnings (basic, allowances)
- Deductions (taxes, contributions)
- Payslips
- Payroll publication
- Payroll periods

**Resolution:**
Payroll module with role-based access.
Salary/payroll settings configurable.
Sensitive payroll data protected.

---

## R8 — Goals vs. Appraisals

**Status:** LOCKED

**Decision:**

Goals and Appraisals are DIFFERENT concepts.

**Goals:**
- Employee-driven personal development targets
- Continuous, not formal events
- Can update progress anytime
- Manager may have visibility

**Appraisals:**
- Formal HR evaluation cycles
- Structured workflow: Draft → Self-Assessment → Manager Review → HR Review → Published → Acknowledged
- Specific performance levels (1-5)
- Acknowledgement = "I have seen this", NOT "I agree"

**Resolution:**
Two separate modules with distinct workflows.

---

## R9 — Feedback vs. Praise

**Status:** LOCKED

**Decision:**

Three distinct concepts:

**Formal HR Feedback:**
- Official HR records
- Structured format
- Private, confidential

**Instant Feedback:**
- Quick peer/manager feedback
- Can flow multiple directions (employee→manager, manager→employee, peer→peer)
- Workflow: Submitted → Reviewed → Assigned → Responded → Resolved → Closed

**Praise/Recognition:**
- Public recognition
- Celebration of achievements
- Different tone/purpose than feedback

**Resolution:**
Three separate feedback modules with distinct workflows.

---

## R10 — Training is NOT a Full LMS

**Status:** LOCKED

**Decision:**

Training supports resource sharing and progress tracking.
Does NOT include full video hosting.

Supported:
- HR assigns training resources (links/files)
- Employees track progress
- Completion status
- Learning path (aggregate view)

**Out of scope (for now):**
- Full video hosting
- Interactive quizzes
- Certificates (for now)

**Resolution:**
Training module with link/resource tracking.
Learning path as derived view.

---

## R11 — Organization Structure

**Status:** LOCKED

**Decision:**

Platform understands organizational hierarchy:
- Departments
- Teams
- Employees
- Managers
- Org Chart

Org Chart shows:
- Reporting lines
- Departments
- Vacant positions (future)
- Organizational relationships

BUT: Sensitive employee info hidden.

**Resolution:**
Organization module with department/team/hierarchy models.

---

## R12 — Documents (Organization + Staff)

**Status:** LOCKED

**Decision:**

Two document types:

**Organization Documents:**
- Policies, reports, guidelines
- General audience
- Public within organization

**Staff Folders:**
- Confidential employee records
- Employment letters, contracts, certificates, IDs
- Disciplinary records
- HR documents
- Restricted access: category + permission based

**Resolution:**
Document module with category/permission model.
Access control based on user role + document category + employee relationship.

---

## R13 — System Roles Separation

**Status:** LOCKED

**Decision:**

Five major role categories:

1. **Platform Administrator:**
   - Can manage organizations/tenants
   - Can manage platform settings
   - Does NOT automatically see HR data

2. **System Administrator (org-level):**
   - Can manage users, roles, permissions
   - Can manage security settings
   - Does NOT automatically see sensitive HR data (salary, payroll, etc.)

3. **HR Administrator:**
   - Can manage employees, payroll, leave, feedback
   - Can access organization HR settings
   - Can impersonate users (audited)
   - Highest HR data access

4. **Manager:**
   - Can approve leave
   - Can view direct report attendance/goals
   - Can initiate appraisals
   - Scope-based: only their team

5. **Employee:**
   - Can self-serve: attendance, goals, feedback, profile
   - Can request leave, view payslip
   - Can see permitted org directory

**Resolution:**
Roles module with permission matrix.
Separate permissions for platform vs. org vs. HR.

---

## R14 — HR Impersonation

**Status:** LOCKED

**Decision:**

HR can impersonate employees for support.
Impersonation is NOT hidden; UI clearly shows state.
Audit trail records actual actor separately.

Example audit entry:
```
actor: hr_admin_john
effective_user: employee_sarah
action: view_payslip
author: hr_admin_john (impersonating employee_sarah)
timestamp: 2026-10-06T10:30:00Z
```

**Resolution:**
Impersonation feature in HR module.
Actual actor always recorded in audit.

---

## R15 — Notifications

**Status:** LOCKED

**Decision:**

Notifications delivered via:
- In-app
- Email
- Push (future)

Events:
- Leave submitted/approved/rejected
- Payslip published
- Training assigned
- Appraisal started/published
- Feedback updates
- Praise/recognition
- Attendance prompts
- Org announcements

Notifications must respect permissions.

**Resolution:**
Notifications module with channel/event support.
Permission-aware notification delivery.

---

## R16 — Search

**Status:** LOCKED

**Decision:**

Two search types:

**Global Search:**
- Available from main dashboard
- Searches across modules (employees, documents, etc.)
- Results filtered by user permissions

**Contextual Search:**
- Within specific modules (Employees → search employees)
- Faster, scoped results

All search results must respect authorization.

**Resolution:**
Search module with permission-based filtering.

---

## R17 — What's New

**Status:** LOCKED

**Decision:**

Distinct from notifications.
Shows:
- Release notes
- Platform announcements
- Organization announcements
- Feature launches

**Resolution:**
What's New section with announcement board.

---

## R18 — Product Scope — V1

**Status:** LOCKED

**Decision:**

V1 includes:
- Multi-tenancy ✓
- Authentication ✓
- Authorization ✓
- Employees ✓
- Organization structure ✓
- Attendance ✓
- Leave ✓
- Payroll ✓
- Goals ✓
- Feedback/Praise ✓
- Training/Learning ✓
- Appraisal ✓
- Documents ✓
- Notifications ✓
- Audit ✓
- Search ✓
- Reports ✓
- Settings ✓

V1 explicitly excludes:
- Forms module
- Competencies module
- Full LMS/video hosting
- Advanced analytics/AI
- Biometric attendance

**Resolution:**
Scope locked. Future phase decisions if these are added.

---

## R19 — No Hard-Coded YandyTech Logic

**Status:** LOCKED

**Decision:**

YandyTech is the first tenant, not the product definition.
YandyTech-specific rules must be configured, not hard-coded.

Examples of WRONG:
```python
if organization.name == "YandyTech":
    geofence_radius = 20  # WRONG!
```

Examples of RIGHT:
```python
geofence_radius = organization.settings.attendance_geofence_radius
# Default to 20 if not configured
```

**Resolution:**
All organizational differences in settings tables.
No organization-specific branching logic.

---
