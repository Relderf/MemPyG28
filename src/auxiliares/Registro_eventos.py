from src.auxiliares.Funciones_generales import get_info_usuario_actual as info_usuario
import datetime as dt
import pandas as pd
import os


ruta_inicio = os.getcwd() + os.sep
ruta_registro_eventos = ruta_inicio + 'data' + os.sep + 'usuarios' + os.sep + 'registro_eventos.csv'
columnas = ['fecha', 'hora', 'tiempo', 'partida', 
            '# palabras a adivinar', 'nombre_evento', 
            'usuarie-nick', 'usuarie-genero', 'usuarie-edad',
            'estado', 'palabra', 'nivel', 'dificultad']


def existe_registro_eventos():
    """ Se comprueba que exista el archivo de registro de eventos, en caso de no existir se crea
    vacio con los correspondientes nombres de columnas """

    #esta expresion evalua si existe el directorio que recibe como parametro y retorna un booleano
    if not os.path.isfile(ruta_registro_eventos):
        datos = []
        df_registro_eventos = pd.DataFrame(datos, columns=columnas)
        df_registro_eventos.to_csv(ruta_registro_eventos, index=False, encoding='latin-1')


def numero_partida():
    """ Si el archivo ya esta creado, se lee y consulta si esta vacio, en caso de estar vacio
    el numero de partida va a ser 0 y luego se le suma 1, si no está vacío lee el valor del campo
    "partida" del último registro y lo retorna. En caso de no existir el archivo, llama a que se
    cree y luego se vuelve a ejecutar a si mismo para obtener el numero de la partida """

    if os.path.isfile(ruta_registro_eventos):
        df_registro_eventos = pd.read_csv(ruta_registro_eventos)
        if len(df_registro_eventos) == 0:
            num_partida = 0
            return num_partida

        else:
            num_partida = df_registro_eventos['partida'].iloc[-1]
            return num_partida

    else:
        existe_registro_eventos()
        numero_partida()


def evento_intento(evento_intento):
        """ Se recibe el objeto Evento con algunos datos, 
        se terminan de cargar valores en comun
        para los dos posibles estados y luego se carga
        en el archivo csv """

        evento_intento.partida = numero_partida()
        evento_intento.genero = info_usuario()['Género']
        evento_intento.edad = info_usuario()['Edad']

        evento_intento.cargar_evento()


class Evento():
    def __init__(self): #, tiempo, partida, cant_palabras, nombre_evento, nick, 
                        #genero, edad, estado, palabra, nivel, dificultad):
        self._fecha = self.get_fecha()
        self._hora = self.get_hora()
        self._tiempo = None
        self._partida = None
        self._cant_palabras = None
        self._nombre_evento = None
        self._nick = None
        self._genero = None
        self._edad = None
        self._estado = None
        self._palabra = None
        self._nivel = None
        self._dificultad = None


    @property
    def fecha(self):
        return self._fecha
    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @property
    def hora(self):
        return self._hora
    @hora.setter
    def hora(self, hora):
        self._hora = hora

    @property
    def tiempo(self):
        return self._tiempo
    @tiempo.setter
    def tiempo(self, tiempo):
        self._tiempo = tiempo

    @property
    def partida(self):
        return self._partida
    @partida.setter
    def partida(self, partida):
        self._partida = partida

    @property
    def cant_palabras(self):
        return self._cant_palabras
    @cant_palabras.setter
    def cant_palabras(self, cant_palabras):
        self._cant_palabras = cant_palabras

    @property
    def nombre_evento(self):
        return self._nombre_evento
    @nombre_evento.setter
    def nombre_evento(self, nombre_evento):
        self._nombre_evento = nombre_evento

    @property
    def nick(self):
        return self._nick
    @nick.setter
    def nick(self, nick):
        self._nick = nick

    @property
    def genero(self):
        return self._genero
    @genero.setter
    def genero(self, genero):
        self._genero = genero

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    
    @property
    def estado(self):
        return self._estado
    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @property
    def palabra(self):
        return self._palabra
    @palabra.setter
    def palabra(self, palabra):
        self._palabra = palabra

    @property
    def nivel(self):
        return self._nivel
    @nivel.setter
    def nivel(self, nivel):
        self._nivel = nivel

    @property
    def dificultad(self):
        return self._dificultad
    @dificultad.setter
    def dificultad(self, dificultad):
        self._dificultad = dificultad
    
    def get_fecha(self):
        fecha = dt.datetime.now().strftime("%d/%m/%y")
        return fecha

    def get_hora(self):
        hora = dt.datetime.now().strftime("%H:%M:%S")
        return hora


    def cargar_evento(self):
        """ Se carga la nueva fila al registro de eventos
        con los datos del nuevo evento que se registro """
        
        df_registro_eventos = pd.read_csv(ruta_registro_eventos, encoding='latin-1')
        datos = [[self._fecha, self._hora, self._tiempo, self._partida, self._cant_palabras, self._nombre_evento, self._nick,
                 self._genero, self._edad, self._estado, self._palabra, self._nivel, self._dificultad]]

        df_nueva_fila = pd.DataFrame(datos, columns=columnas)
        df_registro_eventos = df_registro_eventos.append(df_nueva_fila, ignore_index=True)
        df_registro_eventos.to_csv(ruta_registro_eventos, index=False, encoding='latin-1')