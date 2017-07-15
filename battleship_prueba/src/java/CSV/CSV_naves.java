/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package CSV;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import servlets.conexion;

/**
 *
 * @author marcosmayen
 */
public class CSV_naves extends HttpServlet {

    /**
     * Processes requests for both HTTP <code>GET</code> and <code>POST</code>
     * methods.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    
    private String tam(String izq, String der){
        for(int j=0;j<izq.length();j++){
            if(izq.charAt(j)<der.charAt(j)){
                return der;
            }else if(izq.charAt(j)>der.charAt(j)){
                return izq;
            }
        }
        return izq;
                    
    }
    
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        
        
        try (PrintWriter out = response.getWriter()) {
           
            response.setContentType("text/plain");
            
            String []csv = request.getParameter("cadena").split("\n");
            String valor="";
            int fila=0;
            for(int i=1;i<csv.length;i++){
                String user[]=csv[i].split(",");
                if(user[1].length()>valor.length()){
                    valor=user[1];
                }else if(user[1].length()==valor.length()){
                    valor=tam(user[1],valor);
                }
                if(Integer.parseInt(user[2])>fila){
                    fila=Integer.parseInt(user[2]);
                }
                
                
            }
            conexion con= new conexion();
            convertir_a_entero cae = new convertir_a_entero();
            con.CrearTablero(fila+4,cae.a_entero(valor)+4);
            
            for(int i=1;i<csv.length-1;i++){
                String user[]=csv[i].split(",");
                con.CargarNave(user[0],user[1],user[2],user[3],user[4],user[5]);
                
            }
        }
        
        
    }

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}
