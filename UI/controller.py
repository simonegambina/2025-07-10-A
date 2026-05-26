import datetime

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._categoryValue = None

    def handleCreaGrafo(self, e):
        cat = self._categoryValue
        date1 = self._view._dp1.value
        date2 = self._view._dp2.value
        self._model.buildGraph(cat, date1, date2)

        nNodi, nArchi = self._model.getGraphDetails()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Date selezionate:"))
        self._view.txt_result.controls.append(ft.Text(f"Start Date: {self._view._dp1.value.date()}"))
        self._view.txt_result.controls.append(ft.Text(f"End Date: {self._view._dp2.value.date()}"))

        self._view.txt_result.controls.append(ft.Text("Grafo creato:"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {nNodi}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {nArchi}"))
        self._view.update_page()

    def handleBestProdotti(self, e):
        bestProdotti = self._model.getNodiPiuVenduti()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Di seguito i nodi maggiormente profittevoli"))
        for p in bestProdotti:
            self._view.txt_result.controls.append(ft.Text(f"{p[0]} - score = {p[1]}"))
        self._view.update_page()

    def handleCercaCammino(self, e):
        pass

    def fillDDCategorie(self):
        categories = self._model.getCategorie()
        categoriesDDOptions = list(map(lambda x: ft.dropdown.Option(
            data = x,
            key = x.category_name,
            on_click= self._choiceCategory),categories))

        self._view._ddcategory.options = categoriesDDOptions
        self._view.update_page()

    def _choiceCategory(self, e):
        self._categoryValue = e.control.data


    def setDates(self):
        first, last = self._model.getDateRange()

        self._view._dp1.first_date = datetime.date(first.year, first.month, first.day)
        self._view._dp1.last_date = datetime.date(last.year, last.month, last.day)
        self._view._dp1.current_date = datetime.date(first.year, first.month, first.day)

        self._view._dp2.first_date = datetime.date(first.year, first.month, first.day)
        self._view._dp2.last_date = datetime.date(last.year, last.month, last.day)
        self._view._dp2.current_date = datetime.date(last.year, last.month, last.day)
