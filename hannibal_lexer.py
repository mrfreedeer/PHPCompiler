import sys
import ply.lex as lex

inputtype = 0
#Lista de tokens
'''
 #PALABRAS   RESERVADAS
            'IF', 'ENDIF','ELSE', 'ELSEIF', 'WHILE',
            'VAR', 'CONST', 'FUNCTION', 'ECHO', 'EXTENDS', 'PRINT', 'RETURN',
            'FOR', 'FOREACH', 'ENDFOREACH', 'ENDFOR', 'REQUIRE', 'EHTML',
'''
tokens = [
            #OPERADORES
            'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'ASSIGN', 'SEMICOLON',
            'LPAREN','RPAREN', 'LBRACKET', 'RBRACKET', 'COMMA', 'MODULE', 'LT',
            'LE', 'EQUAL', 'GE', 'GT', 'NEQUAL', 'AND', 'OR', 'NOT', 'ANDBT',
            'ORBT','POSITIVEINCREASE', 'INCREASE','DECREASE', 'IDENTICAL',
            'NEGATIVEINCREASE', 'MULTIPLIINCREASE', 'DIVIDEINCREASE',
            #TOKENS COMPUESTOS
            'ID', 'FUNCID',
            #TIPOS DE DATOS
            'STRING', 'NUMBER'
            ]
t_ignore = '\t\r | \n| \ '

reserved = {
   'if' : 'IF',
   'endif' : 'ENDIF',
   'else' : 'ELSE',
   'elseif' : 'ELSEIF',
   'while' : 'WHILE',
   'var' : 'VAR',
   'const' : 'CONST',
   'function' : 'FUNCTION',
   'echo'   : 'ECHO',
   'extends' : 'EXTENDS',
   'print' : 'PRINT',
   'return' : 'RETURN',
   'for' : 'FOR',
   'foreach' : 'FOREACH',
   'endfor' : 'ENDFOR',
   'endforeach' : 'ENDFOREACH',
   'require' : 'REQUIRE'
   }


tokens += list(reserved.values())
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_MULTIPLY     = r'\*'
t_DIVIDE    = r'/'
t_ASSIGN    = r'='
t_SEMICOLON = r';'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_COMMA     = r','
t_LT        = r'<'
t_LE        = r'<='
t_GT        = r'>'
t_GE        = r'>='
t_AND      = r'\&\&'
t_OR       = r'\|\|'
t_EQUAL     = r'=='
t_IDENTICAL = r'==='
t_NEQUAL    = r'!='

# ----------------------------------------------------------------------
#                                 NUEVOS
# ----------------------------------------------------------------------
t_MODULE           = r'%'
t_ANDBT            = r'\&'
t_ORBT             = r'\|'
t_POSITIVEINCREASE = r'\+='
t_NEGATIVEINCREASE = r'-='
t_MULTIPLIINCREASE = r'\*='
t_DIVIDEINCREASE   = r'/='
t_INCREASE         = r'\+\+'
t_DECREASE         = r'\-\-'


# ----------------------------------------------------------------------
#                              COMPUESTOS
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                              TIPOS DE DATOS
# ----------------------------------------------------------------------
t_STRING           = r'(\"(.)*\"|\'(.)*\')'

def t_NUMBER(t):
    r'-?[0-9]+(\.[0-9]+)?((E|e)-?[0-9]*(\.[0-9])?)?'
    return t

def t_ID(t):
    r'\$((\_?[a-z A-Z]| \_[0-9])+)(_\d\w)*'
    s = str(t.value.lower())
    if s[-1:] == ' ':
        s = s[:-1]
    t.type = reserved.get(s,'ID')
    return t
    
def t_FUNCID(t):
    r'\w+(_\d\w)*'
    s = str(t.value.lower())
    if s[-1:] == ' ':
        s = s[:-1]
    t.type = reserved.get(s,'FUNCID')
    return t


#Definicion de error que se va a mostrar cuando un caracter ingresado no es valido
def t_error(t):
	print("******Caracter no valido: {}".format(t.value[0]))
	t.lexer.skip(1)
	return t
def t_comments(t):
    r'/\*(.|\n)*?\*/|(//.*|\#.*)'
    t.lexer.lineno += t.value.count('\n')


'''
RECURSIVE COMMENT
    r'/\*(.|\n)*?(/\*(.|\n)*?\*/)(.|\n)*\*/|(//.*|\#.*)'
NORMAL COMMENT
    r'/\*(.|\n)*?\*/|(//.*|\#.*)'

'''

lex.lex()

if __name__ == '__main__':
    if inputtype:
        if (len(sys.argv) > 1):
            fin = sys.argv[1]
        else:
            fin = 'prueba.txt'

        f = open(fin, 'r')
        data = f.read()
    	#print (data)
    	# Almacena la operacion en s

        lex.input(data)


        # Muestra todos los tokens en la operacion
        while True:
        	tok = lex.token()
        	if not tok:
        		break
        	print(tok)
    else:

#Funcion para recibir la operacion a calcular y
#definir donde hay errores lexicos segun los caracteres ingresados
        while True:
        	try:
        		s = raw_input('operacion > ')
        	except EOFError:
        		break
        	if not s:
        		continue

        # Almacena la operacion en s
        	lex.input(s)


        # Muestra todos los tokens en la operacion
        	while True:
        		tok = lex.token()
        		if not tok:
        			break
        		print(tok)
