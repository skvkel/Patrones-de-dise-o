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