import json


# Clase Nodo
class Nodo:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre


# Clase Arista
class Arista:
    def __init__(self, emisor, receptor, peso):
        self.emisor = emisor
        self.receptor = receptor
        self.peso = peso


# Clase GrafoDirigido
class GrafoDirigido:
    def __init__(self):
        self.nodos = {}  # Un diccionario para guardar los nodos
        self.aristas = []  # Una lista para guardar las aristas

    # Función para agregar un nodo
    def agregar_nodo(self, nodo_id, nombre):
        nuevo_nodo = Nodo(nodo_id, nombre)
        self.nodos[nodo_id] = nuevo_nodo

    # Función para agregar una arista
    def agregar_arista(self, emisor_id, receptor_id, peso):
        if emisor_id in self.nodos and receptor_id in self.nodos:
            nueva_arista = Arista(emisor_id, receptor_id, peso)
            self.aristas.append(nueva_arista)

    # Función para obtener la persona con más interacciones
    def persona_con_mas_interacciones(self):
        max_interacciones = 0
        persona = None
        for nodo_id, nodo in self.nodos.items():
            cantidad_interacciones = sum(
                1 for arista in self.aristas if arista.emisor == nodo_id or arista.receptor == nodo_id)
            if cantidad_interacciones > max_interacciones:
                max_interacciones = cantidad_interacciones
                persona = nodo.nombre
        return persona, max_interacciones

    # Función para obtener la relación más fuerte
    def relacion_mas_fuerte(self):
        max_peso = 0
        relacion = None
        for arista in self.aristas:
            if arista.peso > max_peso:
                max_peso = arista.peso
                relacion = (self.nodos[arista.emisor].nombre, self.nodos[arista.receptor].nombre)
        return relacion

    # Función para obtener las personas con más interacciones
    def personas_mas_amigas(self):
        mensajes_entre_personas = {}
        for arista in self.aristas:
            emisor = arista.emisor
            receptor = arista.receptor
            if (emisor, receptor) in mensajes_entre_personas:
                mensajes_entre_personas[(emisor, receptor)] += 1
            else:
                mensajes_entre_personas[(emisor, receptor)] = 1
        max_mensajes = max(mensajes_entre_personas.values())
        personas_con_mas_mensajes = [(self.nodos[emisor].nombre, self.nodos[receptor].nombre) for
                                     (emisor, receptor), cantidad_mensajes in mensajes_entre_personas.items() if
                                     cantidad_mensajes == max_mensajes]
        return personas_con_mas_mensajes, max_mensajes

    # Función para mostrar las interacciones entre personas
    def mostrar_interacciones(self):
        print("Interacciones entre personas:")
        for arista in self.aristas:
            nombre_emisor = self.nodos[arista.emisor].nombre
            nombre_receptor = self.nodos[arista.receptor].nombre
            cantidad_mensajes = arista.peso
            print(f"{nombre_emisor} y {nombre_receptor}: {cantidad_mensajes} interacción.")


# Cargar datos del archivo json
with open('historial_comunicaciones.json', 'r') as archivo_json:
    datos = json.load(archivo_json)
# Crear el grafo dirigido y agregar nodos y aristas desde los datos
grafo = GrafoDirigido()
for dato in datos:
    id_emisor = dato['id_emisor']
    nombre_emisor = dato['nombre_emisor']
    id_receptor = dato['id_receptor']
    nombre_receptor = dato['nombre_receptor']
    peso = 1
    grafo.agregar_nodo(id_emisor, nombre_emisor)
    grafo.agregar_nodo(id_receptor, nombre_receptor)
    grafo.agregar_arista(id_emisor, id_receptor, peso)
# Mostrar todas las interacciones
grafo.mostrar_interacciones()
# Obtener la persona con más interacciones
persona_interacciones, cantidad_interacciones = grafo.persona_con_mas_interacciones()
print(f"La persona con más interacciones es {persona_interacciones} con {cantidad_interacciones} interacciones.")
# Obtener la relación más fuerte
relacion_fuerte = grafo.relacion_mas_fuerte()
print(f"La relación más fuerte es entre {relacion_fuerte[0]} y {relacion_fuerte[1]}.")
# Obtener las personas con más interacciones
personas_interacciones, max_interacciones = grafo.personas_mas_amigas()
print(
    f"Las personas con más interacciones entre si son: {personas_interacciones} con {max_interacciones} interacciones.")
