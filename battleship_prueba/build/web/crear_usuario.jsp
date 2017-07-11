<%-- 
    Document   : crear_usuario
    Created on : 10-jul-2017, 18:54:45
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
      <div clas="col-lg-6"></div>
      <div class="col-lg-4">
        <h1>Crear usuario</h1>
        <form action="crear_usuario" nethod="post">
            <p>Nombre<input type="text" name ="nombre" id="user"/></p>
            <p>Passwd<input type="text" name ="passwd" id="passwd"/></p>
            <p><input type="submit" name="crear" value="Crear" class="btn-primary col-lg-8"/></p>
        </form>
        </div>
      <div class="col-lg-4"></div>
      
    </body>
    
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
     <script src="js/bootstrap.min.js"></script>
  </body>
</html>
