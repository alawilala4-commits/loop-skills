---
name: freelance-job-search
description: "Find freelance work, apply to gigs, and manage income generation — especially for entry-level Indonesian freelancers on platforms like DataAnnotation, Appen, Telus, Fiverr, Upwork, Freelancer.com. Use when user says 'cari kerja freelance', 'cari penghasilan', 'apply kerja', 'lowongan freelance', 'gig kerja', or asks about data annotation / AI training jobs."
version: 1.0.0
author: agent
license: MIT
platforms: [linux, android, termux]
metadata:
  hermes:
    tags: [freelance, job-search, income, data-annotation, remote-work, indonesia, entry-level]
---

# Freelance Job Search & Income Generation

Help users find real freelance work, apply strategically, and manage income — with focus on entry-level Indonesian workers using Android/Termux.

## Trigger Conditions

- User asks about finding freelance work, gigs, or income
- User mentions platforms: DataAnnotation, Appen, Telus, Fiverr, Upwork, Freelancer, Projects.co.id, Sribu, Fastwork
- User asks about data annotation, AI training, search engine evaluation
- User says "cari kerja", "butuh uang", "penghasilan", "apply lowongan"

## Platform Database (Indonesia-Friendly)

### Tier 1: Apply Immediately — No Experience Needed

| Platform | Job Types | Pay | Requirements | Apply URL |
|----------|-----------|-----|--------------|-----------|
| DataAnnotation.tech | AI coding, writing, evaluation | $20+/hr | Python basics, AI tools | https://dataannotation.tech |
| Appen | Search evaluator, data annotation, text collection | $3-7/hr | Indonesian fluency, 10hr/wk | https://appen.com/jobs/ |
| Telus International | Search Engine Evaluator, linguist | $4-7/hr | Indonesian native, KTP | https://telusinternational.com/careers |
| Outlier.ai | AI training, coding tasks | $5-25/hr | Varies by project | https://outlier.ai |
| Welocalize | Search quality rater | ~$5/hr | Indonesian, located in ID | https://welocalize.com/careers/ |

### Tier 2: Bid/Apply Per Job (Higher Competition)

| Platform | Job Types | Pay | Notes |
|----------|-----------|-----|-------|
| Freelancer.com | Data entry, VA, web research | $10-250/project | High competition, start cheap |
| Upwork | Data entry, VA, research | $3-15/hr | Needs Connects ($0.15/bid) |
| OnlineJobs.ph | VA, customer support | $3-5/hr | E-commerce roles |

### Tier 3: Create Your Own Gigs (Passive Leads)

| Platform | Best Gig Ideas | Pricing |
|----------|---------------|---------|
| Fiverr | Research & summarization, data entry, web research | $5-20/gig |
| Fastwork.id | Same as Fiverr, IDR pricing | Rp 50K-200K/gig |
| Sribu.com | Writing, design, data | Varies |

### Tier 4: Indonesian Local (Lower Competition)

| Platform | URL | Notes |
|----------|-----|-------|
| Projects.co.id | https://projects.co.id/ | Local job board |
| Sribu | https://sribu.com/ | Indonesian marketplace |
| Facebook Groups | "Freelancer Indonesia", "Remote Work Indonesia", "VA Indonesia" | Daily leads, less competition |
| Telegram | "Info Freelance Indonesia" channels | Job alerts |

## Application Workflow

### Step 1: Prepare User Profile Data

Collect and store these fields for auto-filling applications:
```
Full name: ________
Email: ________
Date of birth: ________
City/Province: ________
Country: Indonesia
Languages: Indonesian (Native), English (Passive)
Skills: [data entry, web research, AI tools, Python basics, summarization]
Availability: 10-20 hours/week
KTP/ID: yes/no
PayPal: yes/no
```

### Step 2: Apply to Tier 1 Platforms First

Priority order:
1. DataAnnotation.tech (highest pay, best fit for Python+AI users)
2. Appen (reliable, long-term projects)
3. Telus International (stable, search evaluation)

**Rule: Focus on ONE platform at a time.** Wait 3-7 days for response before moving to next.

### Step 3: Create Fiverr Gig (Passive Income)

Use the templates in `references/fiverr-gig-templates.md` for:
- Research & Summarization
- Data Entry
- Web Research

### Step 4: Apply to Tier 2-4 as Backup

## Email/Message Templates

### For Data Annotation Platforms (DataAnnotation, Appen, Telus)

```
Subject: Application — Indonesian Data Annotator / AI Trainer

Hello,

I am interested in the Indonesian Data Annotator / AI Training position.

My qualifications:
- Native Indonesian speaker
- Basic Python programming skills
- Proficient with AI tools (ChatGPT, Claude)
- Strong attention to detail
- Reliable internet access
- Available immediately

I am ready to start any assessment or training.

Thank you,
[Name]
Email: [email]
```

### For Fiverr Buyer Outreach

```
Hi! I saw you need [research/data entry/summarization]. I can help with that.

I offer:
- Fast, accurate work using AI tools + human review
- 24-hour delivery
- Indonesian & English

Let me know if you'd like to discuss the details!
```

### For Direct Client WhatsApp (Indonesian)

```
Halo [nama],

Saya bisa bantu untuk:
- Input data & spreadsheet
- Riset web & ringkasan
- Data entry

Saya detail, bisa deadline, dan komunikasi cepat.
Rate saya: [sesuaikan budget mereka]

Ada yang bisa saya bantu minggu ini?

Salam,
[Nama]
```

## User Profile Form

When user provides their information, store it in a structured format for reuse:

```json
{
  "profile": {
    "full_name": "",
    "email": "",
    "dob": "",
    "city": "",
    "skills": [],
    "languages": ["Indonesian (Native)"],
    "availability_hours_per_week": 0,
    "has_ktp": false,
    "has_paypal": false,
    "has_laptop": false,
    "internet_reliable": true
  },
  "applications": [],
  "gigs_created": [],
  "income_earned": []
}
```

## Pitfalls & Lessons

### Web Search for Job Listings
- **Do NOT rely on delegate_task for job search** — web search via delegate often returns empty or generic results
- **Do NOT repeatedly re-dispatch the same search** — if 2 attempts fail, give user the direct URLs and data to apply themselves
- Instead: provide platform URLs, user data templates, and let user apply manually
- Job listings rotate hourly on Freelancer/Upwork — category URLs are more stable than individual job URLs

### Platform-Specific Pitfalls
- **DataAnnotation**: Requires PayPal/Wise for payment — user must have or create account
- **Appen**: May require laptop for some tasks; phone works for most
- **Telus**: Needs KTP for verification; underage may have issues
- **Fiverr**: Needs good profile photo; first gig should be cheap to get reviews
- **Upwork**: Needs Connects ($0.15 per bid) — costs money to apply

### Underage Worker Considerations
- Some platforms require 18+ (Upwork, PayPal)
- Workarounds: parent/guardian account, local Indonesian platforms, data annotation (often no age verification)
- Always warn user if platform may have age restrictions

### Payment Setup
- **PayPal**: Most common for international platforms — needs ID verification
- **Wise**: Alternative, sometimes better rates
- **Bank transfer**: Some Indonesian platforms support local bank
- **Crypto**: Some AI platforms pay via crypto

## Daily Action Plan Template

```
Day 1: Setup
- [ ] Create accounts on 2-3 platforms
- [ ] Fill profile with template data
- [ ] Prepare application materials

Day 2-3: Apply
- [ ] Apply to 5+ jobs/gigs
- [ ] Send 3+ outreach messages
- [ ] Check email (including spam)

Day 4-7: Follow up
- [ ] Follow up on applications
- [ ] Apply to more jobs
- [ ] Create Fiverr gig if not done

Week 2+: Iterate
- [ ] Adjust pricing based on response
- [ ] Improve profile/gig descriptions
- [ ] Accept first gig (even cheap) for reviews
```

## Verification

After helping user apply:
- Confirm which platforms they successfully registered on
- Track which applications were submitted
- Set reminder to check email in 3-7 days
- Follow up on any responses received
