
# CONSTANT
# CONFIG
# OPTION
# SETTING

QUERIES = {
    "cities": "SELECT * FROM cities LIMIT 0, 5;",
    "customers": 
        """
            SELECT customerNumber, customerName, cityid 
            FROM customers 
            LIMIT 0, 5;
        """,
    "customersinfo": 
        """
            SELECT customerNumber, customerName, cityid 
            FROM customers 
            WHERE customerNumber = %s
            LIMIT 0, 1;
        """,
    "mostbuyingcompanies":
    """
SELECT c.customerNumber, c.customerName, COUNT(*) as cnt
FROM code.orders o
INNER JOIN code.customers c ON c.customerNumber = o.customerNumber
GROUP BY c.customerNumber, c.customerName
ORDER BY 3 DESC
LIMIT 10;
    """
}

# QUERY TEMPLATE
# The queries which are called inside a program/python may have parameters!! = params as %s


TRAIN_RATIO, TEST_RATIO = 0.80, 0.20


