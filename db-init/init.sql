-- Créer le tableau Users
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    email VARCHAR(80) NOT NULL
);

-- Créer des enregistrements dans Users
INSERT INTO users (name, email) VALUES
('Ada Lovelace', 'alovelace@example.com'),
('Adele Goldberg', 'agoldberg@example.com'),
('Alan Turing', 'aturing@example.com');

-- Créer le tableau Products
CREATE TABLE IF NOT EXISTS Products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    brand VARCHAR(20) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- Créer des enregistrements dans Products
INSERT INTO Products (name, brand) VALUES
('Bag', 'Bentley'),
('Watch', 'Rolex'),
('Car', 'Alfa Romeo');

Select users.name, Products.name,Product.brand
FROM users
JOIN Products
ON users.id = Products.id

-- Agregation en Mongo en commentaire tant que emplacement dans projet non déterminé.
/*
db.users.aggregate([
    {
        $lookup: {
            from: "Products",
            localField: "name",
            foreignField: "name","brand",
            as: "achat"
        }
    }
]);
*/