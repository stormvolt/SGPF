-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 02-05-2018 a las 04:12:41
-- Versión del servidor: 10.1.10-MariaDB
-- Versión de PHP: 5.6.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `budgetsoft`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `buscar_datos` (IN `my_user` VARCHAR(20))  READS SQL DATA
SELECT
id, usuario, DES_DECRYPT(password), nombre, email
        FROM
            usuarios
        WHERE
            usuario=my_user$$

CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `insertar_usuario` (IN `my_user` VARCHAR(20), IN `my_pass` VARCHAR(20), IN `my_name` VARCHAR(50), IN `my_email` VARCHAR(50))  MODIFIES SQL DATA
INSERT INTO usuarios
(id,usuario,password,nombre,email)
VALUES (null,
        my_user,
        DES_ENCRYPT(my_pass),
        my_name,
        my_email)$$

CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `modificar_datos` (IN `my_user` VARCHAR(20), IN `my_pass` VARCHAR(20), IN `my_name` VARCHAR(50), IN `my_email` VARCHAR(50))  MODIFIES SQL DATA
UPDATE usuarios
SET password=DES_ENCRYPT(my_pass), nombre=my_name, email=my_email
WHERE usuario=my_user$$

CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `verificar_inicio_sesion` (IN `my_user` VARCHAR(20), IN `my_pass` VARCHAR(20), OUT `resultado` BOOLEAN)  READS SQL DATA
    DETERMINISTIC
BEGIN

   DECLARE num_rows INT;
        SELECT COUNT(id) INTO num_rows
        FROM
            usuarios
        WHERE
            usuario=my_user AND password=DES_ENCRYPT(my_pass);
			
	IF num_rows = 1 THEN
      SET resultado = True;

   ELSE
      SET resultado = False;

   END IF;
   
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(7) NOT NULL,
  `usuario` varchar(20) NOT NULL,
  `password` varchar(20) CHARACTER SET latin1 COLLATE latin1_bin NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `usuario`, `password`, `nombre`, `email`) VALUES
(1, 'user1', '€Xç>w\nðìa', 'Carlos Diaz', 'carlin@gmail.com');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
