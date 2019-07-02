"""
program vylosuje ze seznamu slovicek 5 slovicek na základě vybraného ročníku
"""

from PyQt5 import QtWidgets as QW, uic
import importlib_resources
from random import choice

def find_widget(window, name):
	widget = window.findChild(QW.QWidget, name) #nemusim hledat konkretni jmeno widgetu
	if widget == None:
		raise LookupError(name)
	return widget

def main():
	#vytvori se aplikace a okno
	app = QW.QApplication([]) 
	window = QW.QDialog()

	#nacte se ui vytvorene v Qt Degigneru
	with importlib_resources.open_text("losovatko", "losovatko.ui") as file:
		window = uic.loadUi(file)

	#vyhledani prvku, se kterymi bude aplikace pracovat
	cb_year =  find_widget(window, "cb_year")
	cb_translate = find_widget(window, "cb_translate")
	lw_result = find_widget(window, "lw_result")
	te_minute = find_widget(window, "te_minute")
	pb_start = find_widget(window, "pb_start")

	def set_year():
		#nacteni rocniku
		year = cb_year.currentText()
		

		#na zaklade zvoleneho rocniku se saha do souboru se slovicky z daneho rocniku
		if year == "2. třída":
			source = "slovicka2.txt"
		elif year == "3. třída":
			source = "slovicka3.txt"
		elif year == "4. třída":
			source = "slovicka4.txt"
		elif year == "5. třída":
			source = "slovicka5.txt"
		else:
			raise ValueError(year)

		#nacteni slovicek do programu
		slovnik = []
		with importlib_resources.open_text("slovicka", source) as file:
			for line in file:
				line = line.rstrip()
				slovnik.append(line)

		#vylosovani urceneho poctu slovicek
		vyber = []
		pocet = 5
		while len(vyber) < pocet:
			slovo = choice(slovnik)
			if slovo not in vyber:
				vyber.append(slovo)
			else:
				slovo= choice(slovnik)

		#nejprve plochu vycistim a pak na ni vypisu slovicka z vyberu
		lw_result.clear()
		lw_result.addItems(vyber)

	#pri kazde zmene rocniku se zmeni set  vypsanych slovicek
	cb_year.currentTextChanged.connect(set_year)
	lw_result.itemChanged.connect(set_year)

	#spusteni okna a aplikace
	window.show()
	return app.exec()