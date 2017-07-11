<%-- 
    Document   : crear_usuario
    Created on : 10-jul-2017, 18:54:45
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
        <h1>Crear usuario</h1>
        <form action="crear_usuario" nethod="post">
        <input type="text" name ="nombre" id="user"/>
        <input type="text" name ="passwd" id="passwd"/>
        <input type="submit" name="entrar" value="Entrar"/>
        </form>
    </body>
</html>
