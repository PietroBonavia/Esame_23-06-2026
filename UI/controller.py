from model.model import Model
from UI.view import View
import flet as ft

class Controller:
    def __init__(self, view : View, model : Model):
        self._view = view
        self._model = model

    def handler_crea_grafo(self, e):

        self._view._lst_result.controls.clear()
        self._model._graph.clear()

        valore_inserito = self._view._txt_nBus.value

        try:
            valore = int(valore_inserito)

            if valore <= 0:
                self._view.show_alert('Inserire un valore > 0')
                return

        except(ValueError, TypeError):
            self._view.show_alert('Inserire un valore intero valido')
            return

        self._model.build_graph(self._view._txt_nBus.value)


        self._view._lst_result.controls.append(ft.Text(f'Numero di nodi: {self._model._graph.number_of_nodes()}'))
        self._view._lst_result.controls.append(ft.Text(f'Numero di archi: {self._model._graph.number_of_edges()}'))


        for nodo in self._model._graph.nodes():
            self._view._ddUtente.options.append(ft.dropdown.Option(f'{nodo.name} ({nodo.user_id})'))



        self._view.update_page()


    def handler_utenti_connessi(self, e):

        result = []

        for nodo in self._model._graph.nodes():
            contatore = 0
            for u, v, w in self._model._graph.edges(nodo, data = True):
                contatore += w['weight']

            result.append((nodo, contatore))

        result.sort(key = lambda x: x[1], reverse = True)

        for elemento in result:
            self._view._lst_result.controls.append(ft.Text(f'{elemento[0].name} ({elemento[0].user_id}) - strenght = {elemento[1]}'))

        self._view.update_page()

    def cerca_sequenza(self, e):

        valore_inserito = self._view._txtL.value
        try:
            valore = int(valore_inserito)

            if valore < 2 or valore > self._model._graph.number_of_nodes():
                self._view.show_alert('Inserire un valore compreso nel range')
        except(ValueError, TypeError):
            self._view.show_alert('Inserire un valore intero valido')

        self._view.update_page()








