# Mutual Fund Analytics - Data Dictionary

## Database

- Database Name: bluestock_mf.db
- Database Type: SQLite

---

## Table: nav_processed

| Column | Data Type | Description |
|---------|-----------|-------------|
| date | TEXT | NAV Date |
| nav | DOUBLE | Net Asset Value |

---

## Table: investor_transactions

| Column | Data Type | Description |
|---------|-----------|-------------|
| transaction_id | INT | Unique Transaction ID |
| fund_id | INT | Mutual Fund ID |
| transaction_date | TEXT | Transaction Date |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount | INT | Transaction Amount |
| kyc_status | TEXT | KYC Verification Status |
| state | TEXT | Investor State |

---

## Table: scheme_performance

| Column | Data Type | Description |
|---------|-----------|-------------|
| fund_id | INT | Mutual Fund ID |
| return_1y | DOUBLE | 1-Year Return (%) |
| return_3y | DOUBLE | 3-Year Return (%) |
| return_5y | DOUBLE | 5-Year Return (%) |
| expense_ratio | DOUBLE | Expense Ratio (%) |

---

## Table: aum

| Column | Data Type | Description |
|---------|-----------|-------------|
| aum_id | INT | AUM Record ID |
| fund_id | INT | Mutual Fund ID |
| date | TEXT | AUM Date |
| aum | INT | Assets Under Management |