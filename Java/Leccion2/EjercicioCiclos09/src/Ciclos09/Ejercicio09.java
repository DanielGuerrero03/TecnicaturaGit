/*
Ejercicio 9 : Pedir el día, mes y año de una fecha e 
indicar su la fecha es correcta. Suponiendo que
todos los mese son de 30 días
 */
package Ciclos09;

import javax.swing.JOptionPane;


public class Ejercicio09 {
    public static void main(String[] args) {
        int dia = Integer.parseInt(JOptionPane.showInputDialog("Digite el dia: "));
        int mes = Integer.parseInt(JOptionPane.showInputDialog("Digite el Mes: "));
        int anio = Integer.parseInt(JOptionPane.showInputDialog("Digite el Año: "));
        if((dia != 0)&&(dia <= 30)){
            if ((mes != 0)&&(mes <= 12)){
                if ((anio != 0)&&(anio <= 2022)){
                    JOptionPane.showMessageDialog(null, "La fecha ingresada es: "+dia+"/"+mes+"/"+anio);
                }
                else{
                    JOptionPane.showMessageDialog(null, "Fecha incorrecta, año incorrecto");
                }
            }
            else{
                JOptionPane.showMessageDialog(null, "Fecha incorrecta, mes incorrecto");
            }
        }
        else{
            JOptionPane.showMessageDialog(null, "Fecha incorrecta, dia incorrecto");
        }
    }
}
