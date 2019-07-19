#!/usr/bin/env python

# ejemplo helloworld.py

import pygtk
pygtk.require('2.0')
import gtk

class HelloWorld:

      # Esta es una funcion de retrollamada. Se ignoran los argumentos de datos
      # en este ejemplo. Mas sobre retrollamadas mas abajo.
      def hello(self, widget, data=None):
          print "Hello World"

      def delete_event(self, widget, event, data=None):
        # Si se devuelve FALSE en el gestor de la senal "delete_event",
        # GTK emitira la senal "destroy". La devolucion de TRUE significa
        # que no se desea la destruccion de la ventana.
        # Esto sirve para presentar dialogos como: 'Esta seguro de que desea salir'
        # 
        print "delete event occurred"
           # Si se cambia FALSE a TRUE la ventana principal no se
         # destruira con "delete_event".
        return gtk.FALSE

      # Otra retrollamada
      def destroy(self, widget, data=None):
          gtk.main_quit()

      def __init__(self):
          # se crea una ventana nueva
          self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

          # Cuando se envia a una ventana la senal "delete_event" (esto lo hace
          # generalmente el gestor de ventanas, usualmente con "cerrar", o con el icono
          # de la ventana de titulo), pedimos que llame la funcion delete_event ()
          # definida arriba. Los datos pasados a la retrollamada son
          # NULL y se ignoran en la funcion de retrollamada.
          self.window.connect("delete_event", self.delete_event)

          # Conectamos el evento "destroy" a un manejador de sennl.
          # Ete evento sucede cuando llamamos gtk_widget_destroy() para la ventana,
          # o si  devolvemos FALSE en la retrollamada "delete_event".
          self.window.connect("destroy", self.destroy)

          # Establece el grosor del borde de la ventana.
          self.window.set_border_width(200)

          # Crea un nuevo boton con la etiqueta "Hello World".
          self.button = gtk.Button("Hello miltin")

          # Cuando el boton recibe la senal "clicked", llamara la
          # funcion hello() a la que pasa None como argumento.  La funcion hello()
          # se define mas arriba.
          self.button.connect("clicked", self.hello, None)

          # Esto causara la destruccion de la ventana al llamar a
          # gtk_widget_destroy(window) cuando se produzca "clicked".  De nuevo,
          # la senal podria venir de aqui o del gestor de ventanas.
          self.button.connect_object("clicked", gtk.Widget.destroy, self.window)

          # Esto empaqueta el boton en la ventana (un contenedor de GTK+).
          self.window.add(self.button)

          # El paso final es mostrar el control recien creado.
          self.button.show()

          # y la ventana
          self.window.show()

      def main(self):
          # Todas las aplicaciones de PyGTK deben tener una llamada a gtk.main(). Aqui se deja
          # el control y se espera que suceda un evento (como un evento de teclado o raton).
          gtk.main()

# Si el programa se ejecuta directamente o se pasa como argumento al interprete
# de Python, entonces se crea una instancia de HelloWorld y se muestra
if __name__ == "__main__":
  hello = HelloWorld()
  hello.main()