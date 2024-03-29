ORG 0
    ADD: NOP I CALL INDRCT
        READ U JMP NEXT
        ADD U JMP FETCH
    ORG 4
    BRANCH: NOP Z JMP OVER
            NOP U JMP FETCH
    OVER:   NOP I CALL INDRCT
            ARTPC U JMP FETCH
    ORG 8
    STORE: NOP I CALL INDRCT
           ACTDR U JMP NEXT 
           WRITE U JMP FETCH
    ORG 12
    EXCHANGE:   NOP              I CALL INDRCT
                READ             U JMP NEXT
                ACTDR, DRTAC     U JMP NEXT
                WRITE            U JMP FETCH
    ORG 20
    LOAD: NOP I CALL INDRCT
                READ  U JMP FETCH
    ORG 24
    SUB: NOP I CALL INDRCT
         READ U JMP NEXT
         SUB U JMP FETCH
    ORG 16
    HAL: HAL U JMP
    ORG 64 
    FETCH: PCTAR U JMP NEXT
           READ, INCPC U JMP NEXT
           DRTAR U MAP
    INDRCT: READ U JMP NEXT
            DRTAR U RET