/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Vistas;

/**
 *
 * @author marcosmayen
 */
public class header_footer {
    
    
    public String getHeader(){
        return "<!DOCTYPE html>\n" +
"<html lang=\"en\">\n" +
"  <head>\n" +
"    <meta charset=\"utf-8\">\n" +
"    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n" +
"    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n" +
"    <title>Bootstrap 101 Template</title>\n" +
"\n" +
"    <link href=\"css/bootstrap.min.css\" rel=\"stylesheet\">\n" +
"\n" +
"   </head>\n" +
"  <body>";
    }
    
    public String getFooter(){
        return "\n" +
"\n" +
"    <script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js\"></script>\n" +
"     <script src=\"js/bootstrap.min.js\"></script>\n" +
"  </body>\n" +
"</html>";
    }
}
