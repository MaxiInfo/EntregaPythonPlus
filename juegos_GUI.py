import hangman
import reversegam
import tictactoeModificado
import pickle
import PySimpleGUI as sg
import os
from datetime import datetime

nom_arch = "ARCHIVO/jugadoresGUI.txt"

list_players = []


def add_player(player):
	if (player['name'] != None):
		global list_players
		global nom_arch
		if os.path.exists(nom_arch):
			with open("ARCHIVO/jugadoresGUI.txt", 'rb') as arch_rb:
				list_players = pickle.load(arch_rb)
		list_players.append(player)
		with open("ARCHIVO/jugadoresGUI.txt", 'wb') as arch_wb:
			pickle.dump(list_players, arch_wb)
	else:
		print('es necesario un nombre de jugador para ingresarlo a la base de datos')

def print_list_player():
	global list_players
	if os.path.exists(nom_arch):
		with open("ARCHIVO/jugadoresGUI.txt", 'rb') as arch_rb:
			list_players = pickle.load(arch_rb)
	else:
		print('el archivo no existe')
	if (list_players != []):
		for i in list_players:
			print('jugador:'
				  '\nnombre:', i['name'],
				  '\nUltima conexion:', i['time'],
				  '\nJuegos:', i['games']
				  )
	else:
		print('el archivo esta vacio')


format = '%d-%m-%y %H:%M:%S'
layout = [
	[sg.Text('Ingrese un nombre de jugador')],
	[sg.InputText(size=(20,1),key='nom'),sg.Button('Cambiar nombre',key='change')],
	[sg.Text('_'*20)],
	[sg.Text('Seleccione el juego que desee jugar')],
	[sg.Button('Ahorcado',key='ahorcado'),sg.Button('Ta-Te-Ti',key='tateti'),sg.Button('Otello',key='otello')],
	[sg.Text('_'*20)],
	[sg.Button('Salir',key='salir')]
	]

def main(args):
	player = {'name': '', 'time': '', 'games': []}
	window = sg.Window('Menu').Layout(layout)
	while True:
		button, data = window.Read()
		#genero el dia y horario cuando se ejecuta el menu para luego poder cargar al archivo
		T = datetime.today()
		T = T.strftime(format)
		player['time'] = T
		player['name']= data['nom']
		if button == 'ahorcado':
			player['games'].append('Ahorcado')
			hangman.main()
		elif button == 'tateti':
			player['games'].append('Ta-TE-TI')
			tictactoeModificado.main()
		elif button == 'otello':
			player['games'].append('Otello')
			reversegam.main()
		elif(button == 'change'):
			window.FindElement('nom').Update('')
			# AGREGO UN JUGADOR A LA BASE DE DATOS
			add_player(player)
			player['games']= []
		elif button in ('salir',None):
	 		break

	# AGREGO UN JUGADOR A LA BASE DE DATOS
	add_player(player)
	Imp = bool(int(input('Imprimir la lista? SI = 1 | NO = 0')))
	if Imp:
		# IMPRIMO LA LISTA DE JUGADORES
		print_list_player()
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))