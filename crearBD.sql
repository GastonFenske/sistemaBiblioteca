-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema biblioteca_base
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema biblioteca_base
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `biblioteca_base` DEFAULT CHARACTER SET utf8 ;
USE `biblioteca_base` ;

-- -----------------------------------------------------
-- Table `biblioteca_base`.`libros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca_base`.`libros` (
  `idlibro` INT NOT NULL AUTO_INCREMENT,
  `nombre_libro` VARCHAR(45) NOT NULL,
  `autor` VARCHAR(45) NOT NULL,
  `año_libro` VARCHAR(45) NOT NULL,
  `cantidad_paginas_libro` INT(8) NOT NULL,
  `disponibilidad_libro` TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`idlibro`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biblioteca_base`.`clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca_base`.`clientes` (
  `idcliente` INT NOT NULL AUTO_INCREMENT,
  `nombre_cliente` VARCHAR(45) NOT NULL,
  `apellido_cliente` VARCHAR(45) NOT NULL,
  `dni_cliente` INT(8) NOT NULL,
  `direccion` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idcliente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biblioteca_base`.`asignaciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca_base`.`asignaciones` (
  `idasignacione` INT NOT NULL AUTO_INCREMENT,
  `fecha` VARCHAR(45) NOT NULL,
  `libro_idlibro` INT NOT NULL,
  `cliente_idcliente` INT NOT NULL,
  PRIMARY KEY (`idasignacione`),
  INDEX `fk_asignaciones_libros_idx` (`libro_idlibro` ASC) VISIBLE,
  INDEX `fk_asignaciones_clientes1_idx` (`cliente_idcliente` ASC) VISIBLE,
  CONSTRAINT `fk_asignaciones_libros`
    FOREIGN KEY (`libro_idlibro`)
    REFERENCES `biblioteca_base`.`libros` (`idlibro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_asignaciones_clientes1`
    FOREIGN KEY (`cliente_idcliente`)
    REFERENCES `biblioteca_base`.`clientes` (`idcliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
