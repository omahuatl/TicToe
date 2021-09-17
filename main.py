from tictoe import TicToe

gato=TicToe()

print("Tic Toe")
while gato.status == "_":
    print(f"turno de {gato.turn}")
    la_x=input("Coordenada X..:")
    la_y=input("Coordenada Y..:")
    if gato.play_turn(int(la_x),int(la_y)):
        gato.print_board()
    else:
        print("jugada no valida, intenta de nuevo")


print("Fin del juego")
gato.print_board()

