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
      <h1>Administrador: "${sessionScope.usuario}"</h1>
    <div class="col-lg-2"></div>
        <div class="col-lg-8">
            <table>
                <tr>
                    <form action="crear_usuario" nethod="post">
                        <td><h3>cargar usuarios</h3></td>
                        <td><input type="text" name ="nombre" id="user" class="form-control"/></td>
                        <td>r</td>
                    </form>
                </tr>
                
                <tr>
                    <form action="crear_usuario" nethod="post">
                        <td><h3>Cargar naves</h3></td>
                        <td><input type="text" name ="nombre" id="user" class="form-control"/></td>
                        <td>r</td>
                    </form>
                </tr>
                
                <tr>
                    <form action="crear_usuario" nethod="post">
                        <td><h3>Cargar juegos</h3></td>
                        <td><input type="text" name ="nombre" id="user" class="form-control"/></td>
                        <td></td>
                    </form>
                </tr>
                
                <tr>
                    <form action="crear_usuario" nethod="post">
                        <td><h3>Partida actual</h3></td>
                        <td><input type="text" name ="nombre" id="user" class="form-control"/></td>
                        <td></td>
                    </form>
                </tr>
                
                <tr>
                    <form action="crear_usuario" nethod="post">
        
                        <td><h3>Historial</h3></td>
                        <td><input type="text" name ="nombre" id="user" class="form-control"/></td>
                        <td></td>
                    </form>
                </tr>
                
                
                <tr>
                    <form action="crear_usuario" nethod="post">
        
                        <td><h3>Contactos</h3></td>
                        <td><input type="text" name ="nombre" id="user" class="form-control"/></td>
                        <td></td>
                    </form>
                </tr>
                
                <tr>
                    <form action="crear_usuario" nethod="post">
                        <td><h3>Tiros</h3></td>
                        <td><input type="text" name ="nombre" id="user" class="form-control"/></td>
                        <td></td>
                    </form>
                </tr>
            </table>
        </div>
    <div class="col-lg-2"></div>
    
    <div class="col-lg-4"></div><div class="col-lg-4">
        <form action="crear_usuario" nethod="post">
            <p><h2>Usuario</h2><input type="text" name ="nombre" id="user" class="form-control"/></p>
        <p><h2>password</h2><input type="text" name ="passwd" id="passwd" class="form-control"/></p>
    <p><input type="submit" name="entrar" value="Entrar" class="btn-primary col-lg-12"/></p>
        </form>
            <p>
                <a href="crear_usuario.jsp"> o crear usuario</a></p> 
        </div>
    <div class="col-lg-4"></div>
    

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
     <script src="js/bootstrap.min.js"></script>
  </body>
</html>