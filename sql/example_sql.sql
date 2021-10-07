-- Databricks notebook source

SELECT
    a.account_id,
    MAX(a.month) AS final_month
FROM schema.table1 AS a
INNER JOIN schema.table2
USING (account_id)
WHERE a.dt BETWEEN '2020-01-01' AND '2021-01-01'
GROUP BY 1
ORDER BY 2 DESC;
