USE cardo;
SELECT 姓名, SUM(是否計算黑名單) FROM 主資料表 GROUP BY 姓名;
SELECT COUNT(DISTINCT(姓名)) FROM 主資料表;