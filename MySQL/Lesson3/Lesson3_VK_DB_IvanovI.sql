-- MySQL Script generated by MySQL Workbench
-- Mon Aug  2 21:31:44 2021
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema vk
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema vk
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `vk` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `vk` ;

-- -----------------------------------------------------
-- Table `vk`.`media_type`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `vk`.`media_type` ;

CREATE TABLE IF NOT EXISTS `vk`.`media_type` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `vk`.`media`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `vk`.`media` ;

CREATE TABLE IF NOT EXISTS `vk`.`media` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `media_type_id` INT UNSIGNED NOT NULL,
  `user_id` INT UNSIGNED NOT NULL,
  `url` VARCHAR(45) NULL DEFAULT NULL COMMENT '/files/image/2021/12312dassdas123/12.jpg',
  `blob` BLOB NULL DEFAULT NULL,
  `metadata` JSON NULL DEFAULT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_media_media_type1_idx` (`media_type_id` ASC) VISIBLE,
  INDEX `fk_media_profile1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_media_media_type1`
    FOREIGN KEY (`media_type_id`)
    REFERENCES `vk`.`media_type` (`id`),
  CONSTRAINT `fk_media_profile1`
    FOREIGN KEY (`user_id`)
    REFERENCES `vk`.`profile` (`user_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `vk`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `vk`.`user` ;

CREATE TABLE IF NOT EXISTS `vk`.`user` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(245) NOT NULL,
  `phone` BIGINT NOT NULL,
  `password_hash` CHAR(65) NULL DEFAULT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `deleted_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  UNIQUE INDEX `phone_UNIQUE` (`phone` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `vk`.`profile`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `vk`.`profile` ;

CREATE TABLE IF NOT EXISTS `vk`.`profile` (
  `user_id` INT UNSIGNED NOT NULL,
  `firstname` VARCHAR(245) NOT NULL,
  `lastname` VARCHAR(245) NOT NULL,
  `gender` ENUM('m', 'f', 'x') NOT NULL,
  `birthday` DATE NOT NULL,
  `address` VARCHAR(245) NULL DEFAULT NULL,
  `media_id` INT UNSIGNED NULL DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  INDEX `user_name` (`lastname` ASC, `firstname` ASC) VISIBLE,
  INDEX `fk_profile_media1_idx` (`media_id` ASC) VISIBLE,
  CONSTRAINT `fk_profile_media1`
    FOREIGN KEY (`media_id`)
    REFERENCES `vk`.`media` (`id`),
  CONSTRAINT `fk_profile_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `vk`.`user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `vk`.`community`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `vk`.`community` ;

CREATE TABLE IF NOT EXISTS `vk`.`community` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `admin_user_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE,
  INDEX `fk_community_profile1_idx` (`admin_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_community_profile1`
    FOREIGN KEY (`admin_user_id`)
    REFERENCES `vk`.`profile` (`user_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `vk`.`friendship_request`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `vk`.`friendship_request` ;

CREATE TABLE IF NOT EXISTS `vk`.`friendship_request` (
  `from_user_id` INT UNSIGNED NOT NULL,
  `to_user_id` INT UNSIGNED NOT NULL,
  `status` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '-1 - отклонён\\n0 - запрос\\n1 - дружба',
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`from_user_id`, `to_user_id`),
  INDEX `fk_friendship_request_profile1_idx` (`from_user_id` ASC) VISIBLE,
  INDEX `fk_friendship_request_profile2_idx` (`to_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_friendship_request_profile1`
    FOREIGN KEY (`from_user_id`)
    REFERENCES `vk`.`profile` (`user_id`),
  CONSTRAINT `fk_friendship_request_profile2`
    FOREIGN KEY (`to_user_id`)
    REFERENCES `vk`.`profile` (`user_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `vk`.`likes_media`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `vk`.`likes_media` ;

CREATE TABLE IF NOT EXISTS `vk`.`likes_media` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `like_type` TINYINT(1) NOT NULL DEFAULT '1',
  `user_from_id` INT UNSIGNED NOT NULL,
  `media_id` INT UNSIGNED NOT NULL,
  `added_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_on` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_likes_user_from_idx` (`user_from_id` ASC) VISIBLE,
  INDEX `fk_likes_media_idx` (`media_id` ASC) VISIBLE,
  CONSTRAINT `fk_likes_media`
    FOREIGN KEY (`media_id`)
    REFERENCES `vk`.`media` (`id`),
  CONSTRAINT `fk_likes_media_user_from`
    FOREIGN KEY (`user_from_id`)
    REFERENCES `vk`.`profile` (`user_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `vk`.`post`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `vk`.`post` ;

CREATE TABLE IF NOT EXISTS `vk`.`post` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id` INT UNSIGNED NOT NULL,
  `community_id` INT UNSIGNED NULL DEFAULT NULL,
  `post_id` INT UNSIGNED NULL DEFAULT NULL,
  `text` TEXT NULL DEFAULT NULL,
  `media_id` INT UNSIGNED NULL DEFAULT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_post_profile1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_post_community1_idx` (`community_id` ASC) VISIBLE,
  INDEX `fk_post_post1_idx` (`post_id` ASC) VISIBLE,
  INDEX `fk_post_media1_idx` (`media_id` ASC) VISIBLE,
  CONSTRAINT `fk_post_community1`
    FOREIGN KEY (`community_id`)
    REFERENCES `vk`.`community` (`id`),
  CONSTRAINT `fk_post_media1`
    FOREIGN KEY (`media_id`)
    REFERENCES `vk`.`media` (`id`),
  CONSTRAINT `fk_post_post1`
    FOREIGN KEY (`post_id`)
    REFERENCES `vk`.`post` (`id`),
  CONSTRAINT `fk_post_profile1`
    FOREIGN KEY (`user_id`)
    REFERENCES `vk`.`profile` (`user_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `vk`.`likes_post`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `vk`.`likes_post` ;

CREATE TABLE IF NOT EXISTS `vk`.`likes_post` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `like_type` TINYINT(1) NOT NULL DEFAULT '1',
  `user_from_id` INT UNSIGNED NOT NULL,
  `post_id` INT UNSIGNED NOT NULL,
  `added_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_on` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_likes_user_from_idx` (`user_from_id` ASC) VISIBLE,
  INDEX `fk_likes_post_idx` (`post_id` ASC) VISIBLE,
  CONSTRAINT `fk_likes_post`
    FOREIGN KEY (`post_id`)
    REFERENCES `vk`.`post` (`id`),
  CONSTRAINT `fk_likes_post_user_from`
    FOREIGN KEY (`user_from_id`)
    REFERENCES `vk`.`profile` (`user_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `vk`.`likes_user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `vk`.`likes_user` ;

CREATE TABLE IF NOT EXISTS `vk`.`likes_user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `like_type` TINYINT(1) NOT NULL DEFAULT '1',
  `user_from_id` INT UNSIGNED NOT NULL,
  `user_to_id` INT UNSIGNED NOT NULL,
  `added_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_on` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_likes_user_from_idx` (`user_from_id` ASC) VISIBLE,
  INDEX `fk_likes_user_to_idx` (`user_to_id` ASC) VISIBLE,
  CONSTRAINT `fk_likes_user_from`
    FOREIGN KEY (`user_from_id`)
    REFERENCES `vk`.`profile` (`user_id`),
  CONSTRAINT `fk_likes_user_to`
    FOREIGN KEY (`user_to_id`)
    REFERENCES `vk`.`profile` (`user_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `vk`.`message`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `vk`.`message` ;

CREATE TABLE IF NOT EXISTS `vk`.`message` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `from_user_id` INT UNSIGNED NOT NULL,
  `to_user_id` INT UNSIGNED NOT NULL,
  `text` TEXT NULL DEFAULT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `read_at` DATETIME NULL DEFAULT NULL,
  `deleted_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_message_profile1_idx` (`from_user_id` ASC) VISIBLE,
  INDEX `fk_message_profile2_idx` (`to_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_message_profile1`
    FOREIGN KEY (`from_user_id`)
    REFERENCES `vk`.`profile` (`user_id`),
  CONSTRAINT `fk_message_profile2`
    FOREIGN KEY (`to_user_id`)
    REFERENCES `vk`.`profile` (`user_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `vk`.`user_community`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `vk`.`user_community` ;

CREATE TABLE IF NOT EXISTS `vk`.`user_community` (
  `community_id` INT UNSIGNED NOT NULL,
  `user_id` INT UNSIGNED NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`community_id`, `user_id`),
  INDEX `fk_community_has_profile_profile1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_community_has_profile_community1_idx` (`community_id` ASC) VISIBLE,
  CONSTRAINT `fk_community_has_profile_community1`
    FOREIGN KEY (`community_id`)
    REFERENCES `vk`.`community` (`id`),
  CONSTRAINT `fk_community_has_profile_profile1`
    FOREIGN KEY (`user_id`)
    REFERENCES `vk`.`profile` (`user_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
