TASK1
======================
DROP TABLE IF EXISTS logs;
CREATE TABLE lesson4.logs (
  created_at DATETIME COMMENT 'Дата создания записи',
  table_name VARCHAR(255) COMMENT 'Название таблицы',
  pk_id BIGINT COMMENT 'Primary key id',
  obj_name VARCHAR(255) COMMENT 'Added object name'
) COMMENT = 'Логгирование добавления' ENGINE=Archive;


DELIMITER $$
DROP TRIGGER IF EXISTS catalogs_logger $$
CREATE TRIGGER catalogs_logger AFTER INSERT ON catalogs
FOR EACH ROW
BEGIN
    INSERT INTO lesson4.logs (created_at, table_name, pk_id, obj_name)
      VALUE (NOW(), 'catalogs', NEW.id, NEW.name);
END$$

DROP TRIGGER IF EXISTS products_logger $$
CREATE TRIGGER products_logger AFTER INSERT ON products
FOR EACH ROW
BEGIN
    INSERT INTO lesson4.logs (created_at, table_name, pk_id, obj_name)
      VALUE (NOW(), 'products', NEW.id, NEW.name);
END$$

DELIMITER ;

INSERT INTO catalogs (name)
VALUE ('New goods1');

INSERT INTO products (name, description, price, catalog_id)
VALUE ('Antivirus', 'Software product', 3800, 2);


