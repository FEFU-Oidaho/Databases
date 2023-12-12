"""
This file describes the main queries that form the structure of the database.
"""
# Table
DRIVERS = """
CREATE TABLE IF NOT EXISTS drivers
    (
        license_number INTEGER PRIMARY KEY NOT NULL UNIQUE,

        full_name VARCHAR(255),
        address TEXT,
        phone_number INTEGER UNIQUE,
        
        CONSTRAINT driver UNIQUE (license_number, phone_number)
    );
"""

CARS = """
CREATE TABLE IF NOT EXISTS cars
    (
        registration_number INTEGER PRIMARY KEY NOT NULL,

        brand VARCHAR(255),
        model VARCHAR(255),
        color VARCHAR(255),
        manufactured_year YEAR,
        registration_date DATE,
        owner_license INTEGER NOT NULL,
        
        FOREIGN KEY (owner_license) REFERENCES drivers(license_number) ON DELETE CASCADE,
        CONSTRAINT car UNIQUE (owner_license, registration_number)
    );
"""

FINE = """
CREATE TABLE IF NOT EXISTS fine
    (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,

        violation_code INTEGER,
        driver_license INTEGER,
        inspector_number INTEGER,
        date DATE,
        time TIME,
        area TEXT,
        payment_state BOOLEAN,
        payment_size FLOAT,
        deprivation_size TINYINT(36),
        
        FOREIGN KEY (violation_code) REFERENCES violations(code) ON DELETE CASCADE,
        FOREIGN KEY (driver_license) REFERENCES drivers(license_number) ON DELETE CASCADE,
        CONSTRAINT car UNIQUE (id)
    );
"""

VIOLATIONS = """
CREATE TABLE IF NOT EXISTS violations
    (
        code INTEGER PRIMARY KEY,

        type VARCHAR(100),
        warn_possibility BOOLEAN,
        payment_diapason VARCHAR(100),
        deprivation_diapason VARCHAR(100),
        
        CONSTRAINT violation UNIQUE (code)
    );
"""

# Table
tables = [DRIVERS, CARS, VIOLATIONS, FINE]
