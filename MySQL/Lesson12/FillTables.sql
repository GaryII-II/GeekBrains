DELETE FROM sample.user_roles;
ALTER TABLE sample.user_roles AUTO_INCREMENT = 1;
INSERT INTO user_roles VALUES
  (DEFAULT, 'su'),
  (DEFAULT, 'admin'),
  (DEFAULT, 'tester');

DELETE FROM sample.projects;
ALTER TABLE sample.projects AUTO_INCREMENT = 1;
INSERT INTO projects VALUES
  (DEFAULT, 'Compatibility Tests'),
  (DEFAULT, 'i18n Tests'),
  (DEFAULT, 'Stress Tests'),
  (DEFAULT, 'Boundary Tests');


DELETE FROM sample.files;
ALTER TABLE sample.files AUTO_INCREMENT = 1;
INSERT INTO files VALUES
  (DEFAULT, '/data/excel/file1.xls', NULL, DEFAULT),
  (DEFAULT, '/data/excel/file2.xls', NULL, DEFAULT),
  (DEFAULT, '/data/img/picture1.jpeg', NULL, DEFAULT),
  (DEFAULT, '/data/img/picture2.jpeg', NULL, DEFAULT),
  (DEFAULT, '/data/img/picture3.jpeg', NULL, DEFAULT),
  (DEFAULT, '/data/img/picture4.jpeg', NULL, DEFAULT),
  (DEFAULT, '/data/scripts/data_load.sql', NULL, DEFAULT);


DELETE FROM sample.units_types;
ALTER TABLE sample.units_types AUTO_INCREMENT = 1;
INSERT INTO units_types VALUES
  (DEFAULT, 'Mobile Messenger'),
  (DEFAULT, 'SNS Service'),
  (DEFAULT, 'Accomodation Service'),
  (DEFAULT, 'Car Rental Service');

DELETE FROM sample.users;
ALTER TABLE sample.users AUTO_INCREMENT = 1;
INSERT INTO users VALUES
  (DEFAULT, 'John Smith', 1),
  (DEFAULT, 'Sergio Morales', 3),
  (DEFAULT, 'Eric Strong', 3),
  (DEFAULT, 'Monic Shlesinger', 3),
  (DEFAULT, 'Sarah Conelli', 2),
  (DEFAULT, 'Jessica Tailor', 2 );

DELETE FROM sample.units;
ALTER TABLE sample.units AUTO_INCREMENT = 1;
INSERT INTO units VALUES
  (DEFAULT, 'Telegram', 1),
  (DEFAULT, 'WhatsUp', 1),
  (DEFAULT, 'Viber', 1),
  (DEFAULT, 'Facebook', 2),
  (DEFAULT, 'VKontakte', 2),
  (DEFAULT, 'Odnoklassniki', 2),
  (DEFAULT, 'Booking', 3),
  (DEFAULT, 'Venere', 3),
  (DEFAULT, 'Trivago', 3),
  (DEFAULT, 'Hotels', 3),
  (DEFAULT, 'Sixt', 4 ),
  (DEFAULT, 'Europcar', 4 ),
  (DEFAULT, 'Budget', 4 ),
  (DEFAULT, 'Avis', 4 );

DELETE FROM sample.schedules;
ALTER TABLE sample.schedules AUTO_INCREMENT = 1;
INSERT INTO schedules VALUES
  (DEFAULT, 'Early Morning', '06:00:00', '07:00:00'),
  (DEFAULT, 'Morning', '08:00:00', '11:00:00'),
  (DEFAULT, 'Noon', '12:00:00', '13:00:00'),
  (DEFAULT, 'Afternoon', '14:00:00', '16:00:00'),
  (DEFAULT, 'Evening', '18:00:00', '20:00:00'),
  (DEFAULT, 'Night', '00:00:00', '01:00:00'),
  (DEFAULT, 'Midnight', '01:00:01', '04:00:00');

DELETE FROM sample.tests;
ALTER TABLE sample.tests AUTO_INCREMENT = 1;
INSERT INTO tests VALUES
  (DEFAULT, 1, 'Compatibility Chat 1', 1, NULL, 3, 'Step1, Step2, Step3'),
  (DEFAULT, 1, 'Compatibility Chat 2', 1, NULL, 3, 'Step21, Step22, Step23'),
  (DEFAULT, 1, 'Compatibility Chat 3', 1, NULL, 3, 'Step31, Step32, Step33'),
  (DEFAULT, 1, 'Compatibility Chat 4', 1, NULL, 3, 'Step41, Step42, Step43'),
  (DEFAULT, 1, 'Compatibility SNS 1', 2, NULL, 4, 'Step1, Step2, Step3'),
  (DEFAULT, 1, 'Compatibility SNS 2', 2, NULL, 4, 'Step21, Step22, Step23'),
  (DEFAULT, 1, 'Compatibility SNS 3', 2, NULL, 4, 'Step31, Step32, Step33'),
  (DEFAULT, 1, 'Compatibility SNS 4', 2, NULL, 4, 'Step41, Step42, Step43'),
  (DEFAULT, 2, 'i18n Stay 1', 3, 1, 1, 'Step1, Step2, Step3'),
  (DEFAULT, 2, 'i18n Stay 2', 3, 2, 1, 'StepA, StepB, StepC'),
  (DEFAULT, 2, 'i18n Stay 3', 3, 2, 1, 'StepAC, StepAB, StepAA'),
  (DEFAULT, 2, 'i18n Car 1', 4, 3, 5, 'Step1, Step2, Step3'),
  (DEFAULT, 2, 'i18n Car 2', 4, NULL, 5, 'StepAA, StepBB, StepCC'),
  (DEFAULT, 2, 'i18n Car 3', 4, 4, 5, 'Step22, Step23, Step24'),
  (DEFAULT, 3, 'Stress Stay 1', 3, NULL, 3, 'Step11, Step12, Step13'),
  (DEFAULT, 3, 'Stress Stay 2', 3, NULL, 3, 'Step221, Step222, Step223'),
  (DEFAULT, 3, 'Stress Stay 3', 3, NULL, 3, 'Step331, Step332, Step333'),
  (DEFAULT, 3, 'Stress Stay 4', 3, NULL, 3, 'Step441, Step442, Step443'),
  (DEFAULT, 3, 'Stress Car 1', 4, 4, 5, 'StepA1, StepA2, StepA3'),
  (DEFAULT, 3, 'Stress Car 2', 4, 5, 5, 'StepB1, StepB2, StepB3'),
  (DEFAULT, 3, 'Stress Car 3', 4, 6, 5, 'StepC1, StepC2, StepC3'),
  (DEFAULT, 2, 'Boundary Stay 1', 3, 3, 3, 'Step1, Step2, Step3'),
  (DEFAULT, 2, 'Boundary Stay 2', 3, 3, 3, 'StepA, StepB, StepC'),
  (DEFAULT, 2, 'Boundary Stay 3', 3, 3, 3, 'StepAC, StepAB, StepAA');


DELETE FROM sample.test_tasks;
ALTER TABLE sample.test_tasks AUTO_INCREMENT = 1;
INSERT INTO test_tasks VALUES
  (DEFAULT, 1, 1, 1, 3, 3),
  (DEFAULT, 2, 1, 1, 3, 3),
  (DEFAULT, 3, 1, 1, 3, 3),  
  (DEFAULT, 4, 1, 1, 1, 3),
  (DEFAULT, 1, 2, 2, 1, 4),
  (DEFAULT, 2, 2, 2, 1, 4),
  (DEFAULT, 3, 2, 2, 1, 4),  
  (DEFAULT, 4, 2, 2, 1, 4),
  (DEFAULT, 9, 7, 5, 5, 2),
  (DEFAULT, 12, 4, 5, 3, 5),
  (DEFAULT, 13, 4, 5, 3, 5),
  (DEFAULT, 14, 4, 5, 3, 5),  
  (DEFAULT, 22, 2, 2, 1, 1),
  (DEFAULT, 23, 2, 2, 1, 1),
  (DEFAULT, 24, 2, 2, 1, 1);  

DELETE FROM sample.tasks_results;
ALTER TABLE sample.tasks_results AUTO_INCREMENT = 1;
INSERT INTO tasks_results VALUES
  (1, 1, 'PASS', '2021-08-21 06:00:05', '2021-08-21 06:21:00'),
  (1, 2, 'PASS', '2021-08-21 06:30:00', '2021-08-21 06:40:10'),
  (1, 3, 'FAIL', '2021-08-21 06:51:21', '2021-08-21 06:59:44'),  
  (2, 1, 'PASS', '2021-08-21 06:01:11', '2021-08-21 06:10:55'),
  (2, 2, 'PASS', '2021-08-21 06:03:22', '2021-08-21 06:09:27'),
  (2, 3, 'PASS', '2021-08-21 06:10:34', '2021-08-21 06:12:44'),  
  (3, 1, 'PASS', '2021-08-21 06:21:11', '2021-08-21 06:30:30'),
  (3, 2, 'PASS', '2021-08-21 06:30:22', '2021-08-21 06:39:01'),
  (3, 3, 'PASS', '2021-08-21 06:42:12', '2021-08-21 06:49:28'),  
  (9, 1, 'FAIL', '2021-08-21 18:00:05', '2021-08-21 18:21:00'),
  (10, 1, 'PASS', '2021-08-21 18:30:00', '2021-08-21 18:40:10'),
  (10, 2, 'PASS', '2021-08-21 18:35:00', '2021-08-21 18:45:10'),
  (11, 1, 'FAIL', '2021-08-21 18:51:21', '2021-08-21 18:59:44'),  
  (12, 1, 'FAIL', '2021-08-21 08:00:05', '2021-08-21 08:21:00'),
  (13, 1, 'PASS', '2021-08-21 08:30:00', '2021-08-21 08:40:10'),
  (14, 1, 'PASS', '2021-08-21 08:51:21', '2021-08-21 08:59:44');  
