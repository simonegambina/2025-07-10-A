import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._products = []
        self._idMapP = {}

    def buildGraph(self, cat, date1, date2):
        self._graph.clear()
        self._products = DAO.getProductsByCategory(cat)
        for p in self._products:
            self._idMapP[p.product_id] = p

        self._graph.add_nodes_from(self._products)

        allEdges = DAO.getAllEdges(cat, date1, date2, self._idMapP)
        for e in allEdges:
            self._graph.add_edge(e.p1, e.p2, weight = e.peso)

    def getNodiPiuVenduti(self):
        listNodesPesata = []
        for n in self._graph.nodes:
            score = 0
            for e in self._graph.out_edges(n, data=True):
                score += e[2]["weight"]
            for e in self._graph.in_edges(n, data=True):
                score -= e[2]["weight"]

            listNodesPesata.append((n, score))

        listNodesPesata.sort(key=lambda x: x[1], reverse=True)

        return listNodesPesata[0:5]


    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getDateRange(self):
        return DAO.getDateRange()

    def getCategorie(self):
        return DAO.getCategorie()

