def intro():
    print("""
        TTTTTT  AA        TTTTTT EEEE       TTTTTT III 
          TT   A  A         TT   E            TT    I  
          TT   AAAA  ===    TT   EEE   ===    TT    I  
          TT   A  A         TT   E            TT    I  
          TT   A  A         TT   EEEE         TT   III 

                           ▄▀▄     ▄▀▄
                          ▄█░░▀▀▀▀▀░░█▄
                     ▄▄   █░░░░░░░░░░░█   ▄▄
                    █▄▄█  █░░▀░░┬░░▀░░█  █▄▄█
        ===============================================
    """)                                    
                                           
    print("""Hey! Juguemos al TaTeTi! Primero cada jugador debe elegir cual será su marcador. 
    Luego irán eligiendo, por turnos, donde colocar sus marcadores.
    Imagina las posiciones como el teclado numérico de tu computadora\n""")


def imprimir_tablero(board):
    print()
    print("┏━┯━┯━┓")
    print(f"┃{board[7]}│{board[8]}│{board[9]}┃")
    print("┠─┼─┼─┨")
    print(f"┃{board[4]}│{board[5]}│{board[6]}┃")
    print("┠─┼─┼─┨")
    print(f"┃{board[1]}│{board[2]}│{board[3]}┃")
    print("┗━┷━┷━┛")
    print()


def player_marcador():
    marcador = " "
    
    while marcador not in ['X', 'x', '0', 'o', 'O']:       
        marcador = input("Jugador 1, ¿Quieres jugar con las X o con los O?: ")
        
    if marcador in ["X", 'x']:
        player1 = "ᳵ"
        player2 = "○"
    else:
        player1 = "○"
        player2 = "ᳵ"
    
    print(f"Okay! Jugador 1 juega con '{player1}', jugador 2 juega con '{player2}'!")
    
    return (player1, player2)


def turno_player(board, player):
    while True:
        print(f"Jugador '{player}' es tu turno")
        posicion = input(f"Elegi una posición VACIA del 1 al 9: ")
        
        if posicion.isdigit() == False:
            print("Eso no es un número :|")
            continue

        posicion = int(posicion)
        if 0 < posicion < 10:
            if board[posicion].isdigit():
                board[posicion] = player
                return


def termino_el_juego(board):
    """
        Recibe el tablero y chequea si el juego termino, devuelve verdadero si asi fue.
    """

    for n in [1, 4, 7]:  # Filas
        if board[n] == board[n+1] == board[n+2]:
            print(f"Gano '{board[n]}'!!")
            return True

    for m in [1, 2, 3]:  # Columnas
        if board[m] == board[m+3] == board[m+6]:
            print(f"Gano '{board[m]}'!!")
            return True
    
    if (board[1] == board[5] == board[9] or
        board[3] == board[5] == board[7]):
        print(f"Gano '{board[5]}'!!")
        return True
    
    for i in range(1,10):
        if board[i].isdigit():
            return False

    print("Empataron!!")
    return True


def turno(board, player):
    imprimir_tablero(board)
    turno_player(board, player)


def init():
    tablero = list(map(str, range(10)))
    return tablero


def juego_completo():
    board = init() 
    cont = 0

    intro()
    jugadores = list(player_marcador())

    while True:
        while not termino_el_juego(board):
            turno(board, jugadores[cont])
            cont = (cont + 1) % 2
                
        print("Game over!")
        imprimir_tablero(board)

        jugar_de_nuevo = 'l'
        while jugar_de_nuevo not in ['s', 'n', 'S', 'N']:
            jugar_de_nuevo = input("Jugamos de nuevo? s/n: ")          
            if jugar_de_nuevo in ['s', 'S']:
                board = init()
                print('\n' * 10)
                intro()
            elif jugar_de_nuevo in ['n', 'N']:
                print('Ok, bye :(')
                return


if __name__ == '__main__':  # Solo corre si se ejecuto, no si se importa
    juego_completo()