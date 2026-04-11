SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| reethika           |
| sys                |
+--------------------+
5 rows in set (0.01 sec)

mysql> CREATE DATABASE medicine_tracker;
Query OK, 1 row affected (0.01 sec)

mysql> USE medicine_tracker;
Database changed
mysql> CREATE TABLE Users (
    ->     user_id INT AUTO_INCREMENT PRIMARY KEY,
    ->     name VARCHAR(100) NOT NULL,
    ->     email VARCHAR(100) UNIQUE NOT NULL,
    ->     password VARCHAR(200) NOT NULL,
    ->     phone VARCHAR(15),
    ->     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    -> );
Query OK, 0 rows affected (0.04 sec)

mysql> CREATE TABLE Categories (
    ->     category_id INT AUTO_INCREMENT PRIMARY KEY,
    ->     name VARCHAR(50) NOT NULL
    -> );
Query OK, 0 rows affected (0.02 sec)

mysql>
mysql> -- Insert default categories
mysql> INSERT INTO Categories (name) VALUES
    -> ('Tablet'), ('Syrup'), ('Injection'), ('Ointment'), ('Drops');
Query OK, 5 rows affected (0.00 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> CREATE TABLE FamilyMembers (
    ->     member_id INT AUTO_INCREMENT PRIMARY KEY,
    ->     user_id INT NOT NULL,
    ->     name VARCHAR(100) NOT NULL,
    ->     age INT,
    ->     relation VARCHAR(50),
    ->     FOREIGN KEY (user_id) REFERENCES Users(user_id)
    ->         ON DELETE CASCADE
    -> );
Query OK, 0 rows affected (0.06 sec)

mysql> CREATE TABLE Medicines (
    ->     medicine_id INT AUTO_INCREMENT PRIMARY KEY,
    ->     user_id INT NOT NULL,
    ->     member_id INT NOT NULL,
    ->     category_id INT NOT NULL,
    ->     name VARCHAR(100) NOT NULL,
    ->     quantity INT DEFAULT 1,
    ->     purchase_date DATE,
    ->     expiry_date DATE NOT NULL,
    ->     status VARCHAR(20) DEFAULT 'active',
    ->     FOREIGN KEY (user_id) REFERENCES Users(user_id)
    ->         ON DELETE CASCADE,
    ->     FOREIGN KEY (member_id) REFERENCES FamilyMembers(member_id)
    ->         ON DELETE CASCADE,
    ->     FOREIGN KEY (category_id) REFERENCES Categories(category_id)
    -> );
Query OK, 0 rows affected (0.05 sec)

mysql> CREATE TABLE Alerts (
    ->     alert_id INT AUTO_INCREMENT PRIMARY KEY,
    ->     medicine_id INT NOT NULL,
    ->     user_id INT NOT NULL,
    ->     alert_type VARCHAR(50),
    ->     sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ->     is_read BOOLEAN DEFAULT FALSE,
    ->     FOREIGN KEY (medicine_id) REFERENCES Medicines(medicine_id)
    ->         ON DELETE CASCADE,
    ->     FOREIGN KEY (user_id) REFERENCES Users(user_id)
    ->         ON DELETE CASCADE
    -> );
Query OK, 0 rows affected (0.05 sec)

mysql> SHOW TABLES;
+----------------------------+
| Tables_in_medicine_tracker |
+----------------------------+
| alerts                     |
| categories                 |
| familymembers              |
| medicines                  |
| users                      |
+----------------------------+
5 rows in set (0.00 sec)

mysql> DESC Users;
+------------+--------------+------+-----+-------------------+-------------------+
| Field      | Type         | Null | Key | Default           | Extra             |
+------------+--------------+------+-----+-------------------+-------------------+
| user_id    | int          | NO   | PRI | NULL              | auto_increment    |
| name       | varchar(100) | NO   |     | NULL              |                   |
| email      | varchar(100) | NO   | UNI | NULL              |                   |
| password   | varchar(200) | NO   |     | NULL              |                   |
| phone      | varchar(15)  | YES  |     | NULL              |                   |
| created_at | timestamp    | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+------------+--------------+------+-----+-------------------+-------------------+
6 rows in set (0.01 sec)

mysql> DESC Categories;
+-------------+-------------+------+-----+---------+----------------+
| Field       | Type        | Null | Key | Default | Extra          |
+-------------+-------------+------+-----+---------+----------------+
| category_id | int         | NO   | PRI | NULL    | auto_increment |
| name        | varchar(50) | NO   |     | NULL    |                |
+-------------+-------------+------+-----+---------+----------------+
2 rows in set (0.00 sec)

mysql> DESC FamilyMembers;
+-----------+--------------+------+-----+---------+----------------+
| Field     | Type         | Null | Key | Default | Extra          |
+-----------+--------------+------+-----+---------+----------------+
| member_id | int          | NO   | PRI | NULL    | auto_increment |
| user_id   | int          | NO   | MUL | NULL    |                |
| name      | varchar(100) | NO   |     | NULL    |                |
| age       | int          | YES  |     | NULL    |                |
| relation  | varchar(50)  | YES  |     | NULL    |                |
+-----------+--------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)

mysql> DESC Medicines;
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| medicine_id   | int          | NO   | PRI | NULL    | auto_increment |
| user_id       | int          | NO   | MUL | NULL    |                |
| member_id     | int          | NO   | MUL | NULL    |                |
| category_id   | int          | NO   | MUL | NULL    |                |
| name          | varchar(100) | NO   |     | NULL    |                |
| quantity      | int          | YES  |     | 1       |                |
| purchase_date | date         | YES  |     | NULL    |                |
| expiry_date   | date         | NO   |     | NULL    |                |
| status        | varchar(20)  | YES  |     | active  |                |
+---------------+--------------+------+-----+---------+----------------+
9 rows in set (0.00 sec)

mysql> DESC Alerts;
+-------------+-------------+------+-----+-------------------+-------------------+
| Field       | Type        | Null | Key | Default           | Extra             |
+-------------+-------------+------+-----+-------------------+-------------------+
| alert_id    | int         | NO   | PRI | NULL              | auto_increment    |
| medicine_id | int         | NO   | MUL | NULL              |                   |
| user_id     | int         | NO   | MUL | NULL              |                   |
| alert_type  | varchar(50) | YES  |     | NULL              |                   |
| sent_at     | timestamp   | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| is_read     | tinyint(1)  | YES  |     | 0                 |                   |
+-------------+-------------+------+-----+-------------------+-------------------+
6 rows in set (0.00 sec)

mysql> INSERT INTO Users (name, email, password, phone) VALUES
    -> ('Rahul Kumar', 'rahul@gmail.com', '1234', '9876543210'),
    -> ('Anita Sharma', 'anita@gmail.com', 'abcd', '9123456780'),
    -> ('Vikram Singh', 'vikram@gmail.com', 'pass123', '9988776655'),
    -> ('Priya Mehta', 'priya@gmail.com', 'secure', '9876501234'),
    -> ('Arjun Patel', 'arjun@gmail.com', 'mypwd', '9812345678'),
    -> ('Sneha Rao', 'sneha@gmail.com', 'hello123', '9123987654'),
    -> ('Ravi Verma', 'ravi@gmail.com', 'testpwd', '9001122334'),
    -> ('Kiran Das', 'kiran@gmail.com', 'pass999', '9112233445'),
    -> ('Meena Joshi', 'meena@gmail.com', 'meena321', '9223344556'),
    -> ('Suresh Nair', 'suresh@gmail.com', 'sureshpwd', '9334455667');
Query OK, 10 rows affected (0.01 sec)
Records: 10  Duplicates: 0  Warnings: 0

mysql> INSERT INTO FamilyMembers (user_id, name, age, relation) VALUES
    -> (1, 'Mom', 55, 'Mother'),
    -> (1, 'Dad', 58, 'Father'),
    -> (2, 'Child', 12, 'Son'),
    -> (2, 'Spouse', 35, 'Wife'),
    -> (3, 'Brother', 25, 'Brother'),
    -> (3, 'Sister', 22, 'Sister'),
    -> (4, 'Grandfather', 70, 'Grandfather'),
    -> (5, 'Grandmother', 68, 'Grandmother'),
    -> (6, 'Self', 30, 'Self'),
    -> (7, 'Daughter', 18, 'Daughter');
Query OK, 10 rows affected (0.00 sec)
Records: 10  Duplicates: 0  Warnings: 0

mysql> INSERT INTO Medicines
    -> (user_id, member_id, category_id, name, quantity, purchase_date, expiry_date) VALUES
    -> (1, 1, 1, 'Dolo 650', 10, '2025-01-01', '2025-03-01'),   -- expired
    -> (1, 2, 1, 'Metformin', 30, '2025-01-01', '2025-04-20'), -- expires in <30 days
    -> (2, 3, 2, 'Cough Syrup', 1, '2026-03-01', '2026-04-25'),-- expires in <30 days
    -> (2, 4, 3, 'Insulin', 5, '2026-03-15', '2026-05-15'),    -- future
    -> (3, 5, 1, 'Paracetamol', 15, '2026-01-10', '2026-06-01'), -- future
    -> (3, 6, 2, 'Vitamin Syrup', 2, '2026-02-01', '2026-04-01'), -- expired
    -> (4, 7, 4, 'Skin Ointment', 1, '2026-03-01', '2026-04-10'), -- expires in <30 days
    -> (5, 8, 5, 'Eye Drops', 2, '2026-03-20', '2026-07-01'),   -- future
    -> (6, 9, 1, 'Amoxicillin', 20, '2026-03-01', '2026-03-25'), -- expired
    -> (7, 10, 2, 'Iron Syrup', 1, '2026-03-15', '2026-04-15'); -- expires in <30 days
Query OK, 10 rows affected (0.01 sec)
Records: 10  Duplicates: 0  Warnings: 0

mysql> INSERT INTO Alerts (medicine_id, user_id, alert_type, is_read) VALUES
    -> (1, 1, 'Expiry Reminder', FALSE),
    -> (2, 1, 'Expiry Reminder', TRUE),
    -> (3, 2, 'Expiry Reminder', FALSE),
    -> (4, 2, 'Stock Low', FALSE),
    -> (5, 3, 'Expiry Reminder', TRUE),
    -> (6, 3, 'Expiry Reminder', FALSE),
    -> (7, 4, 'Expiry Reminder', FALSE),
    -> (8, 5, 'Stock Low', TRUE),
    -> (9, 6, 'Expiry Reminder', FALSE),
    -> (10, 7, 'Expiry Reminder', TRUE);
Query OK, 10 rows affected (0.01 sec)
Records: 10  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM Users;
+---------+--------------+------------------+-----------+------------+---------------------+
| user_id | name         | email            | password  | phone      | created_at          |
+---------+--------------+------------------+-----------+------------+---------------------+
|       1 | Rahul Kumar  | rahul@gmail.com  | 1234      | 9876543210 | 2026-04-05 17:41:29 |
|       2 | Anita Sharma | anita@gmail.com  | abcd      | 9123456780 | 2026-04-05 17:41:29 |
|       3 | Vikram Singh | vikram@gmail.com | pass123   | 9988776655 | 2026-04-05 17:41:29 |
|       4 | Priya Mehta  | priya@gmail.com  | secure    | 9876501234 | 2026-04-05 17:41:29 |
|       5 | Arjun Patel  | arjun@gmail.com  | mypwd     | 9812345678 | 2026-04-05 17:41:29 |
|       6 | Sneha Rao    | sneha@gmail.com  | hello123  | 9123987654 | 2026-04-05 17:41:29 |
|       7 | Ravi Verma   | ravi@gmail.com   | testpwd   | 9001122334 | 2026-04-05 17:41:29 |
|       8 | Kiran Das    | kiran@gmail.com  | pass999   | 9112233445 | 2026-04-05 17:41:29 |
|       9 | Meena Joshi  | meena@gmail.com  | meena321  | 9223344556 | 2026-04-05 17:41:29 |
|      10 | Suresh Nair  | suresh@gmail.com | sureshpwd | 9334455667 | 2026-04-05 17:41:29 |
+---------+--------------+------------------+-----------+------------+---------------------+
10 rows in set (0.00 sec)

mysql> SELECT * FROM Categories;
+-------------+-----------+
| category_id | name      |
+-------------+-----------+
|           1 | Tablet    |
|           2 | Syrup     |
|           3 | Injection |
|           4 | Ointment  |
|           5 | Drops     |
+-------------+-----------+
5 rows in set (0.00 sec)

mysql> SELECT * FROM FamilyMembers;
+-----------+---------+-------------+------+-------------+
| member_id | user_id | name        | age  | relation    |
+-----------+---------+-------------+------+-------------+
|         1 |       1 | Mom         |   55 | Mother      |
|         2 |       1 | Dad         |   58 | Father      |
|         3 |       2 | Child       |   12 | Son         |
|         4 |       2 | Spouse      |   35 | Wife        |
|         5 |       3 | Brother     |   25 | Brother     |
|         6 |       3 | Sister      |   22 | Sister      |
|         7 |       4 | Grandfather |   70 | Grandfather |
|         8 |       5 | Grandmother |   68 | Grandmother |
|         9 |       6 | Self        |   30 | Self        |
|        10 |       7 | Daughter    |   18 | Daughter    |
+-----------+---------+-------------+------+-------------+
10 rows in set (0.00 sec)

mysql> SELECT * FROM Medicines;
+-------------+---------+-----------+-------------+---------------+----------+---------------+-------------+--------+
| medicine_id | user_id | member_id | category_id | name          | quantity | purchase_date | expiry_date | status |
+-------------+---------+-----------+-------------+---------------+----------+---------------+-------------+--------+
|           1 |       1 |         1 |           1 | Dolo 650      |       10 | 2025-01-01    | 2025-03-01  | active |
|           2 |       1 |         2 |           1 | Metformin     |       30 | 2025-01-01    | 2025-04-20  | active |
|           3 |       2 |         3 |           2 | Cough Syrup   |        1 | 2026-03-01    | 2026-04-25  | active |
|           4 |       2 |         4 |           3 | Insulin       |        5 | 2026-03-15    | 2026-05-15  | active |
|           5 |       3 |         5 |           1 | Paracetamol   |       15 | 2026-01-10    | 2026-06-01  | active |
|           6 |       3 |         6 |           2 | Vitamin Syrup |        2 | 2026-02-01    | 2026-04-01  | active |
|           7 |       4 |         7 |           4 | Skin Ointment |        1 | 2026-03-01    | 2026-04-10  | active |
|           8 |       5 |         8 |           5 | Eye Drops     |        2 | 2026-03-20    | 2026-07-01  | active |
|           9 |       6 |         9 |           1 | Amoxicillin   |       20 | 2026-03-01    | 2026-03-25  | active |
|          10 |       7 |        10 |           2 | Iron Syrup    |        1 | 2026-03-15    | 2026-04-15  | active |
+-------------+---------+-----------+-------------+---------------+----------+---------------+-------------+--------+
10 rows in set (0.00 sec)

mysql> SELECT * FROM Alerts;
+----------+-------------+---------+-----------------+---------------------+---------+
| alert_id | medicine_id | user_id | alert_type      | sent_at             | is_read |
+----------+-------------+---------+-----------------+---------------------+---------+
|        1 |           1 |       1 | Expiry Reminder | 2026-04-05 17:42:10 |       0 |
|        2 |           2 |       1 | Expiry Reminder | 2026-04-05 17:42:10 |       1 |
|        3 |           3 |       2 | Expiry Reminder | 2026-04-05 17:42:10 |       0 |
|        4 |           4 |       2 | Stock Low       | 2026-04-05 17:42:10 |       0 |
|        5 |           5 |       3 | Expiry Reminder | 2026-04-05 17:42:10 |       1 |
|        6 |           6 |       3 | Expiry Reminder | 2026-04-05 17:42:10 |       0 |
|        7 |           7 |       4 | Expiry Reminder | 2026-04-05 17:42:10 |       0 |
|        8 |           8 |       5 | Stock Low       | 2026-04-05 17:42:10 |       1 |
|        9 |           9 |       6 | Expiry Reminder | 2026-04-05 17:42:10 |       0 |
|       10 |          10 |       7 | Expiry Reminder | 2026-04-05 17:42:10 |       1 |
+----------+-------------+---------+-----------------+---------------------+---------+
10 rows in set (0.00 sec)

mysql> SELECT m.name AS Medicine, f.name AS Member,
    ->        c.name AS Category, m.expiry_date, m.status
    -> FROM Medicines m
    -> JOIN FamilyMembers f ON m.member_id = f.member_id
    -> JOIN Categories c ON m.category_id = c.category_id
    -> WHERE m.user_id = 1;
+-----------+--------+----------+-------------+--------+
| Medicine  | Member | Category | expiry_date | status |
+-----------+--------+----------+-------------+--------+
| Dolo 650  | Mom    | Tablet   | 2025-03-01  | active |
| Metformin | Dad    | Tablet   | 2025-04-20  | active |
+-----------+--------+----------+-------------+--------+
2 rows in set (0.00 sec)

mysql> SELECT m.name, f.name AS Member, m.expiry_date,
    ->        DATEDIFF(m.expiry_date, CURDATE()) AS days_left
    -> FROM Medicines m
    -> JOIN FamilyMembers f ON m.member_id = f.member_id
    -> WHERE m.expiry_date BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 30 DAY);
+---------------+-------------+-------------+-----------+
| name          | Member      | expiry_date | days_left |
+---------------+-------------+-------------+-----------+
| Cough Syrup   | Child       | 2026-04-25  |        20 |
| Skin Ointment | Grandfather | 2026-04-10  |         5 |
| Iron Syrup    | Daughter    | 2026-04-15  |        10 |
+---------------+-------------+-------------+-----------+
3 rows in set (0.00 sec)

mysql> SELECT m.name, f.name AS Member,
    ->        m.expiry_date AS expired_on
    -> FROM Medicines m
    -> JOIN FamilyMembers f ON m.member_id = f.member_id
    -> WHERE m.expiry_date < CURDATE();
+---------------+--------+------------+
| name          | Member | expired_on |
+---------------+--------+------------+
| Dolo 650      | Mom    | 2025-03-01 |
| Metformin     | Dad    | 2025-04-20 |
| Vitamin Syrup | Sister | 2026-04-01 |
| Amoxicillin   | Self   | 2026-03-25 |
+---------------+--------+------------+
4 rows in set (0.00 sec)

mysql> SELECT c.name AS Category,
    ->        COUNT(*) AS Total_Medicines
    -> FROM Medicines m
    -> JOIN Categories c ON m.category_id = c.category_id
    -> GROUP BY c.name;
+-----------+-----------------+
| Category  | Total_Medicines |
+-----------+-----------------+
| Tablet    |               4 |
| Syrup     |               3 |
| Injection |               1 |
| Ointment  |               1 |
| Drops     |               1 |
+-----------+-----------------+
5 rows in set (0.00 sec)

mysql> SELECT f.name AS Member,
    ->        COUNT(*) AS Total_Medicines
    -> FROM Medicines m
    -> JOIN FamilyMembers f ON m.member_id = f.member_id
    -> GROUP BY f.name
    -> ORDER BY Total_Medicines DESC;
+-------------+-----------------+
| Member      | Total_Medicines |
+-------------+-----------------+
| Mom         |               1 |
| Dad         |               1 |
| Child       |               1 |
| Spouse      |               1 |
| Brother     |               1 |
| Sister      |               1 |
| Grandfather |               1 |
| Grandmother |               1 |
| Self        |               1 |
| Daughter    |               1 |
+-------------+-----------------+
10 rows in set (0.00 sec)
