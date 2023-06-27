f1_opt = ['000', '001', '010', '011', '100', '101', '110', '111']
f1_asm = ['NOP', 'ADD', 'CLRAC', 'INCAC', 'DRTAC', 'DRTAR','PCTAR', 'WRITE']

f2_opt = ['000', '001', '010', '011', '100', '101', '110', '111']
f2_asm = ['NOP', 'SUB', 'OR', 'AND', 'READ', 'ACTDR','INCDR', 'PCTDR']

f3_opt = ['000', '001', '010', '011', '100', '101', '110', '111']
f3_asm = ['NOP', 'XOR', 'COM', 'SHL', 'SHR', 'INCPC','ARTPC', 'RES']

CD_opt = ['00', '01', '10', '11']
CD_asm = ['U', 'I', 'S', 'Z']

BR_opt = ['00', '01', '10', '11']
BR_asm = ['JMP', 'CALL', 'RET', 'MAP']

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
    ans = '0'*(7-len(ans)) + ans
    return ans

def translate_line(line):
    # translate line to its binary code
    f1 = '000'
    f2 = '000'
    f3 = '000'
    CD = '00'
    BR = '00'
    AD = '0000000'
    for i in line:
        if i in f1_asm:
            f1 = f1_opt[f1_asm.index(i)]
        elif i in f2_asm:
            f2 = f2_opt[f2_asm.index(i)]
        elif i in f3_asm:
            f3 = f3_opt[f3_asm.index(i)]
        elif i in CD_asm:
            CD = CD_opt[CD_asm.index(i)]
        elif i in BR_asm:
            BR = BR_opt[BR_asm.index(i)]
        if i == 'NEXT':
            AD = dec_to_bin(int(line[-1])+1)
        if i in table:
            AD = dec_to_bin(int(table[i]))

    return ''.join([f1, f2, f3, CD, BR, AD, '-'+str(line[-1])])




def assembler(code):
    # translate the code to binary code and return the binary code and items of table that can be used outside of the microprogram assembly 
    code = fill_table(code)
    code = list(map(translate_line, code))
    ans = dict()
    for i in table.items():
        if i[1]%4 == 0 and i[1] < 64:
            ans[i[0]]  = dec_to_bin(i[1])
    return code, ans


if __name__ == '__main__':

    sample_code = """ORG 64 
    FETCH: PCTAR U JMP NEXT
    TEST:  READ, INCPC U JMP NEXT
        DRTAR U JMP MAP"""
    
    x, y = assembler(sample_code)

    for i in x:
        print(i)
    print(y)
