% Estado del Arte
% Casallas - Espinel - Rodríguez



La planeación de redes inalámbricas es un área muy activa por la comunidad científica, sin embargo el foco de las las investigaciones  están principalmente en la planeación de redes móviles. En cuanto a los trabajos disponibles en este campo, se puede  encontrar una generalidad de los problemas mas importantes en la planeación de redes móviles en  \cite{Hitlarie2008}, donde se  presenta una literatura detallada de los problemas que se presentan  en la planeación de la topología celular 3G, la cual, esta basada en el Sistema universal de telecomunicaciones móviles **UMTS** (“*Universal Mobile Telecommunications System*”); para entender las dificultades que se presentan en la planeación, es importante  hacer una pequeña descripción de la arquitectura UMTS.


## Arquitectura UMTS


Una arquitectura típica de   UMTS se muestra en la figura (1), donde se observa que una red UMTS esta dividida en dos partes: la *red de acceso* y la *red de núcleo*. La primera, es también llamada red  UMTS  de radio terrestre **UTRAN**, la cual esta compuesta por muchos  subsistemas de red de radio **RNS** (“*radio network subsystem*”). Cada RNS contiene un controlador de red de radio **RNC** (“*radio network controller*” ) y una o mas estaciones bases *BS* (“*base estation*”).


Las estaciones bases (en este caso son los *nodos B*) son usados  para trasmitir/recibir radiofrecuencia  hacia/desde los usuarios móviles, mientras que las RNC se ocupa de los recursos y la gestión de trafico de datos. El principal objetivo de la UTRAN (“*UMTS Terrestrial Radio Access Network*”) es hacer el enlace entre los usuarios móviles y el núcleo red.

El autor *Hitlarie*, descompone la planeación de las redes móviles de manera modular, con el fin de reducir  la complejidad y los divide en los siguientes subproblemas:

* Subproblemas  de planeación de celdas.
* Subproblemas de planeación de red de acceso.
* Subproblemas de planeación de núcleo de red.

La parte de los subproblemas que se necesita abordar con mas detalle, son los de planeación  de celdas, ya que se asemeja mas al enfoque que se necesita en la planeación de redes inalámbricas de banda ancha; a continuación  se describe dicho subproblema, así como algunos trabajos que se han realizado.



### Subproblema de celdas o localización de estación base

El problema inicial de planeación es cubrir todos los usuarios móviles en un determinado
área con el número mínimo de BSs. En la planeación de celdas se encarga de resolver los siguientes items:


*  optimizar el número de BSs.
* la mejor localización para instalar BSs.
* escoger el tipo o modelo de BSs.
* la configuración (altura, orientación, potencia, etc).
* La asignación de usuarios móviles a la BS.


Los problemas de planeación pueden variar dependiendo en la planeación de red objetivo. Usualmente, en la planeación de red se requiere minimizar los costos de la red, maximizar la calidad de la señal y maximizar el área de cobertura. Sin embargo esto puede ser contradictorio,ya que por ejemplo, si se quiere maximizar la cobertura se necesitaran desplegar mas BSs y esto por supuesto, aumentara los costos.


Al principio la planeación de redes inalámbricas se realizaba teniendo en cuenta la predicción de la señal, sin embargo en las redes UMTS, la planeación de radio no puede ser solo basado en la predicción de la señal sino que se deben tener en cuenta la distribución de trafico. 
En esta parte aparece gran cantidad de literatura del autor Amaldi,en \cite{Amaldi2003}, el autor contextualiza que en la planeación de radio en el El sistema global para las comunicaciones móviles **GSM** (“Global System for Mobile communications”) se realizaba en dos fases, la fase de planeación de cobertura donde se define la mejor localización de las BSs teniendo en cuenta los modelos de propagación y la fase de planeación de frecuencia, que define el numero de canales para cada BS teniendo en cuenta la calidad de la señal de interferencia de radio **SIR** (“Signal-to-Interference Ratio”).

Sin embargo, teniendo en cuenta el Acceso múltiple por división de código de banda ancha W-CDMA(“Wideband Code Division Multiple Access”), esto ya no se puede realizar en estas dos fases, debido a que el ancho de banda es compartido por todas las conexiones activas y no por la frecuencia asignada, así como también el área de cobertura de cada BS es afectada por la cantidad de trafico. 

Para la planeación de celdas, se tiene en cuenta los parámetros de calidad de la SIR, en el cual se define una SIR mínima, el cual depende de la potencia recibida; Esta depende de la potencia trasmitida y las atenuaciones de señal en la propagación, por ende la potencia trasmitida se puede ajustar para minimizar la interferencia, aquí aparece un concepto importante, el cual es el control de potencia **PC**(“*power control*”), en donde se ajusta la potencia de trasmisión para cumplir dos objetivos, la potencia objetivo recibida $P_{tar}$ y la SIR objetivo $SIR_{tar}$. En este articulo *Amaldi* propone un modelo de programación matemática, que ayuda en la decisión de planear redes móviles, teniendo en cuenta la mejor localización y configuración de las BSs, teniendo en cuenta el modelo de propagación *Hata*, donde se ajusta el PC y  este a su vez es probado con un algoritmo aleatorio voraz, el cual añade o remueve BSs de la topología; En este artículo se describe el rendimiento de esta solución dando resultados óptimos  y también demuestra que este problema es un problema típico de NP-hard. 


En la planeación de redes, ha menudo se utiliza la optimización de varios objetivos, mas conocido como optimización multi-objetivo, el cual es diferente de una optimización simple , puesto que aquí solo importa optimizar un parámetro, dando como resultado el mejor diseño o la mejor optimización, teniendo en cuenta un máximo o un mínimo global que dependerá del objetivo de la optimización (maximizar o minimizar), sin embargo en  la optimización multi-objetivo, existe mas de una solución optima con respecto a todos los objetivos; aquí, el objetivo consiste en encontrar un optimo de pareto, el cual nos dice que una solución es optima  cuando no existe otra solución tal que mejore en un objetivo sin empeorar al menos uno de los otros.

Como se ha visto anteriormente, en la planeación se pueden abordar diferentes objetivos(lugar de instalación de BS, configuración, altura, potencia, etc), sin embargo, al momento de planificar la red, atacar todos los problemas al tiempo es un problema complejo, por esto, se han venido implementando algoritmos multi-objetivos, generalmente para estos casos se han venido desarrollando algoritmos genéticos AG, en el trabajo de (Raisanen and Whitaker, 2005), los autores recolectan  cuatro estados del arte de algoritmos genéticos multi-objetivo, donde  los ponen a prueba para planificar una red aumentando la cobertura teniendo en cuenta los costos  y los comparan teniendo en cuenta su desempeño en ciertas pruebas sintetizadas ; los autores toman como referencia los algoritmos: **SPEA2**, **NSGAII**, **PGSA** y  **SEAMO**. A continuación de hará una breve descripción de cada uno.

* **SPEA2** (*The Strength Pareto Evolutionary Algorithm version II*): 

La población inicial es sometida a un fittness (aptitud), donde se escoge el valor individual mas *fit* de la unión del archivo y la población hija. El valor  de  fitness, esta dado por la suma de dos partes, *raw fitness*, el cual esta dada por cuantas soluciones domina y la *densidad estimada*, el cual es la proximidad de otras soluciones en el espacio objetivo. Cada generación $n$ es guardada en el archivo, en donde es de nuevo aplicado el operador a la nueva generación; Este proceso se repite hasta terminar el proceso.

*  **NSGA II**
El individuo mas *fit* esta determinado por la unión del archivo y la población hijo, determinado por mecanismos de clasificación compuesto de dos partes. La primera parte esta compuesta al determinar la capa de soluciones que no son dominadas, es decir, las que están mas cerca al frente de pareto. La segunda parte es una medida de dispersión, determinada por la distancia de hacinamiento crowding distance), el cual se escogerá el que tenga menor hacinamiento, puesto que esto significa que tendra mas población cubierta y la solución sera mas diversificada. Este proceso se repetira $n$ repeticiones, guardando el valor de los dos resultados y repitiendo lo mismo con las nuevas generaciones, hasta que el algoritmo finalice.

* **PESA** (*The Pareto Envelope-based Selection Algorithm*)

A diferencia de los dos algoritmos anteriores, el *PESA* no tiene un  tamaño de archivo fijo y solo permite que las soluciones no dominadas sean miembros, por ende es mas limitado. Si el archivo excede el tamaño de $n$ soluciones, un  factor *squeeze* o factor de compresión, es calculado para todos los miembros del archivo. El factor de *squeeze* es el total de miembros en una subregión en una cuadricula (las que están en el  espacio de búsqueda, dentro de la subregión). El factor *squeeze*  mas alto es el que tenga mas vecinos locales en una solución. Los miembros aleatorios de la región de la cuadrícula con el factor de *squeeze* más alto se eliminan hasta que se reduce el tamaño del archivo a $n$. Los operadores genéticos son aplicados en los miembros del archivo a una nueva población hijo. Este proceso se repite hasta la finalización.

* **SEAMO** (*Simple Evolutionary Algorithm for Multi-objective Optimization*) 

La principal diferencia entre SEAMO y otro algoritmo, es que este es de estado estable y solo mantiene una población(de un tamaño constante $n$). La principal ventaja del algoritmo SEAMO es su simplicidad, el cual usa la dispocicion de todos los mecanismos de selección basado en fitness o rango. El avance de la busqueda esta definido por tres simples reglas:

los padres solo son remplazados por su propia descendencia.

Las poblaciones duplicadas son eliminadas.

La descendencia solo puede reemplazar a los padres si es superior: elitismo.

Los operadores genéticos se aplican a cada padre  para formar un nuevo hijo, que se considera para la sustitución en la población de padres según las tres reglas. Este proceso se repite hasta la terminación.


El aspecto clave de este marco es una decodificador que utiliza un orden de ubicaciones de sitios candidatos para construir una celda. En este trabajo se concluyo que los algoritmos son similares en sus resultados en términos reales, sin embargo se encuentran algunas diferencias, el  NGSA-II y SPEA2, tienen resultados similares en cuanto al rendimiento, el algoritmo PESA generalmente obtiene ligeramente una baja calidad en el conjunto de soluciones, pero en cuanto a la velocidad de convergencia y distribución de soluciones tiene el mejor desempeño. En cuanto a SEAMO, se destaca por su simplicidad, su elegancia conceptual, su fácil implementación y su velocidad de ejecución , pero su simplicidad impide tener calidad en cuanto a la distribución de las soluciones obtenidas y en el bajo rendimiento en los factores medidos en el desarrollo del test. Para finalizar el trabajo, los autores determinaron que el algoritmo NSGA-II tiene el mejor rendimiento, siendo el que mejor se podría implementar en la planeación de celdas ya que obtuvo los mejores resultados de calidad en las soluciones obtenidas.







\begin{thebibliography}{0}
  \bibitem{Amaldi2003}
  \bibitem{Hitlarie2008}

@Article{,
  author  = {Amaldi, E., Capone, A. y Malucelli, F.},
  title   = {Planning UMTS base station location: optimization models with power control and algorithms},
  journal = {IEEE Transactions on Wireless Communications},
  year    = {2003},
  volume  = {2},
  pages   = {939 - 952},
  month   = Septiembre,
  issn    = {1536-1276},
}

@Article{,
  author  = {Marc St-Hilaire},
  title   = {Topological planning and design of UMTS mobile networks: a survey},
  journal = {WIRELESS COMMUNICATIONS AND MOBILE COMPUTING},
  year    = {2008},
  volume  = {9},
  pages   = {11},
  month   = Julio,
}

\end{thebibliography}
