from random import shuffle, randint
from copy import deepcopy 




#Armazena as informações padrões dos comodos
class ComodosInfo:
    def __init__(self, simbol, minSize, maxSize):
        self.simbol = simbol
        self.minSize = minSize 
        self.maxSize = maxSize 

simbols = dict(
    sala = ComodosInfo("1", 30, 40),
    cozinha = ComodosInfo("2", 10, 15),
    banheiro = ComodosInfo("3", 3, 8),
    corredor = ComodosInfo("*", 2,2),
    escada = ComodosInfo("4", 4, 4),
    salaDeJantar = ComodosInfo("5", 15, 20),
    areaServico = ComodosInfo('6', 6, 10),
    closet = ComodosInfo('7', 3, 4),
    quarto = ComodosInfo('8', 12, 30),
    ginastica = ComodosInfo('9', 20, 30)
)



class Casa:
    def __init__(self, width , height):
        #Armazena os andares
        self.andares = []
        self.width = width
        self.height = height
        self.fitness = 0
        self.portax = ''
        self.portay = ''
        self.usedSpace = 0
        self.totalSpace = 0

    def printHouse(self):
        print(f"fitness: {self.fitness}")
        # print(f"porta de entrada: \n x: {self.portax}, y: {self.portay}")
       
        self.printFloors()

    def printFloors(self):
        for andar in self.andares:
            andar.print()

    def calcFitness(self):
        fitness = 0
        
        for i in range(len(self.andares)):
            for comodo in self.andares[i].comodos:
                if i == 0: 
                    if comodo.tipo == 'areaServico' or comodo.tipo == 'banheiro':
                        fitness+= 10
                
                elif i == 1: 
                    if comodo.tipo == 'quarto' or comodo.tipo == 'closet':
                        fitness+= 10

                elif i == 2:
                    if comodo.tipo == 'areaServico':
                        fitness+= 10

        #Dá um bonus por uso de espaço
        totalspace = self.width * self.height
        usedSpace = 0
        for i in range(0,2):
            usedSpace += totalspace - calcRemaningSpace(self.andares[i], self.width, self.height)

       
        bonusSpaceUsed =  0.2 * usedSpace
        fitness += bonusSpaceUsed
        self.fitness = fitness
        self.usedSpace = usedSpace
        self.totalSpace = totalspace

        

    def generateHouse(self):
        for i in range(len(self.andares)):
            self.andares[i].createMap(self.width, self.height)

    
        

class Andar:
    def __init__(self, nome):
        #nome do andar 
        self.nome = nome
        #lista dos comodos presentes no andar
        self.comodos = []
        #Como os cômodos foram posicionados
        self.mapa= []

    def print(self):
        print(f"####### {self.nome} #######")
        for comodo in self.comodos:
            comodo.print()
        
    def insertRoom(self, type, width, height):
        newRoom = Comodo(type, width, height)
        self.comodos.append(newRoom)

    
class Comodo:
    def __init__(self, tipo, largura, altura):
        self.tipo = tipo
        self.altura = altura
        self.largura = largura
        self.iniciox, self.inicioy = 0, 0
        self.portax, self.portay = 0, 0
        self.janelax, self.janelay = 0, 0

    def print(self):
        print(f'------{self.tipo}')
        print(f'altura: {self.altura}, largura: {self.largura}')
        # print(f'iniciox: {self.iniciox}, inicioY: {self.inicioy} ')
        # print(f'portax: {self.portax}, portay: {self.portay}')
        # print(f'janelax: {self.janelax}, janelay: {self.janelay}')


#Calcula quanto espaço da área total de uma andar foi ocupada por quartos
def calcRemaningSpace(andar, totalWidth, totalHeight):

    areaTotal = totalWidth * totalHeight
    for room in andar.comodos:
        roomm2 = room.altura * room.largura
        areaTotal -= roomm2

    return areaTotal


#Preenche todos os andares da casa com comodos
def sorteiaComodos(casa):

    #Comodos obrigatórios do térreo
    RoomsT = ['sala', 'cozinha', 'escada', 'salaDeJantar']
    #Quartos que não foram adicionados no terreo
    remainingRooms = [x for x in list(simbols.keys()) if x not in RoomsT and x != 'corredor']
    remainingRooms.extend(['quarto'] * 2)

    shuffle(remainingRooms)

    #Sorteia os valores do térreo
    for roomName in RoomsT:
        width, height = drawRoomsSize(roomName, casa) 
        casa.andares[0].insertRoom(roomName, width, height)

    remainingSpaceT = calcRemaningSpace(casa.andares[0], casa.width, casa.height)
    remainingSpace1 =  casa.width * casa.height



    #enquanto a lista não está vazia vai distribuindo os comodos pelos andares
    while(remainingRooms):

        roomWidth, roomHeight = drawRoomsSize(remainingRooms[0], casa) 
        roomSize = roomWidth * roomHeight
        floor = 0

        #se ambos os quartos tem espaço pra colocar, sorteia quem recebe o quarto
        if remainingSpaceT >= roomSize and remainingSpace1 >= roomSize :
            #chance da laje receber area de serviço
            if(remainingRooms[0] == 'areaServico'):
                floor = randint(0,2)
            else:
                floor = randint(0,1)

        elif remainingSpaceT >= roomSize and remainingSpace1 < roomSize:
            floor = 0
            
        elif remainingSpace1 >= roomSize and remainingSpaceT < roomSize:
            floor = 1
            

        if floor == 0:
            remainingSpaceT -= roomSize
        elif floor == 1:
            remainingSpace1 -= roomSize

        casa.andares[floor].insertRoom(remainingRooms[0], roomWidth, roomHeight)
        remainingRooms.pop(0) 

    casa.andares[1].insertRoom('escada', 2,2)
    casa.andares[2].insertRoom('escada', 2,2)
    
#retorno valores aletórias da largura e altura
def drawRoomsSize(comodo,casa):

    minS = simbols[comodo].minSize
    maxS = simbols[comodo].maxSize
    
    if minS == maxS:
        return int(minS/2), int(maxS/2)
    
    while True:

        alturaSize = randint(1, 10)
        larguraSize = randint(1, 10)

        if comodo != 'sala' and alturaSize == casa.height or larguraSize == casa.width:
            continue

        if alturaSize*larguraSize >= minS and alturaSize*larguraSize <= maxS and alturaSize <= casa.height and larguraSize <= casa.width:
            if alturaSize > casa.height:
                return alturaSize, larguraSize
            return larguraSize, alturaSize
        

# Adiciona corredores para acesso a todos os cômodos
def addCorridors(planta, width, height):   
    for y in range(height):
        for x in range(width):
            if planta[y][x] == ' ':
                # Verifica se há cômodos adjacentes
                if (x > 0 and planta[y][x-1] != ' ' and planta[y][x-1] != simbols['corredor'].simbol) or \
                    (x < width-1 and planta[y][x+1] != ' ' and planta[y][x+1] != simbols['corredor'].simbol) or \
                    (y > 0 and planta[y-1][x] != ' ' and planta[y-1][x] != simbols['corredor'].simbol) or \
                    (y < height-1 and planta[y+1][x] != ' ' and planta[y+1][x] != simbols['corredor'].simbol):
                    planta[y][x] = simbols['corredor'].simbol

    # Conecta os corredores horizontalmente
    for y in range(height):
        start = None
        for x in range(width):
            if planta[y][x] == simbols['corredor'].simbol:
                if start is None:
                    start = x
            elif start is not None:
                for i in range(start, x):
                    planta[y][i] = simbols['corredor'].simbol
                start = None

    # Conecta os corredores verticalmente
    for x in range(width):
        start = None
        for y in range(height):
            if planta[y][x] == simbols['corredor'].simbol:
                if start is None:
                    start = y
            elif start is not None:
                for i in range(start, y):
                    planta[i][x] = simbols['corredor'].simbol
                start = None



def addFrontDoor(casa, planta, dir):
    start, finish = 0, casa.width - 1
    comodos = casa.andares[0].comodos

    for x in range(start, finish):
        if planta[0][x] == simbols['sala'].simbol:
            index = next(i for i, p in enumerate(comodos) if p.tipo == 'sala')
            ix = comodos[index].iniciox
            iy = comodos[index].inicioy
            fx = comodos[index].largura - 1
            positionDoor = randint(ix + 1, fx - 1)
            planta[0][positionDoor] = 'P'
            casa.portax = positionDoor
            casa.portay = 0
            break


def addInternalDoors(andar, planta, width, height, dir):
    comodos = andar.comodos

    for comodo in comodos:

        if comodo.tipo == 'escada':
            continue

        #coordenadas de inicio/fim do comodo
        ix, iy = comodo.iniciox, comodo.inicioy
        fx = comodo.largura + ix - 1
        fy = comodo.altura + iy - 1
        sides = checkInternalWalls(comodo, width, height)

        isruning = True

        while(isruning):
            if(len(sides) == 0): 
                break

            if(len(sides) > 1):
                r = randint(0, len(sides) - 1)
            else:
                r = 0

            #TODO: adaptar pra poder colocar portas entre comodos (exige mudar os corredores)
            match sides[r]:
                    case 'C':
                        #garante que é em um corredor
                        for x in range(ix, fx):
                            if planta[iy - 1][x] == simbols['corredor'].simbol:
                                r = randint(x, fx)
                                planta[iy][r] = 'p'
                                comodo.portax = r
                                comodo.portay = iy
                                isruning = False
                                break

                        #Se não for corredor
                        sides.remove('C')
                    case 'B':
                         #garante que é em um corredor
                        for x in range(ix, fx):
                            if planta[fy + 1][x] == simbols['corredor'].simbol:
                                r = randint(x, fx)
                                planta[fy][r] = 'p'
                                comodo.portax = r
                                comodo.portay = fy
                                isruning = False
                                break

                        #Se não for corredor
                        sides.remove('B')
                    case 'E':
                         #garante que é em um corredor
                        for y in range(iy, fy):
                            if planta[y][ix - 1] == simbols['corredor'].simbol:
                                r = randint(y, fy)
                                print(f"radint: {r}")
                                planta[r][ix] = 'p'
                                comodo.portax = ix
                                comodo.portay = r
                                isruning = False
                                break
                        
                        #Se não for corredor
                        sides.remove('E')

                    case 'D':
                        #garante que é em um corredor
                        for y in range(iy, fy):
                            if planta[y][fx + 1] == simbols['corredor'].simbol:
                                r = randint(y, fy)
                                planta[r][fx] = 'p'
                                comodo.portax = fx
                                comodo.portay = r
                                isruning = False
                                break
                        
                        #Se não for corredor
                        sides.remove('D')


#Retonra uma lista de paredes do comodo que estão dentro da casa
def checkInternalWalls(comodo, width, height):
    sides = []

    #coordenadas de inicio/fim do comodo
    ix, iy = comodo.iniciox, comodo.inicioy
    fx = comodo.largura + ix - 1
    fy = comodo.altura + iy - 1

    if (fx + 1) < width:
        sides.append('D')
    
    if (fy + 1) < height:
        sides.append('B')

    if (ix - 1) > 0:
        sides.append('E')

    if (iy - 1) > 0:
        sides.append('C') 
    
    return sides

#Retorna uma lista com todas as paredes viradas pra rua  do comodo
def checkExternalWalls(comodo, width, height):
    sides = []

    #coordenadas de inicio/fim do comodo
    ix, iy = comodo.iniciox, comodo.inicioy
    fx = comodo.largura + ix - 1
    fy = comodo.altura + iy - 1

    #esquerda
    if ix-1 < 0:
        sides.append('E')
    #cima
    if iy - 1 < 0:
        sides.append('C')
    #baixo
    if  fy + 1 > height:
        sides.append('B')
    #direita
    if fx + 1 > width:
        sides.append('D')

    return sides



def addWindows(andar, planta, width, height):

    for comodo in andar.comodos:
        if comodo.tipo == 'escada':
            continue
        
        #coordenadas de inicio/fim do comodo
        ix, iy = comodo.iniciox, comodo.inicioy
        fx = comodo.largura + ix - 1
        fy = comodo.altura + iy - 1

        sides = checkExternalWalls(comodo, width, height)

        #um canto aleatório pra por a janela
        if len(sides) != 0:
            r = randint(0, len(sides) - 1)


            match sides[r]:
                case 'C':
            
                    r = randint(ix, fx)
                    planta[iy][r] = 'W'
                    comodo.janelax = r
                    comodo.janelay = iy

                case 'B':

                    r = randint(ix, fx)
                    planta[fy][r] = 'W'
                    comodo.janelax = r
                    comodo.janelay = fy

                case 'E':

                    r = randint(iy, fy)
                    planta[r][ix] = 'W'
                    comodo.janelax = ix
                    comodo.janelay = r

                case 'D':

                    r = randint(iy, fy)
                    planta[r][fx] = 'W'
                    comodo.janelax = fx
                    comodo.janelay = r
                    
            

# Função para desenhar a casa no terminal
def drawHouse(casa, direcao):
    # Obtém as dimensões da casa
    width = casa.width
    height = casa.height

    # Cria uma matriz para representar a planta da casa
    planta = [[' ' for _ in range(width)] for _ in range(height)]

    # Preenche a matriz com os cômodos
    for andar in casa.andares:
        for comodo in andar.comodos:
            # Encontra uma posição livre para o cômodo
            comodo.print()
            
            # Define a ordem de preenchimento com base na direção
            if direcao == 'C':
                x_range = range(width)
                y_range = range(height)
            elif direcao == 'D':
                #se o sentido for para direira ele preenche da esquerda para direita 
                x_range = range(width - 1, -1, -1)
                y_range = range(height)
            elif direcao == 'B':
                #se o sentido for para baixo ele preenche do final da altura para o inicio 
                x_range = range(width)
                y_range = range(height - 1, -1, -1)
            elif direcao == 'E':
                #se o sentido for para esquerda e normal
                x_range = range(width )
                y_range = range(height )
            else:
                # Caso a direção não seja reconhecida, usa a ordem padrão
                x_range = range(width)
                y_range = range(height)

            for y in y_range:
                for x in x_range:
                    if (x + comodo.largura <= width and y + comodo.altura <= height and
                        all(planta[y+i][x+j] == ' ' for i in range(comodo.altura) for j in range(comodo.largura))):
                        # Preenche o espaço do cômodo na matriz
                        for i in range(comodo.altura):
                            for j in range(comodo.largura):
                                planta[y+i][x+j] = simbols[comodo.tipo].simbol

                        comodo.iniciox = x
                        comodo.inicioy = y
                        
                        # Sai dos loops após posicionar o cômodo
                        break
                else:
                    continue
                break

        addCorridors(planta, width, height)
        #addFrontDoor(casa, planta, direcao)
        addInternalDoors(andar, planta, width, height, direcao)
        addWindows(andar, planta, width, height)

        # Imprime a planta da casa
        # print("\nPlanta da Casa:")
        # print("+" + "-" * (width) + "+")
        # for linha in planta:
        #     print("|" + "".join(linha) + "|")
        # print("+" + "-" * (width) + "+")

        # # Imprime a legenda
        # print("\nLegenda:")
        # for tipo, info in simbols.items():
        #     print(f"{info.simbol}: {tipo}")
        
        planta = [[' ' for _ in range(width)] for _ in range(height)]

def geraPopInicial( width, height):
    for i in range(0, popSize):
        casa = Casa(width, height)

        #inicializa os andares
        casa.andares = [Andar('Térreo'), Andar('1 Andar'), Andar('Laje')]
    
        #preenche os andares da casa com comodos aleatórios
        sorteiaComodos(casa)
        casa.calcFitness()
        pop.append(casa)
    

def printPop(pop):
    for i in range(len(pop)):
        print('\n')
        # pop[i].printFloors()
        # print(f'\n{pop[i].fitness}')
        

def getFitness(casa):
    return casa.fitness

#Retorna uma sublista com cromossomos aleatórios e distintos
def drawSubPop(pop, size):
    subPop = []
    tempPop = deepcopy(pop)
    for i in range(size):
        r = randint(0, len(tempPop) - 1)
        subPop.append(tempPop[r])
        tempPop.pop(r)

    return subPop

#Substitui os piores cromossomos pelos novos
def insertIntoPop(pop, newCromossomes):
    sizePop = len(pop) - 1
    for i in range(len(newCromossomes)):
        pop[sizePop - i] = newCromossomes[i]

#Seleção por torneio.
#Insere 3 novos mutantes toda geração
def selectParentes():
    newMutants = []

    for i in range(3):
        r = randint(2, len(pop))
        subPop = drawSubPop(pop, r)
        subPop.sort(key = getFitness, reverse = True)
        mutant = mutate(subPop[0])
        newMutants.append(mutant)

    insertIntoPop(pop, newMutants)

def mutate(casa):
    
    #muta os andares---------------------------
    #Quartos que não podem ser mutados
    fixedT = ['sala', 'cozinha', 'escada', 'salaDeJantar']

    remaingT = [x for x in casa.andares[0].comodos if x.tipo not in fixedT]
    remaning1A = [x for x in casa.andares[1].comodos if x.tipo != 'escada']

    if len(remaingT) != 0:

        rt = randint(0,  len(remaingT) - 1) if len(remaingT) > 1 else 0
        r1 = randint(0,  len(remaning1A) - 1)

        roomt = remaingT[rt]
        indexrt = casa.andares[0].comodos.index(roomt)
        room1 = remaning1A[r1]

        #Realizar a troca
        casa.andares[0].comodos.remove(roomt)
        casa.andares[1].comodos.pop(r1)

        casa.andares[0].comodos.insert(r1, room1)
        casa.andares[1].comodos.insert(indexrt, roomt)

    #muta o tamanho dos comodos ----
    for i in range(0,2):
        rand = randint(1, 100)
        if rand >= 50:
            rand = randint(0, len(casa.andares[i].comodos) - 1)
            #Só muda o valor do cômodo se ele couber  
            space = calcRemaningSpace(casa.andares[i], casa.width, casa.height)
            newW, newH =  drawRoomsSize(casa.andares[i].comodos[rand].tipo, casa)
            if(space >= newW * newH):
                casa.andares[i].comodos[rand].altura, casa.andares[i].comodos[rand].altura = newW, newH

    casa.calcFitness()
    return casa



pop = []
popSize = 10
geracoes = 2
# dir = 'N'
def main(dir):
    with open('input_data.txt', 'r') as file:
        data = file.readline().strip()
        width, height = map(int, data.split(' '))

    # width = int(input("Digite a largura da casa: "))
    # height = int(input("Digite a altura da casa: "))
    # dir = input("Digite a direção da casa: ")
    geraPopInicial(width, height)
    # printPop(pop)
    pop.sort(key = getFitness, reverse = True)

    # # TODO: desenhar as casas
    for i in range(0, geracoes):
        # print("-------------------------------")
        selectParentes()
        pop.sort(key = getFitness, reverse = True)
        # printPop(pop[i])


    # print(pop[0].fitness)
    drawHouse(pop[0], dir)

    # pop[0].printHouse()
    return pop[0]



if __name__ == "__main__":
    main()