<%@page import="java.io.*"%>
<%@page contentType="text/html" pageEncoding="UTF8"%>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap 101 Template</title>

    <link href="css/bootstrap.min.css" rel="stylesheet">
    <script type="text/javascript" scr="lector.js"></script>
   </head>
  <body>
      <h1>Administrador: "${sessionScope.usuario}"</h1>
    <div class="col-lg-1"></div>
        <div class="col-lg-10">
            <table>
                <tr><th><h2>tipo</h2></th><th><h2>archivo</h2></th><th><h2>cargar</h2></th><th><h2>ver</h2></th><tr>
                <tr>
                <form action="load_user" name="formu_user" method="post" enctype="multipart/form-data">
                       
                    <td><h3>Usuarios</h3></td>
                    <td><input type="file" name ="nombre" value="cargar" id="ipnput_usu" /></td>
                        <td><input type="submit" name="btn_usuario" value="procesar"  class="btn-primary"/></td>
                        <td></td>
                    </form>
                    <input type="hidden" name="it_user" value=""/>
                    <iframe name="if_user" style="display: none;"></iframe>
                
                </tr>
                
                <tr>
                    <form action="load_ship" name="formu_ship" method="post">
                        <td><h3>Naves</h3></td>
                        <td><input type="file" name ="nombre" id="user" /></td>
                        <td><input type="submit" name="btn_user"value="procesar" class="btn-primary"/></td>
                        <td></td>
                    </form>
                    <input type="hidden" name="it_ship" value=""/>
                    <iframe name="if_ship" style="display: none;"></iframe>
                </tr>
                
                <tr>
                <form action="load_game" name="formu_juego" method="post">
                        <td><h3>Juegos</h3></td>
                        <td><input type="file" name ="nombre" id="user" /></td>
                        <td><input type="submit" value="procesar" class="btn-primary"/></td>
                        <td></td>
                    </form>
                    <input type="hidden" name="it_game" value=""/>
                    <iframe name="if_game" style="display: none;"></iframe>
                </tr>
                
                <tr>
                <form action="actual_match" name="formu_partida" method="post">
                        <td><h3>Partida actual</h3></td>
                        <td><input type="file" name ="nombre" id="user" /></td>
                        <td><input type="submit" value="procesar" class="btn-primary"/></td>
                    </form>
                    <input type="hidden" name="it_match" value=""/>
                    <iframe name="if_match" style="display: none;"></iframe>
                </tr>
                
                <tr>
                <form action="history" name="formu_historial" method="post">
        
                        <td><h3>Historial</h3></td>
                        <td><input type="file" name ="nombre" id="user" /></td>
                        <td><input type="submit" value="procesar" class="btn-primary"/></td>
                    </form>
                    <input type="hidden" name="it_history" value=""/>
                    <iframe name="if_history" style="display: none;"></iframe>
                </tr>
                
                
                <tr>
                <form action="contact" name="formu_contactos" method="post">
        
                        <td><h3>Contactos</h3></td>
                        <td><input type="file" name ="nombre" id="user" /></td>
                        <td><input type="submit" value="procesar" class="btn-primary"/></td>
                    </form>
                    <input type="hidden" name="it_contact" value=""/>
                    <iframe name="if_contact" style="display: none;"></iframe>
                </tr>
                
                <tr>
                <form action="shoots" name="formu_disparos" method="post">
                        <td><h3>Tiros</h3></td>
                        <td><input type="file" name ="nombre" id="user_shoot" /></td>
                        <td><input type="submit" value="procesar" class="btn-primary"/></td>
                        <td></td>
                    </form>
                    <input type="hidden" name="it_shoot" value=""/>
                    <iframe name="if_shoot" style="display: none;"></iframe>
                </tr>
            </table>
            <input type="hidden" name="nombre" value=""/>
            <iframe name="if_usuario" style="display: none;"></iframe>
            
<input type="file" id="myFile" size="50">
            <button id="loadfile" onclick="clickeo()">lrt</button>
            
        </div>
    <script>
        
        function clickeo(){
    var x = document.getElementById("myFile").value;
    document.getElementById("demo").innerHTML = x;
}
        
        
    </script>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
     <script src="js/bootstrap.min.js"></script>
  </body>
</html>