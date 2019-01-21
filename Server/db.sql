DROP SCHEMA [IF EXISTS] paytm_inventory_db;

CREATE DATABASE paytm_inventory_db;

CREATE TABLE `paytm_inventory_db`.`productItem` (
`ItemId` INT NOT NULL AUTO_INCREMENT,
`name` VARCHAR(45) NOT NULL,
`brand` VARCHAR(45) NOT NULL,
`category` VARCHAR(45) NOT NULL,
`product_code` VARCHAR(45) NOT NULL,
PRIMARY KEY (`ItemId`));

CREATE TABLE `paytm_inventory_db`.`variantItem` (
`variantId` INT NOT NULL AUTO_INCREMENT,
`name` number (45) NOT NULL,
`quantity` VARCHAR(45) NOT NULL,
`properties` JSON NOT NULL,
`cost_price` DECIMAL(10, 2) NOT NULL,
`selling_price` DECIMAL(10, 2) NOT NULL,
PRIMARY KEY (`variantId`),
FOREIGN KEY (ItemId) REFERENCES productItem(ItemId)
);

INSERT INTO `paytm_inventory_db`.`productItem`(
    `name` ,
    `brand` ,
    `category` ,
    `product_code`
)
VALUES(
    'Iphone' ,
    'Apple' ,
    'Mobile' ,
    '1'
);

INSERT INTO `paytm_inventory_db`.`variantItem`(
    `name` ,
    `quantity` ,
    `properties` ,
    `cost_price`,
    `selling_price`,
    `ItemId`
)
VALUES(
    '16 GB' ,
    '1' ,
    '{"memory": "16 GB", "color": "black"}' ,
    12.1,
    13.2,
    1
);
