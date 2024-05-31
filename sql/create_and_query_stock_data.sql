-- Create table for stock data
CREATE TABLE stock_data (
    Date DATE PRIMARY KEY,
    Open FLOAT,
    High FLOAT,
    Low FLOAT,
    Close FLOAT,
    Volume INT
);

-- Insert data into stock_data table (Replace as needed)
INSERT INTO stock_data (Date, Open, High, Low, Close, Volume) VALUES 
('2024-01-01', 100.0, 105.0, 95.0, 102.0, 10000),
('2024-01-02', 102.0, 110.0, 101.0, 108.0, 15000),
-- Add more rows as necessary
;

-- Query to select data for analysis
SELECT 
    Date,
    Open,
    High,
    Low,
    Close,
    Volume,
    EXTRACT(DAY FROM Date) AS Day,
    EXTRACT(MONTH FROM Date) AS Month,
    EXTRACT(YEAR FROM Date) AS Year
FROM 
    stock_data;
