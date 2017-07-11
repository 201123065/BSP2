<%-- 
    Document   : index
    Created on : 10-jul-2017, 17:46:35
    Author     : marcosmayen
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <h1>Bienvenido a battleship</h1>
        <div class="col-lg-12">
        <form action="crear_usuario" nethod="post">
            <p>Usuario<input type="text" name ="nombre" id="user"/></p>
        <p>password<input type="text" name ="passwd" id="passwd"/></p>
        <p><input type="submit" name="entrar" value="Entrar"/></p>
        </form>
        <a href="crear_usuario.jsp">crear usuario</a>
        </div>
    </body>
</html>
