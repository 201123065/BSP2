/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package CSV;

/**
 *
 * @author marcosmayen
 */
public class convertir_a_entero {
    public int a_entero(String cadena){
        int valor=0;
        switch(cadena.length()){
            case 9:
                valor+=(cadena.charAt(8)-64)*100000000;
            case 8:
                valor+=(cadena.charAt(7)-64)*10000000;
            case 7:
                valor+=(cadena.charAt(6)-64)*1000000;
            case 6:
                valor+=(cadena.charAt(5)-64)*100000;
            case 5:
                valor+=(cadena.charAt(4)-64)*10000;
            case 4:
                valor+=(cadena.charAt(3)-64)*1000;
            case 3:
                valor+=(cadena.charAt(2)-64)*100;
            case 2:
                valor+=(cadena.charAt(1)-64)*10;
            case 1:
                valor+=(cadena.charAt(0)-64);
        }
        System.out.println(valor);
        System.out.println(valor);
        System.out.println(valor);
        System.out.println(valor);
        return valor;
        
    }
}
