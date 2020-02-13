USE cardo;
SELECT 姓名, SUM(是否計算黑名單) AS "黑名單次數", SUM(CARDO點數) AS "CARDO點數總計", 電子郵件, 聯絡電話, 性別, 身份別, 一級單位, 二級單位, 職稱, 生日 FROM 主資料表 GROUP BY 姓名, 性別, 身份別, 一級單位, 二級單位, 職稱, 電子郵件, 聯絡電話, 生日 ORDER BY 黑名單次數 DESC;
SELECT 姓名, SUM(是否計算黑名單) AS "黑名單次數", SUM(CARDO點數) AS "CARDO點數總計", 電子郵件, 聯絡電話, 性別, 身份別, 一級單位, 二級單位, 職稱, 生日 FROM 主資料表 GROUP BY 姓名, 性別, 身份別, 一級單位, 二級單位, 職稱, 電子郵件, 聯絡電話, 生日 HAVING SUM(是否計算黑名單) >= 5 ORDER BY 黑名單次數 DESC;
SELECT COUNT(DISTINCT(姓名)) FROM 主資料表;