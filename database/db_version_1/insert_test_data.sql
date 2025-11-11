SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

-- SQL DDL Statements go here ...
USE inventory;

INSERT INTO suppliers (name, location)
VALUES
	('Acme Fasteners', 'NY'),
	('Global Parts Co.', 'CA'),
	('Metro Hardware', 'TX'),
	('Prime Components', 'IL'),
	('Northstar Supply', 'FL'),
	('Eastern Industrial', 'MA'),
	('Western Tools', 'WA'),
	('Midwest Fabrication', 'OH'),
	('Southern Machines', 'GA'),
	('Precision Parts Ltd.', 'MI'),
	('Allied Components', 'NJ'),
	('Value Supplies', 'PA'),
	('QuickSource', 'CO'),
	('Engineered Solutions', 'MN'),
	('Cornerstone Hardware', 'OR');

INSERT INTO parts (name, description)
VALUES
	('Bolt', 'Hex head steel bolt, M8 x 30mm'),
	('Nut', 'M8 hex nut, zinc plated'),
	('Washer', 'Flat steel washer, 8mm ID'),
	('Screw', 'Phillips-head screw, #6 x 1/2"'),
	('Bracket', 'Mounting bracket, zinc plated'),
	('Gasket', 'Rubber gasket, 2mm thick'),
	('Bearing', 'Ball bearing, 6001 series'),
	('Seal', 'Oil seal, 25x47x7'),
	('Pulley', 'Timing pulley, 20T'),
	('Shaft', 'Hardened steel shaft, 12mm dia'),
	('Pin', 'Dowel pin, 4mm x 20mm'),
	('Rivet', 'Solid rivet, 3.2mm'),
	('Spacer', 'Aluminum spacer, 10mm'),
	('Spring', 'Compression spring, 20mm free length'),
	('Clip', 'Retaining clip, stainless steel');

INSERT INTO supply_xref (supplier_id, part_id, price, lead_time)
VALUES
	(1,1,5.50,'3 days'),
	(2,1,5.20,'4 days'),
	(1,2,2.40,'2 days'),
	(3,3,0.15,'1 day'),
	(3,4,0.55,'3 days'),
	(4,5,7.80,'5 days'),
	(4,7,12.50,'7 days'),
	(5,6,1.10,'4 days'),
	(5,4,0.45,'2 days'),
	(6,7,11.90,'6 days'),
	(7,3,0.16,'1 day'),
	(7,5,7.50,'5 days'),
	(8,8,3.25,'2 days'),
	(9,9,18.75,'7 days'),
	(10,10,24.00,'10 days'),
	(11,11,0.75,'3 days'),
	(12,12,0.30,'5 days'),
	(13,13,1.95,'4 days'),
	(14,14,2.50,'6 days'),
	(15,15,0.60,'2 days'),
	(2,5,8.10,'5 days'),
	(6,1,5.40,'4 days'),
	(8,3,0.14,'2 days'),
	(9,7,11.50,'8 days'),
	(10,2,2.60,'6 days');


COMMIT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;