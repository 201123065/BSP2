package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;
import java.io.*;

public final class admin_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent {

  private static final JspFactory _jspxFactory = JspFactory.getDefaultFactory();

  private static java.util.List<String> _jspx_dependants;

  private org.glassfish.jsp.api.ResourceInjector _jspx_resourceInjector;

  public java.util.List<String> getDependants() {
    return _jspx_dependants;
  }

  public void _jspService(HttpServletRequest request, HttpServletResponse response)
        throws java.io.IOException, ServletException {

    PageContext pageContext = null;
    HttpSession session = null;
    ServletContext application = null;
    ServletConfig config = null;
    JspWriter out = null;
    Object page = this;
    JspWriter _jspx_out = null;
    PageContext _jspx_page_context = null;

    try {
      response.setContentType("text/html;charset=UTF8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;
      _jspx_resourceInjector = (org.glassfish.jsp.api.ResourceInjector) application.getAttribute("com.sun.appserv.jsp.resource.injector");

      out.write("\n");
      out.write("\n");
      out.write("<!DOCTYPE html>\n");
      out.write("<html lang=\"en\">\n");
      out.write("  <head>\n");
      out.write("    <meta charset=\"utf-8\">\n");
      out.write("    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n");
      out.write("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n");
      out.write("    <title>Bootstrap 101 Template</title>\n");
      out.write("    <script type=\"text/javascript\" src=\"js/jquery-3.2.1.min.js\"></script>\n");
      out.write("    <link href=\"css/bootstrap.min.css\" rel=\"stylesheet\">\n");
      out.write("    \n");
      out.write("    \n");
      out.write("    <script>\n");
      out.write("\n");
      out.write("function processFiles(files) {\n");
      out.write("var file = files[0];\n");
      out.write("\n");
      out.write("var reader = new FileReader();\n");
      out.write("\n");
      out.write("reader.onload = function (e) {\n");
      out.write("// Cuando éste evento se dispara, los datos están ya disponibles.\n");
      out.write("// Se trata de copiarlos a una área <div> en la página.\n");
      out.write("var output = document.getElementById(\"fileOutput\"); \n");
      out.write("output.textContent = pruebaCarga(e.target.result);\n");
      out.write("};\n");
      out.write("reader.readAsText(file);\n");
      out.write("}\n");
      out.write("\n");
      out.write("        \n");
      out.write("\n");
      out.write("</script>\n");
      out.write("    \n");
      out.write("    \n");
      out.write("    \n");
      out.write("    \n");
      out.write("    \n");
      out.write("   </head>\n");
      out.write("  <body>\n");
      out.write("      <h1>Administrador: \"");
      out.write((java.lang.String) org.apache.jasper.runtime.PageContextImpl.evaluateExpression("${sessionScope.usuario}", java.lang.String.class, (PageContext)_jspx_page_context, null));
      out.write("\"</h1>\n");
      out.write("    <div class=\"col-lg-1\"></div>\n");
      out.write("        <div class=\"col-lg-10\">\n");
      out.write("            <table>\n");
      out.write("                <tr><th><h2>tipo</h2></th><th><h2>archivo</h2></th><th><h2>cargar</h2></th><th><h2 class=\"bottom-left\">ver</h2></th><tr>\n");
      out.write("                <tr>\n");
      out.write("                <form action=\"load_user\" name=\"formu_user\" method=\"post\" enctype=\"multipart/form-data\">\n");
      out.write("                       \n");
      out.write("                    <td><h3>Usuarios</h3></td>\n");
      out.write("                    <td><input type=\"file\" name =\"nombre\" value=\"cargar\" id=\"ipnput_usu\" /></td>\n");
      out.write("                        <td><input type=\"submit\" name=\"btn_usuario\" value=\"procesar\"  class=\"btn-primary\"/></td>\n");
      out.write("                        <td></td>\n");
      out.write("                    </form>\n");
      out.write("                    <input type=\"hidden\" name=\"it_user\" value=\"\"/>\n");
      out.write("                    <iframe name=\"if_user\" style=\"display: none;\"></iframe>\n");
      out.write("                \n");
      out.write("                </tr>\n");
      out.write("                \n");
      out.write("                <tr>\n");
      out.write("                    <form action=\"load_ship\" name=\"formu_ship\" method=\"post\">\n");
      out.write("                        <td><h3>Naves</h3></td>\n");
      out.write("                        <td><input type=\"file\" name =\"nombre\" id=\"user\" /></td>\n");
      out.write("                        <td><input type=\"submit\" name=\"btn_user\"value=\"procesar\" class=\"btn-primary\"/></td>\n");
      out.write("                        <td></td>\n");
      out.write("                    </form>\n");
      out.write("                    <input type=\"hidden\" name=\"it_ship\" value=\"\"/>\n");
      out.write("                    <iframe name=\"if_ship\" style=\"display: none;\"></iframe>\n");
      out.write("                </tr>\n");
      out.write("                \n");
      out.write("                <tr>\n");
      out.write("                <form action=\"load_game\" name=\"formu_juego\" method=\"post\">\n");
      out.write("                        <td><h3>Juegos</h3></td>\n");
      out.write("                        <td><input type=\"file\" name =\"nombre\" id=\"user\" /></td>\n");
      out.write("                        <td><input type=\"submit\" value=\"procesar\" class=\"btn-primary\"/></td>\n");
      out.write("                        <td></td>\n");
      out.write("                    </form>\n");
      out.write("                    <input type=\"hidden\" name=\"it_game\" value=\"\"/>\n");
      out.write("                    <iframe name=\"if_game\" style=\"display: none;\"></iframe>\n");
      out.write("                </tr>\n");
      out.write("                \n");
      out.write("                <tr>\n");
      out.write("                <form action=\"actual_match\" name=\"formu_partida\" method=\"post\">\n");
      out.write("                        <td><h3>Partida actual</h3></td>\n");
      out.write("                        <td><input type=\"file\" name =\"nombre\" id=\"user\" /></td>\n");
      out.write("                        <td><input type=\"submit\" value=\"procesar\" class=\"btn-primary\"/></td>\n");
      out.write("                    </form>\n");
      out.write("                    <input type=\"hidden\" name=\"it_match\" value=\"\"/>\n");
      out.write("                    <iframe name=\"if_match\" style=\"display: none;\"></iframe>\n");
      out.write("                </tr>\n");
      out.write("                \n");
      out.write("                <tr>\n");
      out.write("                <form action=\"history\" name=\"formu_historial\" method=\"post\">\n");
      out.write("        \n");
      out.write("                        <td><h3>Historial</h3></td>\n");
      out.write("                        <td><input type=\"file\" name =\"nombre\" id=\"user\" /></td>\n");
      out.write("                        <td><input type=\"submit\" value=\"procesar\" class=\"btn-primary\"/></td>\n");
      out.write("                    </form>\n");
      out.write("                    <input type=\"hidden\" name=\"it_history\" value=\"\"/>\n");
      out.write("                    <iframe name=\"if_history\" style=\"display: none;\"></iframe>\n");
      out.write("                </tr>\n");
      out.write("                \n");
      out.write("                \n");
      out.write("                <tr>\n");
      out.write("                <form action=\"contact\" name=\"formu_contactos\" method=\"post\">\n");
      out.write("        \n");
      out.write("                        <td><h3>Contactos</h3></td>\n");
      out.write("                        <td><input type=\"file\" name =\"nombre\" id=\"user\" /></td>\n");
      out.write("                        <td><input type=\"submit\" value=\"procesar\" class=\"btn-primary\"/></td>\n");
      out.write("                    </form>\n");
      out.write("                    <input type=\"hidden\" name=\"it_contact\" value=\"\"/>\n");
      out.write("                    <iframe name=\"if_contact\" style=\"display: none;\"></iframe>\n");
      out.write("                </tr>\n");
      out.write("                \n");
      out.write("                <tr>\n");
      out.write("                <form action=\"shoots\" name=\"formu_disparos\" method=\"post\">\n");
      out.write("                        <td><h3>Tiros</h3></td>\n");
      out.write("                        <td><input type=\"file\" name =\"nombre\" id=\"user_shoot\" /></td>\n");
      out.write("                        <td><input type=\"submit\" value=\"procesar\" class=\"btn-primary\"/></td>\n");
      out.write("                        <td></td>\n");
      out.write("                    </form>\n");
      out.write("                    <input type=\"hidden\" name=\"it_shoot\" value=\"\"/>\n");
      out.write("                    <iframe name=\"if_shoot\" style=\"display: none;\"></iframe>\n");
      out.write("                </tr>\n");
      out.write("            </table>\n");
      out.write("            <input type=\"hidden\" name=\"nombre\" value=\"\"/>\n");
      out.write("            <iframe name=\"if_usuario\" style=\"display: none;\"></iframe>\n");
      out.write("          \n");
      out.write("            \n");
      out.write("            \n");
      out.write("            \n");
      out.write("<input id=\"fileInput\" type=\"file\" size=\"50\" onchange=\"processFiles(this.files)\">\n");
      out.write("<div id=\"fileOutput\"></div>\n");
      out.write("            \n");
      out.write("            \n");
      out.write("            \n");
      out.write("            \n");
      out.write("<script>\n");
      out.write("    \n");
      out.write("        function pruebaCarga(str){\n");
      out.write("            \n");
      out.write("            $.ajax({\n");
      out.write("                data:{\n");
      out.write("                    'cadena':str\n");
      out.write("                },\n");
      out.write("                url:'usuario_csv',\n");
      out.write("                type:'get',\n");
      out.write("                success: function (data) {\n");
      out.write("                        alert(\"si\")\n");
      out.write("                    }   \n");
      out.write("            });\n");
      out.write("        }\n");
      out.write("    \n");
      out.write("    \n");
      out.write("</script>\n");
      out.write("            \n");
      out.write("            \n");
      out.write("            \n");
      out.write("\n");
      out.write("    <script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js\"></script>\n");
      out.write("     <script src=\"js/bootstrap.min.js\"></script>\n");
      out.write("  </body>\n");
      out.write("</html>");
    } catch (Throwable t) {
      if (!(t instanceof SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          out.clearBuffer();
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}
