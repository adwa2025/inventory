-- START MYSQL
-- mysql -u root


-- SHOW ALL TABLES
USE inventory;
SHOW TABLES;

-- SELECT ALL FROM SUPPLIERS
SELECT * FROM suppliers;

-- SELECT ALL FROM PART
SELECT * FROM parts;

-- SELECT ALL FROM supply_xref;
SELECT * FROM supply_xref;

-- SELECT A SPECIFIC SUPPLIER
SELECT * FROM suppliers WHERE name = 'Metro Hardware';
SELECT * FROM suppliers WHERE location = 'IL';
    
-- SHOW PART WITH THEIR SUPPLIERS
SELECT s.name AS Supplier, p.name AS Part, x.price, x.lead_time
    FROM suppliers s, parts p, supply_xref x
    WHERE x.supplier_id = s.id AND X.part_id = p.id;
-- SELECT SUPPLIER NAME AS (SHOWEN NAME)
    -- FROM 3 TABLES SUPPLEIRS S(CODE FOR THE TABLE NAME)
    -- 