# Patrones de diseño
Los patrones de diseño son soluciones habituales a problemas
que ocurren con frecuencia durante el diseño del sofware. Podríamos verlos como 
"planos" que se pueden personalizar y modificar para adaptarlos a un problema concreto.
Aprender los patrones de diseño **no es estricamente necesario pero sí muy conveniente**.  
Es muy posible que hayas aplicado algún patrón de diseño a lo largo de tu vida sin saberlo. Sin embargo, es bueno "poner nombre"
a su solución con el fin de mejorar la comunicación entre desarrolladores (entre otros
beneficios). Es más fácil decir "he aplicado el patrón Singleton" a explicar lo que 
has implementado.
Además, dominando los patrones de diseño podrás tomar una decisión de diseño que
podrá ser entendida por todos los desarrolladores y consensuada mucho más fácil. 

Los patrones de diseño se dividen en tres grupos:
1. **CREACIONALES**
2. **ESTRUCTURALES**
3. **DE COMPORTAMIENTO**

## PATRONES CREACIONALES
Proporcionan varios mecanismos de creación de objetos que incrementan la flexibilidad y la reutilización del código 
existente. Los patrones de diseño creacionales son los siguientes:
![creacionales.png](../../Documents/creacionales.png)

### Patrón Singleton
Este patrón nos permite que solamente haya una instancia de la clase.  
Imagina que tienes un objeto logger. ¿Para qué querrías instanciar varios de ellos para la misma
funcionalidad? Para ello, se puede utilizar este patrón y controlar la cantidad de instancias de una 
clase. Si la clase ya ha sido instanciada. se devuelve esa instancia. Si no, se instancia y se devuelve.  
Otro ejemplo podría ser una pool de conexiones a la base de datos. Normalmente no vamos a querer instanciar
más de una pool de conexiones a base de datos, por lo que la creamos una vez y devolvemos la instancia.

> **IMPORTANTE**: tenemos que tener cuidado con la concurrencia, ya que la creación de la
primera instancia (la sección crítica) debe ser protegida para evitar condiciones de 
carrera.
`````python
python creacionales/singleton.py
`````

En el ejemplo podremos ver que la intentar instanciar dos veces la misma clase, la primera se instanciará
correctamente pero al segundo intento nos devolverá la clase anteriormente instanciada. No se sobreescriben
los valores de los atributos de instancia ya que no se llega a instanciar.

#### RESUMIDO
Si necesitamos una única instancia de una clase, usaremos este patrón. Casos de uso pueden ser
un único log, pool de conexiones a base de datos, acceso a fichero, etc.


### Patrón Prototype
Imagina que tienes un objeto de una clase y necesitas clonarlo. Para esto, tendremos que crear un nuevo objeto
y modificar todos sus atributos. Pero, ¿cómo sabemos el estado de los atributos privados una instancia? No podemos
conocer el estado "completo" de una instancia, debido a la encapsulación. Solo podremos conocer aquello que nos
proporcione la interfaz.  
Imagina que tenemos un coche y queremos tener otro igual. Entonces, podremos tener la misma carrocería, interior, etc. 
Sin embargo, no podremos copiar exactamente el motor, cómo arranca, etc. Este es el principal problema en la 
copia de objetos.  
El patrón Prototype nos da una solución para esto: declarar una interfaz para la clonación.
Lo que tendremos que hacer será declarar una interfaz con un solo método público (clone()) e implementar la 
interfaz con los métodos y atributos que necesitemos.
> En python, tenemos los métodos copy.copy() y copy.deepcopy(). Por lo tanto, no es necesario
> la implementación de este patrón, ya que viene "intrínseco" al lenguage

Si quisiésemos modificar el comportamiento, tendríamos que sobreescribir los métodos
**__copy__** y **__deepcopy__**
`````python
python creacionales/prototype.py
`````

#### RESUMIDO
Si necesitas una copia de un objecto, puedes utilizar este patrón. En Python ya viene
implementado este patrón "por defecto", ya que copy.copy() y copy.deepcopy() son métodos
para copiar de manera superficial y de manera profunda, respectivamente, un objeto.


### Patrón Builder
Imagina que necesitas construir un objeto complejo paso a paso.
Imaginemos que necesitamos crear un orquestador, que necesita una gran cantidad de
parámetros para controlar absolutamente todo lo que necesita (ya de por si, pasar más de 3 parámetros
no es muy recomendable), que a veces no se necesitan todos. Imaginemos también un 
constructor con 100 parámetros para una casa. Tenemos que incluir parámetros para un porche,
pero hay casas que no tienen porche. ¿Tendremos que pasar Null para ese valor?

Este patrón nos da una solución para esto. El patrón Builder nos dice que saquemos
el código para construir ese objeto (el código dentro del constructor) y lo 
coloquemos dentro de objetos independientes llamados **constructores**.

El patrón organiza la construcción del objeto con diferentes constructores. Es 
decir, el constructor "base" llamada a "constructores sencillos". Siguiendo 
el ejemplo de la casa, el constructor para una casa está "compuesto" por un 
constructor de paredes, un constructor del porche, etc. Lo bueno de esto es 
que puedes invocar a los constructores que necesites y no todos. Para ello, 
simplemente implementamos diferentes constructores de casa con diferentes pasos
constructores.

Vayamos a otro ejemplo: imaginemos que queremos crear una pizza. Sin el patrón
Builder, lo que se haría es crear un constructor con todos los parámetros posibles,
pudiendo ser None indicando que no se incluye ese "ingrediente". Sin embargo,
imagina un constructor con 20 parámetros. Una muy mala práctica. Para esto, podemos
utilizar este patrón e ir construyendo la pizza poco a poco. 

En el siguiente ejemplo, podremos crear una pizza con los ingredientes que queramos,
llamando a los métodos que se necesiten.
````python
python creacionales/builder.py
````

En este otro ejemplo, creamos los distintos builders para cada tipo de pizza
y cada uno creará una pizza distinta. Todos los builders implementan todos 
los métodos de la interfaz, pero algunos no hacen nada. Podríamos incluso
crear una interfaz builder por cada tipo de pizza. Esto es, uno para las vegetarianas, que 
no se le pueden añadir queso u otros ingredientes, por ejemplo. Y con este
ejemplo nos obliga a implementar el método set_cheese.

````python
pyhton creacionales/builder_2.py
````

### Resumido
Cuando necesites implementar una clase con un constructor con numerosos
parámetros, plantéate si se puede construir el objeto paso a paso, y si 
hay varios posibles objetos resultantes. Si es así, podrás usar este patrón.
Implementando una interfaz builder, que es la que define pero no implementa cada
uno de los pasos. Se implementarán tantos builders de esta interfaz como tipos
resultantes se necesiten y así evitarás tener un constructor con demasiados
parámetros, que pueden no ser usados.
