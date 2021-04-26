--
-- File generated with SQLiteStudio v3.3.2 on Fri Apr 23 15:56:40 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: foods
CREATE TABLE foods (name STRING NOT NULL, description VARCHAR (250) NOT NULL, quantity INTEGER NOT NULL, orgNumber INTEGER REFERENCES restaurants (orgNumber) NOT NULL, foodId INTEGER PRIMARY KEY NOT NULL UNIQUE);

-- Table: foods_orders
CREATE TABLE foods_orders (foodId INTEGER REFERENCES foods (foodId) NOT NULL, orderId INTEGER REFERENCES orders (orderId) NOT NULL);

-- Table: orders
CREATE TABLE orders (orderId INTEGER PRIMARY KEY NOT NULL UNIQUE, description VARCHAR (250) NOT NULL, pickupTime DATETIME NOT NULL, orgNumber INTEGER REFERENCES organizations (orgNumber) NOT NULL);

-- Table: organizations
CREATE TABLE organizations (orgNumber INTEGER PRIMARY KEY NOT NULL UNIQUE, name VARCHAR (70) NOT NULL, location VARCHAR (250) NOT NULL, phone VARCHAR (12) UNIQUE NOT NULL, userName VARCHAR (25) UNIQUE NOT NULL, password CHAR (11) NOT NULL);

-- Table: restaurants
CREATE TABLE restaurants (orgNumber INTEGER PRIMARY KEY NOT NULL UNIQUE, name VARCHAR (70) NOT NULL, location VARCHAR (250) NOT NULL, phone VARCHAR (12) NOT NULL UNIQUE, userName VARCHAR (25) UNIQUE NOT NULL, password CHAR (11) NOT NULL);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
