class AGV_status:
    def __init__(self,number):
        self.n=number;
        self.mission_sent = False;
        self.in_mission = False;
        self.paused = False;
        self.in_node = 1;
        self.distanceTravelled = 0;
    def set_pos(self,pos):
        self.in_node=pos;
    def new_mission(self,mission_blocks_nodes,mission_blocks_dist, mission_IBE):
        self.mission_block_nodes = mission_blocks_nodes # Lista de listas de nodos
        self.mission_dists = mission_blocks_dist # Lista de listas de distancias
        self.mission_IBE = mission_IBE #Inter block events.
        self.in_mission = True;
        self.currBlock=0;
        self.currStep=0;
        self.paused=True;
        if self.mission_IBE[self.currBlock] == "None": #En el caso que no necesite evento para arrancar misión
            self.paused = False;
    def curr_block_len(self):
        return len(self.mission_block_nodes[self.currBlock])
    def n_of_blocks(self):
        return len(self.mission_block_nodes)
    def continue_mission(self):
        self.paused=False;
        if self.n_of_blocks() == self.currBlock :
            self.in_mission = False;
    def mission_step_reached(self):
        self.currStep += 1;  ##Avanza step de misiones
        self.in_node=self.mission_block_nodes[self.currBlock][self.currStep]
        if self.currStep == self.curr_block_len(): #Si terminó el bloque de misión
            self.currStep=0
            self.currBlock += 1;
            if (self.n_of_blocks() == self.currBlock) and (self.mission_IBE[self.currBlock] == "None"): ##En caso de que termine la misión.
                self.in_mission=False;
            elif self.mission_IBE[self.currBlock] == "None": #En caso de que no necesite evento para arrancar con el siguiente bloque
                self.paused = False;
            else:
                self.paused = True;


    def get_agv_pos_nodes(self):
        prev = self.in_node
        next = self.in_node
        if self.in_mission == True:
            if self.currStep+1 < self.curr_block_len(): #En el caso de que queden steps en el bloque
                next = self.mission_block_nodes[self.currBlock][self.currStep+1]
            elif self.curr_block_len() < self.n_of_blocks(): #Sino, es el primero del siguiente bloque
                next = self.mission_block_nodes[self.currBlock+1][0]

        return prev, next, self.distanceTravelled