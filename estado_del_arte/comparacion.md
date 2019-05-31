% Comparaciones tesis diseño redes rurales

según los autores *Sayandeep Sen y Bhaskaran Raman*[ ], en las últimas décadas se ha proliferado de manera masiva  el uso de internet, sin embargo, la expansión de la conectividad a internet se ha limitado solo en países desarrollados y  áreas metropolitanas de países en desarrollo, generando la brecha digital, que hace referencia a la distinción entre los que tienen acceso a servicios de internet y los que están excluidos de estos. Esto es realmente lamentable para los países en desarrollo como la India, donde alrededor del 74% de la población es rural y está en el lado equivocado de la brecha digital. una forma de cerrar esta brecha es mejorando  la conectividad en cada pueblo.

Proporcionar internet expandiendo la red de telefonía corriente no es factible debido a los altos costos de infraestructura inicial; sin embargo esto no es un problema en la telefonía móvil  debido a que es un modelo de negocio, ya que es un servicio demandado por una gran cantidad de clientes, lo que exige una mayor densidad de consumo bien pagado.


Disminuir la brecha digital es una tarea en la que tecnologías como IEEE 802.11 ha mostrado gran crecimiento y aceptación como solución debido a su bajo costo [Sen], aunque esta tecnología fue diseñada para conexión inalámbrica en interiores, se ha establecido la posibilidad de utilizar 802.11 en redes de larga distancia [sent, Bernardi].

Para mejorar la conectividad en grandes zonas de cobertura se han utilizado tecnologías emergentes como la 802.16 WIMAX, pero todavía no ha escalado a la producción en masa competitiva, haciendo que los equipos sean más caros, por esto los autores detallan que para estos casos la solución más viable es utilizar las tecnologías 802.11 de Wifi, ya que ha tenido un amplio crecimiento y gran aceptabilidad como una solución de acceso inalámbrica por su bajo precio.


_Sent_ propone la posibilidad de usar IEEE 802.11 como una opción para proporcionar conectividad a internet en zonas rurales en desarrollo permitiendoles acceso a los servicios de tecnología de información y comunicación. Las tecnologías 802.11 se  ha presentado como una opción de bajo costo y efectiva para cubrir largas distancias, ya que permite que zonas muy amplias puedan conectarse a un nodo de  línea terrestre con conectividad a internet de forma cableada (como fibra óptica) por medio de enlaces inalámbricos. Cada enlace inalámbrico corresponde a una antena en una torre instalada en cada pueblo, estos deben tener línea de vista **L.O.S.** (*line of sight*).

Gracias a su bajo costo esta tecnología sirve como herramienta para la planificación de redes minimizando el costo del sistema, se convierte entonces en una tarea trivial ya que tiene en cuenta los siguientes conjuntos de variables:

1. Afectan el coste del sistema
    - Topología de la red
    - Altura de las torres

2. Afectan el rendimiento global de la red
    - Tipos de antena 
    - Potencias de transmisión de radio



![Dependencias de requermientos a demás](dependencias.pdf){ width=70% }


Basado en un proyecto titulado ´Digital Gangetic Plains´ los autores argumentan que el costo principal en redes de larga distancia con 802.11 es el conjunto de torres de antenas, puesto que una antena puede valer $50, una torre de 30 m puede valer $1000, por esto es de vital importancia tener una buena planeación en la primera decisión de despliegue; la tesis de *Sayandeep Sen y Bhaskaran Raman* [] se enfoca en que el principal problema es minimizar los costos, por esto se hace énfasis en la planeación de una topología de red inalámbrica optimizando los costos el despliegue, cabe destacer que al igual que _Bernardi_ el despliegue con redes Ad-hoc no presta atención al costo del sistema y no permite escalar a grandes redes. Como característica definida se tiene que la falta de planificación impide que se garantice el rendimiento de la red.

Lla formulación en la construcción de una topología que permita el rendimiento de la red, se estipulan de tres principales restricciones:

1. Aplicación (restricción de rendimiento): Capacidad de carga y descarga por cada nodo o pueblo.
2. Restricción de Potencia: Se refiere al límite superior de la Potencia Isotrópica Irradiado (EIRP) en cada transmisor y el límite inferior de potencia recibida en el receptor (sensibilidad del receptor).
3. Restricción de interferencia: La señal recibida debe ser mayor al umbral de interferencia.

                   
Los ítems 1 y 3 Usan el protocolo de control de Acceso al medio MAC, sin embargo, [sent] plantea la implementación del protocolo 2PMAC debido a que permite a multiples enlaces operar simultáneamente (funcionamiento síncrono) y está específicamente diseñado para redes inalámbricas de larga distancia. Los protocolos MAC tienen limitaciones ya sea de acceso múltiple por división de tiempo (TDMA) o detección de portadora de Acceso Múltiple con prevención de colisiones (CSMA/CA), una en la que los enlaces operan en turnos predeterminados y la siguiente en la que los enlaces no tienen un orden predeterminado compitiendo por una pequeña duración para seleccionar el enlace que operara al mimo tiempo, respectivamente. De acuerdo al protocolo MAC utilizado se determina el máximo rendimiento alcanzable por un nodo en la topología y la potencia de transmisión de cada uno de ellos.

El problema de construcción de la topología se puede establecer como:

“ *Teniendo en cuenta, (a) las ubicaciones (coordenadas $<x, y, z>$) de un conjunto de aldeas que se proporcionarán con conectividad de red y la de la línea terrestre que proporciona y (b) el requisito de ancho de banda específico por nodo de aldea, lo que es la topología de costo mínimo que satisface las tres restricciones: rendimiento, interferencia y potencia.* ”

Los ítems 1 y 3 Usan el protocolo de control de Acceso al medio MAC, sin embargo, [sent] plantea la implementación del protocolo 2PMAC debido a que permite a multiples enlaces operar simultáneamente (funcionamiento síncrono) y está específicamente diseñado para redes inalámbricas de larga distancia. Los protocolos MAC tienen limitaciones ya sea de acceso múltiple por división de tiempo (TDMA) o detección de portadora de Acceso Múltiple con prevención de colisiones (CSMA/CA), una en la que los enlaces operan en turnos predeterminados y la siguiente en la que los enlaces no tienen un orden predeterminado compitiendo por una pequeña duración para seleccionar el enlace que operara al mimo tiempo, respectivamente. De acuerdo al protocolo MAC utilizado se determina el máximo rendimiento alcanzable por un nodo en la topología y la potencia de transmisión de cada uno de ellos.

Consideraciones de diseño y enfoque de solución para las variables

### Topología de Búsqueda (TS): 

Explorar el espacio de búsqueda para encontrar la topología de la red, se hace uso del algoritmo Branch-and-bound (Algoritmo de ramificación y límite), con ello se construye la topología de árbol.
      
### Asignación de altura (HA):
Consiste en la altura óptima de las torres en las ubicaciones dadas una vez que se ha formado la topología, para ello se utiliza un conjunto de ecuaciones de programación lineal (LP).

### Asignación de Antena (AA):
Asignación apropiada de las antenas y sus respectivas orientaciones, se desarrolla un algoritmo heurístico de tiempo complejo polinómico.

### Asignación de Potencias (PA):
Proporcionar las potencias de transmisión en los radios del sistema usando LP.

El objetivo principal es el de reducir el mínimo costo de implementación, sabiendo que el rendimiento de la red depende del tipo de enrutamiento y del protocolo MAC implementado. Por su simplicidad se propone la topología de árbol ya que proporciona una fácil conectividad y para este caso no aborda la tolerancia a fallos, cabe resaltar que utiliza un enrutamiento fijo.


El problema radica en el hecho de que las zonas rurales tienen baja densidad de usuarios y grandes distancias entre grupos de usuarios, esto conlleva a que compañías de telecomunicaciones o proveedores de internet (ISP) vean poco atractiva la inversión en estos lugares debido al costo inicial de infraestructura y despliegue de la red y bajo retorno de su inversión. 



Según Bernardi, en las últimas décadas se ha incrementado la conectividad de banda ancha, siendo la ADSL (del inglés Asymmetric digital subscriber line) con más del 60% de las conexiones de banda ancha en países de la Organización para la Cooperación y el Desarrollo Económicos es un organismo de cooperación internacional (OCDE); esto se debe principalmente al éxito de la capitalización de ADSL debido al éxito de la red de telefonía. Esta tecnología se caracteriza por que la tasa de trasmisión máxima que puede alcanzar esta en función de la distancia entre el usuario y la central telefónica, es decir, entre más larga sea la distancia, la velocidad de trasmisión es más lenta, por esta razón es comúnmente más utilizada en áreas metropolitanas debido a que tiene más suscriptores y sea más efectivo retornar la inversión de despliegue de una infraestructura. Esto es la principal causa de la brecha digital que existe entre las áreas rurales y metropolitanas. 

El internet satelital se podría decir que es una alternativa de conexión, puesto que está disponible prácticamente en cualquier parte y es frecuentemente subsidiada en áreas remotas incomunicadas, sin embargo, también tiene latencia de tiempo de ida y vuelta muy altos, lo cual lo hace inadecuado para aplicaciones que consuman un ancho de banda considerable, como es el caso de una videollamada (skape). 

Pero Bernardi expone el Despliegue de una red Rural de Banda Ancha (BWA) argumentando que la planeación ad-hoc no es una alternativa de diseño eficiente para este tipo de redes, sin embargo, refiere que la industria ofrece software para planeamiento de redes inalámbricas pero estos no están disponibles ni son adecuados para comunicar pequeñas comunidades y pequeños proveedores de servicio de Internet inalámbrico (WISP) ; cabe resaltar que las BWA usan un modelo de dos niveles, consistiendo en radioenlace Punto Multipunto (PMP) y Punto a Punto (PTP), el primero enlazando la Antena de la torre a los diferentes clientes y el segundo correspondiente al Backhaul.
A través del planeamiento de red incremental Bernardi  desarrolla un software denominado IncrEase cuyo enfoque es identificar la estrategia de despliegue más económica para planear la red teniendo en cuenta que los CPE (customer Premises Equipment) son la opción más rentable para llegar a la población en zonas rurales. 

Los proveedores de servicio de internet inalámbrico implementan una metodología de diseño para operar en escenarios rurales obteniendo remuneración de su inversión, este consiste en planificar su crecimiento ampliando su cobertura, tomando variables como:

- Limitar el alcance geográfico de los WISP:Para reducir los costos de operación
      
- Infraestructura de la red: En áreas rurales la fibra para el Backhaul no está disponible, por ello los WISP deben desplegar  su propio Backhaul inalámbrico, aumentando los costos.
      
- Cobertura de la red: El despliegue rural está basado en la cobertura más no en la capacidad
      
 - Presupuesto ajustado: Los proveedores de internet buscan obtener un retorno de su inversión desde su etapa de despliegue ya que las zonas rurales son entornos de baja rentabilidad
      
- Clientes agrupados: Proporcionar acceso a la red en sectores dónde haya más densidad de la población, para así captar más usuarios. 

La falta de herramientas de software para el diseño, gestión y evaluación de redes de acceso inalámbrico de banda han obstaculizado su despliegue generalizado a pesar de sus costos y ventajas operativas sobre otras alternativas de Tecnologías de acceso de banda. Bernardi desarrolla un paquete de software para llenar esta brecha, con especial énfasis en las regiones rurales y en desarrollo. Se resalta que abordó tres desafíos técnicos  en el contexto de redes de acceso inalámbrico de banda ancha:

- Mapeo de Banda Ancha
- Planeación de redes 
- Administración de redes


##Herramienta IncrEase

Se desarrolla un software de código abierto IncrEase implementado como una aplicación de escritorio multiplataforma en Java. IncrEase esta basado en un GIS de software libre de la NASA World Wind Java y en una base de datos gráfica Neo4J. 

Para la implementación de IncrEase se toman tres fuentes: 

- Demanda de la cobertura: Posibles usuarios de zonas rurales que no tienen acceso al servicio
- Usuarios que fallaron en la etapa de instalación: Cobertura insuficiente 
- Reporte mesas de ayuda:  Localización de los usuarios existentes

Además se obtienen otros datos de factores influyentes como la disponibilidad DSL, la cobertura de red 3G y datos demográficos. IncrEase  a través de datos en forma de arreglo bidimensional cubre regiones de interés y con ello obtiene mapas de calor (áreas de mayor beneficio por la actualización de la red). En estos mapas a mayor calor menor es la cobertura, una posible solución es la instalación de una torre a partir de una lista de torres disponibles en esa área. 

##Modo de operación herramienta IncrEase

Flujo de información de la herramienta 




- IncrEase Targeted: En este modo de operación el operador selecciona una región específica de cobertura, como parte de expansión de la red
      
- Búsqueda Estratégica: Dónde la herramienta guía al operador para decidir el orden de despliegue de sitios de transmisión en el horizonte de corto o largo plazo basado en la rentabilidad esperada
      
La contribución de Bernardi es potenciar el negocio de los pequeños proveedores de internet inalámbrico (WISP) en zonas rurales a través de un sistema de software, haciéndolo más eficiente reduciendo la brecha digital.




Aunque existen estructuras de algoritmos para solucionar problemáticas en la planeación incremental de redes inalámbricas [Whitaker] proporciona información sobre la evolución de modelos y técnicas para la planificación automática de servicios inalámbricos celulares, cabe resaltar que la documentación existente hace énfasis en redes móviles, sin embargo, este concepto es aplicable para el despliegue de redes inalámbricas rurales. Dentro de la planificación de los sistemas de comunicación inalámbrica se [whitaker] da claridad en los modelos de requerimientos, tales como la información sobre la ubicación de los lugares para la transmisión, este es necesario para establecer una optima conectividad, además de proporcionar información sobre el servicio prestado, aquí se tienen en cuenta los puntos de prueba de recepción (RTP), los puntos de prueba de servicio (STP)y los puntos de prueba de Tráfico (TTP). En cuanto a las especificaciones del equipo, se refiere al tipo y número de antenas a usar; incluye también un modelo de propagación para determinar la perdida de propagación de la señal de al antena al usuario.





