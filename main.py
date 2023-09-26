import re

def GetNextChar(input,index):
    index += 1
    if index >= len(input):
        return ''
    else:
        return input[index]
    
def GetTag(input,index):
    inputLen = len(input)
    buffer = ''
    if index >= inputLen:
        return ''
    if input[index] == '<':
        while True:
            if index >= inputLen:
                return buffer
            buffer += input[index]
            index += 1
            if input[index] == '>':
                buffer += input[index]
                return buffer
    else:
        return '' 

###### DEVE SER RESOLVIDO UM BUG AQUI NESSA DEF QUE ESTÁ REPETINDO O "CONTEUDO"####
def GetContent(input,index):
    inputLen = len(input)
    buffer = ''
    if index >= inputLen:
        return ''
    while True:
        if index >= inputLen:
            return buffer
        char = input[index]
        if char == '<':
            return buffer 
        buffer += char
        index += 1

singleTags = [
    '<br>'
]   
def IsSingleTag(tag):
    for singletag in singleTags:
        if tag == singletag:
            return True 
    return False

def GetAttributes(tag):
    attributes = re.findall(r'(\S+)\s*=\s*"([^"]*)"', tag)
    if attributes:
        return attributes
    else:
        return []

def GetAttributeNames(attributes):
    return [attribute[0] for attribute in attributes]

def GetAttributeNames(attributes):
    return [attribute[1] for attribute in attributes]


input = '<html><head> <title> Compiladores </title> </head><body> <p style="color:red;background:blue;" id="abc"> Unipinhal </p> <br> </body></html>'

tagStack = []
done = False
index = -1

while True:
    #Move index
    index += 1
    
    #Verify if string ended
    if index >= len(input):
        break

    #Take a caracter
    char = input[index]
    
    #If could be either opening or ending
    if char == '<':
        #If is ending caracter
        if GetNextChar(input,index) == '/':
            tag = GetTag(input,index)
            index += len(tag) -1
            if len(tagStack) > 0:
                print(f"Tag de fechamento: {tag}, Nível {len(tagStack)}")
            else:
                print(f"Tag de fechamento: {tag}, Nível 0")
            if len(tagStack) > 0 and tagStack[-1] == tag:
                tagStack.pop()
        else: 
            tag = GetTag(input,index)
            index += len(tag) - 1 
            print(f"Tag de abertura: {tag}, Nível {len(tagStack)}")
            if not IsSingleTag(tag):
                tagStack.append(tag)
            attributes = GetAttributes(tag)
            attribute_names = GetAttributeNames(attributes)
            attribute_values = GetAttributeValues(attributes)
            for i in range(len(attribute_names)):
                print(f"Atributo: {attribute_names[i]} Valor: {attribute_values[i]}")
    elif char != ' ':
        content = GetContent(input, index)
        if content.strip() != '':
            print(f"Conteúdo: {content.strip()}, Nível {len(tagStack)}")