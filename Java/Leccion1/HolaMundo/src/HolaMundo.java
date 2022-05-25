
import java.util.Scanner;

//Nuestro primer programa Hola Mundo
/*
Comentarios extensivos de muchas lineas
mas, mas, y mas lienas
 */
public class HolaMundo {

    public static void main(String args[]) {
        /*System.out.println("Hola mundo desde Java");
        
        int miVariable = 10;
        System.out.println("miVariable");
        miVariable = 5;
        System.out.println("miVariable");
        //Tipo String
        String miVariableCadena = "Bienvenidos";
        System.out.println("miVariableCadena");
        miVariableCadena = "Sigamos creciendo en Programación";
        System.out.println(miVariableCadena)
                ;*/
 /*var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        //soutv + tab
        //Para ejecutar Shift + F6
        //Reglas para definir una variable en Java
        //Tipo de escritura camel case se comienza con minuscula la definicion de variable
        //Se recomineda no poner acento en la fefinicion de variables
        //Numeral no se puede colocar es ilegal 
        var miVariableEjemplo = 45;

        var usuario = "Daniel";
        var titulo = "Estudiante";
        var union = titulo + " " + usuario;
        System.out.println("union = " + union);

        var a = 8;
        var b = 4;
        System.out.println(usuario + (a + b));
        //Ejercicios: Carectares especiales en Java

        var nombre = "Daniel";
        System.out.println("\nNueva linea\n" + nombre); //Diegonal inversa y letra n
        System.out.println("Tabulador: \t" + nombre); //Tabulado un espacio para centrar
        System.out.println("\t\t : MENU: .");
        System.out.println("Retroceso: \b\b" + nombre); //Caracter de retroceso
        System.out.println("Comillas simples: \'" + nombre + "\'");//Colocar comillas
        System.out.println("Comillas Dobles: \"" + nombre + "\"");// Colocar comillas dobles
         */
        //Clase Scanner
        /*Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: "+titulo2+" "+usuario2 ");
         */

 /* byte numEnteroByte = (byte) 129;
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor minimo del byte: " + Byte.MIN_VALUE);
        System.out.println("Valor maximo del byte: " + Byte.MAX_VALUE);

        short numEnteroShort = 10;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("Valor minimo del short: " + Short.MIN_VALUE);
        System.out.println("Valor maximo del short: " + Short.MAX_VALUE);

        int numEnteroInt = 10;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("Valor minimo del int: " + Integer.MIN_VALUE);
        System.out.println("Valor minimo del int: " + Integer.MAX_VALUE);
        
        long numEnteroLong = 10;
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor minimo del long: "+ Long.MIN_VALUE);
        System.out.println("Valor maximo del long: "+ Long.MAX_VALUE);*/
 /*float numFloat = 3.4028235E38F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("Valor minimo del float: "+ Float.MIN_VALUE);
        System.out.println("Valor mazimo del float: "+ Float.MAX_VALUE);
        
        double numDouble = 1.7976931348623157E308D;
        System.out.println("numDouble = " + numDouble);
        System.out.println("El valor minimo del valor double: "+ Double.MIN_VALUE);
        System.out.println("El valor maximo del valor double: "+ Double.MAX_VALUE);
         */
        // Inferencia de tipos var y tipos primitivos
        /*  var numEntero = 20; // Las literales sin punto automaticamente son del tipo int
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0F;
        System.out.println("numFloat = " + numFloat); // Automaticamente con el punto se transforma en tipo Double
        var numDoble = 10.0;*/
        
        //Tipos primitivos char
       /* char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
        
        char varCaracter = '\u0024'; //($)Indicamos a Java la asignacion con el codigo unicode
        System.out.println("varCaracter = " + varCaracter);
        char varCaracterDecimal = 36; //Valor decimal del juego de caracteres unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$'; //Un caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        
        var varCaracter1 = '\u0024'; //($)Indicamos a Java la asignacion con el codigo unicode
        System.out.println("varCaracter1 = " + varCaracter1);
        var varCaracterDecimal1 = (char)36; //Valor Entero y le asigna un tipo int
        System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
        var varCaracterSimbolo1 = '$'; //Un caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);
        
        int varEnteroChar = '$'; // Aca nos muestra el valor decimal referenciado al simbolo
        System.out.println("varEnteroChar = " + varEnteroChar);
        int caracterChar = 'g';
        System.out.println("caracterChar = " + caracterChar);
        */
        //Tipos primitivos tipos booleanos
        /*var varBool = true;
        System.out.println("varBool = " + varBool);
        
        if(varBool){
            System.out.println("La bandera es verde");
        }
        else{
            System.out.println("La bandera es roja");
        }
        
        //Algoritmo: ¿Es mayor de edad?
        var edad = 30; //Literal tener presente la inferencia de tipos
        //var adulto = edad >= 18; //Esta es una expresion booleana
        if (edad >= 18){
            System.out.println("Eres mayor de edad");
        }
        else{
            System.out.println("Eres menor de edad");
            */
        
        //Conversion de tipos primitivos
//        var edad = Integer.parseInt("20");
//        System.out.println("edad = " + (edad + 1));
//        var valorPi = Double.parseDouble("3.1416");
//        System.out.println("valorPi = " + valorPi);
//        
//        //Pedir un valor
       var entrada = new Scanner(System.in);
//        System.out.println("Digite su edad");
//        edad = Integer.parseInt(entrada.nextLine());
//        System.out.println("edad = " + edad);
       
        
        //Conversiòn de tipos primitivos en Java parte 2
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        var fraseChar = "programadores".charAt(0);
        System.out.println("fraseChar = " + fraseChar);
        
        System.out.println("Digite un caracter");
        fraseChar = entrada.nextLine().charAt(0); 
        System.out.println("fraseChar = " + fraseChar);
        
        
    }
}
