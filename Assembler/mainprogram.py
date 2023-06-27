import  microprogram as micro



table = dict()

def split_line(line):
    #split line into words
    line = line.split(' ')
    line = [word.strip() for word in line]
    ans = []
    for i in line:
        for j in i.split(','):
            if j != '':
                ans.append(j)
    return ans

def give_line_number(code):
    # calculate the line number of each line in the memory
    ans = []
    line_count = 0
    for i in range(len(code)):
        temp = code[i]
        if temp == []:
            line_count += 1
            continue
        if 'ORG' not in temp:
            code[i].append(line_count)
            ans.append(code[i])
            line_count += 1
        else:
            line_count = int(temp[1])
    
    return ans

def add_item_to_table(line):
    # add line number and their name to the table
    if ':' in line[0]:
        name = line[0][:-1]
        table[name] = line[-1]
        return line[1:]
    else:
        return line

def fill_table(code):
    # fill the table with the line number and their name
    code = code.split('\n')
    code = [line.strip() for line in code]
    code = [split_line(line) for line in code]
    code = give_line_number(code)
    code = list(map(add_item_to_table, code))
    return code


def dec_to_bin(num):
    # convert decimal number to binary number
    ans = bin(num)[2:]
    ans = '0'*(16-len(ans)) + ans
    return ans

def bin_to_bin(num):
    ans = '0'*(16-len(num)) + num
    return ans

def hex_to_bin(num):
    ans = bin(int(num, 16))[2:]
    ans = '0'*(16-len(ans)) + ans
    return ans

def transfer_number(cell):
    inp = str(cell)
    if inp[:3] == "BIN":
        return bin_to_bin(inp[3:])
    elif inp[:3] == "DEC":
        return dec_to_bin(int(inp[3:]))
    elif inp[:3] == "HEX":
        return hex_to_bin(inp[3:])
    else:
        return cell

def assembler(microcode, maincode):
    microbin, microtable = micro.assembler(microcode)
    maincode = fill_table(maincode)
    mainbin = []
    for i in maincode:
        ans = []
        for j in i:
                temp = transfer_number(j)
                if j in microtable:
                    temp = microtable[j][1:-2]
                elif j == 'I':
                    temp = '1'
                elif j in table:
                    temp = dec_to_bin(table[j])
                ans.append(temp)
        if len(ans) == 3:
            ans = '0' + ans[0] + ans[1][-11:] + '-'+str(ans[-1])
        elif len(ans) == 4:
            ans = '1' + ans[0] + ans[1][-11:] + '-'+str(ans[-1])
        else:
            ans = ans[0] + '-' + str(ans[-1])
        mainbin.append(ans)
    return microbin, mainbin



if __name__ == "__main__":
    micro_code = """ORG 0
    ADD: NOP I CALL INDRCT
        READ U JMP NEXT
        ADD U JMP FETCH
    ORG 4
    BRANCH: NOP S JMP OVER
            NOP U JMP FETCH
    OVER:   NOP I CALL INDRCT
            ARTPC U JMP FETCH
    ORG 8
    STORE: NOP I CALL INDRCT
           ACTOR U JMP NEXT 
           WRITE U JMP FETCH
    ORG 12
    EXCHANGE:   NOP              I CALL INDRCT
                READ             U JMP NEXT
                ACTDR, DRTAC     U JMP NEXT
                WRITE            U JMP FETCH
    ORG 64 
    FETCH: PCTAR U JMP NEXT
           READ, INCPC U JMP NEXT
           DRTAR U JMP MAP
    INDRCT: READ U JMP NEXT
            DRTAR U RET"""
    

    main_code = """ORG 0
        ADD BIN111 I
        ADD A2 
        ADD A3 I
        STORE DEC100
        STORE HEXFF
        STORE BIN1111
    ORG 1000
        DEC20
    A2: BIN111
    A3: HEXF
    """
    x, y = assembler(micro_code, main_code)
    for i in x:
        print(i)
    
    print("----------------------")

    for j in y:
        print(j)
