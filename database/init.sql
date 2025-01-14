\c ml;

CREATE TABLE IF NOT EXISTS predictions (
    id SERIAL PRIMARY KEY,
    seniority INTEGER,
    home VARCHAR(50),
    time INTEGER,
    age INTEGER,
    marital VARCHAR(50),
    records VARCHAR(5),
    job VARCHAR(50),
    expenses FLOAT,
    income FLOAT,
    assets FLOAT,
    debt FLOAT,
    amount FLOAT,
    price FLOAT,
    probability FLOAT,
    prediction FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
); 