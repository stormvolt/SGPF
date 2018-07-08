-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-07-2018 a las 21:58:10
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
CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `agregarGasto` (IN `user_id` INT(11), `my_monto` DOUBLE, IN `cat_id` INT(11), IN `my_fecha` DATE, IN `descrip` VARCHAR(50))  MODIFIES SQL DATA
INSERT INTO gastos
(id,id_usuario,id_categoria,monto,fecha,descripcion)
VALUES (null,
        user_id,
        cat_id,
        my_monto,
        my_fecha,
        descrip)$$

CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `agregarIngreso` (IN `user_id` INT(11), IN `my_monto` DOUBLE, IN `my_fecha` DATE, IN `descrip` VARCHAR(50))  MODIFIES SQL DATA
INSERT INTO ingresos
(id,id_usuario,monto,fecha,descripcion)
VALUES (null,
        user_id,
        my_monto,
        my_fecha,
        descrip)$$

CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `agregarMeta` (IN `user_id` INT(11), IN `my_nombre` VARCHAR(20), IN `my_monto` DOUBLE, IN `fecha_ini` DATE, IN `fecha_fin` DATE)  MODIFIES SQL DATA
INSERT INTO metas
(id,id_usuario,nombre,monto,inicio,final)
VALUES (null,
        user_id,
        my_nombre,
        my_monto,
        fecha_ini,
        fecha_fin)$$

CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `agregarUsuario` (IN `my_user` VARCHAR(20), IN `my_pass` VARCHAR(20), IN `my_name` VARCHAR(50), IN `my_email` VARCHAR(50))  MODIFIES SQL DATA
INSERT INTO usuarios
(id,usuario,password,nombre,email)
VALUES (null,
        my_user,
        DES_ENCRYPT(my_pass),
        my_name,
        my_email)$$

CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `borrarGasto` (IN `id_gasto` INT(11))  MODIFIES SQL DATA
DELETE FROM gastos
WHERE id = id_gasto$$

CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `borrarIngreso` (IN `id_ingreso` INT(11))  MODIFIES SQL DATA
DELETE FROM ingresos
WHERE id = id_ingreso$$

CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `borrarMeta` (IN `id_meta` INT(11))  MODIFIES SQL DATA
DELETE FROM metas
WHERE id = id_meta$$

CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `cargarMetas` (IN `user_id` INT(11))  READS SQL DATA
SELECT
	id, nombre, monto, inicio, final
        FROM
            metas
        WHERE
            id_usuario=user_id 
        ORDER BY inicio ASC$$

CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `ingresar` (IN `my_user` VARCHAR(20), IN `my_pass` VARCHAR(20), OUT `resultado` BOOLEAN)  READS SQL DATA
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

CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `modificarDatos` (IN `my_user` VARCHAR(20), IN `my_pass` VARCHAR(20), IN `my_name` VARCHAR(50), IN `my_email` VARCHAR(50))  MODIFIES SQL DATA
UPDATE usuarios
SET password=DES_ENCRYPT(my_pass), nombre=my_name, email=my_email
WHERE usuario=my_user$$

CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `modificarGastos` (IN `id_gasto` INT(11), IN `cat_id` INT(11), IN `my_monto` DOUBLE, IN `my_date` DATE, IN `descrip` VARCHAR(50))  MODIFIES SQL DATA
UPDATE gastos
SET monto=my_monto, id_categoria=cat_id, fecha=my_date, descripcion=descrip
WHERE id=id_gasto$$

CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `modificarIngreso` (IN `id_ingreso` INT(11), IN `my_monto` DOUBLE, IN `my_date` DATE, IN `descrip` VARCHAR(50))  MODIFIES SQL DATA
UPDATE ingresos
SET monto=my_monto, fecha=my_date, descripcion=descrip
WHERE id=id_ingreso$$

CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `modificarMeta` (IN `id_meta` INT(11), IN `my_nombre` VARCHAR(20), IN `my_monto` DOUBLE, IN `fecha_ini` DATE, IN `fecha_fin` DATE)  MODIFIES SQL DATA
UPDATE metas
SET nombre=my_nombre, monto=my_monto, inicio=fecha_ini, final=fecha_fin
WHERE id=id_meta$$

CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `requerirInformacionUsuario` (IN `my_user` VARCHAR(20))  READS SQL DATA
SELECT
id, usuario, DES_DECRYPT(password), nombre, email
        FROM
            usuarios
        WHERE
            usuario=my_user$$

CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `verCategorias` ()  READS SQL DATA
SELECT
	categorias.id, categorias.nombre
        FROM
            categorias$$

CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `verGastos` (IN `user_id` INT(11), IN `fecha_ini` DATE, IN `fecha_fin` DATE)  READS SQL DATA
SELECT
	gastos.id, gastos.monto, categorias.id AS 'id_cat', categorias.nombre, gastos.fecha, gastos.descripcion
        FROM
            gastos
        INNER JOIN
        	categorias
        ON
        	categorias.id = gastos.id_categoria
        WHERE
            id_usuario=user_id AND fecha BETWEEN fecha_ini AND fecha_fin
        ORDER BY fecha ASC$$

CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `verGastosGrafico` (IN `user_id` INT(11), IN `fecha_ini` DATE, IN `fecha_fin` DATE)  READS SQL DATA
SELECT 
	categorias.nombre, COALESCE(t1.monto, 0 )
	FROM
    categorias
    LEFT JOIN
    (
        SELECT id_categoria,monto FROM gastos
        WHERE id_usuario=user_id AND fecha BETWEEN fecha_ini AND fecha_fin
        GROUP BY id_categoria
    ) AS t1
	ON categorias.id = t1.id_categoria$$

CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `verIngresos` (IN `user_id` INT(11), IN `fecha_ini` DATE, IN `fecha_fin` DATE)  READS SQL DATA
SELECT
	id, monto, fecha, descripcion
        FROM
            ingresos
        WHERE
            id_usuario=user_id AND fecha BETWEEN fecha_ini AND fecha_fin
        ORDER BY fecha ASC$$

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

--
-- Volcado de datos para la tabla `gastos`
--

INSERT INTO `gastos` (`id`, `id_usuario`, `id_categoria`, `monto`, `fecha`, `descripcion`) VALUES
(11, 1, 1, 5, '2018-06-01', 'desayuno'),
(12, 1, 2, 10, '2018-06-01', 'taxi'),
(13, 1, 1, 5, '2018-06-02', 'desayuno'),
(14, 1, 1, 15, '2018-06-01', 'Almuerzo con los profesores'),
(15, 1, 1, 40, '2018-06-01', 'Cena'),
(16, 1, 1, 7, '2018-06-02', 'Almuerzo'),
(17, 1, 2, 100, '2018-06-02', 'Gasolina'),
(18, 1, 3, 250, '2018-06-03', 'Compras de la semana'),
(19, 1, 8, 30, '2018-06-03', 'utensilios de la semana'),
(20, 1, 7, 4, '2018-06-04', 'Cigarrillos'),
(21, 1, 4, 100, '2018-06-05', 'Cuenta de luz'),
(22, 1, 4, 95, '2018-06-05', 'Cuenta de Agua'),
(23, 1, 6, 15, '2018-06-05', 'Pastillas para la gripe (hija)'),
(24, 1, 6, 60, '2018-06-05', 'Cuenta del medico'),
(25, 1, 1, 7, '2018-06-06', 'Desayuno'),
(26, 1, 7, 9, '2018-06-09', 'Juego para movil (hija)'),
(27, 1, 1, 7, '2018-06-06', 'Almuerzo'),
(28, 1, 5, 30, '2018-06-07', 'Medias nuevas (yo)'),
(29, 1, 8, 50, '2018-06-10', 'Perfume nuevo'),
(30, 1, 1, 20, '2018-06-09', 'Desayuno con empresarios de zapaterias'),
(31, 1, 1, 50, '2018-06-09', 'Almuerzo con ejecutivos de la UCSM'),
(32, 1, 3, 233, '2018-06-10', 'Compras de la semana'),
(33, 1, 8, 33, '2018-06-10', 'utensilios de la semana'),
(34, 1, 9, 19, '2018-06-11', 'Libro de mano'),
(35, 1, 7, 5, '2018-06-11', 'Cigarrillos'),
(36, 1, 1, 7, '2018-06-13', 'desayuno'),
(37, 1, 7, 3, '2018-06-12', 'Cigarrillos'),
(38, 1, 7, 7, '2018-06-13', 'Cigarrillos'),
(39, 1, 8, 120, '2018-06-14', 'Maquina de afeitar LG'),
(40, 1, 1, 8, '2018-06-13', 'Almuerzo'),
(41, 1, 1, 7, '2018-06-14', 'desayuno'),
(42, 1, 1, 8, '2018-06-14', 'Almuerzo'),
(44, 1, 1, 50, '2018-06-14', 'Pequena cena familiar'),
(45, 1, 1, 7, '2018-06-15', 'desayuno de emergencia en la UCSP'),
(46, 1, 1, 2, '2018-06-15', 'Refresco'),
(47, 1, 1, 3, '2018-06-15', 'Pastel para uno'),
(48, 1, 1, 8, '2018-06-15', 'Almuerzo'),
(49, 1, 5, 20, '2018-06-16', 'Corbata nueva (Provisional)'),
(50, 1, 1, 5, '2018-06-16', 'Desayuno'),
(51, 1, 1, 7, '2018-06-16', 'Almuerzo'),
(52, 1, 3, 248, '2018-06-17', 'Compras de la semana'),
(53, 1, 1, 80, '2018-06-17', 'Almuerzo en familia'),
(54, 1, 8, 34, '2018-06-17', 'utensilios de la semana'),
(55, 1, 7, 2, '2018-06-18', 'Cigarrillos'),
(56, 1, 4, 130, '2018-06-18', 'SOAT'),
(57, 1, 1, 6, '2018-06-20', 'Desayuno'),
(58, 1, 1, 25, '2018-06-19', 'Cafe instantaneo (de buena calidad)'),
(59, 1, 1, 8, '2018-06-20', 'Almuerzo'),
(60, 1, 1, 7, '2018-06-21', 'desayuno'),
(61, 1, 7, 5, '2018-06-18', 'Cigarrillos'),
(62, 1, 1, 10, '2018-06-21', 'Almuerzo');

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
(1, 1, 1500, '2018-05-08', 'Sueldo'),
(2, 1, 300, '2018-05-18', 'Bingo'),
(3, 1, 10, '2018-05-04', 'Billete en la calle'),
(11, 1, 1500, '2018-05-23', 'sueldo'),
(12, 1, 200, '2018-06-05', 'Ingreso de Victor (me debia dinero)'),
(14, 1, 25, '2018-06-12', 'pequena loteria'),
(15, 1, 1500, '2018-06-08', 'sueldo'),
(16, 1, 300, '2018-06-09', 'Bono por el dia del padre'),
(17, 1, 6500, '2018-05-01', 'monto hasta el momento'),
(18, 1, 2000, '2018-05-16', 'sueldo de mi esposa'),
(19, 1, 2000, '2018-06-16', 'sueldo de mi esposa'),
(20, 1, 300, '2018-07-07', 'Sueldo');

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
  `final` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `metas`
--

INSERT INTO `metas` (`id`, `id_usuario`, `nombre`, `monto`, `inicio`, `final`) VALUES
(4, 1, 'consola para los nin', 1800, '2018-06-18', '2018-12-13'),
(5, 1, 'Regalo para mi hija', 50, '2018-06-18', '2018-08-08'),
(6, 1, 'Television para el m', 2000, '2018-04-04', '2018-06-30'),
(7, 1, 'nuevo estante para l', 400, '2018-09-13', '2019-03-20'),
(8, 1, 'Corredora', 2000, '2018-06-19', '2019-12-24'),
(9, 1, 'Nueva cocina', 500, '2018-07-01', '2018-07-31');

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
(1, 'user1', '€Xç>w\nðìa', 'Carlos Mendoza', 'carlin@gmail.com');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;
--
-- AUTO_INCREMENT de la tabla `ingresos`
--
ALTER TABLE `ingresos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
--
-- AUTO_INCREMENT de la tabla `metas`
--
ALTER TABLE `metas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
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
