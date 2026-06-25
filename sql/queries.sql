-- 1. Top 5 Funds by AUM
SELECT * FROM aum ORDER BY aum DESC LIMIT 5;

-- 2. Average NAV
SELECT AVG(nav) AS average_nav FROM nav_processed;

-- 3. Total SIP Amount
SELECT SUM(amount) AS total_sip_amount FROM investor_transactions WHERE transaction_type='SIP';

-- 4. Transactions by State
SELECT state, COUNT(*) AS total_transactions FROM investor_transactions GROUP BY state;

-- 5. Funds with Expense Ratio Less Than 1%
SELECT * FROM scheme_performance WHERE expense_ratio < 1;

-- 6. Fund Transactions with 1-Year Return (JOIN)
SELECT it.fund_id, it.transaction_type, it.amount, sp.return_1y FROM investor_transactions it JOIN scheme_performance sp ON it.fund_id=sp.fund_id;

-- 7. Fund AUM with 5-Year Return (JOIN)
SELECT a.fund_id, a.aum, sp.return_5y FROM aum a JOIN scheme_performance sp ON a.fund_id=sp.fund_id ORDER BY a.aum DESC;

-- 8. Fund Transactions with AUM (JOIN)
SELECT it.fund_id, it.amount, a.aum FROM investor_transactions it JOIN aum a ON it.fund_id=a.fund_id;

-- 9. Fund Performance with Expense Ratio and AUM (JOIN)
SELECT sp.fund_id, sp.return_1y, sp.expense_ratio, a.aum FROM scheme_performance sp JOIN aum a ON sp.fund_id=a.fund_id;

-- 10. Maximum and Minimum NAV
SELECT MAX(nav) AS maximum_nav, MIN(nav) AS minimum_nav FROM nav_processed;