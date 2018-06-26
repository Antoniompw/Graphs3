import queue


class DiGraph:
    def __init__(self):
        self.Vertexes = []

    class Vertex:
        def __init__(self, info):
            self.info = info
            self.mark = False
            self.links = []

        class Link:
            def __init__(self, to, cost):
                self.cost = cost
                self.to = to

    def demark(self):
        for i in self.Vertexes:
            i.mark = False

    def mark_all(self):
        for i in self.Vertexes:
            i.mark = True

    def add_vertex(self, info):
        for vertex in self.Vertexes:
            if vertex.info == info:
                return None
        new_vertex = self.Vertex(info)
        self.Vertexes.append(new_vertex)
        return new_vertex

    def add_link(self, info_a, info_b, cost):
        a = None
        b = None
        for vertex in self.Vertexes:
            if vertex.info == info_a:
                a = vertex
                # if they are both found
                if b is not None:
                    for link in a.links:
                        if link.to.info == info_b:
                            return
                    a.links.append(a.Link(b, cost))
            elif vertex.info == info_b:
                b = vertex
                # if they are both found
                if a is not None:
                    for link in a.links:
                        if link.to.info == info_b:
                            return
                    a.links.append(a.Link(b, cost))

    def add_bulk(self, file_name):
        f = open(file_name)
        for line in f:
            args = line.split(" ")
            # Came only with node info
            if len(args) == 1:
                self.Vertexes.append(self.Vertex(args[0]))
            if len(args) == 4:
                if args[1] == "==":
                    info_a = args[0]
                    info_b = args[2]
                    cost = int(args[3].rstrip("\n"))
                    self.add_vertex(info_a)
                    self.add_vertex(info_b)
                    self.add_link(info_a, info_b, cost)
                    self.add_link(info_b, info_a, cost)
                elif args[1] == "<":
                    info_a = args[0]
                    info_b = args[2]
                    cost = int(args[3].rstrip("\n"))
                    self.add_vertex(info_a)
                    self.add_vertex(info_b)
                    self.add_link(info_b, info_a, cost)
                elif args[1] == ">":
                    info_a = args[0]
                    info_b = args[2]
                    cost = int(args[3].rstrip("\n"))
                    self.add_vertex(info_a)
                    self.add_vertex(info_b)
                    self.add_link(info_a, info_b, cost)

    def lista_de_adjacencias(self):
        for vertex in self.Vertexes:
            print("Aresta: " + str(vertex.info))
            for link in vertex.links:
                print("|| Identificador da aresta ligada: " + str(link.to.info), end=" ")
                print("Custo: " + str(link.cost), end=" || \n")

    def matriz_de_adjacencias(self):
        for vertex in self.Vertexes:
            print("  "+vertex.info, end="")
        for vertex in self.Vertexes:
            print("\n"+vertex.info, end=" ")
            for vertex_2 in self.Vertexes:
                found = False
                for link in vertex.links:
                    if link.to.info == vertex_2.info:
                        print(str(link.cost), end=" ")
                        found = True
                if not found:
                    print(end="   ")
        print()

    def busca_em_largura(self, key):
        fila = queue.Queue()
        if len(self.Vertexes) > 0:
            first = self.Vertexes[0]
            first.mark = True
            fila.put(first)
            print(first.info, end=" => ")
            # Enquanto a fila estiver cheia, visite todos os links e coloque na fila
            while not fila.empty():
                # Tira o primeiro da fila
                vertex = fila.get()
                for link in vertex.links:
                    current_vertex = link.to
                    print(current_vertex.info, end=" => ")

                    # Se nao tiver sido visitado, marque e visite o vertice
                    if not current_vertex.mark:
                        fila.put(current_vertex)
                        current_vertex.mark = True
                    # Se for encontrado
                    if current_vertex.info == key:
                        self.demark()
                        print()
                        return

    def busca_em_profundidade(self, key):
        if len(self.Vertexes) > 0:
            vertex = self.Vertexes[0]
            stack = [vertex]
            vertex.mark = True
            print(vertex.info, end=" => ")
            while vertex is not None:
                item_pushed = False
                for link in vertex.links:
                    # Se ele nao tiver sido marcado
                    if not link.to.mark:
                        vertex = link.to
                        vertex.mark = True
                        stack.append(vertex)
                        item_pushed = True
                        print(vertex.info, end=" => ")
                        if vertex.info == key:
                            self.demark()
                            return
                        break
                if not item_pushed:
                    vertex = stack.pop()

'''
class Graph:

    def __init__(self):
        self.Vertexes = []

    class Vertex:
        def __init__(self, info):
            self.info = info
            self.links = []

        class Link:
            def __init__(self, to, cost):
                self.cost = cost
                self.to = to

    def add_node(self, info):
        self.Vertexes.append(self.Vertex(info))

    def add_link(self, info_a, info_b, cost):
        a = None
        b = None
        for Vertex in self.Vertexes:
            if Vertex.info == info_a:
                a = Vertex
                # if they are both found
                if b is not None:
                    a.links.append(a.Link(self.b, cost))
            elif Vertex.info == info_b:
                b = Vertex
                # if they are both found
                if a is not None:
                    a.links.append(a.Link(self.b, cost))
'''
if __name__ == '__main__':
    di_graph = DiGraph()
    di_graph.add_bulk("test.txt")

    print("Lista de adjacencias:")
    di_graph.lista_de_adjacencias()

    print("Matriz de adjacencias:")
    di_graph.matriz_de_adjacencias()

    print("Busca em largura por Z:")
    di_graph.busca_em_largura("Z")

    print("Busca em profundidade por Z:")
    di_graph.busca_em_profundidade("Z")
