<?php

    /*Creamos una funcion llamada conectar*/
    function conectar(){
    /*Informacion del servidor*/
    $hots="localhost";
    $user="root";
    $pass="";

    /*Base de datos*/
    $db="aw221";

    /*Permite conectarnos a MySQL*/
    $con=mysqli_connect($hots,$user,$pass);

    /*Le vamos a decir que BD y la informacion de con*/
    mysqli_select_db($con,$db);

    return $con;

}
?>