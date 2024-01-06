# Módulo jugadores.py
class Jugador:
    def __init__(self, id_jugador, nombre, edad):
        self.id_jugador = id_jugador
        self.nombre = nombre
        self.edad = edad
        self.partidos_jugados = 0
        self.partidos_ganados = 0
        self.partidos_perdidos = 0
        self.puntos_a_favor = 0

    def __str__(self):
        return f"{self.id_jugador} {self.nombre} {self.partidos_jugados} {self.partidos_ganados} {self.partidos_perdidos} {self.puntos_a_favor}"

# Módulo torneo.py
#from jugadores import Jugador

class TorneoTenisMesa:
    def __init__(self):
        self.jugadores = {"Novato": [], "Intermedio": [], "Avanzado": []}

    def registrar_jugador(self, id_jugador, nombre, edad, categoria):
        jugador = Jugador(id_jugador, nombre, edad)
        self.jugadores[categoria].append(jugador)

    def iniciar_partidos(self, categoria):
        # Aquí deberías implementar la lógica de los partidos y actualizar los atributos de los jugadores.

    #def mostrar_registros(self):
        print("Id Jugador PJ PG PP PA TP")
        for categoria, jugadores_categoria in self.jugadores.items():
            for jugador in jugadores_categoria:
                print(jugador)

    def obtener_ganador_categoria(self, categoria):
        jugadores_categoria = self.jugadores[categoria]

        if len(jugadores_categoria) < 5:
            print(f"No hay suficientes jugadores en la categoría {categoria} para determinar un ganador.")
            return None

        ganador = max(jugadores_categoria, key=lambda jugador: jugador.puntos_a_favor)
        print(f"Ganador de la categoría {categoria}: {ganador.nombre} con {ganador.puntos_a_favor} puntos a favor.")
        return ganador
