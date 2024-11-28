CREATE TABLE phonebook (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(200) NOT NULL,
    last_name VARCHAR(200) NOT NULL,
    username VARCHAR(200) UNIQUE NOT NULL,
    phone_number VARCHAR(200) NOT NULL
);
