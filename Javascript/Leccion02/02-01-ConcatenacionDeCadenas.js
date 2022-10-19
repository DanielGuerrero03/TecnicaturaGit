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