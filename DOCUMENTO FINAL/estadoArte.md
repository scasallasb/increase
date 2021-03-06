
# Capítulo 1. El problema

## Planteamiento del problema

En Colombia, se puede apreciar la baja accesibilidad de banda ancha en zonas rurales, ya que de acuerdo con “Estado de la banda ancha en América Latina y el Caribe” dado por la Comisión Económica para América Latina y el Caribe [@cepal2017], menos del 10% de esta población tiene accesibilidad a servicio de banda ancha en el territorio nacional. Además, se espera que para los próximos años la comisión de regulaciones de las Comunicaciones aumente el ancho de banda para las zonas rurales, para el año 2020: 1 Mbps a 10 Mbps de bajada y de 512 Kbps a 1Mbps [@crt2016], lo cual, si comparamos esto con los datos actuales que se tienen del ancho de banda en la red libre de Bosachoque [@florez2018], se puede evidenciar que no se alcanzara el nivel de banda ancha, por lo tanto, es necesario modificar la red, y para esto los Proveedores Inalámbricos de Servicios de Internet WISP solo pueden tomar dos acciones para extender su cobertura de banda ancha, estas son Incrementar la cobertura de red, o mejora las áreas ya existentes. En ambos casos, estas acciones son limitadas por el presupuesto y solo un pequeño conjunto de acciones pueden ser ejecutadas.

La planeación de redes se convierte en un proceso fundamental para estos casos, sin embargo, existen gran cantidad de software para el planeamiento de redes inalámbricas, pero estas herramientas a menudo no están disponibles, ni tampoco son adecuados para comunicar pequeñas comunidades y pequeños WISP (en este caso la Universidad de Cundinamarca) [@bernardi2012]. El difícil acceso a herramientas de planeación de redes inalámbricas limita la presencia de ISP en zonas rurales ya que ellos no saben con certeza como invertir en infraestructura que permita acceso a internet de banda ancha. Las comunidades excluidas de la banda ancha corren el riesgo de quedar al margen de toda una gama de aplicaciones y ventajas que proporciona Internet, dejando a un lado la posibilidad de generar un desarrollo económico [@onu2013].

¿Cómo planificar la expansión estratégica de la Red Libre de Bosachoque con un
algoritmo de planificación de redes inalámbricas en zonas rurales?

## Objetivos del estudio

### Objetivo general

Diseñar un algoritmo para la planeación incremental de redes inalámbricas en áreas rurales evaluándolo en la red Libre de Bosachoque

### Objetivos específicos 

* Generar el estado del arte de los algoritmos utilizados en la planeación de redes inalámbricas que permitan identificar y determinar los requerimientos del algoritmo que sugieran la mejor estrategia de expansión de una red

* Diseñar un algoritmo que permita identificar la mejor estrategia de expansión de la red inalámbrica en zonas rurales

* Evaluar el algoritmo mediante una simulación numérica, comparándolo con Heurística simple.

* Aplicar el algoritmo diseñado en la red libre de Bosachoque analizando los resultados obtenidos

## Justificación

 El acceso a Internet de banda ancha tiene impactos positivos en la sociedad, puesto que contribuye de manera significativa al crecimiento económico en muchos aspectos, ya que mejora la productividad, facilita la adopción de procesos de negocio eficientes ,aumenta la innovación y mejora los procesos de funcionamiento en las empresas [@uit2012], por esta razón la Comisión de Ciencia y Tecnología para el Desarrollo de las Naciones Unidas mediante su informe “El acceso de banda ancha a Internet como medio de lograr una sociedad digital inclusiva” véase en [@PNUD2018], sugiere a todas las naciones miembros de la ONU (“Organización de las Naciones Unidas”) aumentar los esfuerzos de que todas las personas y comunidades tengan acceso a banda ancha. Sin embargo, la falta de accesibilidad a banda ancha en zonas rurales se debe a que los Proveedores de Servicios de Internet ISP, tienen que desplegar su infraestructura en lugares donde probablemente no retornaran su inversión, por esto, es importante planificar un óptimo despliegue o actualización de la red. En la actualidad, se encuentran toneladas de software para la planeación de redes, sin embargo, estas están enfocadas al planeamiento de redes de banda ancha de telefonía móvil [@hilarie2008] y redes inalámbricas locales WLAN [@bosio2007], mientras que para la planificación de redes BWA en zonas rulares estos enfoques son limitados por la comunidad de investigación.

Nuestro enfoque está basado en las necesidades de guiar WISP en áreas rurales que se enfrentan con el único reto de extender su rendimiento con inversiones estrechas en un ambiente de ganancias limitadas. La clave para tales organizaciones es identificar la estrategia de despliegue más económica para planear su red mientras se toma en consideración su cobertura. Por esto, en el presente anteproyecto, se propone el diseño de un algoritmo de optimización, que permita identificar el camino de solución de menor costo, seguido del desarrollo de un software que permita mostrar visualmente las posibles acciones a seguir, para finalmente, implementar el presente software en la Red Libre de Bosachoque, en donde se evaluará los resultados.

### Beneficios tecnológicos

Se dará a conocer una nueva perspectiva a las WISP en la planificación de redes BWA en zonas rurales, incentivando la conectividad y accesibilidad a la banda ancha, además de que tendrá accesibilidad a la herramienta , puesto que se tiene previsto el desarrollo de un software libre, el cual podrá ser propenso a actualizaciones o mejoras por parte de la comunidad tecnológica, además de que fomentará la posibilidad de generar otras herramientas de software para la solución de problemas de optimización y planeación de redes.

### Beneficios institucionales

El desarrollo del proyecto permitirá al programa de ingeniería electrónica de la Universidad de Cundinamarca a contar con una herramienta que permita el desarrollo económico de la comunidad rural del municipio (vereda de Bosachoque) y demás lugares donde esta herramienta se pueda implementar, además que permitirá mejorar el servicio como WISP, que presta la Universidad en la Red Libre de Bosachoque. También permitirá el fortalecimiento del semillero de investigación Kinestasis, fomentando el desarrollo de herramientas tecnológicas al servicio de la sociedad.

### Beneficio social

La herramienta permitirá sugerir las mejores decisiones al momento de planear una red o mejorar la cobertura de Internet de banda ancha, llevando consigo un desarrollo económico, puesto que la comunidad podrá tener a su disponibilidad un sin fin de herramientas que permitan generar un desarrollo económico en el entorno, además de fortalecer el sector rural y disminuir la brecha digital que existe en los países en desarrollo.

## Alcances y limitaciones

### Alcances

El presente proyecto tiene como objeto diseñar un algoritmo para la planeación incremental de redes inalámbricas que permita sugerir las mejores opciones para incrementar la cobertura de ancho de banda y acceso a internet en zonas rurales. 
Este algoritmo se implementará y evaluará en la red libre comunitaria de Bosachoque, se espera que sea una herramienta adecuada que permita la toma de decisiones al momento de planificar la expansión de la red, además se plantea la base para desarrollar futuros trabajos en el campo de las redes y las telecomunicaciones como puede ser el diseño de un software.

### Limitaciones

El proyecto estará limitado por la infinidad de soluciones válidas para realizar la planeación incremental de una red ya que se pueden generar problemas de
algoritmos como bucles infinitos, NP-hard, entre otros. 
En la evaluación se tiene limitaciones en cuanto a infraestructura disponible para desplegar torres nuevas, nodos nuevos, ampliación de nodos, y demás acciones sugeridas por la herramienta.


# Capítulo 2. Marco referencial

## Antecedentes

El acceso a Internet a través de las tecnologías de la información y las comunicaciones (TIC) se ha convertido en un instrumento fundamental de desarrollo social, económico, político y cultural para los gobiernos y sociedades en todo el mundo, lo que ha conllevado a un desarrollo digital.

El desarrollo digital hace referencia a aspectos como Infraestructuras que faciliten el acceso universal, geográfico y social a las tecnologías; sector TIC respecto a la industria tecnológica existente; competencias digitales o nivel de alfabetización digital en un tiempo determinado; marco legal y regulatorio referente a normatividad, políticas y estrategias de las TIC; contenidos y servicios que incluye la oferta de servicios digitales[@maseratti2011].

Aunque la era digital es un fenómeno mundial existente en países más desarrollados que otros, conlleva a la denominada brecha digital que es la ausencia de una o varias dimensiones contenidas en el desarrollo digital, es esta entonces un reto para la sociedad de la información.

Una alternativa para disminuir la brecha digital, son las redes Libres comunitarias (RLC), entendidas no solo como redes de computadores sino como redes comunitarias implementadas en poblaciones vulnerables donde el acceso a la información es una posibilidad y no una realidad [@gordillo2013].

Debido a que las redes comunitarias por lo general se encuentran desplegadas en áreas geográficamente separadas, se utilizan tecnologías inalámbricas como mesh y radioenlaces usando bandas libres como la de 2,4 GHz; Las tecnologías inalámbricas son ampliamente utilizadas en áreas rurales, ya que, por cuestiones de acceso e infraestructura, las tecnologías cableadas no resultan ser viables para estos casos, dando como solución las redes inalámbricas comunitarias (WCN) [@flickenger2008] . Además, en este tipo de redes, se emplean materiales que pueden ser adquiridos por la comunidad, y donde este autor muestra una guía detallada para realizar conexiones inalámbricas, que permitan conectar con un ancho de banda significativo lugares remotos y de difícil acceso, además de tener un enfoque orientado a países en desarrollo. En varias partes del mundo se pueden encontrar diferentes redes comunitarias, un ejemplo bastante significativo y de gran éxito es la red guifi.net, que comenzó en 2004 en la comarca de Osona (Catalunya), este es un proyecto tecnológico, social y económico, impulsado desde la ciudadanía que tiene por objetivo la creación de una red de telecomunicaciones abierta, libre y neutral, basada en un modelo de procomún
[@guifi.net2016]. Guifi.net tiene a la fecha de diciembre de 2016, 32.500 nodos activos y se calcula que más de 50.000 personas reciben servicio de Internet gracias a esta red. Sin embargo, el éxito de esta red no radica especialmente en la gran cobertura que ofrece y de cómo ha sido el impacto en los países en que se ha desarrollado, sino que según (Roger 2015), ha permitido mostrar la importancia de mantener la infraestructura de la red como bien colectivo ya que el principio subyacente detrás de guifi.net es la firme convicción de que la mejor manera de mantener una red es estableciéndola como un recurso colectivo común (CPR).

A pesar que gran parte de los nodo están conectados con tecnología WiFi en Guifi.net, también utiliza tecnología cableada y de fibra óptica, debido a que se desarrolló en gran parte en zonas urbanas, sin embargo como ya hemos mencionado, la WCN ha tenido gran participación en zonas rurales, en este enfoque se destaca una red inalámbrica mesh (WMN), desplegada por la universidad de Lancaster en Wray (Inglaterra), proporcionando servicio de Internet a una villa en un área aproximada de dos kilómetros por un periodo de tres años [@ishmael2008].  Esto a pesar de haber tenido algunas limitaciones y complicaciones, muestra cómo se tuvo que reeducar a la gente para que se pueda hacer uso de la red de la mejor manera, dando como resultado la disponibilidad de banda ancha y mejorando la calidad de los servicios que se prestan.

En el ámbito local, en Bogotá se han desplegado diferentes redes inalámbricas comunitarias, las cuales valen la pena resaltar a pesar de no ser un entorno rural, estas muestran la forma de cómo se puede hacer inclusión social a sectores populares, en esta aparece [@pedraza2012], una red desplegada desde la Universidad Francisco José de Caldas, la cual muestra desde el proceso de selección de puntos donde se desplegaron los nodos, hasta la evaluación de los resultados después de su despliegue; en esta investigación se logró ampliar la cobertura en más de 40% con el uso de antenas artesanales, utilizando guías y herramientas propuestas por [@flickenger2008] , demostrando, que la participación de la ciudadanía es fundamental para el éxito de estas redes.

### Descripción de la red de Bosachoque Libre

La Red Bosachoque Libre es un macroproyecto misional de investigación de la Universidad de Cundinamarca de Facultad de Ingeniería (redes libres como alternativa de innovación social e inclusión digital en la vereda Bosachoque del municipio de Fusagasugá), con el fin de proveer servicio de Internet a la vereda Bosachoque utilizando conexiones inalámbricas, dado que, por ser una zona rural, una conexión cableada sería costosa y difícil. Esta red, se implementó con el fin de generar a la comunidad una herramienta que permita la conectividad, fomentando el desarrollo y crecimiento de esta, utilizando las tecnologías, protocolos y herramientas típicas de una red inalámbrica en países en desarrollo. El proceso de cómo se planeó esta red se encuentra documentado en [@achury2018].

La red de Bosachoque fue planeada e implementada como una red BWA (acceso inalámbrico de banda ancha “Broad Band Wireless Access”) de dos niveles, nivel de back-haul donde de manera inalámbrica se adquiere el servicio de internet y nivel de acceso donde se conectan los usuarios finales.
El nivel back-haul hace referencia a los sitios de transmisión que están interconectados usando enlaces inalámbricos punto a punto de larga distancia (PTP), mientras que el nivel de acceso proporciona conectividad al equipo del cliente (CPE) a través de un enlace punto multipunto (PMP).

La universidad de Cundinamarca sede Fusagasugá hace la función de proveedor de servicio de Internet (ISP) con el fin de desarrollar y ejecutar el macroproyecto mencionado.

Para el diseño, se especificó un DNS, este se tomó a partir del DNS asignado a la universidad de Cundinamarca, el cual es 200.14.41.2 y, como respaldo se utilizó el DNS de Google 8.8.8.8, además, la red cuenta con servicios de DHCP y firewall, cumpliendo con las especificaciones de enrutamiento y seguridad que una red de esta magnitud debe tener.

El dimensionamiento del número de usuarios se estableció según el POT (plan deordenamiento territorial) 2014, cuyos datos reposan de manera oficial en la alcaldía de Fusagasugá, donde se consta que en esta población rural se encuentran un número aproximado de 4000 personas, por ende, el direccionamiento está diseñado para suplir de servicio de Internet a la comunidad a un total de 4000 Host. 

En este nivel se utiliza un enrutador y una antena Access Point ubicada en la Universidad de Cundinamarca específicamente en el bloque F, donde por medio de un enlace punto a punto (PTP) y utilizando dos antenas RocketM5 AC a una frecuencia de trabajo entre 5.2 GHz 5.8 GHz , se direcciona a un punto ubicado en la vereda san José del chocho del municipio de Silvania-Cundinamarca; Aquí se encuentra el nivel de acceso , donde un enlace multipunto con topología anillo se encarga de la distribución de la señal por medio de una antena sectorial Rocket Prism AC, a todas las subredes que se encuentra dentro de la vereda Bosachoque [@achury2018].

## Marco Teórico  


### Brecha Digital


En el año 1995 eclosionan para la población dos tecnologías totalmente disruptivas, Internet y la telefonía móvil, ellas sugieren una nueva revolución, la llamada revolución digital, que a su vez crea la sociedad de la información (S.I), dando inicio al planteamiento sobre cómo medir y modelizar la S.I, el nivel de desarrollo digital y el impacto del desarrollo digital en el ser humano. De igual manera, el acceso a Internet a través de las Tecnologías de la Información y las Comunicaciones (TIC) ha tenido un auge exponencial en los últimos años, en efecto, este avance se presenta en países desarrollados o zonas metropolitanas de países en desarrollo [@sen2007], sin embargo, existen unas comunidades con poco o ningún acceso a las TIC [@maseratti2011] y otras con acceso casi universal a telefonía fija, móvil e Internet de banda ancha, es así que resulta el concepto de **brecha digital** entendiéndose como la ausencia de una o varias dimensiones contenidas en el desarrollo digital. En relación con lo anterior, las poblaciones sin acceso a las TIC poseen un bajo nivel socioeconómico, viven en zonas de difícil acceso con condiciones climatológicas desfavorables e incluso con ineficiencia o inexistencia de redes eléctricas, al mismo tiempo, las personas que viven en áreas rurales sufren el efecto de la brecha digital incluso más fuerte que los habitantes urbanos, debido a que no pueden acceder a servicios como el aprendizaje a distancia, la salud y el comercio electrónico [@bernardi2012].
 
 ![Brecha Digital](imagen_brdigital.pdf){width=10sss0%}

 La ilustración 1 enmarca la definición de Brecha Digital en donde se aprecia que es la separación entre personas, comunidades y estados que tienen o no acceso a las Tecnologías de las Información y las Comunicaciones debido a la falta de infraestructura, difícil acceso a zonas apartadas de centros poblados y su nivel de alfabetización digital. 


### Redes Libres Comunitarias  



Una alternativa para disminuir la brecha digital, son las Redes Libres Comunitarias (RLC), entendidas no solo como redes de computadores sino como redes comunitarias implementadas en poblaciones vulnerables donde el acceso a la información es una posibilidad y no una realidad [@gordillo2013].

Una red libre comunitaria, es una red troncal, dividida en subconjuntos de redes construidas y gestionadas de manera colectiva por la comunidad, la cual se involucra en la red de forma activa y participativa.


#### Principios generales

- Libertad de utilizar la red para cualquier propósito mientras no se perjudique el funcionamiento de la propia red, la libertad de otros usuarios, y se respete las condiciones de los contenidos y servicios que circulan libremente.  

- Libertad de conocer como es la red, sus componentes y su funcionamiento, también se puede difundir su espíritu y funcionamiento libremente.
       
- Libertad para incorporar servicios y contenidos a la red con las condiciones que se quiera. 
      
- Libertad de Incorporarse a la red y ayudar a extender estas libertades y condiciones [@guifi.net2016].  

#### Características de RLC  



- Abiertas: porque todo el mundo tiene el derecho a conocer la forma en que
se construyen.

- Libres: ya que el acceso a esta red está impulsado por un principio de no
discriminación, por lo que son de acceso universal.


- Neutrales: porque cualquier solución técnica disponible se puede emplear para ampliar la red, y porque la red se puede utilizar para trasmitir datos de cualquier tipo por cualquier participante, incluyendo también fines comerciales(@guifi.net2016). 


Debido a que las redes comunitarias por lo general se encuentran desplegadas en áreas geográficamente separadas, se utilizan tecnologías inalámbricas como mesh y radioenlaces usando bandas libres como la de 2,4 GHz; las tecnologías inalámbricas son ampliamente utilizadas en áreas rurales, ya que, por cuestiones de acceso e infraestructura, las tecnologías cableadas no resultan ser viables para estos casos, dando como solución las redes inalámbricas comunitarias (WCN)  en donde ya se han realizado trabajos importantes como se muestra en [@flickenger2008].




### Planeación de Redes Inalámbricas



Una red inalámbrica es la interconexión de varios nodos entre sí mediante la transmisión y recepción de señales electromagnéticas sin ninguna guía, empleando como medio el aire o el espacio vacío.  La planificación de redes supone la definición de requisitos para la creación de una infraestructura que permita conectar estos sistemas a través de una red [@IBM2019], se debe agregar que, la planeación de redes inalámbricas es un área muy activa por la comunidad científica, sin embargo, el foco de las investigaciones son las redes de banda ancha móvil y redes de área local inalámbrica. 


#### Factores clave de la planeación  



A continuación, se detallan factores claves de la planeación de redes inalámbricas.

* Costos de despliegue: valor inicial de instalación de la red.

* Costos de implementación: coste del mantenimiento y funcionamiento de la red.

* Expansión de la red: crecimiento de la red, abarcando más territorio.

* Cobertura de la red: área geográfica que cubre la red.

* Capacidad de la red: ancho de banda requerido para la transferencia de datos.

* Retorno de la inversión: beneficio obtenido en relación a la inversión realizada.





### Algoritmos utilizados en la planeación




Aunque existen estructuras de algoritmos para solucionar problemáticas en la planeación incremental de redes inalámbricas [@Whitaker] proporcionan información acerca de los enfoques propuestos para el diseño de redes, que muestran la evolución de modelos y técnicas para la planificación automática de servicios inalámbricos celulares, cabe resaltar que la documentación existente hace énfasis en redes móviles, sin embargo, este concepto es aplicable para el despliegue de redes inalámbricas rurales. Dicho lo anterior, *Whitaker* facilita la descripción de diferentes clases de algoritmos que se pueden usar para realizar la planeación de redes inalámbricas.



* **Algoritmos voraces**

Es una estrategia de búsqueda por la cual se sigue una heurística consistente en elegir la opción óptima en cada paso local con la esperanza de llegar a una solución general óptima. El procedimiento central del algoritmo voraz apunta a asignar las mejores ubicaciones posibles a un conjunto dado de estaciones base activas.



* **Algoritmos genéticos (GA)**

Estos algoritmos imitan algunos de los procesos de evolución y selección natural al mantener una población de soluciones candidatas que están representadas por una cadena de genes (con frecuencia binarios). Con el tiempo, la población evoluciona a través de procesos que emulan procesos biológicos como la reproducción. Los miembros de la población se combinan para producir descendientes. El concepto básico es que los fuertes tienden a adaptarse y sobrevivir, mientras que los débiles tienden a desaparecer. En la planeación de redes se utiliza la optimización de varios objetivos, estos se conocen como optimización multiobjetivo, en la que existe más de una solución óptima con respecto a todos los objetivos, entre ellos lugar de instalación de una torre, configuración de una antena,asignación de altura, etc.

 <!-- cambiar de definición-->

* **Búsqueda tabú (TS)**

La búsqueda tabú es un algoritmo heurístico de nivel superior para resolver problemas de optimización combinatoria.  Es un procedimiento de mejora iterativo que comienza a partir de cualquier solución inicial y trata de determinar una mejor solución. TS (por sus siglas en inglés *tabu search*) se caracteriza por su capacidad para evitar el atrapamiento en la solución óptima local y para evitar los ciclos, utiliza una memoria visible del historial de búsqueda. Normalmente, el algoritmo TS comienza sin conocer la solución correcta, dependiendo completamente de las respuestas del entorno que interactúa para llegar a la solución óptima (@Abido2002). Este algoritmo permite encontrar una ubicación de las torres en la fase de planeación para lograr un óptimo rendimiento de la red.



### Representación de la topología



Topología se refiere a la configuración de la red, es decir, a su forma de conectividad física en la que los dispositivos intercambian datos entre sí.

Para diseñar la infraestructura de la topología de la red requerida, es necesario describir la topología por medio del uso de grafos ya que es a través de esta estructura de datos que se elabora el procesamiento computacional del problema [@rios2015]



#### Grafo

Un grafo en el ámbito de las ciencias de la computación es un tipo abstracto de datos (TAD), que consiste en un conjunto de nodos (también llamados vértices) y un conjunto de arcos (aristas) que establecen relaciones entre los nodos. Formalmente se representa mediante el par $G=(V, A)$, dónde:



* $V$ es un conjunto de objetos llamados vértices o nodos.

* $A$ es un conjunto de objetos denominados aristas o arcos.

* Las aristas representan relaciones entre los vértices, de forma que una arista es un par $(u,v)$ de vértices de $V$.



##### Herramientas de manipulación de grafos


* **Python**

Python es un lenguaje de programación multiparadigma, ya que soporta orientación a objetos, programación imperativa y, en menor medida, programación funcional. Además, por ser un lenguaje de programación de licencia libre, se han desarrollado un gran número de paquetes, librerías y Framework que permite trabajar un sinfín de aplicaciones, entre estas se encuentra Networkx.


* **NetworkX**


NetworkX es un paquete de Python para la creación, manipulación y estudio de la estructura, dinámica y funciones de redes complejas.  

NetworkX proporciona:

* Herramientas para el estudio de la estructura y dinámica de redes sociales, biológicas y de infraestructura;  

* Una interfaz de programación estándar e implementación de gráficos que es adecuada para muchas aplicaciones;  

* Un entorno de rápido desarrollo para proyectos colaborativos, multidisciplinarios;  

* Una interfaz para los algoritmos numéricos existentes y el código escrito en C, C ++ y FORTRAN;

* La capacidad de trabajar con grandes conjuntos de datos no estándar.  


 
NetworkX permite cargar y almacenar redes en formatos de datos estándar y no estándar, generar muchos tipos de redes aleatorias y clásicas, analizar la estructura de la red, construir modelos de red, diseñar nuevos algoritmos de red, dibujar redes entre otros. [@NetworkX2019]. 



## ESTADO DEL ARTE

### Planeación de redes móviles UMTS   


En [@hilarie2008], se presenta una literatura detallada de los problemas que se presentan en la planeación de la topología celular 3G, la cual está basada en el Sistema universal de telecomunicaciones móviles **UMTS** (“*Universal Mobile Telecommunications System*”); para entender las dificultades que se presentan en la planeación, es importante hacer una pequeña descripción de la arquitectura UMTS.


Una arquitectura típica de   UMTS se muestra en la figura (1), donde se observa que una red UMTS está dividida en dos partes: la *red de acceso* y la *red de núcleo*. La primera, es también llamada red UMT de radio terrestre **UTRAN**, la cual está compuesta por muchos subsistemas de red de radio **RNS** (“*radio network subsystem*”). Cada RNS contiene un controlador de red de radio **RNC** (“*radio network controller*”) y una o más estaciones bases *BS* (“*base estation*”).

![Estructura básica de una infraestructura UMTS. Tomado de @hilarie2008](UMTS.pdf)

Las estaciones bases (en este caso son los *nodos B*) son usados para trasmitir/recibir radiofrecuencia hacia/desde los usuarios móviles, mientras que las RNC se ocupa de los recursos y la gestión de tráfico de datos. El principal objetivo de la UTRAN (“*UMTS Terrestrial Radio Access Network*”) es hacer el enlace entre los usuarios móviles y el núcleo red.




<!-- estructura de la planeación -->



#### Planeación de Celda



El autor *Hitlarie*, descompone la planeación de las redes móviles de manera modular, con el fin de reducir la complejidad y los divide en los siguientes subproblemas:



* Subproblemas de planeación de celdas.

* Subproblemas de planeación de red de acceso.

* Subproblemas de planeación de núcleo de red.



La parte de los subproblemas que se necesita abordar con más detalle, son los de planeación de celdas, ya que se asemeja más al enfoque que se necesita en la planeación de redes inalámbricas de banda ancha; a continuación, se describe dicho subproblema, así como algunos trabajos que se han realizado.



<!-- Descripción  de subproblema de celdas... -->

##### Subproblemas de planeación de celdas



El problema inicial de planeación es cubrir todos los usuarios móviles en un área determinada con el número mínimo de BSs. En la planeación de celdas se encarga de resolver los siguientes ítems:



* Optimizar el número de BSs.

* Mejor localización para instalar BSs.

* Escoger el tipo o modelo de BSs.

* Configuración (altura, orientación, potencia, etc).

* Asignación de usuarios móviles a la BS.

Los problemas de planeación pueden variar dependiendo en la planeación de red objetivo. Usualmente, en la planeación de red se requiere:



* Minimizar los costos de la red.

* Maximizar la calidad de la señal.

* Maximizar el área de cobertura.


Sin embargo, esto puede ser contradictorio, ya que, por ejemplo, si se quiere maximizar la cobertura se necesitarán desplegar más BSs y esto por supuesto, aumentara los costos. Al principio, la planeación de redes inalámbricas se realizaba teniendo en cuenta la predicción de la señal, sin embargo, en las redes UMTS, la planeación de radio no puede ser solo basado en la predicción de la señal, sino que se deben tener en cuenta la distribución de tráfico. En esta parte aparece gran cantidad de literatura del autor Amaldi, en [@amaldi2003], el autor contextualiza que en la planeación de radio en el Sistema Global para las Comunicaciones Móviles GSM (“*Global System for Mobile communications*”) se realizaba en dos fases, la fase de planeación de cobertura donde se define la mejor localización de las BSs teniendo en cuenta los modelos de propagación y la fase de planeación de frecuencia, que define el número de canales para cada BS teniendo en cuenta la calidad de la señal de interferencia de radio SIR (“*Signal-to-Interference Ratio*”).


Sin embargo, teniendo en cuenta el Acceso Múltiple por División de Código de Banda Ancha W-CDMA (“*Wideband Code Division Multiple Access*”), esto ya no se puede realizar en estas dos fases, debido a que el ancho de banda es compartido por todas las conexiones activas y no por la frecuencia asignada, así como también el área de cobertura de cada BS es afectada por la cantidad de tráfico.  



Para la planeación de celdas, se tiene en cuenta los parámetros de calidad de la SIR, en el cual se define una SIR mínima, el cual depende de la potencia recibida; Esta depende de la potencia trasmitida y las atenuaciones de señal en la propagación, por ende la potencia trasmitida se puede ajustar para minimizar la interferencia, aquí aparece un concepto importante, el cual es el control de potencia PC (“*power control*”), en donde se ajusta la potencia de trasmisión para cumplir dos objetivos, la potencia objetivo recibida $P_{tar}$ y la SIR objetivo $SIR_{tar}$. En este articulo *Amaldi* propone un modelo de programación matemática, que ayuda en la decisión de planear redes móviles, teniendo en cuenta la mejor localización y configuración de las BSs, teniendo en cuenta el modelo de propagación *Hata*, donde se ajusta el PC y  este a su vez es probado con un algoritmo aleatorio voraz, el cual añade o remueve BSs de la topología; En este artículo se describe el rendimiento de esta solución dando resultados óptimos  y también demuestra que este problema es un problema típico de NP-hard. Este trabajo se resalta por ser pionero en la planeación de celdas.


En la planeación de redes, a menudo se utiliza la optimización de varios objetivos, más conocido como optimización multiobjetivo, el cual es diferente de una optimización simple , puesto que aquí solo importa optimizar un parámetro, dando como resultado el mejor diseño o la mejor optimización, teniendo en cuenta un máximo o un mínimo global que dependerá del objetivo de la optimización (maximizar o minimizar), sin embargo, en  la optimización multiobjetivo existe más de una solución óptima con respecto a todos los objetivos; aquí, el objetivo consiste en encontrar un óptimo de Pareto, el cual nos dice que una solución es óptima  cuando no existe otra solución tal que mejore en un objetivo sin empeorar al menos uno de los otros.  



Como se ha visto anteriormente, en la planeación se pueden abordar diferentes objetivos (lugar de instalación de BS, configuración, altura, potencia, etc.), sin embargo, al momento de planificar la red, atacar todos los problemas al tiempo es un problema complejo, por esto, se han venido implementando algoritmos multiobjetivo, generalmente para estos casos se han venido desarrollando algoritmos genéticos AG, en el trabajo de [@raisanen2005], los autores recolectan cuatro estados del arte de algoritmos genéticos multiobjetivo, donde  los ponen a prueba para planificar una red aumentando la cobertura teniendo en cuenta los costos  y los comparan teniendo en cuenta su desempeño en ciertas pruebas sintetizadas; los autores toman como referencia los algoritmos: **SPEA2**, **NSGAII**, **PGSA** y **SEAMO**. A continuación, se hará una breve descripción de cada uno.  



* **SPEA2** (*The Strength Pareto Evolutionary Algorithm version II*)



La población inicial es sometida a una función de adecuación (“Fitness Function”), donde se escoge el valor individual más apto o el más “*fit*” de la unión del archivo y la población hija. El valor de la función de adecuación está dado por la suma de dos partes: cuantas soluciones domina (“*raw fitness*”) y la *densidad estimada*, el cual es la proximidad de otras soluciones en el espacio objetivo. Cada generación $n$ es guardada en el archivo, en donde es de nuevo aplicado el operador a la nueva generación; Este proceso se repite hasta terminar el proceso.



* **NSGA II**



El individuo más apto está determinado por la unión del archivo y la población hijo, determinado por mecanismos de clasificación compuesto de dos partes. La primera parte está compuesta al determinar la capa de soluciones que no son dominadas, es decir, las que están más cerca al frente de pareto. La segunda parte es una medida de dispersión, determinada por la distancia de hacinamiento crowding distance), el cual se escogerá el que tenga menor hacinamiento, puesto que esto significa que tendrá más población cubierta y la solución será más diversificada. Este proceso se repetirá $n$ repeticiones, guardando el valor de los dos resultados y repitiendo lo mismo con las nuevas generaciones, hasta que el algoritmo finalice.



* **PESA** (*The Pareto Envelope-based Selection Algorithm*)



A diferencia de los dos algoritmos anteriores, el *PESA* no tiene un tamaño de archivo fijo y solo permite que las soluciones no dominadas sean miembros, por ende, es más limitado. Si el archivo excede el tamaño de $n$ soluciones, un factor de compresión o factor *squeeze* , es calculado para todos los miembros del archivo. El factor de compresión es el total de miembros en una subregión en una cuadricula (las que están en el espacio de búsqueda, dentro de la subregión). El factor de compresión más alto es el que tenga más vecinos locales en una solución. Los miembros aleatorios de la región de la cuadrícula con el factor de compresión más alto se eliminan hasta que se reduce el tamaño del archivo a $n$. Los operadores genéticos son aplicados en los miembros del archivo a una nueva población hijo. Este proceso se repite hasta la finalización.



* **SEAMO** (*Simple Evolutionary Algorithm for Multi-objective Optimization*)



La principal diferencia entre SEAMO y otro algoritmo, es que este es de estado estable y solo mantiene una población (de un tamaño constante $n$). La principal ventaja del algoritmo SEAMO es su simplicidad, el cual usa la disposición de todos los mecanismos de selección basado en fitness o rango. El avance de la búsqueda está definido por tres simples reglas:

* los padres solo son remplazados por su propia descendencia.

* Las poblaciones duplicadas son eliminadas.

* La descendencia solo puede reemplazar a los padres si es superior: elitismo.


Los operadores genéticos se aplican a cada padre para formar un nuevo hijo, que se considera para la sustitución en la población de padres según las tres reglas. Este proceso se repite hasta la terminación.


El aspecto clave de este marco es un decodificador que utiliza un orden de ubicaciones de sitios candidatos para construir una celda. En este trabajo se concluyó que los algoritmos son similares en sus resultados en términos reales, sin embargo, se encuentran algunas diferencias, el **NGSA-II** y **SPEA2**, tienen resultados similares en cuanto al rendimiento, el algoritmo **PESA** generalmente obtiene ligeramente una baja calidad en el conjunto de soluciones, pero en cuanto a la velocidad de convergencia y distribución de soluciones tiene el mejor desempeño. En cuanto a **SEAMO**, se destaca por su simplicidad, su elegancia conceptual, su fácil implementación y su velocidad de ejecución, pero su simplicidad impide tener calidad en cuanto a la distribución de las soluciones obtenidas y en el bajo rendimiento en los factores medidos en el desarrollo del test. Para finalizar el trabajo, los autores determinaron que el algoritmo **NSGA-II** tiene el mejor rendimiento, siendo el que mejor se podría implementar en la planeación de celdas ya que obtuvo los mejores resultados de calidad en las soluciones obtenidas.



### Redes WiMAX



En la planeación de celda, se han realizado trabajos con la tecnología 802.16e o WiMax; el autor (@gordejuela2009), presenta un marco de referencia de optimización multiobjetivo que resuelve uno de los principales problemas dentro del diseño inicial de redes de acceso móvil, el cual es encontrar el mejor sitio de instalación de BSs dentro de un conjunto de lugares posibles.



La forma en que le autor trabaja la planeación de la red, consiste en que primero se realiza una predicción de la señal; aquí se tiene en cuenta el tráfico de diferentes sitios candidatos posicionados aleatoriamente en diferentes áreas geográficas, en esta fase evidencia las densidades de tráfico entre áreas rurales y áreas urbanas. Una vez se ha definido este modelo de tráfico, para realizar las funciones de costos, el autor realiza una función de costos en la cual tiene en cuenta el punto de equilibrio entre los diferentes factores que se presentan en el diseño de una red, los cuales son:



* Área de cobertura.

* Interferencia.

* Rendimiento.

* Rentabilidad de la operación de la red.

* Equipamiento y otros costos.



La función de costos está dividida en dos partes, una consiste en una función que tiene en cuenta los parámetros técnicos de rendimiento que debe tener la red, como lo son penalizada con diferentes parámetros de requerimientos que debe tener la red como son ancho de banda para establecer videoconferencias, Voz IP, servicios en la red, etc. Calidad de servicios QoS que deben tener los usuarios, entre otros.  La otra función de costos está contemplada por todos los parámetros de rentabilidad que debe tener la red, para que la solución sea adecuada para los proveedores de internet, en esta se tiene en cuenta la rentabilidad de la red menos los costos de funcionamiento.



Una vez calculado estas funciones de costos, el paso a seguir es realizar la optimización multiobjetivo de los parámetros anteriormente analizados, esto se hace mediante el marco de referencia, en donde se va realizando la simulación de la red con la herramienta de planeación *ForsK’s Atoll*, donde posteriormente se va a realizar una técnica de optimización con el algoritmo búsqueda tabú, donde el autor, modifica el algoritmo para buscar la solución multiobjetivo, una vez realizado esto, se van graficando las soluciones, con el fin de mostrarlas en el óptimo de Pareto. Este procedimiento de realiza n veces, donde en cada iteración, se realiza la técnica de optimización y se hace el ajuste correspondiente a la solución, donde se vuelve a simular, esto hace hasta encontrar una solución óptima.



En el trabajo de *Gordejuela*, se realizó la implementación de este marco de referencia de optimización multiobjetivo, donde se tuvo en cuenta como criterio de planeación una cobertura basada en QoS, lograr reducir al mínimo la interferencia y los costos de ubicar un conjunto de 20 BSs, luego se muestran los resultados de 600 iteraciones y se demuestra que el maco de referencia a contribuido a un mejor resultado con respecto a la solución sin planeación y que además  tiene en cuenta factores económicos que se pueden ajustar según las necesidades del proveedor de la red, dando como resultado una herramienta de optimización flexible y  ofreciendo en este caso una comprensión detallada de cómo se puede hacer la planeación optima utilizando redes WiMax.



### Redes BWA en zonas Rurales

Prestar servicios de banda ancha en zonas rurales requiere de sistemas de planeación dado que el acceso a estas zonas apartadas requiere inversión en infraestructura para desplegar la topología física de la red. Además, el desarrollo de las telecomunicaciones de banda ancha en zonas rurales se enfrenta a numerosos desafíos dentro del ecosistema de las telecomunicaciones de banda ancha, entre ellos se encuentran:

* Los gobiernos: Perspectiva política, jurídica y reglamentaria

* Los reguladores: Políticas para el despliegue de infraestructura en zonas distantes

* Los proveedores de servicios de telecomunicaciones: La inversión en telecomunicaciones rurales debe garantizar un negocio sostenible y viable

* Los fabricantes de equipos de cliente (CPE): Costo de los equipos 

* Los consumidores: Costo elevado de los servicios, dificultad de acceso y disponibilidad, menor nivel de alfabetización tecnológica lo que imposibilita usar los servicios disponibles.

En la planeación de redes inalámbricas en áreas rurales, destacan los autores (Sen, Bernardi, Rios), cada uno de ellos propone una planeación de redes teniendo en cuenta su país de origen y priorizando las necesidades, requisitos y restricciones que se tienen en cada uno de ellos.

Con el objetivo de reducir la brecha digital, autores [@bernardi2012],[@maseratti2011],[@sen2007] han propuesto como solución la planeación y despliegue de redes de banda ancha inalámbrica en zonas rurales; considerando las condiciones locales, como la ubicación geográfica, el bienestar económico de la comunidad, el tipo de entorno rural o urbano y el relieve del terreno, puede identificarse un conjunto de posibles soluciones para prestar accesos de banda ancha, y que van, entre otros, desde sistemas de cable a sistemas inalámbricos fijos, sistemas satelitales o de enlaces de microondas, sistemas ADSL y tecnologías móviles. A su vez, se destacan algunos trabajos de planeación de redes BWA, los cuales se desarrollan en países con marcadas diferencias de índices de desarrollo humano y el porcentaje de población que vive en áreas rurales; se habla entonces de Reino Unido, un país desarrollado donde el 17% de la población vive en área rurales y la India, un país en vía de desarrollo, donde el 66% de la población vive en áreas rurales. 



#### Redes BWA en la India

**Ubicación de la red**:

El autor *Sen* se enfoca específicamente en la planeación de redes de banda ancha en áreas rurales, en su tesis [@sen2007] trabaja sobre una red desplegada en el distrito de Andhra del Oeste de Godavari Pradesh ubicado en la India.

**Población a quién va dirigido:** 

La India es un país donde la mayoría de la población vive en áreas rurales (66% según el Banco Mundial) y esta hace parte de la brecha digital, esto se resuelve dando conectividad a todas las aldeas y pueblos. Lograr esto expandiendo la red actual de telefónia fija en zonas rurales no es factible teniendo en cuenta los costos elevados de la instalación de la infraestructura inicial, sin embargo, este caso no ocurre en la telefonía móvil, donde la demanda de usuarios es más densa y por ende se considera un modelo de negocio, puesto que se retribuye la inversión teniendo en cuenta la cantidad de usuarios dispuestos a pagar por este servicio.

**Problemática:**

El problema radica en el hecho de que las zonas rurales tienen baja densidad de usuarios y grandes distancias entre grupos de usuarios, esto conlleva a que compañías de telecomunicaciones o proveedores de Internet (ISP) vean poco atractiva la inversión en estos lugares debido al costo inicial de infraestructura y despliegue de la red y bajo retorno de su inversión.

**Causas:** 

 - Costo elevado de la expansión de la red telefónica fija
 - No es un modelo de negocio debido al bajo retorno de la inversión
 - Baja densidad de usuarios
 - Costo de infraestructura

**Solución:** 

Por consiguiente, el autor propone la planeación de la topología de una red inalámbrica con el uso de la tecnología 802.11, puesto que permite una buena solución teniendo en cuenta su gran aceptabilidad, principalmente por su bajo costo. Por ende, esta tecnología se ha presentado como una opción de económica y efectiva para cubrir largas distancias, ya que permite que zonas muy amplias puedan conectarse a un nodo de línea terrestre con conectividad a Internet de forma cableada (como fibra óptica) por medio de enlaces inalámbricos. Cada enlace inalámbrico corresponde a una antena en una torre instalada en cada pueblo, los cuales deben tener línea de vista *L.O.S.* (*Line Of Sight*).

Para la formulación en la construcción de una topología que permita el desempeño de la red, se estipulan de tres principales restricciones:

1. Restricción de rendimiento: Capacidad de carga y descarga por cada nodo o pueblo que en el caso de la red en que se realizó el trabajo, se establecido que en cada nodo se tuviera un ancho de banda mínimo de 384 Kps .

2. Restricción de Potencia: Se refiere al límite superior de la Potencia Isotrópica Irradiado (PIRE) en cada transmisor y el límite inferior de potencia recibida en el receptor (sensibilidad del receptor).

3. Restricción de interferencia: La señal recibida debe ser mayor al umbral de interferencia.

El problema de la planeación es resuelto teniendo en cuenta una serie de dependencias, los cuales están mostradas en la *figura 2*. A continuación se explicarán cada una de estas dependencias:

* La tasa de transferencia de datos depende de la MAC

El rendimiento requerido se logra dependiendo del protocolo MAC que se esté implementando, en este caso, el autor propone utilizar el protocolo de capa de Enlace de Datos 2P, puesto que en comparación con los protocolos más utilizados como TDMA y CSMA/CA, este tiene una capacidad de datos más elevada.

* La velocidad de transmisión depende del diseño físico de la red

El rendimiento depende del tipo de enlace, Punto a Punto (PTP) ó Punto Multipunto (PMP), puesto que si es PTP se usa todo el rendimiento permitido por la MAC, en cambio sí es PMP el rendimiento permitido por la MAC se divide entre los enlaces que están conectados, de esta manera el protocolo de enlace de todos tendrá que conmutar entre los enlaces existentes reduciendo el rendimiento del protocolo MAC.

* La potencia de trasmisión depende del tamaño del enlace

La señal trasmitida tendrá una degradación en su intensidad, dependiendo de la distancia del enlace. Cada antena tiene una ganancia especifica el cual es la relación de densidad de energía que radia en una dirección especifica.  

* La MAC depende de la potencia de trasmisión

Esto es específicamente  para el protocolo MAC 2P, en el que múltiples enlaces pueden operar simultáneamente. La operación simultánea de múltiples enlaces requiere que se asegure que la relación de potencias de la señal real y de la interferencia (SIR) sea mayor que un margen especificado por el sistema.

* La Altura de la torre depende del tamaño del enlace  

 La formación de un enlace Wifi entre dos nodos distanciados está basada en L.O.S.  el cual debe tener despejado el 60% de la curvatura de la zona de Fresnel. El tamaño de la zona de Fresnel dependerá de la distancia del enlace.  

* Los costos de despliegue dependen de la altura de las torres

Los costos de despliegue dependen principalmente del tamaño de la torre que se van a implementar. Los costos de la torre crecen linealmente con la altura de la torre, así que en este punto se debe considerar que se debe diseñar la topología de tal forma que la altura sea la mínima, esto ahorrará los costos principales del despliegue de una red.     


![Dependencias de requerimientos](dependencias.pdf){ width=10sss0% }


##### Consideraciones de diseño y enfoque de solución


![Secuencia de pasos solución del problema de planeación en la india](sen.pdf){ width=10sss0% }


Una vez se ha visto como se divide el problema, el autor sugiere resolver las dependencias con los siguientes pasos, el cual van a ser explicados:

* **Topología de Búsqueda (TS)**:  


Explorar el espacio de búsqueda para encontrar la topología de la red, se hace uso del algoritmo Branch-and-bound (Algoritmo de ramificación y límite), con ello se construye la topología de árbol, el cual va a dar una topología inicial de la red.


* **Asignación de altura (HA)**:

Consiste en la altura óptima de las torres en las ubicaciones dadas una vez que se ha formado la topología, para ello se utiliza un conjunto de ecuaciones de programación lineal (LP), el cual se va a obtener la altura que sea optima.


* **Asignación de Antena (AA)**:

Asignación apropiada de las antenas y sus respectivas orientaciones, se desarrolla un algoritmo heurístico de tiempo complejo polinómico.


* **Asignación de Potencias (PA)**:

Proporcionar las potencias de transmisión en los radios del sistema usando LP.


**Aporte final:**

Como aporte *Sen* entrega un algoritmo de planeación de redes en zonas rurales y, una vez implementado, el autor en los resultados concluye que se  ahorró 22% con respectos a una planeación sin ninguna técnica de optimización.

 
#### Redes BWA en Escocia

**Ubicación de la red:** 

Bernardi diseñó e implementó **Tegola** un banco de pruebas que proporciona internet a algunas comunidades remotas de Gran Bretaña, esta red ha funcionado desde el año 2008 y ha comunicado a 20 comunidades en toda Escocia. Esta red está situada en el  noroeste de Escocia comunicando comunidades rurales (principalmente costeras) en  las penínsulas de Glenelg y Knoydart en el continente británico hasta la península de Sleat en la isla de Skye.

**Población a quién va dirigido:** 

Gran Bretaña es un país desarrollado, comunmente llamado "país del primer mundo" ya que su población en su mayoría vive en zonas urbanas, sin embargo, el proyecto se enfoca en comunicar zonas rurales o apartadas que no cuentan con acceso a internet de banda ancha (16,9% del total de la población).

**Problemática:**

La falta de herramientas de software para el diseño, gestión y evaluación de redes de acceso inalámbrico de banda ancha han obstaculizado su implementación generalizada a pesar de sus costos y ventajas operativas sobre otras tecnologías de Acceso de banda ancha.

**Causas:**

 - Costo de despliegue de ADSL
 - Bajo retorno de la inversión 
 - Los usuarios viven lejos unos de otros
 - Costo de los equipos 
 - No se puede accedes a software para comunicar pequeñas comunidades y pequeños WISP

Según *Bernardi*, en las últimas décadas se ha incrementado la conectividad de banda ancha, siendo la ADSL (del inglés Asymmetric digital subscriber line) con más del 60% de las conexiones de banda ancha en países de la Organización para la Cooperación y el Desarrollo Económicos es un organismo de cooperación internacional (OCDE); esto se debe principalmente al éxito de la capitalización de ADSL debido al éxito de la red de telefonía. Esta tecnología se caracteriza por que la tasa de trasmisión máxima que puede alcanzar esta en función de la distancia entre el usuario y la central telefónica, es decir, entre más larga sea la distancia, la velocidad de trasmisión es más lenta, por esta razón es comúnmente más utilizada en áreas metropolitanas debido a que tiene más suscriptores y sea más efectivo retornar la inversión de despliegue de una infraestructura. Esto es la principal causa de la brecha digital que existe entre las áreas rurales y metropolitanas.

Pero *Bernardi* expone el despliegue de una red Rural de Banda Ancha (BWA) argumentando que la planeación ad-hoc no es una alternativa de diseño eficiente para este tipo de redes, sin embargo, refiere que la industria ofrece software para planeamiento de redes inalámbricas pero estos no están disponibles ni son adecuados para comunicar pequeñas comunidades y pequeños proveedores de servicio de Internet inalámbrico (WISP) ; cabe resaltar que las BWA usan un modelo de dos niveles, consistiendo en radioenlace Punto Multipunto (PMP) y Punto a Punto (PTP), el primero enlazando la Antena de la torre a los diferentes clientes y el segundo correspondiente al Backhaul.

**Solución :**

El Internet satelital se podría decir que es una alternativa de conexión, puesto que está disponible prácticamente en cualquier parte y es frecuentemente subsidiada en áreas remotas incomunicadas, sin embargo, también tiene latencia de tiempo de ida y vuelta muy altos, lo cual lo hace inadecuado para aplicaciones que consuman un ancho de banda considerable, como es el caso de una videollamada (skape).

A través del planeamiento de red incremental *Bernardi*  desarrolla un software denominado IncrEase cuyo enfoque es identificar la estrategia de despliegue más económica para planear la red teniendo en cuenta que los CPE (customer Premises Equipment) son la opción más rentable para llegar a la población en zonas rurales.

Los proveedores de servicio de Internet inalámbrico implementan una metodología de diseño para operar en escenarios rurales obteniendo remuneración de su inversión, este consiste en planificar su crecimiento ampliando su cobertura, tomando variables como:

- Limitar el alcance geográfico de los WISP:Para reducir los costos de operación.

- Infraestructura de la red: En áreas rurales la fibra para el Backhaul no está disponible, por ello los WISP deben desplegar  su propio Backhaul inalámbrico, aumentando los costos.

- Cobertura de la red: El despliegue rural está basado en la cobertura más no en la capacidad.

- Presupuesto ajustado: Los proveedores de Internet buscan obtener un retorno de su inversión desde su etapa de despliegue ya que las zonas rurales son entornos de baja rentabilidad.

- Clientes agrupados: Proporcionar acceso a la red en sectores dónde haya más densidad de la población, para así captar más usuarios.

 *Bernardi* desarrolla un paquete de software con especial énfasis en las regiones rurales y en desarrollo. Se resalta que abordó tres desafíos técnicos  en el contexto de redes de acceso inalámbrico de banda ancha:

- Mapeo de Banda Ancha
- Planeación de redes
- Administración de redes

**Aporte:**

La contribución de *Bernardi* es potenciar el negocio de los pequeños proveedores de Internet inalámbrico (WISP) en zonas rurales a través de un sistema de software, haciéndolo más eficiente reduciendo la brecha digital, a través de la herramienta IncrEase.

Se desarrolla un software de código abierto IncrEase implementado como una aplicación de escritorio multiplataforma en Java. IncrEase esta basado en un GIS de software libre de la NASA World Wind Java y en una base de datos gráfica Neo4J. 

Para la implementación de IncrEase se toman tres fuentes: 

- Demanda de la cobertura: Posibles usuarios de zonas rurales que no tienen acceso al servicio
- Usuarios que fallaron en la etapa de instalación: Cobertura insuficiente 
- Reporte mesas de ayuda:  Localización de los usuarios existentes

Además se obtienen otros datos de factores influyentes como la disponibilidad DSL, la cobertura de red 3G y datos demográficos. IncrEase  a través de datos en forma de arreglo bidimensional cubre regiones de interés y con ello obtiene mapas de calor (áreas de mayor beneficio por la actualización de la red). En estos mapas a mayor calor menor es la cobertura, una posible solución es la instalación de una torre a partir de una lista de torres disponibles en esa área. 

* **Modo de operación herramienta IncrEase**

Flujo de información de la herramienta 

![Ejemplo de flujo de informacion en la herramienta `IncrEase`](figure4_1.png)

- IncrEase Targeted: En este modo de operación el operador selecciona una región específica de cobertura, como parte de expansión de la red
      
- Búsqueda Estratégica: Dónde la herramienta guía al operador para decidir el orden de despliegue de sitios de transmisión en el horizonte de corto o largo plazo basado en la rentabilidad esperada

#### Redes BWA en la región del Sumapaz (Colombia)

**Ubicación de la red:**

A nivel local, [@rios2015] propone una solución de construcción de topología en redes rurales dentro de la realización Del Estudio De Factibilidad, Socialización Y Capacitación, Para Implementación De Infraestructuras De Voz Ip Y Comunicaciones Convergentes En La Región Del Sumapaz ”, del grupo de investigación GIGATT de la universidad de Cundinamarca. 

**Población a quién va dirigido:**

La región del Sumapaz es una de las quince provincias del Departamento de Cundinamarca (Colombia), en ella se encuentra el páramo del Sumapaz, el páramo más grande del mundo. Consta de 10 municipios con un 41% de población rural del total de la población referente al año 2011, el énfasis del proyecto se plantea en la interconexión de estas zonas apartadas.

**Problemática:** 

Las adversas condiciones económicas y de acceso a las tecnologías de la informa­ción, hacen que este proyecto busque evaluar la viabilidad y conseguir alternativas asequibles de diseño e  implementación de redes, en este aspecto este trabajo pretende reducir los principales costos involucrados en la implementación física de redes de comunicaciones rurales

**Causas:**

- Costos de las torres
- Baja densidad de la población
- Bajo poder económico
- Costos de infraestructura y equipos

**Solución:** 

En el informe técnico “Realización del estudio de factibilidad, Socialización y Capacitación, para Implementación de Infraestructuras de Voz Ip y Comisiones Convergentes en la Región del Sumapaz” se plantea la posibilidad de  brindar acceso eficiente por medio de voz y video llamadas a las zonas rurales de la región del Sumapaz, ofreciendo cobertura a todas las localidades incluyendo las más vulnerables con una calidad en el servicio coherente con el tipo de aplicación y con tarifas acordes a la población, y paralelamente llevando a ellos servicios de comunicaciones convergentes, haciendo de este un proyecto autosostenible que coadyuve a la reducción de la brecha digital y permita el aprovechamiento de los beneficios del programa de Mintic Vive Digital. 

Hay que mencionar además que Ríos participó de forma activa en este  proyecto en el que la construcción de redes de comunicación rural presenta particulares desafíos sobre todo en el costo que conlleva establecerlas. Además refiere que un parámetro importante en el costo de redes rurales es la construcción de torres que soporten las antenas a la altura que permite establecer un buen enlace, debido a que este costo domina otros costos de infraestructura como el atribuido a los equipos de comunicación de el estandar IEEE 802.11 (WiFi), entonces el problema principal se convierte en mantener costos mínimos en la construcción de las torres de soporte para las antenas en cada nodo. 

Ríos establece algunos factores principales en la planeación de la construcción de la topología y son: 

* Requerimientos de conectividad:
Primero, es importante asegurar que la topología planteada permita la conexión de la totalidad de la red
* Limitaciones físicas:
Existen dos limitaciones físicas para la altura de las torres. Por ejemplo, existe una altura demasiada alta que representa un umbral para el cual los costos son prohibitivos y una altura mínima que limita el uso de torres tubulares

* Naturaleza de la función de costos:
Para alturas menores a 20m se suelen usar los mástiles económicos. Para alturas mayores, es necesario utilizar torres de acero más elaboradas, y por ende más caras, el costo de estas estructuras varía de manera casi lineal con la altura.
      
* Condiciones sobre las alturas de las torres para establecer un enlace directo:
Para ello se debe garantizar que la potencia de transmisión sea suficiente para superar las pérdidas por espacio libre en toda la distancia del enlace. También, se busca mantener la línea de vista despejada de toda obstrucción. 


Dentro de este contexto y al igual que *Sen*, *Bernardi*, *Maserati*, expone que el principal desafío es el costo que conlleva establecer redes en zonas rurales, haciendo especial enfásis en el costo de construcción de las torres que soportan las antenas, debido a que es el costo más grande en comparación con los atribuidos a los equipos de comunicación. Presenta los siguientes referentes:

##### Topología

Establece que las redes rurales mantienen una topología fija y se realizan enlaces de larga distancia, sin embargo, al ser áreas campestres existe una mayor cantidad de obstrucciones y acorde la topografía varia la altura de los obstáculos.

##### Costo de las torres

Para lograr obtener linea de vista entre los diferentes nodos es necesario que las torres tengan una altura suficiente para superar los obstáculos presentados en el terreno. Para la construcción de estas torres establece dos tipos de materiales:

* Mástiles
* Torres de acero ventadas

El costo de las torres, es proporcional a  su altura y  esta re­lacionado con material de construcción, por ejemplo para un enlace de entre 7-8 Km (distancias típicas) se necesitarfan torres de entre 30 m  y 45 m con costos de entre 25 y 38 millones de pesos colombianos. Este costo es de varios ordenes de magnitud mayor que el de los equipos de comunicaciones, de manera que el principal problema de construcción de redes rurales radica en lograr una topología con el menor costo total de las torres que soportan las antenas.

**Aporte:** 

Para resolver el problema de la planeación  el autor desarrolla un algoritmo basado en [@panagrahi2008], dónde la solución resulta de dos algoritmos TC-ALGO(G,c) y START-TC-ALGO(G,c), el primero determina el valor de altura óptimo que permite obtener el mejor enlace dentro de un grupo de enlaces vecinos a un nodo principal y el segundo permite recorrer el grafo y ubicar el menor enlace o conjunto de enlaces que representan el menor costo beneficio

# Capítulo 3. Diseño metodológico


## Generar el estado del arte de los algoritmos utilizados en la planeación de redes inalámbricas que permitan identificar y determinar los requerimientos del algoritmo que sugieran la mejor estrategia de expansión de una red 


En esta fase se indaga sobre las herramientas de planeación de redes inalámbricas existentes con el propósito de recopilar  información para analizar y seleccionar la que más se adapte a la planeación de redes inalámbricas de banda ancha en zonas rurales, en esta primera etapa se realizan las siguientes actividades:


### **Recolectar información de planeación incremental de redes inalámbricas**


Este recurso se utiliza para registrar información relacionada con la planeación de redes inalámbricas, se usó la técnica de recopilación documental consultando libros, artículos de investigación en su mayoría de la revista de Ingenieros Eléctricos y Electrónicos (IEEE), tesis, informes y demás documentos que contribuyeran a proporcionar datos enfocados en la temática central del proyecto. Lo que permitió obtener un bajo costo considerando la gran cantidad de información que se obtuvo, la bibliografía consultada es de característica técnica lo que permitió lograr una dimensión histórica, social y tecnológica a través del tiempo.


### **Analizar la información recopilada de redes inalámbricas enfocada a zonas rurales**

Una vez se ha captado la información de planeación de redes se procede a realizar su respectivo análisis, tabulando todos los documentos encontrados,haciendo un rastreo y clasificación de los documentos, detallando:

|        |        |
| ---------------------------- | ------ |
| Tipo de documento | |
| Título | |
| Año | |
| URl | |
|Temática central | |
|Estado del arte y marco conceptual reseñado| |
| Metodología | |
| Resultados | |
Table: Ficha bibliográfica para seleccionar los archivos de estudio.

De este análisis de fuentes se encuentra que quince (15) son artículos de investigación, cinco (5) son tesis y dos (2) son libros. De los cuales se delimitan los temas a contextualizar, obteniendo los siguientes:

   - Brecha Digital
   - Redes Libres Comunitarias
   - Planeación de Redes Inalámbricas
   - Algoritmos utilizados en la planeación
   - Representación de la topología
   - Herramientas de manipulación de grafos
   - Planeación de redes móviles UMTS
   - Redes BWA en zonas rurales 

Con ello se pudo establecer que los primeros seis puntos harían parte del marco teórico y los dos siguientes pertenecerían al estado del arte, esto como resultado de que el enfoque de esta investigación está relacionado con la planeación de redes móviles y BWA en zonas rurales. 


### **Determinar la información que cumpla con los requerimientos necesarios para diseñar el algoritmo**

Acorde al análisis ejecutado en la actividad anterior se encontró que los autores *Bernardi*, *Sen* y *Milton* proporcionan la información necesaria para diseñar el algoritmo.  Dentro de los requerimientos proporcionados se tienen:

- Topología de la red actual
- Número de torres disponibles
- Cobertura de la red, hace alusión al alcance geográfico
- Altura de las torres 
- Zona de fresnel 
- Costo de despliegue de la red 
- Costo de la infraestructura y de los equipos 
- Algunos datos demográficos y económicos de la población


### **Documentar el estado del arte** 

Con toda la información analizada y los parámetros claros se documenta el estado del arte realizando una comparación entre los tres autores destacados mencionados con anterioridad. De ellos se establece

- *Sen* plantea su algoritmo en planear la red inalámbrica en zonas rurales de la India, se sabe que su contexto es social y rural
  
- *Bernardi* desarrollo su software basado en Tegola, una red existente en Escocia, ampliando su cobertura a zonas rurales considerando el nivel lucrativo de la red enfocado en pequeños proveedores de internet
  
- *Rios* por su parte, aplica el algoritmo de (Panigrahi) en la región del Sumapaz- Cundinamarca (Colombia) enfocando su idea en la interconexión de escuelas rurales añadiendo el costo de la construcción de la topología de la red.
       
En contexto, el estado del arte se puede estudiar en el capítulo 2 de este Libro.



## Diseñar un algoritmo que permita identificar la mejor estrategia de expansión de la red inalámbrica en zonas rurales

Partiendo del análisis e información recolectada se determinan los parámetros necesarios para continuar con la etapa de diseño del algoritmo para planear el crecimiento de una red inalámbrica en zonas rurales.

Para el desarrollo del algoritmo que permite la creación de una herramienta de planeación incremental de redes inalámbricas rurales, se plantea el modelo cascada que  en el desarrollo de software es un proceso en el que todas las fases se realizan de forma secuencial,  siguiendo un flujo de ejecución de arriba hacia abajo como una cascada. Esto permite hacer un fácil seguimiento del desarrollo del proyecto, realizando una distribución de tareas y delimitando sus fases.

![Estructura metodología cascada](metodologia.pdf){ width=10sss0% }


### Análisis de requerimientos

 <!-- Que necesitamos, explicación del por qué se toman las características de cada autor-->


Resolver la brecha digital que existe entre las áreas urbanas y las áreas rurales requiere aumentar la conectividad a Internet, para asegurar la conexión en áreas rurales es necesario realizar una planeación de redes inalámbricas que permita diseñar una infraestructura con un mínimo costo al momento de desplegar la red. 

Los autores [@sen2007],  [panagrahi2008] y [@rios2015], proponen que la altura de la torre constituye uno de los costos más importantes dentro de la construcción de una infraestructura de red inalámbrica en áreas rurales, por esta razón se va a trabajar la asignación de la altura mínima en las torres de instalación. 

Asignación de altura de torres 

*Sen* propone una heurística que sigue una secuencia de pasos explicados anteriormente y entre estos resuelve el problema de encontrar una solución de alturas optimas utilizando programación lineal (PL), sin embargo, en  [@panagrahi2008] se  propone un algoritmo para asignar la altura donde cita a [@sen2007], puesto que sigue el mismo enfoque de reducir el coste de infraestructura de red en zonas rurales, sin embargo, el autor *Panigrahi* proponen los algoritmos TC-ALGO  Y  START-TC-ALGO que mejora la heurística que propone *Sen*.   

A continuación de describe las ventajas que tienen los algoritmos de *Panagrahi* sobre la heurística propuesta por *Sen*:  

* En la heurística no es posible conocer el límite de posibilidades, mientras en los algoritmos se tiene un límite de respuesta en el peor de los casos.  

* En la heurística se propone solo un obstáculo en la mitad del enlace entre dos nodos, sin embargo, los algoritmos pueden encargarse de encontrar la respuesta optima de la altura de las torres teniendo en cuenta todos los obstáculos entre el enlace de dos nodos.   

* En la heurística se trabaja una función de costo lineal por cada torre, mientras que los algoritmos usan una función de costos más general.  

En [@rios2015] se propone el diseño de una topología de infraestructura de red inalámbrica en la Región del Sumapaz implementando los algoritmos planteados en [@panagrahi2008], en este trabajo se implementan estos algoritmos para proponer una topología que conecten unos puntos propuestos, en donde puede ir conectada una torre de antena con la mínima altura de nodos, creando una topología de mínimo costo. 

Una vez desplegada la red con el mínimo costo es necesario guiar a los ISP en la expansión de la red, de tal manera que puedan retornar la inversión del costo de despliegue, en [@bernardi2012], propone una herramienta que facilita la planeación incremental de la red en zonas rurales, utilizando dos modos de operación, targeted IncrEase y Búsqueda estratégica, el primero permite identificar las zonas que deben ser cubiertas por la red con una prioridad más alta y el segundo permite saber en qué lugares es más factible la inversión. Por lo anterior, y acorde al contexto local de este proyecto, existen proveedores de internet que operan en la región y necesitan una herramienta que les permita saber dónde invertir y aumentar la conexión en zonas rurales, por ello se toma los dos modos de operación propuestos por Bernardi.


Una vez determinado los algoritmos que resuelven los requerimientos, se detallan los parámetros de entrada y salida de cada uno de los algoritmos propuestos por los autores.

#### Definir los datos de entrada y salida del algoritmo

En esta sección se especifican las variables de entrada y salida de los algoritmos, entonces se tiene que:

* **Algoritmo planteado por *Sen* **

| Datos de entrada |
|------------------------------------------------------------------------------ |
|Enumeración de todos los árboles y para cada árbol (coordenadas de la ubicación de las villas)|
| Asignación de las antenas |
| Asignación de los valores de potencia de las antenas |
| Asignación de las alturas de las torres en todos los nodos |
Table: Datos de entrada del algoritmo planteado por *Sen*. 



| Datos de Salida |
|------------------------------------------------------------------------------ |
| Topología de la red |
| Costo del árbol generado  en comparación con otro anteriormente generado, de lo dos se guarda el de menor costo |
Table: Datos de salida del algoritmo propuesto por Sen.

* **Algoritmo diseñado por Bernardi**

| Datos de entrada |   |
| -------------------------------------- |
| Demanda de cobertura |
| Instalaciones fallidas |
| Ubicación y desempeño de los usuarios actuales |
| Solicitud de soporte |
| Torres disponibles |
| Topología de red actual |
| Área de selección |
Table: Parámetros de entrada del algoritmo de Bernardi.

| Datos de salida |
| -------------------------------------- |
| Estrategia incremental de despliegue sugerido  |
| Ruta sugerida para cubrir el área seleccionada |
Table: Datos de Salida del algoritmo de bernardi.

Cabe resaltar que este paquete de software proporciona dos modos de operación que se han mencionado con anterioridad:

* Búsqueda estrategica: Cuya salida es la primer fila de la tabla anterior
* Targeted Increase: donde se sugiere una ruta al área seleccionada 

s

* **Algoritmo implementado por Rios** 

Esta aplicación esta basada en *Panigrahi*, dónde resulta la solución en dos algoritmos, el primero TC-ALGO(G,c) y el segundo START-TC-ALGO(G,c).



| Datos de entrada TC-Algo(G,c) | Datos de Salida TC-ALGO(G,c) |
| ------------------------------------ |  ------------------------------------- |
| Grafo G(V,E) | Función de alturas h |
| Función de costos |  |
Table: Parametros de entrada y salida del primer algoritmo de la aplicación, TC-ALGO (G,c)



| Datos de entrada START-TC-ALGO (G,c) | Datos de salida START-TC-ALGO (G,c) |
| -------------------------------------  | -------------------------------------  |
| Grafo G(V,E) | relación costo beneficio $r'$ best |
| Función de alturas h | incremento de altura incr |
| Nodo n |   |
| Incremento altura  variación  en v |   |
Table: Datos de entrada y salida del segundo algoritmo START-TC-ALGO (G,c). 


Ahora, con los tipos de datos de entrada y salida de los algoritmos estudiados, se determinan los parámetros de entrada y salida del algoritmo que se va a diseñar. Es decir, que el algoritmo que se va a proponer surge de la implementación secuencial de los algoritmos vistos con anterioridad, seleccionando las variables que contribuyen a resolver el problema a nivel local.

*  **Algoritmo propuesto (Datos de entrada y salida)**

| Datos de entrada |
| -------------------------------------- |
|Grafo topología de la red |
|Asignación de antenas|
|Función de costos|
|TC-ALGO|
|START-TC-ALGO|
|Limitar el alcance geográfico|
|Red Backhaul disponible|
|Solicitudes de Cobertura|
|Clientes agrupados|
Table: Parámetros de entrada algoritmo propuesto


|Datos de salida|
| -------------------------------------- |
|Mejor topología de expansión de la red con el menor costo|
Table:Salida del algoritmo


### Determinar los requerimientos necesarios para ejecutar el algoritmo

El estándar IEEE 830-1998 para el SRS(en inglés) o ERS (Especificación de requerimientos de software) es un conjunto de recomendaciones para la especificación de los requerimiento o requisitos de software, basado en este estándar se determina: 


* **Requerimientos funcionales**


|Identificador del requerimiento| Entrada 1                           |
| ----------------------------- |-------------------------------------|
| Nombre del requerimiento      | Cobertura |
| Características               |Ubicación de la red existente|
| Descripción del requerimiento | Límite geográfico de la red actual|
|Requerimiento NO funcional     |   |
|Prioridad del requerimiento    | Alta |
Table:


|Identificador del requerimiento| Entrada 2                                 |
| ----------------------------- |-------------------------------------|
| Nombre del requerimiento      |Ubicación de los usuarios|
| Características               |Identificación de la ubicación geográfica de los usuarios|
| Descripción del requerimiento |Detallar la localización geográfica de los usuarios para analizar la topografía del terreno |
|Requerimiento NO funcional     |   |
|Prioridad del requerimiento    | Alta |
Table:

|Identificador del requerimiento| Entrada 3                                 |
| ----------------------------- |-------------------------------------|
| Nombre del requerimiento      |Torres disponibles|
| Características               |Obtener acceso a la ubicación de las torres |
| Descripción del requerimiento |La ubicación espacial de las torres en el área de implementación de la topología de la red, permite saber que torres o conjuntos de ellas se pueden utilizar y así disminuir los costos de instalación |
|Requerimiento NO funcional     |   |
|Prioridad del requerimiento    | Alta |
Table:

|Identificador del requerimiento| Entrada 4                                 |
| ----------------------------- |-------------------------------------|
| Nombre del requerimiento      |Topología de la red|
| Características               |Obtener topología de la red existente y su ampliación
|
| Descripción del requerimiento |Diseñar a partir de la topología de la red existente una nueva topología con el propósito de aumentar su cobertura y permitir que más usuarios accedad a ella.|
|Requerimiento NO funcional     |   |
|Prioridad del requerimiento    | Alta |
Table:

|Identificador del requerimiento| Entrada 5                                 |
| ----------------------------- |-------------------------------------|
| Nombre del requerimiento      |Área de selección|
| Características               |Determinar la zona rural en dónde se realizará la expansión de la red|
| Descripción del requerimiento |Al seleccionar la ubicación geográfica dónde se aplicará el algoritmo se analizarán las condiciones del terreno para la ubicación de las torres|
|Requerimiento NO funcional     |   |
|Prioridad del requerimiento    | Alta |
Table:

|Identificador del requerimiento| Entrada 6                                 |
| ----------------------------- |-------------------------------------|
| Nombre del requerimiento      |Ingreso de los datos|
| Características               |Datos de entrada del algoritmo|
| Descripción del requerimiento |Permite que los diseñadores del algoritmo ingresen las difernetes variables o datos para el funconamiento del programa.|
|Requerimiento NO funcional     |   |
|Prioridad del requerimiento    | Alta |
Table:
 

|Identificador del requerimiento| Entrada 7                                 |
| ----------------------------- |-------------------------------------|
| Nombre del requerimiento      |Operaciones matemáticas|
| Características               |Procesos matemáticos para obtener una respuesta óptima|
| Descripción del requerimiento |PLas operaciones matemáticas permiten al algoritmo brindar una respuesta óptima sobre la ubicación de las torres en el lugar donde se expandirá la red, esto conlleva a realizar calculos para que su implementación sea de menor costo|
|Requerimiento NO funcional     |   |
|Prioridad del requerimiento    | Alta |
Table:


* **Requerimientos NO funcionales**

|Identificador del requerimiento| INT01                                 |
| ----------------------------- |-------------------------------------|
| Nombre del requerimiento      |Rápidez del algoritmo |
| Características               |Desempeño en la ejecución del algoritmo.|
| Descripción del requerimiento |Evaluar el desempeño en velocidad de respuesta del algoritmo a los datos de entrada ingresados por el diseñador|
|Requerimiento NO funcional     |   |
|Prioridad del requerimiento    | Alta |
Table:

|Identificador del requerimiento| INT02                                 |
| ----------------------------- |-------------------------------------|
| Nombre del requerimiento      |Requerimientos de procesamiento |
| Características               | Capacidad de la memoria del pc para procesar el algoritmo|
| Descripción del requerimiento |Determinar cuanto espacio y memoria necesita el equipo para procesar y ejecutar el algoritmo|
|Requerimiento NO funcional     |   |
|Prioridad del requerimiento    | Alta |
Table:

|Identificador del requerimiento| INT03                                 |
| ----------------------------- |-------------------------------------|
| Nombre del requerimiento      |Lenguaje de programación|
| Características               |Python|
| Descripción del requerimiento |El algoritmo se desarrollará en el lenguaje de programación Python|
|Requerimiento NO funcional     |   |
|Prioridad del requerimiento    | Alta |
Table:


### Diseño

####  Proponer el conjunto de operaciones secuenciales para la realización del Algoritmo

 <!-- que hace cada elemento del sistema-->

A partir de los tres algoritmos estudiados se plantea una nueva propuesta para el planeamiento de redes inalámbricas en zonas rurales.Para esto, se toman algunas características que contribuyen a dar solución al problema local (expandir la red Libre de Bosachoque a la región del Sumapaz), esto con el fin de generar un nuevo algoritmo que permita dar conectividad a internet en zonas apartadas a un bajo costo. 

Para proponer un nuevo algoritmo se establece:

1. Parámetros de entrada
2. Planeación incremental
3. Planeación del costo mínimo 
4. Salida: Obtener una respuesta de planeación de redes inalámbricas rurales económica

En la siguiente figura se establece el diagrama sistémico del modo de operación de la herramienta propuesta.


![Diagrama sistémico](Diagrama_sistemico.pdf){ width=10sss0% }


**Descripción del proceso de operación del algoritmo propuesto** 

1. **Parámetros de entrada**


- Grafo, conexión de toda la red: se ingresa un grafo con una topología propuesta dónde todos los nodos se encuentren conectados entre sí.

- Limitar el alcance geográfico: Se delimita la región en dónde se desea expandir la red existente.

- Solicitudes de cobertura: sectores o usuarios que desean adquirir el servicio de conectividad a Internet.


2. **Planeación incremental de la red**

**Mapas de calor**

Los mapas de calor son una herramienta visual que permite al usuario identificar zonas en dónde se necesita con mayor prioridad brindar conectividad a Internet. Entonces, a mayor concentración de color más alta es la prioridad.

Para realizar estos mapas se utiliza la herramienta QGIS, que es un cliente GIS de código abierto fácil de usar, donde se puede visualizar, administrar, editar, analizar datos y componer mapas imprimibles. Además, incluye una poderosa funcionalidad analítica a través de la integración con GRASS, SAGA, Orfeo Toolbox , GDAL/OGR y muchos otros proveedores de algoritmos. 

Se consideran dos fuentes de información, de cada fuente se genera un mapa de calor diferente.


* Mapa de calor de las solicitudes de cobertura: sugiere los lugares en los que se encuentra mayor cantidad de usuarios que solicitan el servicio.

* Mapa de calor de la ubicación y desempeño de los usuarios actuales: Permite saber la ubicación de los usuarios que hacen parte de la red actual y el nivel de funcionamiento de estos nodos.


Una vez se han obtenido los mapas de calor se hace la unión de los tres a fin de determinar que lugares se deben cubrir con mayor prioridad, teniendo en cuenta la relación costo-beneficio, es decir, que permita el acceso a internet a la mayor cantidad de personas pero a un bajo costo. 

**IncrEase**

Para el caso regional de la Provincia del Sumapaz, se considera la planeación incremental de la red propuesta en [@bernardi2012]. 

En la figura n, se presenta el flujo de información de la herramienta IncrEase.Enla que un conjunto de archivos XML contienen información estadística de la red que es leída y analizada. Bernardi considera tres tres fuentes de información. La primera es la *demanda de cobertura:* La lista de solicitudes de cobertura recibidas (puede ser por ejemplo en la página del proveedor WISP), para posibles usuarios que están viviendo en áreas sin servicio.

El segundo es el conjunto de detalles sobre aquellos usuarios nuevos que *fallaron en la etapa de instalación* debido a una cobertura insuficiente. Finalmente, importa un registro de llamadas de reportes a mesas de ayuda a WISP y localización de los usuarios existentes. Algunos datos extras pueden ser importados capturando otros factores influyentes (disponibilidad de DSL, cobertura 3G, datos demográficos etc.). 
IncrEase elabora cada fuente de datos para formar un arreglo bidimensional cubriendo la región geográfica de interés, con cada valor de celda representando cuántos “ítems” (usuarios actuales) que hacen parte de la región de la celda. Los valores de celda son entonces normalizados como una fracción de la celda que tiene más ítems.

IncrEase presenta visualmente tres arreglos 2D en los mapas como mapas de calor, y los combina como un promedio ponderado donde las ponderaciones están configuradas de acuerdo a cada métrica a la importancia relativa del operador.

Estos mapas de calor combinados suministran una vista de las áreas que podrían beneficiarse más por la actualización de la red. En este caso el calor (celdas con altos valores en el arreglo 2D) es un indicador de cobertura inalámbrica inadecuada que puede ser quitada por una nueva torre de transmisión o un nuevo sector directivo. Los mapas de calor son almacenados en memoria y pueden acercarse, mostrarse u ocultarse seleccionando los elementos gráficos apropiados.
IncrEase puede importar una lista adicional de torres disponibles para ser instaladas. Este inventario podría incluir torres que ya existan disponibles (por ejemplo para arrendar de otro operador), o posibles lugares donde se puedan construir nuevas torres. Una descripción XML de la topología del lugar, incluyendo la ubicación y la altura de cada torre y la configuración y el número de antenas del sector también se pueden importar a IncrEase. Tal información es usada para generar una capa de “cobertura de red” con una granularidad configurable, el cálculo de línea de vista de cada torre existente y considerando
el azimut e inclinación de los sectores existentes y un parámetro de máxima distancia que especifica el rango admisible para enlaces inalámbricos en el nivel de acceso.


Esta herramienta proporciona dos modos de operación



Notaciones:

* $T$: Es el conjunto de todas las torres (instaladas y viables)

* $N$: Es el subconjunto de $T$ de sólo torres que están actualmente utilizadas
* en la topología de red

* $H(t)$: Es la cantidad total de calor para la torre $t \in T$ . definidas como
* la suma de los valores cubiertos de la celda de calor por la torre.

* $C(t)$: es el costo de instalación de la torre $T$



* IncrEase targeted

Los mapas de calor son una ayuda visual para el operador de red, ya que puede ver las áreas que más se pueden beneficiar, debido a una mejora en la cobertura del modo de operación `IncrEase` suministra el nivel más liviano de automatización disponible en `IncrEase`, dejando “el humano en el bucle” preguntándole al operador que visualmente seleccione en el mapa la visión geográfica donde la cobertura se debería mejorar.`IncrEase` entonces automáticamente identifica cuál es la celda más caliente en la región, definida como la que tiene mayor valor en la capa de calor combinada. La Aplicación determina el conjunto de torres más cercanas por ejemplo (20 en la configuración por omisión) del conjunto $T-N$ que están en línea de vista de la celda caliente para formar el conjunto de lugares candidatos que cubrirán el hotspot, considerando varias fuentes de torres, permite la selección de entre un gran número de posibles rutas de retorno, en comparación con enfocarse solo en la torre más cercana al punto de acceso (hotspot).
El software encuentra la mejor manera de conectar cada una de esas torres a la topología de red existente (i.e., el conjunto N) atravesando enlaces en el grafo $G$. La “mejor” solución es la ruta que proporciona el valor más bajo para la diferencia $c(t) - h(t)$ para cada torre t atravesada. En este cálculo, evitamos cuidadosamente contabilizar varias veces el “calor” asociado con una celda que puede estar en línea de vista con diferentes torres, ya que sesgaría los resultados. Así que consideramos el valor de estas celdas solo una vez.
Para pathfinding sobre el grafo $G$, IncrEase usa el algoritmo $A *$ (A-star). A utiliza la mejor búsqueda en primer lugar, basada en una función heurística de distancia más costo, encuentra la ruta de menor costo desde un nodo inicial a un nodo objetivo. 
Nuestra implementación tiene dos pequeños cambios con el algoritmo original $A *$. Primero, toma como entrada un conjunto de nodos de origen (torres más cercanas a la celda más caliente en la región seleccionada) y un conjunto de nodos de objetivo en lugar de un solo inicio / final de nodos, ya que la ruta de retorno puede comenzar desde cualquiera de las ubicaciones candidatas y terminar en cualquiera de las torres existentes. Segundo, en el gráfo $G$, los costos son asociados con los vértices (es decir, torres) en lugar de bordes, por los que consideramos el costo de un borde ($i$, $j$) para que sea el nodo de salida $i$.

$A*$ requiere una función heurística que sea el límite mínimo inferior del posible costo de la ruta (Por ejemplo, para viajar entre dos ciudades, es la distancia por línea recta), así que en nuestro caso necesitamos diseñar una estimación de la mejor $C(t)-h(t)$ que se pueda lograr para el resto del camino desde una o mas torres dada, hasta las torres objetivo. Nosotros adoptamos $(l/d)*Cmin$ como heurística, donde:

* $l$: es la distancia en línea recta entre la torre actual que se está analizando y cualquiera de las torres objetivo 

* $d$ es la máxima distancia permitida para realizar un enlace punto a punto (ambos en km)  

* $Cmin$ es el valor mínimo de $C(t)-h(t)$ de todas las torres

Finalmente, nosotros introducimos dos modificaciones a la función de costos presentada antes. Como $A*$ requiere costos de bordes no-negativos, sumamos un valor  positivo grande constante arbitrario a todos los $C(t)-h(t)$ valores. Por último, para permitir al usuario equilibrar la importancia de ahorrar dinero y ampliar la cobertura permitimos dos coeficientes variables $Co$ y $ho$ y definimos el costo como $Co*C(t)-ho*h(t)$. 

El resultado de la búsqueda de la mejor ruta se presenta como una ruta en el mapa junto con una indicación de texto de las torres que se desplegarán y su orden, como se muestra en la Figura.



* Busqueda estratégica

Mientras que `IncrEase Targeted` es un modo semi automático que requiere que el
operador selecciones una región, el modo operacional de *búsqueda estratégica*
identifica y sugiere la mejor estrategia de expansión de la red. Asumimos que
la topología de la red evoluciona sobre intervalos discretos de tiempo
arbitrarios (meses, semanas) y el capital de inversión sobre un intervalo
discreto de tiempo del WISP está limitado por un parámetro discreto que
determina cuántos movimientos (instalaciones de torres) se pueden realizar en
cada intervalo de tiempo. El ánimo de la búsqueda estratégica es entonces
sugerir la mejor acción que el WISP pudiera tomar durante el siguiente
intervalo de tiempo. Una limitación práctica obia es el denominado *efecto
horizonte*: como en muchos juegos de inteligencia artificial, el número de
posibles estados es tan grande que sólo es posible buscar en una pequeña
porción de todo el potencial de movimientos en el horizonte de tiempo. El
algoritmo de búsqueda necesita ser capaz de reducir el número de posibles
estrategias para analizar, mientras limita el riesgo de excluir unas buenas
regiones.


A continuación se describe el algoritmo de búsqueda estratégica, que se lanza a
traveś del botón  "recalcular estrategias" en la interfaz de usuario de
IncrEase.

* **Paso 1** Un algoritmo de búsqueda de menor costo de múltiples fuentes se
ejecuta en el grafo de intervisibilidad $G$ para identificar los caminos de menor costo, con costos iniciando en $C(t) -h(t)$ como antes, a partir de cada uno de los nodos en el conjunto $T-N$ (las torres disponibles) a cualquiera de los nodos  en $N$. La salida es un árbol $R$, que intuitivamente suministra el mejor camino de la red existente a cada torre disponible. Para generar $R$, `IncreEase` añade un nodo “raíz” ficticia de cero costo conectada a cada torre en $N$ y ejecuta un algortimo de Dijkstra de la raíz a dada nodo en el grafo $G$. Un ejemplo se suministra en la figura  donde (a) muestra el grafo de inter visibilidad $G$ con nodos sombreados siendo aquellos que ya están instalados y (b) los caminos $R$ resultantes luego de la ejecución del algoritmo de Dijkstra.

* **Paso 2** El grafo $R$ se atravieza iniciando desde la raíz y en el transcurso la torres se etiquetan con el marcador 

$$ \frac{h(r) - c(r)}{(1+C)^{distancia(r)}} $$

donde $distancia(r)$ es la cuenta de las torres nuevas que se tiene que
atravezar para alcanzar $r$ a apartir de la “raíz” de $R$ (torres que se
pueden conectar directamente a la red tienen distancia cero). Como no todas
las torres se pueden conectar inmediatamente a la red para ganar los
beneficios de la cobertura asociada a cada una de ellas, otras puden tener que
ser instaldas primero para servir como *back-hauling relays*. Para medir los
beneficios de cubrimientos futuros para hoy tomamos el concepto financiero de
valor presente neto (NPV) que aplica una rata de descuento constante  $C$ (por
ejemplo 5% 0.05) a las ganancias que ocurrirán en el futuro. 

Un ejemplo se muestra en la figura . Acá las dos torres $a$ y $b$ se
podrían instalar y conectar directamente al mástil existente $n$. Los nodos
$b$ y $f$ cada uno produce un beneficio $h(t) - c(t)$ de 100, mientras que las
otras torres suministran un beneficio mucho menor. El parámetro $C$ es una
medida de la voracidad de la selección: si picamos entre $a$ y $b$  basados en
el beneficio total que ellos y sus descendientes podrían producir , podríamos
decidir instalar la torre $a$ como se muestra en la figura 4.4(b). Sin embargo
si incrementamos el valor de $C$ al 5% $b$ se vuelve más atractivo como se ve
en la figura4.4(c). El NPV controla cuán lejos es posible ir para instalar
torres que dejen ganancia, permitiendole al propietario de la red afinar la
duración del retardo del beneficio.

* **Paso 3**. $R$ se atravieza una vez más esta vez desde las hojas hasta la
 raíz. Mientras se hace esto, actualizamos el puntaje de cada nodo $r$ a la
 suma de su propio puntaje y sus descendientes. se muestran los puntajes
 obtenidos después del paso tres en la figura 4.4(b) y 4.4(c).

Finalmente en cada clic en el botón de "próximo movimiento sugerido" `IncrEase`pregunta el número de movimientos (torres a ser instaladas). Entonces genera una lista ordenada $L$ figura (c) que incluye la torres que se deberían instalar inmediatamente ordendas según su puntaje de beneficio, calculado en el paso 3, posteriormente extrae el nodo superior de $L$  y finalmente lo presenta en el mapa de los resultados.



De estos modos de operación se obtiene una ruta de mayor cobertura (Búsqueda estratégica) y un árbol con una lista de nodos viables para conectarse (IncrEase targeted). Estas respuestas ingresan individualmente a la etapa de planeación de mínimo costo de infraestructura, es decir ingresan al algoritmo TC-Algo y alli se le asignará la antena.


3. **Planeación mínimo costo de infraestructura**

**Algoritmo TC-AlGO**

Determina el valor de altura óptimo que permite obtener el mejor enlace dentro de un grupo de enlaces vecinos a un nodo principal; este algoritmo contiene a START-TC-ALGO (algoritmo que permite recorrer el grafo y ubicar el menor enlace o conjunto de enlaces que representan el menor costo beneficio), también, contiene la función de costos C(n).


**Asignación del tipo de antena**  

En el trabajo [@sen2007], se resuelve el problema de evitar la interferencia al máximo, mientras se minimiza el conjunto de antenas a utilizar. 

 Para realizar los enlaces, es necesario saber qué tipo de antena se va a utilizar, aquí el parámetro que se va a tener en cuenta principalmente es la apertura de ancho de haz o el HPBW (*Half Power Beam Width*) que  definirá la cantidad de nodos que pueda cubrir una antena, ya que si por ejemplo se va a realizar un enlace P-T-P, se puede realizar con una antena direccional de un ancho de haz de 8° puesto que el enlace cubrirá un solo punto, mientras que si se realiza un enlace M-T-P, se debe tener en cuenta una antena sectorial con un ancho de haz de 30° o 22° que pueda cubrir más puntos.   

Ahora, teniendo en cuenta esto se describirá la Heurística propuesta por *Sen*.    

* Heuristica de planeación de antena

El autor *Sen* propone una heurística que vamos a implementar la cual está dada en un tiempo complejo de $Ø(n²)$, donde n es el número de nodos hijos. Esta heurística se enfoca en disminuir el número de interferencia entre un conjunto de enlaces.  

* Heurística   

1 - Reorganizar el conjunto de nodos hijos de tal manera que el máximo ángulo de separación sean los nodos que están más alejados.  

2 – Recursivamente en cada nodo se realiza lo siguiente:  

Determinar el conjunto de antenas o antena que cubre la totalidad de los nodos hijos.  

Dividir el ángulo de máxima separación, en subconjunto de ángulos que tiene la torre para que cubra todos los nodos y determinar el costo de cada uno de estos subconjuntos.  

3 – Fin de la recursividad: cuando exista un conjunto de antenas que cubran todos los nodos con el menor costo.  

  
**Asignación de altura de las torres**  

Los autores [@sen2007],  [@panagrahi2008] y [@rios2015], proponen que la altura de la torre constituye uno de los costos más importantes dentro de la construcción de una infraestructura de red inalámbrica en áreas rurales.  

*Sen* propone una heurística que sigue una secuencia de pasos explicados anteriormente y entre estos resuelve el problema de encontrar una solución de alturas optimas utilizando programación lineal (PL), sin embargo, en  [@panagrahi2008] se  propone un algoritmo para asignar la altura donde cita a [@sen2007], puesto que sigue el mismo enfoque de reducir el coste de infraestructura de red en zonas rurales, sin embargo, el autor *Panigrahi* proponen los algoritmos TC-ALGO  Y  START-TC-ALGO que mejora la heurística que propone *Sen*.   

A continuación de describe las ventajas que tienen los algoritmos de *Panagrahi* sobre la heurística propuesta por *Sen*:  

* En la heurística no es posible conocer el límite de posibilidades, mientras en los algoritmos se tiene un límite de respuesta en el peor de los casos.  

* En la heurística se propone solo un obstáculo en la mitad del enlace entre dos nodos, sin embargo, los algoritmos pueden encargarse de encontrar la respuesta optima de la altura de las torres teniendo en cuenta todos los obstáculos entre el enlace de dos nodos. 

* En la heurística se trabaja una función de costo lineal por cada torre, mientras que los algoritmos usan una función de costos más general.  

En [@rios2015] se propone el diseño de una topología de infraestructura de red inalámbrica en la Región del Sumapaz implementando los algoritmos planteados en [@panagrahi2008], en este trabajo se implementan estos algoritmos para proponer una topología que conecten unos puntos propuestos, en donde puede ir conectada una torre de antena con la mínima altura de nodos, creando una topología de mínimo costo.  


4. **Salida** 

Los datos de salida se obtienen una vez realizado la planeación incremental de la red y la planeación del mínimo costo de infraestructura. De acuerdo con la figura n,  a partir de el resultado generado entre Búsqueda estratégica y Algoritmo TC-Algo se obtiene un grafo con la topología de la red y la altura mínima que deben tener las torres para que haya comunicación, además de considerar la relación costo beneficio, es decir, que se pueda llevar acceso a Internet a más población pero con un costo mínimo de despliegue.Por otro lado, el resultado entre IncrEase targeted y el Algoritmo TC-Algo es una lista de nodos viables que se pueden conectar al árbol $R$ con la altura mínima que deben tener las torres a fin de que tengan conexión. 


#### Codificación del algoritmo

Para codificar IncrEase el algoritmo se utilizó el lenguaje de programación Python, puesto que es un lenguaje de alto nivel, multiparadigma y de código libre, que posee una gran cantidad de librerías y Framework que son actualizados frecuentemente por la comunidad. Esto permite una amplia variedad de herramientas, que permiten un desarrollo de software rápido y eficiente en diferentes áreas como la ingeniería; entre estas herramientas se encuentran librerías de procesamiento matemático Numpy y Scipy, además, para trabajar con estructura de datos,  Python tiene la librería Networkx, el cual es un paquete que trabaja con diferentes tipos de estructuras de datos, entre las que se encuentran grafos y árboles, permitiendo trabajar el enfoque propuesto con facilidad y eficiencia.  

En este proyecto, se consideran también algunas desventajas de Python, como su tiempo de ejecución lento si se compara con otros lenguajes de programación como Java, C o C++, sin embargo, sus librerías, herramientas y la simplicidad de su sintaxis, compensan de manera significativa el tiempo de ejecución en un desarrollo eficaz, de fácil entendimiento y con posibilidad de aportar una herramienta libre y de código abierto, que puede ser mejorada por la comunidad. 

En este trabajo se desarrollaron las funciones `TargetedIncrease` y `searchIncrease`, los cuales reperesentan cada uno de los modos de operación del software IncrEase propuesto en [@bernardi2012]. A continuación, se detalla la codificación de cada una de las funciones: 

##### TargetedIncrease 

Para codificar ` TargetedIncrease `, se utilizó y modificó la función ` astar_path ` de la librería Networkx, que retorna una lista $L$ con el camino más corto de un nodo origen a un nodo objetivo utilizando el algoritmo $A*$, sin embargo, en el algoritmo propuesto por *Bernardi*, se propone uno o más nodos fuente y objetivo, y retorna el valor mínimo de costo menos calor. ``` 

    ```
    def targetIncrease(G,listSource,listTarget): 
        """Retorna una lista de nodos en un camino de uno 
        o más nodos origen a uno o más nodos  objetivo, 
        con el valor mínimo de la suma de los valores de costo-calor.  
        
        Parámetros 
        -----------
        G   :   NetworkX graph 
                Grafo con los atributos posición, 
                costo y calor de cada uno de los nodos.         
        listSource  :lista 
                lista con los nodos origen. 
        listTarget  :lista 
                lista con los nodos objetivo. 
        Retorna  
        A   :   lista 
                lista de nodos. 
        """ 
        miniContPath= 9999 
        for i  in listSource: 
            for j in listTarget: 
                answer=astar_path(G,i,j,heuristica,listNodeTarget= listTarget) 
                cont = 0 
                for k in answer: 
                    cont = cont + (G.node[k]['costo'] - G.node[k]['calor'])  
                if cont < miniContPath: 
                    miniContPath = cont  
                    A= answer 
        return A 
    ```
Esta función utiliza la función astar_path con el algoritmo modificado A* como se muestra a continuación: 

    ``` 
    def astar_path(G, source, target, heuristic=None, listNodeTarget= None): 

        """Retorna una lista de nodos en un camino de un nodo origen a un nodo objetivo  
        utilizando el algoritmo A*. 
        Puede haber más de un camino corto, sin embargo, solo devuelve uno. 

        
        Parámetros 
        ---------- 
        G   :   NetworkX graph. 
        source :    node 
                    Nodo inicial del camino. 
        target :    node 
                    Nodo final del camino. 
        heuristic : function 
                    Es una función que estima el valor de cada nodo recorrido  
                    con el valor de (costo - calor). En esta función toma de 
                    argumento un nodo y devuelve un valor numérico. 
                
        Retorna  
        ---------- 
        A   :   lista 
                Lista de nodos. 
        Raises 
        ------ 
        NetworkXNoPath 
            Si no existe un camino entre un origen y un objetivo. 
        """ 
        if G.is_multigraph(): 
            raise NetworkXError("astar_path() not implemented for Multi(Di)Graphs") 
    
        push = heappush 
        pop = heappop 
        #Almacena la cola prioritaria, nodo, costo de atravesarlo y padre. 
        #Usa la libreria heapq para mantener el orden de la prioridad.  
        #Adiciona un contador en la cola para evitar un monto subyacente  
        #intente comparar los nodos.   
        #prioriza y garantiza un unico para todos los nodos del grafo. 
        c = count() 
        queue = [(0, next(c), source, 0, None)] 
    
        #Asigna los nodos en cola a la distancia de las rutas descubiertas y  
        #las heurísticas calculadas al objetivo. Evitamos calcular la heurística 
        #más de una vez e insertar el nodo en la cola demasiadas veces. 
        enqueued = {} 
        # Asigna los nodos explorados al padre más cercano al origen. 
        explored = {} 
        minCosto=[] 
        while queue: 
            # Pop del elemento mas pequeño de la cola queue. 
            _, __, curnode, dist, parent = pop(queue) 
            if curnode == target: 
                path = [curnode] 
                node = parent 
                while node is not None: 
                    path.append(node) 
                    node = explored[node] 
                path.reverse() 
                return path 
            if curnode in explored: 
                continue 
            explored[curnode] = parent 
            maximaDist= maximaDistancia(G) 
            for neighbor, w in G[curnode].items(): 
                if neighbor in explored: 
                    continue 
                ncost = dist 
                if neighbor in enqueued: 
                    qcost, h = enqueued[neighbor] 
                    # sí qcost < ncost 
                    #queda un camino más largo hacia el vecino en cola. 
                    #Eliminarlo necesitaría filtrar toda la cola, es mejor  
                    #dejarlo allí e ignorarlo cuando visitamos el nodo por segunda vez. 
                    if qcost <= ncost: 
                        continue 
                else: 
                    #heurística 
                    #h = l / d * (Cmin) 
                    h = (distNodeTarget(curnode, listNodeTarget)*heuristic(neighbor))/maximaDist 
                    minCosto.append(h)
                enqueued[neighbor] = ncost, h 
                push(queue, (ncost + h, next(c), neighbor, ncost, curnode)) 
        raise nx.NetworkXNoPath("Node %s not reachable from %s" % (source, target)) 
        return minCosto 
    ``` 
y toma como heurística $(l/d)*Cmin$, donde cada variable es calculada por una función: 

$l$ es la función `distMinNodeTarget(G,curnode, listNodeTarget)` que tiene como parámetro de entrada el grafo $G$, el nodo actual  $curnode$ y una lista de nodos objetivos $listNodeTarget$. La salida es la distancia mínima del nodo que se está analizando y cualquiera de los nodos objetivo. En esta función se obtiene del parametro $G$ el valor de la posición de los nodos *pos* que contiene las coordenadas de latitud y longitud, luego, mediante la función `distancia` que retorna la distancia en km de los enlaces para posteriormente comparar el valor de las distancias y retornar la que tiene el mínimo valor. 
    ``` 
    def distNodeTarget(nodo, listTarget): 
        """Retorna mínima distancia entre el nodo y cualquiera
        de los nodos objetivo. 
        
        Parámetros 
        ---------- 
        nodo    :   node 
                    Nodo atravesado. 
        listTarget  :   list 
                        Lista de nodos objetivo. 
        Retorna  
        --------- 
        maxDistancia    :   float 
                            Máxima distancia. 
        """ 
        miniDist = 999 
        for i in listTarget: 
            dis = distancia(nodo, i ) 
            if dis < miniDist: 
                miniDist = dis 
        return miniDist  
    ``` 
$d$ es la función `maximaDistancia(G)` que tiene como parámetro $G$ y retorna la distancia máxima en km de los enlaces. 
    ```
    def maximaDistancia(G): 
        """Retorna el valor de la maxima distancia de un enlace 
        del grafo G.      
        
        Parámetros 
        ---------- 
        G   :   NetworkX graph 
                Grafo con el atributo pos. 
        Retorna  
        --------- 
        maxDistancia    :   float 
                            Máxima distancia. 

        """ 
        pos = nx.get_node_attributes(G,'pos') 
        lisI=[] 
        lisF=[] 
        lista=[] 
        maxDistancia = 0
        for i in pos.keys(): 
            for j in pos.keys(): 
                lat1=pos[i][0] 
                lon1=pos[i][1] 
                lisI.append(lat1) 
                lisI.append(lon1) 
                lat2=pos[j][0] 
                lon2=pos[j][1] 
                lisF.append(lat2) 
                lisF.append(lon2) 
                lista.append(lisI) 
                lista.append(lisF) 
                #distancia calculada para coordenadas 

                distancia = m.cal_dis(lista) 

                if distancia > maxDistancia: 
                    maxDistancia = distancia 
                lisI=[] 
                lisF=[] 
                lista=[] 
        return maxDistancia 
    ``` 
$cmin$ es la función `heuristica(nodo)`, aquí se ingresa un nodo donde se toman los valores *costos* y *calor*, después retorna la diferencia de estos. 
    ``` 
    def heuristica(nodo): 

        """Retorna un valor numerico con el valor del atributo costo - calor 
        de un nodo. 
        
        Parámetros 
        ---------- 
        nodo   :    node 
                    nodos con atributo costo y calor. 
        Retorna 
        ---------- 
        valor numérico de costo - calor de nodo. 

    """ 
    return(G.node[nodo]['costo'] - G.node[nodo]['calor']) 
    ``` 
Por último, se comparan los caminos que se forman al ejecutar la función `astar_path` y retorna una lista $L$ con el camino que tenga el valor minimo de la sumatoria de costo menos calor de cada uno de los nodos. 

##### SearchIncrease 

El algoritmo Search IncrEase es un algoritmo que utiliza el algoritmo Dijkstra, con alguna modificaciones propuestas por *Bernardi* en donde especifica que, en vez de medir el valor de vértices, se mide el valor de unos nodos etiquetados con un valor *NPV*, que corresponde a un concepto de financiación Net Present Value  o en español “Valor Presente Neto”, que aplica una taza de descuento y está representada con la constante $C$ (por ejemplo 5% 0.05) a las ganancias que ocurrirán en el futuro. 

La función `searchIncrease(G, N, T_N,c)`, toma como parámetro el grafo $G$, una lista $N$ que contiene un conjunto de nodos, que representan las torres que están actualmente instaladas, una lista $T_N$ con un conjunto de nodos, que representan las torres viables, y, por último, una constante que dependerá el valor de taza de descuento $C$. 

 Esta función crea un árbol $R$, uniendo los caminos obtenidos ejecutando el algoritmo Dijkstra desde el un nodo ficticio “*root*” que está conectado a todas las torres instaladas $N$, a cada una de las torres $T_N$, utilizando como ponderación la distancia de los enlaces, más el valor de costo – calor, de cada nodo atravesado, y luego, se crea un diccionario, de cada nodo del árbol $R$, con la etiqueta NPV, dada por la ecuación: 

$$ \frac{h(r) - c(r)}{(1+C)^{distancia(r)}} $$ 

Luego, al igual como se explicó en la sección anterior, el grafo es recorrido desde las hojas, hacia el nodo “*root*”, mientras tanto, se actualiza el valor *NPV*, con la suma de su propio valor y el valor de sus descendientes. Por último, una vez todos los nodos tengan actualizado, se devuelve un diccionario con llave nodo y con valor actualizado *NPV*, además, devuelve una lista con los valores de mayor a menor de *NPV*. 

    ```
    def searchIncrease(G, N, T_N,c):
    """Retorna un arból R formado a partir de un nodo "root"y los caminos mas
    cortos del conjunto de torres instaladas N a todas las torres viables T_N 
    utilizando algoritmo dijkstra, con la diferencia de que no se cuenta el valor
    de la arista, sino del nodo etiquetado con el valor NPV. Un diccionario con los 
    nodos con el atributo NPV, ademas de una lista con los nodos
    ordenados de mayor a menor NPV. 
    
    Utiliza el algoritmo searIncrease diseñado por Bernardi 2012.
    
    Parámetros
    ----------
    G   :    NetworkX graph.
    
    N   :   list
            Lista con nodos de torres instaladas.
            
    T_N :   list
            Lista con nodos de torres viables.
    
    c   :   float
            coeficiente de ganancia o retorno de inversión.
    
    
    Retorna
    ----------
    R   :   NetworkX tree
    
    dicNpv  :   Dictionary
                Diccionario con llave nodo y valor NPV.
                
    listNpv :   list
                Lista ordenada de mayor a menor con valores NPV.
                .
    """
    #agregar nodo raiz 
    G.add_node('root', cab = [0, 0])
    lista=[]
    for i in N:
        tupla=('root', i)
        lista.append(tupla)
    G.add_edges_from(lista)
    listPath=[]
    #aplicar el algoritmo Dkjistra desde el nodo raiz a cada n de G
    R=nx.Graph()
    v= nx.get_node_attributes(G, 'pos')
    for i  in v.keys():
        path = dijkstra_path(G, "root", i, weight='diferencia', N=N)
        listPath.append(path)
        for i in range(len(path)-1):
                R.add_edge(path[i],path[i+1])
    for i in N:
        tupla=('root', i)
        lista.append(tupla)
    R.add_edges_from(lista)

    #list generaciones 
    listGen=[]
    ###etiquetar nodos
    #atributos de distance r : distancia al nodo raiz
    NPV= {}
    lista = []
    pasado = N
    GenR=  nextGeneration(R,N)
    listGen.append(GenR)
    for i in GenR:
        NPV[i]= G.node[i]['diferencia']/(1 + c)
    bandera=0
    cont = 1

    while bandera==0:
        cont += 1
        nextGen = nextGeneration(R,GenR, pasado= pasado)
        pasado = GenR
        GenR=nextGen
        listGen.append(GenR)
        for j in nextGen:
                NPV[j]= G.node[j]['diferencia'] /(1 + c)**cont 
        if nextGen == []:
                bandera=1
    nx.set_node_attributes(R,NPV,'NPV')

    #ponderar puntos 
    u= T_N
    for i in listGen[::-1]:
        if  i == []:
                continue
        for j in i: 
                path =nx.shortest_path(R, "root", j)
                cont=0
                for k in path[::-1]:
                    if k in u :     
                            cont += R.node[k]['NPV']
                            R.node[k]['NPV']= cont     
    #listar nodos con mas valor
    listNpv= []
    dicNpv =nx.get_node_attributes(R,"NPV")
    for i in dicNpv.keys():
        listNpv.append(R.node[i]['NPV'])
    listNpv=sorted(listNpv)
    listNpv=listNpv[::-1]
    
    return R , dicNpv, listNpv 

    ```
Ahora, la función search utiliza una función `nextGeneration` para listar los nodos de el arbol $R$, donde utiliza una lista con los nodos instalados y una lista con los nodos pertenecientes a la pasada generación:

    ```
    def nextGeneration(R, N , pasado= None ):
    """Retorna una lista con los nodos de la 
    siguiente generación de hijos.
    
    Parámetros
    ----------
    R   :   NetworkX tree.
    
    N   :   list
            Lista de nodos que funcionaran como backhaul.
    
    pasado  :   list
                Lista con la generacíon de nodos pasado.
    
    
    Retorna
    ----------
    listNeih    :   list
                    Lista con los nodos de la siguiente generación
                    de hijos.
    
    """
    #listar nodos primera generacion
    listNeih=[]
    for  i in N:
        Neigh= R[i]
        
        neigh= [i for i in Neigh.keys() if not i =='root' and not i in N]
        
        if not neigh == [] :
                for i in neigh:
                    if pasado == None:
                            listNeih.append(i)
                    else :
                            if not i in pasado:
                                listNeih.append(i)
    #borrar elementos repetidos 
    unico=[]
    for i in listNeih:
        if i not in unico:
                unico.append(i)
    
    listNeih= unico
    return listNeih

    ```
Se modifica la función dijkstra_path de la librería Networkx.

    ```     
    def dijkstra_path(G, source, target, weight='weight',N="N"):
        """Devuelve la ruta más corta desde el origen al destino en un 
        grafo ponderado G.

        parámetros
        ----------
        G   :   NetworkX graph.
        
        source : node
            Nodo inicial del camino.

        target : node
            Nodo final del camino.
        
        weight: string, optional (default='weight')
        Edge data key corresponding to the edge weight.
        
        N   :   lista 
            Lista con torres que pueden ser backhaul 
        
        

        Retorna
        -------
        path : list
        Lista de nodos con el camino más corto.

        Raises
        ------
        NetworkXNoPath
        If no path exists between source and target.

        Ejemplos
        --------
        >>> G=nx.path_graph(5)
        >>> print(nx.dijkstra_path(G,0,4))
        [0, 1, 2, 3, 4]

        Nota
        ------
        El peso del atributo debe ser numérico.
        Las distancias son calculados con la ponderación de 
        los nodos atravesados.

        """
        (length, path) = single_source_dijkstra(G, source, target=target,
                                                weight=weight, N=N)
        try:
            return path[target]
        except KeyError:
            raise nx.NetworkXNoPath(
                "node %s not reachable from %s" % (source, target))

    ```
Al igual que lo propone *Bernardi*, se modifica la función `dijkstra_path` de la librería Networkx, 
Esta a su vez utiliza la funcion single_source_dijkstra que encuentra el camino más corto 
implementando el algoritmo Dijkstra, esta ingresa como función de ponderación de costo 
la distancia de enlaces entre el nodo raíz al nodo evaluado y la distancia en km de los enlaces  
utilizando la función de distancia. 
    
    ```
    def single_source_dijkstra(G, source, target=None, cutoff=None, weight='weight', N="N"):
        """Computa el camino mas corto de las distancias con la ponderación de una función.
        
        Usa el algoritmo Dijkstra para encontrar el camino mas corto. 
        
        parámetros
        ----------
        G : NetworkX graph

        source : node
            Nodo inicial del camino.

        target : node
            Nodo final del camino.
        
        cutoff : integer or float, optional
            Profundidad para detener la búsqueda. Solo se devuelven rutas de longitud <= cutoff.
        

        Retorna
        -------
        distance,path : dictionaries
        
        Devuelve una tupla de dos diccionarios con clave por nodo.
        El primer diccionario almacena la distancia desde la fuente.
        El segundo almacena la ruta desde la fuente a ese nodo.

        Examples
        --------
        >>> G=nx.path_graph(5)
        >>> length,path=nx.single_source_dijkstra(G,0)
        >>> print(length[4])
        4
        >>> print(length)
        {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
        >>> path[4]
        [0, 1, 2, 3, 4]

        Notas
        ---------
        Implementar una función que da la sumatoria entre la distancia en
        numero de aristas de distancia al nodo root al nodo actual y la
        distancia de un enlace.

        Basado en libro "Python cookbook" recipe (119466) de
        http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/119466
        """
        def func(u,v, d):
            if v in N :
                return 1
            
            if u in N :
                return 1
            node_v_wt = G.nodes[v].get(weight, 1)+distancia(u, v)
            return node_v_wt

        if source == target:
            return ({source: 0}, {source: [source]})
        
        if G.is_multigraph():
            get_weight = lambda u, v, data: min(
                eattr.get(weight, 1) for eattr in data.values())
        else:
            get_weight =  lambda u, v, data: func(u,v, data)
            
        paths = {source: [source]}  # diccionario de rutas
        return _dijkstra(G, source, get_weight, paths=paths, cutoff=cutoff,
                        target=target)
        ```
Por último, se tiene la función que implementa el algoritmo Dijkstra
    
    ```
    def _dijkstra(G, source, get_weight, pred=None, paths=None, cutoff=None,
              target=None):
        """Implementación del algoritmo Dijkstra con la diferencia que no itera en 
        los vértices, sino sobre los nodos atravesados. 
        
        parámetros
        ----------
        G : NetworkX graph

        source : node
            Nodo inicial del camino.

        get_weight: function
            Función que retorna el peso del enlace.

        pred: list, optional(default=None)
            Lista de nodos predecesores.

        paths: dict, optional (default=None)
            Camino del nodo fuente a nodo objetivo.
            
        target : node
            Nodo final del camino.
        
        cutoff : integer or float, optional
            Profundidad para detener la búsqueda. Solo se devuelven rutas de longitud <= cutoff.
        
        Retorna
        -------

        distance,path : dictionaries
        
        Devuelve una tupla de dos diccionarios con clave por nodo.
        El primer diccionario almacena la distancia desde la fuente.
        El segundo almacena la ruta desde la fuente a ese nodo.

        
        pred,distance : dictionaries
            Retorna dos diccionarios que representan una lista de nodos
            predecesores de un nodo y la distancia de cada nodo.
        
        distance : dictionary
            Diccionario del los caminos mas corto con llave y nodo objetivo.
        """
        G_succ = G.succ if G.is_directed() else G.adj
        push = heappush
        pop = heappop
        
        dist = {}  # dictionary of final distances
        seen = {source: 0}
        c = count()
        fringe = []  # use heapq with (distance,label) tuples
        push(fringe, (0, next(c), source))

        
        while fringe:
            (d, _, v) = pop(fringe)
            if v in dist:
                continue  # already searched this node.
            dist[v] = d
            if v == target:
                break
            
            #lista de nodos vecinos
            lisNeigV=list(G_succ[v].keys())
            
            for u in lisNeigV:

                cost = get_weight(v, u, len(nx.shortest_path(G, "root", u))-1) 
                
                if cost is None:
                    continue
                
                vu_dist = dist[v] + get_weight(v, u, len(nx.shortest_path(G, "root", u))-1)
                
                if cutoff is not None:
                    if vu_dist > cutoff:
                        continue
                if u in dist:
                    if vu_dist < dist[u]:
                        raise ValueError('Contradictory paths found:',
                                        'negative weights?')
                elif u not in seen or vu_dist < seen[u]:
                    seen[u] = vu_dist
                    push(fringe, (vu_dist, next(c), u))
                    if paths is not None:
                        paths[u] = paths[v] + [u]
                    if pred is not None:
                        pred[u] = [v]
                elif vu_dist == seen[u]:
                    if pred is not None:
                        pred[u].append(v)

        if paths is not None:
            return (dist, paths)
        if pred is not None:
            return (pred, dist)
        return dist
    ```
## Evaluar el algoritmo mediante una simulación numérica, comparándolo con Heurística simple

### verificación 

### Pruebas
 
Para comprobar que el algoritmo genera una topología con el menor valor de costo/beneficio, se realizaron pruebas utilizando simulaciones numéricas donde se implementa el algoritmo propuesto por Bernardi y se comparó con una heurística simple. 

Para implementar el algoritmo se creó un grafo $G$, con un número aleatorio de nodos $n$ y vértices $v$, luego, a cada nodo $n$ se le asigna un valor aleatorio de posición $pos$, calor $M$, costo $C$ y altura $h$ de torres para cada uno de los nodos $n$. Posteriormente, se ejecuta la función TargetedIncrease con parámetros de entrada $G$, un nodo con el menor valor de calor $Hmin(n)$ que representará un nodo origen que funcionará como *backhaul* y un nodo destino con el mayor valor de $Hmax(n)$ que supondrá las zonas que se requieren más cobertura. Luego, se implementa la función TC_ALGO para generar un grafo $Ghmin$ con unsa topología que permite conectar todos los nodos con una altura mínima h dando como resultado una planeación de menor costo de instalación de infraestructura física. 

 Esto se comparará con una heurística que consiste en generar un árbol de mínimo de expansión con unas restricciones de tamaño de enlace, luego, al igual que anteriormente se ejecuta el algoritmo TC_ALGO para reducir el valor de costo. Los resultados en ambos casos es un resultado de costo menos beneficio (calor). Esto se realiza en iteraciones y se ilustra en la siguiente imagen.



## Aplicar el algoritmo propuesto en la Red Libre de Bosachoque analizando la topología adecuada para futuras expansiones de la red en las Instituciones Educativas Rurales de la región del Sumapaz-Cundinamarca considerando la relación costo-beneficio


Al aplicar el algoritmo propuesto en la red libre de Bosachoque se obtiene:

- Grafo: Topología de la red en la que todos los nodos se encuentran conectados

- Limitar el alcance geográfico:

En este punto se escogen dos zonas, siendo la primera la vereda Bosachoque (red actual) y la segunda la región del Sumapaz (Futura expansión de la red).  Cabe añadir, que la vereda Bosachoque se encuentra ubicada en el municipio de Fusagasugá y hace parte del corregimiento occidental del municipio junto con las veredas El Resguardo, Cucharal, Novillero y Viena. A su vez, Fusagasugasugá hace parte de los diez municipios que conforman la provincia del Sumapaz en el Departamento de Cundinamarca.

![Ubicación](Bosachoque_sumapaz.pdf){ width=10sss0% }


En la Figura \ref{mylabel} se puede evidenciar con color amarillo la vereda Bosachoque, lugar en el que se encuentra la red Libre de Bosachoque y en color gris la región del Sumapaz, zona en dónde se desea expandir la red.

- Solicitudes de cobertura:

Las solicitudes de cobertura se analizaron en las dos regiones, la red actual y la futura expansión de la red. 

Red Libre de Bosachoque:

De acuerdo con (Tobón) la red se implementó en la parte alta de la vereda Bosachoque (Parte alta de la vía 40 express) instalando diez puntos conectados a la torre de la vereda San José del Chocho en el municipio de Silvania (Cundinamarca). Sin embargo, los habitantes de la parte baja de la vereda no tenían acceso a la red, por lo tanto, las personas solicitaron se les provea conectividad a Internet, acorde con esto, se estableció en que coordenadas era posible instalar las antenas y a partir de ahí verificar la población afectada.

 
![Mapa de calor, solicitud de cobertura Bosachoque \label{mylabel}](mc_b_solicitudes.pdf){ width=100% }


En la figura \ref{mylabel} se puede encontrar el mapa de calor de las solicitudes de cobertura en la vereda Bosachoque, entendiendo que el color rojo es una solicitud más alta de cobertura y el color verde una solicitud baja. Para realizar este mapa se tomó el dato de la concentración de viviendas que podian acceder al servicio. 


Región del Sumapaz: 

Se desea expandir la red libre de Bosachoque a la región del Sumapaz, para ello se plantea la interconexión de todas las Instituciones Educativas Rurales de la región. A partir de este hecho, se obtienen las coordenadas de cada Institución y la cantidad de estudiantes por cada sede, (la información es proporcionada por la base de datos del Ministerio de Educación Nacional), con estos datos se realiza el mapa de calor.

![Ubicación de las Instituciones Educativas Rurales en el Sumapaz](Ubicacion_IE_Rurales.pdf){ width=10sss0% }

En la figura n, se aprecia la ubicación de las escuelas rurales de la región del Sumapaz (punto de color verde). Cabe resaltar que las I.E Rurales están ubicadas en zonas apartadas o de dificil acceso, lo anterior se aprecia mejor en la figura n. 

![Relieve de la región del Sumapaz](relieve_sumapaz_escuela.pdf){ width=10sss0% }




![Mapa de calor solicitudes en la región del Sumapaz](calor_s.pdf){ width=10sss0% }

En la figura n, se puede visualizar el mapa de calor de las solicitudes de servicio en la provincia del Sumapaz, entonces, a mayor cantidad de estudiantes en la sede mayor será la cobertura, por ende, el color amarillo simboliza una mayor concentración de estudiantes.

- Ubicación y desempeño de los usuarios actuales:

Partiendo que la red actual se encuentra ubicada en la vereda Bosachoque, es allí dónde se genera el mapa de calor y así se determina el desempeño que han tenido los nodos instalados.

![Mapa de calor desempeño y ubicación de los usuarios actuales](Desempeno_usuarios_actuales_bosachoque.pdf){ width=10sss0% }

De acuerdo con la figura n, el color amarillo indica los nodos con mejor desempeño, el color azul brinda la perspectiva de un desempeño medio y el color morado indica un desempeño bajo o sin desempeño. Por ende, la antena ubicada en la "Com. Profe Angela" indica un desempeño alto, al igual que "Don Manuel" y "Don Mario", sin embargo, los nodos ubicados en "Don Guillermo y Señora Lucero" indican un desempeño alto, esto dado la cercania de las dos antenas. 

# Capitulo 4. Análisis de resultados y discusión 

# Conclusiones y trabajos futuros 


# Bibliografía
