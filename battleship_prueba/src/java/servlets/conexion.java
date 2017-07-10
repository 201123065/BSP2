/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package servlets;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;



import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;
public class conexion {
    
    public static OkHttpClient webClient = new OkHttpClient();
    
    
     public static String getString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://localhost:5000/metodo2");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(conexion.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(conexion.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
    
    
    protected void conexion(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            
        String nombre = "Marco";
        RequestBody formBody = new FormEncodingBuilder()
                .add("p", nombre)
                .add("pa", nombre)
                .build();
        String r = getString("metodo2", formBody); 
        System.out.println(r + "---");
            
        }
    }
    
}
