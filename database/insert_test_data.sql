USE inventory;

INSERT INTO suppliers (name, location)
VALUES ('Supplier1', 'VA'), ('Supplier2', 'FA');

INSERT INTO parts (name, description)
VALUES ('Bolt', 'Steel bolt'), ('Nut', 'Metal nut');

INSERT INTO supply_xref (supplier_id, part_id, price, lead_time)
VALUES (1,1,5.50,'3 days'), (2,1,5.20,'4 days'), (1,2,2.40,'2 days');