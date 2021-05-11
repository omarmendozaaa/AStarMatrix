from Constants import DIAGONAL,LINEAL, NEGRO, AZUL, NARANJA

class AStartAlgorithm:
    
    def __init__(self,table):
        self.table = table.board
        self.tableWidth  = table.height
        self.tableHeight = table.height

    def ManhattanDistance(self,origin,target):
        
        targetX = target.col
        targetY = target.row

        originX = origin.col
        originY = origin.row
        
        result = abs(targetX-originX) + abs(targetY-originY)

        return result * 10
        
    def getNeighbors(self,node):

        neighbors = []

        if node.row - 1 >= 0:
            if self.table[node.col][node.row - 1].color != NEGRO:
                self.table[node.col][node.row - 1].direction = "Lineal"
                neighbors.append(self.table[node.col][node.row - 1])

        if node.row + 1 < self.tableWidth:
            if  self.table[node.col][node.row + 1].color != NEGRO:
                self.table[node.col][node.row + 1].direction = "Lineal"
                neighbors.append(self.table[node.col][node.row+1])

        if node.col - 1 >= 0 :
            if  self.table[node.col - 1][node.row].color != NEGRO:
                self.table[node.col - 1][node.row].direction = "Lineal"
                neighbors.append(self.table[node.col - 1][node.row])

        if node.col + 1 < self.tableHeight:
            if  self.table[node.col + 1][node.row].color != NEGRO:
                self.table[node.col + 1][node.row].direction = "Lineal"
                neighbors.append(self.table[node.col + 1][node.row])

        if node.row - 1 >= 0 and node.col - 1 >= 0:
            if (self.table[node.col - 1][node.row - 1].color != NEGRO and 
                (self.table[node.col -1][node.row].color != NEGRO or  self.table[node.col][node.row - 1].color != NEGRO)):    
                self.table[node.col - 1][node.row - 1].direction = "Diagonal"
                neighbors.append(self.table[node.col - 1][node.row - 1])

        if node.row - 1 >= 0 and node.col + 1 < self.tableHeight:
            if (self.table[node.col + 1][node.row - 1].color != NEGRO and
                (self.table[node.col][node.row - 1].color != NEGRO or self.table[node.col + 1][node.row].color != NEGRO)):        
                self.table[node.col + 1][node.row - 1].direction = "Diagonal"
                neighbors.append(self.table[node.col + 1][node.row - 1])

        if node.row + 1 < self.tableWidth and node.col - 1 >= 0:
            if (self.table[node.col - 1][node.row + 1].color != NEGRO and
                (self.table[node.col - 1][node.row].color != NEGRO or self.table[node.col][node.row+1].color != NEGRO) ):        
                self.table[node.col - 1][node.row + 1].direction = "Diagonal"
                neighbors.append(self.table[node.col - 1][node.row + 1])

        if node.row + 1 < self.tableWidth and node.col + 1 < self.tableHeight:
            if ( self.table[node.col + 1][node.row + 1].color != NEGRO and
                (self.table[node.col + 1][node.row].color != NEGRO or self.table[node.col][node.row + 1].color != NEGRO)):
                self.table[node.col + 1][node.row + 1].direction = "Diagonal"
                neighbors.append(self.table[node.col + 1][node.row + 1])

        return neighbors

    def findPath(self,nodeOrigin,nodeTarget):
        
        # Definir los abiertos (Por defecto contendrá el primer nodo)
        openNodes = [nodeOrigin]

        # Definir los cerrados
        closedNodes = []

        # Repetir hasta abiertos es vacio o encontrado
        while  len(openNodes) > 0:


            # Buscar el mejor con la F mínima (Ordenar) [1,2,3,4]
            bestNode = min(openNodes, key=lambda x: x.f)
            
            # Extraer el menor Indice[0] -> MEJOR NODO
            openNodes.remove(bestNode)


            # Mover el nodo a los cerrados
            closedNodes.append(bestNode)
            bestNode.make_closed()

            # Si el mejor nodo es igual a NodeTarget
            if bestNode == nodeTarget:
                print('se encontró el camino')
                break

            neighbors = self.getNeighbors(bestNode)

            for neighbor in neighbors:
                cost = 0
                if neighbor.direction == 'Diagonal':
                    cost =  DIAGONAL
                else:
                    cost = LINEAL
                # Costo actual
                current_cost = bestNode.g + cost

                # Actualizar distancia Manhattan
                neighbor.h =  self.ManhattanDistance(neighbor,nodeTarget)

                # Si se encuentra el hijo en cerrados
                if neighbor in openNodes:
                    # Si el camino actual es menor a valor G del vecino
                    if current_cost <  neighbor.g:
                        neighbor.g =  current_cost
                        neighbor.f = neighbor.g + neighbor.h
                        neighbor.parent = bestNode
                    continue

                # Si se encuentra el hijo en cerrados
                if neighbor in closedNodes:

                    # Si el camino actual es menor a valor G del vecino
                    if current_cost <  neighbor.g:
                        neighbor.g =  current_cost
                        neighbor.f = neighbor.g +  neighbor.h
                        neighbor.parent = bestNode

                        closedNodes.remove(neighbor)
                        neighbor.make_open()
                        openNodes.append(neighbor)
                    continue

                else:
                    neighbor.g  = current_cost
                    neighbor.f = neighbor.g +  neighbor.h
                    neighbor.parent = bestNode
                    neighbor.make_open()
                    openNodes.append(neighbor)
        
        result = []
        endNode = nodeTarget

        while True:
            result.append(endNode)
            if endNode.parent == None:
                break
            endNode = endNode.parent
        
        result.reverse()
        for x in result:
            x.make_path()

        return result    
