SELECT * FROM code.customers;

UPDATE code.customers SET cityid = NULL;

UPDATE code.customers cu
INNER JOIN code.cities c ON cu.city = c.city
SET cu.cityid = c.cityid;











