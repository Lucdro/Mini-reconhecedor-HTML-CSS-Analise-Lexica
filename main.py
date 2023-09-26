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
    return 

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
            tagStack.pop()
            print(f"Tag de fechamento: {tag}, Nível {len(tagStack)}")
        #If is opening caracter
        else: 
            tag = GetTag(input,index)
            index += len(tag) - 1 
            print(f"Tag de abertura: {tag}, Nível {len(tagStack)}")
            if not IsSingleTag(tag):
                tagStack.append(tag)
            while True:
                atributes = GetAtributes(tag)
                if len(atributes > 0):
                    for atrib in atributes:
                        atribName = GetAtributeName(atrib)
                        value = GetAtributeValue(atrib)
                        print(f"Atributo: {atribName} Valor: {value}") 
                        break
                    else:
                        break
    #If is just a caracter
    elif char != ' ':
        content = GetContent(input,index)
        index += len(content) -1 
        print(f"Conteúdo da tag: {content}")
