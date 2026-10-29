<?php

function conectar() {
    $host = "localhost";
    $user = "root";
    $pass = "";
    $db   = "aw221";

    $con = mysqli_connect($host, $user, $pass, $db);

    if (!$con) {
        die("Error de conexión: " . mysqli_connect_error());
    }

    mysqli_set_charset($con, "utf8mb4");

    return $con;
}
?>