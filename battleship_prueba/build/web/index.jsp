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
        <h1>Hello World!</h1>
        <form action="crear_usuario" nethod="post">
        <input type="text" name ="nombre" id="user"/>
        <input type="text" name ="passwd" id="passwd"/>
        <input type="submit" name="entrar" value="Entrar"/>
        </form>
        <a href="crear_usuario.jsp">crear usuario</a>
    </body>
</html>
