<%@page import="java.io.*"%>
<%@page contentType="text/html" pageEncoding="UTF8"%>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap 101 Template</title>
    <script type="text/javascript" src="js/jquery-3.2.1.min.js"></script>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    
    
    <script>

function processUser(files) {
    var file = files[0];
    var reader = new FileReader();
    reader.onload = function (e) {
        var output = document.getElementById("fileOutput"); 
        output.textContent = pruebaCarga(e.target.result,"usuario_csv");
    };
    reader.readAsText(file);
}
function processNaves(files) {
    var file = files[0];
    var reader = new FileReader();
    reader.onload = function (e) {
        var output = document.getElementById("fileOutput"); 
        output.textContent = pruebaCarga(e.target.result,"nave_csv");
    };
    reader.readAsText(file);
}
function processJuegos(files) {
    var file = files[0];
    var reader = new FileReader();
    reader.onload = function (e) {
        var output = document.getElementById("fileOutput"); 
        output.textContent = pruebaCarga(e.target.result,"juego_csv");
    };
    reader.readAsText(file);
}
function processPartida(files) {
    var file = files[0];
    var reader = new FileReader();
    reader.onload = function (e) {
        var output = document.getElementById("fileOutput"); 
        output.textContent = pruebaCarga(e.target.result,"partida_csv");
    };
    reader.readAsText(file);
}
function processHistorial(files) {
    var file = files[0];
    var reader = new FileReader();
    reader.onload = function (e) {
        var output = document.getElementById("fileOutput"); 
        output.textContent = pruebaCarga(e.target.result,"historial_csv");
    };
    reader.readAsText(file);
}
function processContactos(files) {
    var file = files[0];
    var reader = new FileReader();
    reader.onload = function (e) {
        var output = document.getElementById("fileOutput"); 
        output.textContent = pruebaCarga(e.target.result,"contactos_csv");
    };
    reader.readAsText(file);
}
function processTiros(files) {
    var file = files[0];
    var reader = new FileReader();
    reader.onload = function (e) {
        var output = document.getElementById("fileOutput"); 
        output.textContent = pruebaCarga(e.target.result,"tiros_csv");
    };
    reader.readAsText(file);
}

        

</script>
    
    
    
    
    
   </head>
  <body>
      <h1>Administrador: "${sessionScope.usuario}"</h1>
    <div class="col-lg-1"></div>
        <div class="col-lg-10">
            <table>
                <tr><th><h2>tipo</h2></th><th><h2>archivo</h2></th></th></th><tr>
                <tr>
                <form action="load_user" name="formu_user" method="post" enctype="multipart/form-data">
                       
                    <td><h3>Usuarios</h3></td>
                    <td><input id="fileInput" type="file" size="50" onchange="processUser(this.files)"></td>
                    </form>
                    <iframe name="if_user" style="display: none;"></iframe>
                
                </tr>
                
                <tr>
                    <form action="load_ship" name="formu_ship" method="post">
                        <td><h3>Naves</h3></td>
                        <td><input id="fileInput" type="file" size="50" onchange="processNaves(this.files)"></td>
                    </form>
                    <input type="hidden" name="it_ship" value=""/>
                    <iframe name="if_ship" style="display: none;"></iframe>
                </tr>
                
                <tr>
                <form action="load_game" name="formu_juego" method="post">
                        <td><h3>Juegos</h3></td>
                        <td><input id="fileInput" type="file" size="50" onchange="processJuegos(this.files)"></td>
                    </form>
                    <input type="hidden" name="it_game" value=""/>
                    <iframe name="if_game" style="display: none;"></iframe>
                </tr>
                
                <tr>
                <form action="actual_match" name="formu_partida" method="post">
                        <td><h3>Partida actual</h3></td>
                        <td><input id="fileInput" type="file" size="50" onchange="processPartida(this.files)"></td>
                    </form>
                    <input type="hidden" name="it_match" value=""/>
                    <iframe name="if_match" style="display: none;"></iframe>
                </tr>
                
                <tr>
                <form action="history" name="formu_historial" method="post">
        
                        <td><h3>Historial</h3></td>
                        <td><input id="fileInput" type="file" size="50" onchange="processHistorial(this.files)"></td>
                    </form>
                    <input type="hidden" name="it_history" value=""/>
                    <iframe name="if_history" style="display: none;"></iframe>
                </tr>
                
                
                <tr>
                <form action="contact" name="formu_contactos" method="post">
        
                        <td><h3>Contactos</h3></td>
                        <td><input id="fileInput" type="file" size="50" onchange="processContactos(this.files)"></td>
                    </form>
                    <input type="hidden" name="it_contact" value=""/>
                    <iframe name="if_contact" style="display: none;"></iframe>
                </tr>
                
                <tr>
                <form action="shoots" name="formu_disparos" method="post">
                        <td><h3>Tiros</h3></td>
                        <td><input id="fileInput" type="file" size="50" onchange="processTiros(this.files)"></td>
                    </form>
                    <input type="hidden" name="it_shoot" value=""/>
                    <iframe name="if_shoot" style="display: none;"></iframe>
                </tr>
            </table>
            <input type="hidden" name="nombre" value=""/>
            <iframe name="if_usuario" style="display: none;"></iframe>
          
            
            
            
            
            
            
            
<script>
    
        function pruebaCarga(str,url){
            $.ajax({
                data:{
                    'cadena':str
                },
                url:url,
                type:'get',
                success: function (data) {
                        alert("si")
                    }   
            });
        }
    
    
</script>
            
            
            

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
     <script src="js/bootstrap.min.js"></script>
  </body>
</html>