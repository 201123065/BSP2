<%-- 
    Document   : index
    Created on : 10-jul-2017, 17:46:35
    Author     : marcosmayen
--%>

<%@page contentType="text/html" pageEncoding="UTF8"%>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap 101 Template</title>

    <link href="css/bootstrap.min.css" rel="stylesheet">

   </head>
  <body>
      <h1 class="col-lg-12">Bienvenido a battleship</h1>
    <div class="col-lg-4"></div>
        <div class="col-lg-4">
        <form action="login" nethod="post">
            <p><h2>Usuario</h2><input type="text" name ="nombre" id="user" class="form-control"/></p>
        <p><h2>password</h2><input type="text" name ="passwd" id="passwd" class="form-control"/></p>
    <p><input type="submit" name="entrar" value="Entrar" class="btn-primary col-lg-12"/></p>
        </form>
            <p>
                <a href="crear_usuario.jsp"> o crear usuario</a>
            <a href="graficar" class="pull-right">ver arbol</a></p>
        </div>
    <div class="col-lg-4"></div>
    

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
     <script src="js/bootstrap.min.js"></script>
  </body>
</html>
