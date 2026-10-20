<?php 
include("conexion.php");
$con = conectar();

$id = $_GET['id'];

$sql = "SELECT * FROM alumnos WHERE id='$id'";
$query = mysqli_query($con, $sql);
$row = mysqli_fetch_array($query);
?>
 
 <!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Actualizar</title>
    </head>
    <body>
        <h1>Actualizar Alumno</h1>
        <form action="update.php" method="POST">
            <input type="hidden" name="id" value="<?php echo $row['id'] ?>">
            <br><br>
            <input type="text" name="matricula" placeholder="Matricula" value="<?php echo $row['matricula'] ?>"><br><br>
            <br><br>
            <input type="text" name="nombre" placeholder="Nombre" value="<?php echo $row['nombre'] ?>"><br><br>
            <br><br>
            <input type="text" name="apellido_p" placeholder="Apellido Paterno" value="<?php echo $row['apellido_p'] ?>"><br><br>
            <br><br>
            <input type="text" name="apellido_m" placeholder="Apellido Materno" value="<?php echo $row['apellido_m'] ?>"><br><br>
            <br><br>
            <input type="number" name="edad" placeholder="Edad" value="<?php echo $row['edad'] ?>"><br><br>
            <br><br>
            <button type="submit">Actualizar</button>
        </form>
        <br>
        <a href="alumnos.php">Regresar</a>
    </body>
</html>