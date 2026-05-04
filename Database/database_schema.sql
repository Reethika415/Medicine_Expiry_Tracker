CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(200) NOT NULL,
    phone VARCHAR(15),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

INSERT INTO Categories (name) VALUES
('Tablet'), ('Syrup'), ('Injection'), ('Ointment'), ('Drops');

CREATE TABLE FamilyMembers (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    age INT,
    relation VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
        ON DELETE CASCADE
);

CREATE TABLE Medicines (
    medicine_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    member_id INT NOT NULL,
    category_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    quantity INT DEFAULT 1,
    purchase_date DATE,
    expiry_date DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'active',
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (member_id) REFERENCES FamilyMembers(member_id),
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

CREATE TABLE Alerts (
    alert_id INT AUTO_INCREMENT PRIMARY KEY,
    medicine_id INT NOT NULL,
    user_id INT NOT NULL,
    alert_type VARCHAR(50),
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_read BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (medicine_id) REFERENCES Medicines(medicine_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- 🔹 Insert one user (required for foreign key)
INSERT INTO Users (name, email, password, phone) VALUES
('Likitha', 'likitha@gmail.com', '123456', '9876543210');

-- 🔹 Insert family members (THIS FIXES YOUR DROPDOWN ISSUE)
INSERT INTO FamilyMembers (user_id, name, age, relation) VALUES
(1, 'Likitha', 21, 'Self'),
(1, 'Shruthika', 19, 'Sister'),
(1, 'Reethika', 40, 'Mother'),
(1, 'Monika', 45, 'Aunt');
