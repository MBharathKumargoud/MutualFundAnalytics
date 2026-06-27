create database MutualFundAnalytics;
use MutualFundAnalytics;
  CREATE TABLE dim_fund (
    fund_id INT PRIMARY KEY,
    amfi_code VARCHAR(50),
    fund_name VARCHAR(255),
    category VARCHAR(100)
);
DESC dim_fund;
CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY,
    full_date DATE,
    day INTEGER,
    month INTEGER,
    quarter INTEGER,
    year INTEGER
);
DESC dim_date; 
CREATE TABLE fact_nav (
    nav_id INT PRIMARY KEY,
    fund_id INT,
    date_id INT,
    nav DECIMAL(10,4),
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);   

SELECT COUNT(*) FROM investor_transactions;

SELECT COUNT(*) FROM scheme_performance;

SELECT COUNT(*) FROM aum;

SELECT COUNT(*) FROM nav_PROCESSED;

DESCRIBE investor_transactions;
DESCRIBE scheme_performance;
DESCRIBE aum;
DESCRIBE nav_processed;