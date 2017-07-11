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
    <h1>Bienvenido a battleship</h1>
        <div class="col-lg-12">
        <form action="crear_usuario" nethod="post">
            <p><h2>Usuario</h2><input type="text" name ="nombre" id="user"/></p>
        <p><h2>password</h2><input type="text" name ="passwd" id="passwd"/></p>
        <p><input type="submit" name="entrar" value="Entrar"/></p>
        </form>
        <a href="crear_usuario.jsp">crear usuario</a>
        </div>
    

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
     <script src="js/bootstrap.min.js"></script>
  </body>
</html>