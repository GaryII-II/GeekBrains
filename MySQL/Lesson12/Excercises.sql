1. SELECT JOIN
============================================================
SELECT test_tasks.id, from_tests.name as Test, from_units.name AS TestedUnit, from_users.name AS Tester, steps FROM test_tasks
JOIN tests AS from_tests ON test_tasks.id_test = from_tests.id
JOIN units AS from_units ON test_tasks.id_unit = from_units.id
JOIN users AS from_users ON test_tasks.id_tester = from_users.id
LIMIT 5;


Result
--------------
# id	Test			TestedUnit	Tester		steps
------------------------------------------------------------------------
1	Compatibility Chat 1	Telegram	Eric Strong	3
2	Compatibility Chat 2	Telegram	Eric Strong	3
3	Compatibility Chat 3	Telegram	Eric Strong	3
4	Compatibility Chat 4	Telegram	Eric Strong	1
5	Compatibility Chat 1	WhatsUp	Monic Shlesinger	1


2. NESTED SELECT, GROUP, COUNT
=============================================================
SELECT tasks_results.result as TestResult, COUNT(tasks_results.result) AS Total FROM tasks_results
WHERE task_id IN (
    SELECT test_tasks.id FROM test_tasks WHERE test_tasks.id = tasks_results.task_id
)
GROUP BY tasks_results.result WITH ROLLUP
ORDER BY Total ASC;

Result
----------------
# TestResult	Total
---------------------
ONGO		1
FAIL		4
PASS		12
Null		17


SELECT tasks_results.result as TestResult, COUNT(tasks_results.result) AS Total FROM tasks_results
WHERE task_id IN (
    SELECT test_tasks.id FROM test_tasks WHERE test_tasks.id = tasks_results.task_id
)
GROUP BY tasks_results.result HAVING TestResult <> 'ONGO'
ORDER BY Total ASC;

Result
----------------
# TestResult	Total
---------------------
FAIL		4
PASS		12


3. VIEW JOIN
==================================================================
CREATE OR REPLACE VIEW CategorizedTests (Project, Test)
AS SELECT pjt.name AS Project, tests.name AS Test FROM tests
JOIN projects AS pjt ON tests.id_project = pjt.id;

SELECT * from CategorizedTests;

Result
----------------------
# Project		Test
----------------------------------------------
# Project	Test
Compatibility Tests	Compatibility Chat 1
Compatibility Tests	Compatibility Chat 2
Compatibility Tests	Compatibility Chat 3
Compatibility Tests	Compatibility Chat 4
Compatibility Tests	Compatibility SNS 1
Compatibility Tests	Compatibility SNS 2
Compatibility Tests	Compatibility SNS 3
Compatibility Tests	Compatibility SNS 4
........