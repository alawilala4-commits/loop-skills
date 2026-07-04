# Planning Template & Examples

## Step 1: Understand Requirement

**Template:**
```
What: [feature/fix description]
Why: [business reason, problem it solves]
Who: [stakeholder, user, internal team]
When: [deadline, priority]
Constraint: [tech, resource, timeline limitations]
```

**Example:**
```
What: Add user profile page
Why: Users want to see & edit their data
Who: End users
When: Next sprint (2 weeks)
Constraint: Must work on mobile, no new DB schema
```

## Step 2: Break into Subtask

**Template:**
```
1. Design (UI mockup, API spec)
2. Backend (endpoint, DB update, auth)
3. Frontend (component, styling, integration)
4. Testing (unit, e2e)
5. Deploy (staging, production)
```

**Example for Profile Page:**
```
1. Design API endpoint (GET /api/v1/user/:id, PUT /api/v1/user/:id)
2. Implement backend (profile service, DB query, validation)
3. Build frontend component (form, avatar upload, edit mode)
4. Add tests (API tests, component tests, e2e flow)
5. Deploy & verify
```

## Step 3: Estimate & Prioritize

**Estimation:**
- Small: 1 day or less
- Medium: 2-4 days
- Large: 1-2 weeks
- Epic: > 2 weeks (break further)

**Priority Scoring (0-10):**
- Impact (customer value): 0-10
- Urgency (time-sensitive): 0-10
- Complexity (effort/risk): -5 to 0
- Score = Impact + Urgency - Complexity

## Step 4: Order by Dependency

```
DAG (Directed Acyclic Graph):
Design → Backend → Frontend → Testing → Deploy
   ↑         ↑         ↑
   └─────────┴─────────┘
   (backend & frontend can parallel if design done)
```

**Example Order:**
1. Design API (blocks backend & frontend)
2. Backend implementation (backend team)
3. Frontend implementation (frontend team, parallel to backend)
4. Integration testing (after both done)
5. Deploy

## Step 5: Identify Risks

```
Risk: [potential problem]
Probability: Low/Medium/High
Impact: Low/Medium/High
Mitigation: [how to prevent or handle]

Example:
Risk: Avatar upload service down
Probability: Medium (third-party dependency)
Impact: High (feature broken)
Mitigation: Have fallback avatar, cache images locally
```

## Step 6: Create Timeline

```
Task          | Owner    | Duration | Start | End
Design        | Designer | 2 days   | Mon   | Tue
Backend       | Dev1     | 4 days   | Wed   | Fri
Frontend      | Dev2     | 4 days   | Wed   | Fri
Integration   | Dev1/2   | 1 day    | Mon   | Mon
Deploy        | DevOps   | 0.5 day  | Tue   | Tue
```

## Example: Complete Plan

**Feature: User Profile Page**

Subtasks:
1. [Design] Create Figma mockup & API spec (Designer, 2 days)
2. [Backend] Implement GET/PUT profile endpoint (Dev1, 3 days)
3. [Frontend] Build form component & integration (Dev2, 3 days)
4. [Testing] Unit tests & e2e (Dev1/2, 2 days)
5. [Deploy] Staging → Production (DevOps, 1 day)

Risks:
- Avatar service unavailable → Use fallback
- Performance slow with large avatar → Compress & cache
- Mobile layout broken → Test early on real device

Dependencies:
- Backend done before frontend integration
- Testing after backend + frontend done
- All tests green before deploy

Acceptance Criteria:
- [ ] User can view profile data
- [ ] User can edit profile
- [ ] Avatar upload working
- [ ] Mobile responsive
- [ ] Tests ≥ 80% coverage
- [ ] Zero security warnings
