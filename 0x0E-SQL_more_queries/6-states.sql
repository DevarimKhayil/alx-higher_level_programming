-- states database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- creates table if not exists
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
