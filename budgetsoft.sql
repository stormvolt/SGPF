-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-05-2018 a las 19:21:29
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

CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `buscar_ingresos` (IN `my_user` VARCHAR(20), IN `fecha_ini` DATE, IN `fecha_fin` DATE)  READS SQL DATA
SELECT
	monto, fecha, descripcion
        FROM
            usuarios
            INNER JOIN ingresos
            ON usuarios.id = ingresos.id_usuario 
        WHERE
            usuario=my_user AND fecha BETWEEN fecha_ini AND fecha_fin$$

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
-- Estructura de tabla para la tabla `categorias`
--

CREATE TABLE `categorias` (
  `id` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `categorias`
--

INSERT INTO `categorias` (`id`, `nombre`) VALUES
(1, 'Alimentos'),
(2, 'Transporte'),
(3, 'Casa'),
(4, 'Cuentas y pagos'),
(5, 'Ropa'),
(6, 'Salud'),
(7, 'Entretenimiento'),
(8, 'Higiene'),
(9, 'Otros');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gastos`
--

CREATE TABLE `gastos` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_categoria` int(11) NOT NULL,
  `monto` double NOT NULL,
  `fecha` date NOT NULL,
  `descripcion` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ingresos`
--

CREATE TABLE `ingresos` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `monto` double NOT NULL,
  `fecha` date NOT NULL,
  `descripcion` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `ingresos`
--

INSERT INTO `ingresos` (`id`, `id_usuario`, `monto`, `fecha`, `descripcion`) VALUES
(1, 1, 1500, '2018-05-01', 'sueldo'),
(2, 1, 100, '2018-05-10', 'bingo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `metas`
--

CREATE TABLE `metas` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `monto` double NOT NULL,
  `inicio` date NOT NULL,
  `final` date NOT NULL,
  `descripcion` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
-- Indices de la tabla `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `gastos`
--
ALTER TABLE `gastos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_categoria` (`id_categoria`);

--
-- Indices de la tabla `ingresos`
--
ALTER TABLE `ingresos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indices de la tabla `metas`
--
ALTER TABLE `metas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `categorias`
--
ALTER TABLE `categorias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT de la tabla `gastos`
--
ALTER TABLE `gastos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `ingresos`
--
ALTER TABLE `ingresos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT de la tabla `metas`
--
ALTER TABLE `metas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `gastos`
--
ALTER TABLE `gastos`
  ADD CONSTRAINT `gastos_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`),
  ADD CONSTRAINT `gastos_ibfk_2` FOREIGN KEY (`id_categoria`) REFERENCES `categorias` (`id`);

--
-- Filtros para la tabla `ingresos`
--
ALTER TABLE `ingresos`
  ADD CONSTRAINT `ingresos_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`);

--
-- Filtros para la tabla `metas`
--
ALTER TABLE `metas`
  ADD CONSTRAINT `metas_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;