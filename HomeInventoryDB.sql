-- creating user with full access
CREATE USER 'marker'@'localhost' IDENTIFIED BY 'securepassword';
GRANT ALL PRIVILEGES ON inventory_system.* TO 'marker'@'localhost';
FLUSH PRIVILEGES;

CREATE DATABASE inventory_system;
USE inventory_system;

-- USER TABLE
CREATE TABLE User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
    );
    
-- INVENTORY TABLE
CREATE TABLE Inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_updated DATETIME,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- ITEM TABLE
CREATE TABLE Item (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    inventory_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    purchase_price DECIMAL(10, 2),
    current_value DECIMAL(10, 2),
    purchase_date DATE,
    serial_no VARCHAR(255),
    item_condition VARCHAR(255),
    location VARCHAR(255),
    FOREIGN KEY (inventory_id) REFERENCES Inventory(inventory_id)
);

-- CATEGORY TABLE
CREATE TABLE Category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    description TEXT,
    colour VARCHAR(255)
);

-- ITEM_CATEGORY 
CREATE TABLE Item_Category (
    item_id INT NOT NULL,
    category_id INT NOT NULL,
    assigned_date DATE,
    PRIMARY KEY (item_id, category_id),
    FOREIGN KEY (item_id) REFERENCES Item(item_id),
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
);

-- TAG TABLE
CREATE TABLE Tag (
    tag_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    colour VARCHAR(255)
);

-- ITEM_TAG (JUNCTION TABLE)
CREATE TABLE Item_Tag (
    item_id INT NOT NULL,
    tag_id INT NOT NULL,
    assigned_date DATE,
    PRIMARY KEY (item_id, tag_id),
    FOREIGN KEY (item_id) REFERENCES Item(item_id),
    FOREIGN KEY (tag_id) REFERENCES Tag(tag_id)
);

-- REPORT TABLE
CREATE TABLE Report (
    report_id INT AUTO_INCREMENT PRIMARY KEY,
    inventory_id INT NOT NULL,
    report_type VARCHAR(255),
    generated_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    file_name VARCHAR(255),
    total_value DECIMAL(12,2),
    FOREIGN KEY (inventory_id) REFERENCES Inventory(inventory_id)
);

-- IMAGE TABLE
CREATE TABLE Image (
    image_id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT NOT NULL,
    file_name VARCHAR(255),
    file_path VARCHAR(255),
    file_size INT,
    upload_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (item_id) REFERENCES Item(item_id)
);

-- USERS
INSERT INTO User (username, email, password_hash) VALUES
('sjones', 'sjones@email.com', 'abc123'),
('tlee', 'tlee@email.com', 'def456');

-- INVENTORY
INSERT INTO Inventory (user_id, name, description) VALUES
(1, 'Office Inventory', 'All office equipment'),
(2, 'Photography Gear', 'Cameras and lenses');

-- ITEMS
INSERT INTO Item (inventory_id, name, description, purchase_price, current_value, purchase_date, serial_no, item_condition, location)
VALUES
(1, 'Dell Laptop', 'Work laptop', 1200, 800, '2023-01-12', 'DL12345', 'Good', 'Office'),
(2, 'Canon EOS 90D', 'Main camera', 1500, 1200, '2022-07-05', 'CN90D', 'Excellent', 'Studio');

-- CATEGORIES
INSERT INTO Category (name, description, colour)
VALUES ('Electronics', 'Electronic devices', 'Blue'),
       ('Cameras', 'Camera equipment', 'Black');
       
-- ITEM_CATEGORY
INSERT INTO Item_Category VALUES
(1, 1, '2023-03-01'),
(2, 2, '2023-04-15');

