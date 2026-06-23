from database.dao import Dao
import networkx as nx

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._users_list = []
        self.load_all_users()
        self.map = {}

    def load_all_users(self):
        self._users_list = Dao.read_all_users()
        print(f"Users: {self._users_list}")

    def build_graph(self, n_bus):

        for user in self._users_list:
            self.map[user.user_id] = user

        nodi = Dao.get_nodi(n_bus)

        for nodo in nodi:
            nodo1 = self.map[nodo[0]]
            self._graph.add_node(nodo1)


        archi = Dao.get_archi()

        for arco in archi:
            nodo1 = self.map[arco[0]]
            nodo2 = self.map[arco[1]]
            if nodo1 in self._graph.nodes() and nodo2 in self._graph.nodes():
                self._graph.add_edge(nodo1, nodo2, weight=arco[2])
