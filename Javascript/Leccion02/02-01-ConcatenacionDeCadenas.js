var nombre = "Daniel ";
var apellido = "Guerrero";
var nombreCompleto = nombre+" "+apellido; //Primera concatenacion
console.log(nombreCompleto);
var nombreCompleto2 = "Manuel"+" "+"Fernandez"; //Segunda concatenacion
console.log(nombreCompleto2);
var juntos = nombre +219; // Lee de izq a derecha siguiendo la cadena lee el numero como str
console.log(juntos);
juntos = nombre + 78 + 17; // aqui se puede diferenciar a traves de los parentesis
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido; // Tercera Concatenacion usando el operador simplificado
console.log(nombre);

// Hoy ya no se usar var, se utiliza let y const
let nombre2 = "Pedro"
console.log(nombre2);

const apellido2 = "Lepes";
//apellido2 = "Peres"; una constante no puede ser modificada
console.log(apellido2)

let x, y; // Se pueden crear varias variables dentro de una misma linea
x = 17, y = 21; //Se puede hacer asignacion de varias variables dentro de una misma linea
let z = x + y; //Se asigna valor de la operacion
console.log(z);

let _1num = 31; // No utilizar numeros para iniciar el nombre de una variable
let rompiendo = "rompe"; // Bo utilizar palabras reservadas para variables

console.log(_1num)
console.log(rompiendo)