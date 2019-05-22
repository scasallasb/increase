según los autores *Sayandeep Sen y Bhaskaran Raman*[ ], en las últimas décadas se ha proliferado de manera masiva  el uso de internet, sin embargo, la expansión de la conectividad a internet se ha limitado solo en países desarrollados y  áreas metropolitanas de países en desarrollo, generando la brecha digital, que hace referencia a la distinción entre los que tienen acceso a servicios de internet y los que están excluidos de estos. Esto es realmente lamentable para los países en desarrollo como la India, donde alrededor del 74% de la población es rural y está en el lado equivocado de la brecha digital. una forma de cerrar esta brecha es mejorando  la conectividad en cada pueblo.

Proporcionar internet expandiendo la red de telefonía corriente no es factible debido a los altos costos de infraestructura inicial; sin embargo esto no es un problema en la telefonía móvil  debido a que es un modelo de negocio, ya que es un servicio demandado por una gran cantidad de clientes,lo que exige una mayor densidad de consumo bien pagado.

Para mejorar la conectividad en grandes zonas de cobertura se han utilizado tecnologías emergentes como la 802.16 WIMAX, pero todavía no ha escalado a la producción en masa competitiva, haciendo que los equipos sean más caros, por esto los autores detallan que para estos casos la solución más viable es utilizar las tecnologías 802.11 de Wifi, ya que ha tenido un amplio crecimiento y gran aceptabilidad como una solución de acceso inalámbrica por su bajo precio.

Las tecnologías 802.11 se  ha presentado como una opción de bajo costo y efectiva para cubrir largas distancias, esta permite que zonas muy amplias puedan conectarse a un nodo de  línea terrestre con conectividad a internet de forma cableada (como fibra óptica) por medio de enlaces inalámbricos. Cada enlace inalámbrico corresponde a una antena en una torre instalada en cada pueblo, estos deben tener línea de vista **L.O.S.** (*line of sight*) . Los autores argumentan que el costo principal en la 802.11 corresponde a el costo de la torre, puesto que una antena puede valer $50, una torre de 30 m puede valer $1000, por esto es de vital importancia tener una buena planeación en la primera decisión de despliegue; en la tesis de *Sayandeep Sen y Bhaskaran Raman* [] se enfoca en que el principal problema es minimizar los costos, por esto se hace énfasis en la planeación de una topología de red inalámbrica optimizando los costos en la primera decisión de despliegue.

La principal contribución de la tesis es la formulación en la construcción de una topología de red, es esta se estipulación de tres principales restricciones:
                   
* Aplicación de restricción de rendimiento.
* Restricciones de interferencia entre radioenlaces.
* Restricciones de potencia.

                   
La aplicación de rendimiento simplemente establece que requisitos de rendimiento requiere cada nodo de la zona. Esto depende del protocolo MAC que se esté utilizando. En este caso se enfoca en el protocolo 2P MAC. Las restricciones de potencia consisten en un límite superior en el extremo de transmisión de cada enlace  de la Potencia radiada isotrópica efectiva (EIRP), y un límite inferior en la potencia recibida en el extremo de recepción de cada enlace (requisitos de sensibilidad del receptor).



              
El problema de construcción de la topología se puede establecer como:

“ *Teniendo en cuenta, (a) las ubicaciones (coordenadas $<x, y, z>$) de un conjunto de aldeas que se proporcionarán con conectividad de red y la de la línea terrestre que proporciona y (b) el requisito de ancho de banda específico por nodo de aldea, lo que es la topología de costo mínimo que satisface las tres restricciones: rendimiento, interferencia y potencia.* ”



