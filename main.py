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

def GetAtributes(tag):
    atribs = re.findall(r'\s+[a-zA-Z0-9_]+="\s*[a-zA-Z0-9_;:]*"', tag)
    if len(atribs) > 0 :
        for atrib in atribs:
            atrib.strip()
        return atribs
    return []

def GetAtributeName(atrib):
    name = re.search(r'[a-zA-Z0-9_]+=|$',atrib).group()
    if name != None:
        return name[0:len(name)-1]
    return ''

def GetAtributeValue(atrib):
    value = re.search(r'="[a-zA-Z0-9_:;]+"|$',atrib).group()
    if value != None:
        return value[1:] 
    return ''

input = '<html><head> <title> Compiladores </title> </head><body> <p style="color:red;background:blue;" id="abc"> Unipinhal </p> <br> </body></html>'

tagStack = []
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
            tagStack.pop()
            print(f"Tag de fechamento: {tag}, Nível {len(tagStack)}")
        #If is opening caracter
        else: 
            tag = GetTag(input,index)
            index += len(tag) - 1 
            print(f"Tag de abertura: {tag}, Nível {len(tagStack)}")
            if IsSingleTag(tag):
                continue
            #If not single tag just do what is needed    
            tagStack.append(tag)
            atributes = GetAtributes(tag)
            if len(atributes) > 0:
                for atrib in atributes:
                    name = GetAtributeName(atrib)
                    value = GetAtributeValue(atrib)
                    print(f"Atributo: {name} Valor: {value}") 
    #If is just a caracter
    elif char != ' ':
        content = GetContent(input,index)
        index += len(content) -1 
        print(f"Conteúdo da tag: {content}")
