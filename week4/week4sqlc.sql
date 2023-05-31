/* DATA ANALYITCS */
SELECT count(*) FROM code.employees;
/* tabloda kac tane record var */

/* Statistics ! */
SELECT sum(quantityOrdered) FROM orderdetails;

SELECT * FROM orderdetails LIMIT 3;

/*
SUM, MAX, COUNT ==> aggregation function
*/
SELECT sum(quantityOrdered), max(quantityOrdered) FROM orderdetails;

SELECT max(quantityOrdered) FROM orderdetails;
SELECT sum(quantityOrdered) FROM orderdetails;


SELECT AVG(quantityOrdered) FROM orderdetails;
SELECT SUM(quantityOrdered) / COUNT(quantityOrdered) FROM orderdetails;

/* COMPANY NE KADAR KAZANDI !!! TOPLAM */
SELECT sum(quantityOrdered * priceEach) FROM orderdetails;

SELECT productCode, quantityOrdered, priceEach, quantityOrdered * priceEach as Total 
FROM orderdetails;

/*HER BIR PRODUCT TAN KACAR TANE SATILMIS*/

SELECT productCode,  SUM(quantityOrdered*priceEach)
FROM orderdetails
GROUP BY productCode
ORDER BY 2 DESC
LIMIT 10;
/* Bize en cok pul kazandiran, 5 tane producti goster */
/* GROUP !! paketle, kumelendir, cluster et */

/*
select [column], aggregation
from table
group by [colum]
*/



SELECT SUM(quantityOrdered)
FROM orderdetails;



/* EN POPULER CUSTOMER KIM, BIZI EN COK SEVEN */
SELECT customerNumber, COUNT(*) 
FROM code.orders 
GROUP BY customerNumber
ORDER BY 2 DESC
LIMIT 10;




/* EN COK SATINALMA PURCHASING YAPAN 10 CUSTOMERI GOSTER*/
SELECT c.customerNumber, c.customerName, COUNT(*)
FROM code.orders o
INNER JOIN code.customers c ON c.customerNumber = o.customerNumber
GROUP BY c.customerNumber, c.customerName
ORDER BY 3 DESC
LIMIT 10;

/*
SELECT [columns]
FROM [table];
*/

/* HER IL KACAR TANE SATIS YAPTIK?, BUSINESS ANALYST */
SELECT YEAR(orderDate), MONTH(orderDate), COUNT(*) FROM orders
GROUP BY YEAR(orderDate), MONTH(orderDate);


/* gun olarak sirala */
SELECT DAY(orderDate), COUNT(*) FROM orders
GROUP BY DAY(orderDate)
ORDER BY 1;

/* adet count olarak sirala */
SELECT DAY(orderDate), COUNT(*) FROM orders
GROUP BY DAY(orderDate)
ORDER BY 2 DESC;






SELECT od.orderNumber, SUM( quantityOrdered * priceEach )
FROM orderdetails od
GROUP BY od.orderNumber
ORDER BY 2 DESC
LIMIT 10;



/*
priceEach = 20.5 ==> 20
quantity = 10    x 10 = 200
20.5 x 10 = round(205) = 205
*/

SELECT MONTH(o.orderDate), ROUND(SUM( quantityOrdered * priceEach )/1000)
FROM orderdetails od
INNER JOIN orders o ON o.orderNumber = od.orderNumber
WHERE quantityOrdered IS NOT NULL AND priceEach IS NOT NULL
GROUP BY MONTH(o.orderDate)
ORDER BY 1;



SELECT *, ISNULL(comments) FROM orders;



SELECT * FROM orders
WHERE ISNULL(comments) != 1;


SELECT * FROM orders
WHERE ISNULL(shippeddate) != 1;

SELECT orderDate,
	case MONTH(orderDate)
		when 1 THEN 'WINTER'
		when 2 THEN 'WINTER'
		when 3 THEN 'WINTER'
		when 4 THEN 'SPRING'
		when 5 THEN 'SPRING'
  		when 6 THEN 'SPRING'
  		when 7 THEN 'SUMMER'
  		when 8 THEN 'SUMMER'
  		when 9 THEN 'SUMMER'
  		when 10 THEN 'AUTUMN'
  		when 11 THEN 'AUTUMN'
  		when 12 THEN 'AUTUMN'
	end as season
FROM orders;

/*
GENDER = 1/0
GENDER = 1 ==> MALE
GENDER = 0 ==> FEMALE

SELECT CASE GENDER 
WHEN 1 THEN 'MALE'
WHEN 2 THEN 'FEMALE'
END
*/


/* DISTINCT = UNIQUE = YEK / YEGANE / TEK */
SELECT DISTINCT status FROM code.orders;
SELECT DISTINCT country FROM customers;

CREATE TABLE cities
SELECT DISTINCT city FROM customers;



