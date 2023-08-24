ORG 0        
    MULT:   EXCHANGE A2
            BRANCH CON 
            SUB A4
            EXCHANGE A2
            EXCHANGE A3
            ADD A1 
            EXCHANGE A3
            EXCHANGE A5
            BRANCH MULT 
CON:        HAL DEC0
ORG 1000
    A1: DEC6
    A2: DEC3
    A3: DEC0
    A4: DEC1
    A5: DEC0