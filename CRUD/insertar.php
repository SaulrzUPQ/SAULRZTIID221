<?php

/*Incluir la infromacion del archivo conexion.php*/
include("conexion.php");

/*Mandamos a llamar la funcion conectar para ejecutarla*/
$con = conectar();

$matricula  = $_POST['matricula'];
$nombre = $_POST['nombre'];
$apellido_p = $_POST['apellido_p'];
$apellido_m = $_POST['apellido_m'];
$edad = $_POST['edad'];

/*Crear nuestra consulta para insertar datos*/
$sql = "INSERT INTO alumnos
(matricula, nombre, apellido_p, apellido_m, edad) 
VALUES
('$matricula','$nombre','$apellido_p','$apellido_m','$edad')";

/*Ejecutar la consulta*/
$query = mysqli_query($con,$sql);

/*Comprobar y direccionar*/
if($query){
    header("Location: alumnos.php");
}
else{
    echo "No se pudo insertar el registro";
}


?>