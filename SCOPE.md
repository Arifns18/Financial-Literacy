# Project Scope — Financial Literacy Website

## 1. Project Setup

Flask app factory pattern, organised folder structure (`/templates`, `/static`), Tailwind CSS integrated via CDN or CLI build, and a base layout template (`base.html`) that all pages extend.

## 2. Home / Landing Page

Hero section introducing the site's mission. Navigation cards linking to Theory and Practicality sections. Clear entry points for each topic area (Budgeting & Saving, Investing, Debt & Credit).

## 3. Theory: Budgeting & Saving

Explanatory pages covering:
- Budgeting methods: 50/30/20 rule, zero-based budgeting
- Savings strategies: pay-yourself-first, high-yield savings accounts
- Emergency fund guidance: how much to save and where to keep it

## 4. Theory: Investing

Educational content covering:
- Asset types: stocks, bonds, ETFs, index funds
- Compound interest and the time value of money
- Risk tolerance and how to assess it
- Portfolio diversification principles

## 5. Theory: Debt & Credit

Content covering:
- How credit scores are calculated and why they matter
- Types of debt: secured vs unsecured, revolving vs instalment
- How interest accrues on different debt types
- Repayment strategies: debt avalanche vs debt snowball

## 6. Practicality: Budgeting Tools

- **Budget Planner** — Input income and categorised expenses to see a breakdown
- **Savings Goal Calculator** — Calculate how long to reach a savings target given monthly contributions and interest rate

## 7. Practicality: Investment Tools

- **Compound Interest Calculator** — Project investment growth over time with configurable rate and contribution frequency
- **ROI Estimator** — Calculate return on investment given initial cost and final value
- **Investment Growth Visualiser** — Chart showing portfolio value over time

## 8. Practicality: Debt Tools

- **Loan Repayment Calculator** — Monthly payment, total interest, and payoff date for any loan
- **Debt Payoff Timeline** — Side-by-side avalanche vs snowball comparison for a list of debts
- **Credit Utilisation Checker** — Input credit limits and balances to see utilisation ratio and score impact guidance

## 9. UI/UX & Responsive Design

- Mobile-first layout built with Tailwind CSS utility classes
- Consistent navigation bar and footer on all pages
- Topic cards on the landing page with icons and descriptions
- Readable typography with appropriate heading hierarchy and line lengths
- Accessible colour contrast and focus states

## 10. Glossary & Resources

- **Glossary** — Searchable list of financial terms with plain-English definitions (client-side filter)
- **Resources** — Curated external links organised by topic (Budgeting, Investing, Debt & Credit), opening in a new tab
