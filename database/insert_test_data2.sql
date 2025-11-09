USE inventory;

INSERT INTO suppliers (name, location)
VALUES
	('Acme Fasteners','NY'),
	('Global Parts Co.','CA'),
	('Metro Hardware','TX'),
	('Prime Components','IL'),
	('Northstar Supply','FL');

INSERT INTO parts (name, description)
VALUES
	('Washer','Flat steel washer'),
	('Screw','Phillips-head screw'),
	('Bracket','Mounting bracket, zinc plated'),
	('Gasket','Rubber gasket, 2mm'),
	('Bearing','Ball bearing, 6001 series');

INSERT INTO supply_xref (supplier_id, part_id, price, lead_time)
VALUES
	(3,3,0.15,'1 day'),
	(3,4,0.55,'3 days'),
	(4,5,7.80,'5 days'),
	(4,7,12.50,'7 days'),
	(5,6,1.10,'4 days'),
	(5,4,0.45,'2 days'),
	(6,7,11.90,'6 days'),
	(7,3,0.16,'1 day'),
	(7,5,7.50,'5 days');