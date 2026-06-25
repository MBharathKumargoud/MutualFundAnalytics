create database MutualFundAnalytics;
use MutualFundAnalytics;
  CREATE TABLE dim_fund (
    fund_id INT PRIMARY KEY,
    amfi_code VARCHAR(50),
    fund_name VARCHAR(255),
    category VARCHAR(100)
);

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY,
    full_date DATE,
    day INTEGER,
    month INTEGER,
    quarter INTEGER,
    year INTEGER
);

CREATE TABLE fact_nav (
    nav_id INT PRIMARY KEY,
    fund_id INT,
    date_id INT,
    nav DECIMAL(10,4),
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);   

CREATE TABLE fact_transactions (
    transaction_id INT PRIMARY KEY,
    fund_id INT,
    date_id INT,
    investor_id INT,
    transaction_type VARCHAR(50),
    amount DECIMAL(15,2),
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE fact_performance (
    performance_id INT PRIMARY KEY,
    fund_id INT,
    return_1y DECIMAL(10,2),
    return_3y DECIMAL(10,2),
    return_5y DECIMAL(10,2),
    expense_ratio DECIMAL(5,2),
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id)
);

CREATE TABLE fact_aum (
    aum_id INT PRIMARY KEY,
    fund_id INT,
    date_id INT,
    aum DECIMAL(18,2),
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);
