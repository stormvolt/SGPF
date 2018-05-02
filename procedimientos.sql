--Inicio de sesion
CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `verificar_inicio_sesion`(IN `my_user` VARCHAR(20), IN `my_pass` VARCHAR(20), OUT `resultado` BOOLEAN)
    READS SQL DATA
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
   
END




--Insertar un nuevo usuario
CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `insertar_usuario`(IN `my_user` VARCHAR(20), IN `my_pass` VARCHAR(20), IN `my_name` VARCHAR(50), IN `my_email` VARCHAR(50))
    MODIFIES SQL DATA
INSERT INTO usuarios
(id,usuario,password,nombre,email)
VALUES (null,
        my_user,
        DES_ENCRYPT(my_pass),
        my_name,
        my_email)

		

		
--Seleccionar todos los datos de un usuario
CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `buscar_datos`(IN `my_user` VARCHAR(20))
    READS SQL DATA
SELECT
id, usuario, DES_DECRYPT(password), nombre, email
        FROM
            usuarios
        WHERE
            usuario=my_user
			


			
--Modifica los datos del usuario seleccionado
CREATE DEFINER=`root`@`127.0.0.1` PROCEDURE `modificar_datos`(IN `my_user` VARCHAR(20), IN `my_pass` VARCHAR(20), IN `my_name` VARCHAR(50), IN `my_email` VARCHAR(50))
    MODIFIES SQL DATA
UPDATE usuarios
SET password=DES_ENCRYPT(my_pass), nombre=my_name, email=my_email
WHERE usuario=my_user
