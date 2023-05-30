
select * from orders;
select * from orderdetails;
select * from products;

/*import numpy as np
pythondaki classlarin elemanlarina ulasmak icin "." kullaniriz, aynisi
*/
/* JOIN !!! */

SELECT p.productName, od.quantityOrdered 
FROM orders o, orderdetails od, products p
WHERE o.orderNumber = od.orderNumber
AND od.productCode = p.productCode
AND o.orderNumber = 10102;



SELECT 
	c.customerName AS customer, 
	p.productName AS Maşin, 
	od.quantityOrdered AS adet, 
    p.productDescription AS description,
    o.status AS vəziyyət
FROM orders o
INNER JOIN orderdetails od ON o.orderNumber = od.orderNumber
INNER JOIN products p ON od.productCode = p.productCode
INNER JOIN customers c ON c.customerNumber = o.customerNumber
WHERE o.orderNumber = 10103;



SELECT firstname, birthdate, year(now()) - year(birthdate) AS Age, '' as Burc FROM code.Nefer
WHERE MONTH(NOW()) = MONTH(birthdate)
AND DAY(NOW()) = DAY(birthdate);

