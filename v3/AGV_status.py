class AGV_status:
    def __init__(self,number):#Inicializacion del agv
        self.n=number;
        self.mission_sent = False;
        self.in_mission = False;
        self.but_em_pressed=False;
        self.paused = False;
        self.emergency = False;
        self.waiting_for_IBE=False;
        self.in_node = 3;
        self.going_to_node = 3;
        self.distanceTravelled = 0;
    def set_pos(self,pos): #Lo ubica en un nodo en especifico
        self.in_node=pos;
        self.going_to_node = pos;
    def new_mission(self,mission_blocks_nodes,mission_blocks_dist, mission_IBE):
        self.mission_block_nodes = mission_blocks_nodes # Lista de listas de nodos
        self.mission_dists = mission_blocks_dist # Lista de listas de distancias
        self.mission_IBE = mission_IBE #Inter block events.
        self.in_mission = False; #Se pone en realidad cuando el vehículo acepta la misión
        self.currBlock=0;
        self.currStep=0;
        self.waiting_for_IBE=True;
        if self.mission_IBE[self.currBlock] == "None": #En el caso que no necesite evento para arrancar misión
            self.waiting_for_IBE = False;
    def is_waiting_for_houston_continue(self):
        return (self.waiting_for_IBE and self.mission_IBE[self.currBlock] == "Houston") or self.paused or (self.emergency and  not self.but_em_pressed) #En lo de emergencia estaría bueno meter que sea solo cuando liberaron el boton de emergencia
    def curr_block_len(self):
        return len(self.mission_block_nodes[self.currBlock]) #Longitud del bloque de ahora
    def n_of_blocks(self):
        return len(self.mission_block_nodes) #Número de bloques
    def abort_mission(self):
        self.paused = False;
        self.in_mission = False;
        self.waiting_for_IBE = False;
    def resume_mission(self): #En caso de estar en pausa, esta funcion resume la mision
        self.paused=False;
    def continue_mission(self): #Para comunicarle que sucedió un IBE en caso de que esperaba
        self.waiting_for_IBE=False;
        if self.n_of_blocks() == self.currBlock :
            self.in_mission = False;
            self.going_to_node = self.in_node
    def mission_step_reached(self): #Si llegó un step en la misión
        self.currStep += 1;  ##Avanza step de misiones
        self.in_node=self.mission_block_nodes[self.currBlock][self.currStep]
        self.distanceTravelled = 0;
        if self.currStep == self.curr_block_len()-1: #Si terminó el bloque de misión
            self.currStep=0
            self.currBlock += 1;
            if (self.n_of_blocks() == self.currBlock) and (self.mission_IBE[self.currBlock] == "None"): ##En caso de que termine la misión.
                self.in_mission=False;
                self.going_to_node=self.in_node
            elif self.mission_IBE[self.currBlock] == "None": #En caso de que no necesite evento para arrancar con el siguiente bloque
                self.waiting_for_IBE = False;
            else:
                self.waiting_for_IBE = True;


    def get_agv_pos_nodes(self): #Obtiene los datos necesarios para plotearlo en el mapa
        prev = self.in_node
        if self.in_mission == True:
            if self.currBlock == len(self.mission_block_nodes): #En el caso en el que ya hice todos los bloques de misiones pero me quedo esperando por un evento para terminar
                self.going_to_node =prev;
            elif self.currStep+1 < self.curr_block_len(): #En el caso de que queden steps en el bloque
                self.going_to_node  = self.mission_block_nodes[self.currBlock][self.currStep+1]
            elif self.curr_block_len() < self.n_of_blocks(): #Sino, es el primero del siguiente bloque
                self.going_to_node = self.mission_block_nodes[self.currBlock+1][0]
        next = self.going_to_node  # Por default se manda el mismo nodo cuando no hay un siguiente
        return prev, next, self.distanceTravelled