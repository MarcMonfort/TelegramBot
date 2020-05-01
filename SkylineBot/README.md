
El gràfic ha s'ha de veure desde la posició 0 fins la màxima posició del últim edifici, o hauria de d'anar des de la posició del primer edifici (visible o invisible?) fins la màxima posició del útlim edifici?
    Jo crec que seria més interessant si fos desde la posició 0

Al desplaçar el Skyline a l'esquerra, si algun edifici es troba a la part negativa, tallarem aquest, peró si la amplada arriba a una posició superior a cero, mostrarem aquella part. ¿Eliminem l'edifici, o únicament no el mostrem?

Al fer un mirror, ho farem des de la posició del primer edifici, o des de la posició 0? (depen de la primera pregunta) I si hi han edificis a la part negativa, ho farem des de 0

Empexar en el 0 o en el 1?

Podria aparecer problemas al compartir las lista en la operacion Skyline + N, pero como en ningun caso estamos modificando los valores internos, height i top de forma individual, entonces no hay ningun problema en compartir las listas. Y es mas eficiente, con menos espacio.

Mucho tiempo al generar el Plot. Para mejorarlo normalizamos y pintamos el numero mínimo de edificios.