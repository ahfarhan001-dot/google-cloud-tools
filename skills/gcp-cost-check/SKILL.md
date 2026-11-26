---
name: gcp-cost-check
description: A checklist for reviewing Google Cloud spend — find the biggest services, spot idle resources, set budget alerts, and know what to ask before paying. Use when the user asks about a Google Cloud bill, or before turning on a new paid service.
---

# GCP Cost Check

Find out where Google Cloud money is going before the bill surprises you. Check, don't guess.

## How to work

1. **Find the biggest services.** In the Cloud Console, open Billing and list the top 3 services by cost for the current month. Name each one with its amount — no rounding away the small ones.
2. **Look for idle resources.** Check for these common money-wasters:
   - Compute Engine VMs that are running but doing nothing
   - Disks attached to deleted VMs
   - Old snapshots nobody restores from
   - Load balancers with no traffic
   - Cloud SQL instances nobody queries
3. **Check the free tier.** Say clearly which parts of the bill are inside the free tier and which are paid — the free tier hides inside the bill, it doesn't remove it.
4. **Set budget alerts.** Recommend a budget alert at 50%, 80%, and 100% of what the user expects to spend, and say exactly where to set it: Billing → Budgets & alerts.
5. **End with three questions to ask before paying for anything new:**
   - What happens to the bill if this runs for a full month, not just a day?
   - Is there a smaller machine or a cheaper region that does the same job?
   - Can it be turned off automatically when nobody uses it?

## Output format

- A short table: service, this month's cost, and whether it is expected or a surprise.
- A list of idle resources found, with the cost each one adds.
- The budget alert recommendation, with the exact amounts.
- The three questions, in plain words.

## Rules

- Never guess a price. If a number is not in the billing page, say "not shown" and say where to find it.
- Never tell the user to delete something without asking first — deleting the wrong disk or snapshot can lose data.
- If the user is on the free trial, say so, and say when the trial ends and what starts being charged after that.
- Keep every recommendation tied to something the user can check themselves in the console.
