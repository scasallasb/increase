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
