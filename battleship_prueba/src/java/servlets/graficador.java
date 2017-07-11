/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package servlets;

import java.awt.Image;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import javax.swing.Icon;
import javax.swing.ImageIcon;

/**
 *
 * @author marcosmayen
 */
public class graficador {
    
    private String agregarNodo(String nodo){
        
        return "digraph G{\n "+nodo+"\n}";
    }
    
    private void buildfile(String cadena,String ruta){
        File f;
        FileWriter fw;
        try{
            f = new File(cadena);
            fw = new FileWriter(f);
            BufferedWriter bw = new BufferedWriter(fw);
            PrintWriter pw = new PrintWriter(bw);
            pw.write(ruta);
            pw.close();
            bw.close();
            generar(cadena);
        }catch (IOException e){}
    }
    private void generar(String cadena){
        try{
            String ruta = " /usr/local/bin/dot ";
            String acciones=" -Tpng -O ";
            Runtime rt = Runtime.getRuntime();
            String accion =ruta+acciones+cadena;
            rt.exec(accion);
        }catch(Exception e){
            e.printStackTrace();
        }
    }
     public void imagen(String ruta_grafo){
        agregarNodo(ruta_grafo);
        String ruta = System.getProperty("user.dir")+"/filedot";
        buildfile(ruta+"/archivis.dot",ruta_grafo);
     }
}
