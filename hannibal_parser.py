import ply.yacc as yacc
import ply.lex as lex
from hannibal_lexer import tokens
from hannibal_lexer import *
import sys
VERBOSE = 1
def p_program(p):
    'program : declaration_list'
    pass
def p_declaration_list(p):
    'declaration_list : declaration'
    pass
def p_declaration(p):
    '''declaration : var_declaration
                   | fun_declaration
                   | echo'''
    pass
def p_echo(p):
    '''echo : ECHO STRING
            | ECHO ID'''
    pass
def p_var_declaration(p):
    '''var_declaration : ID ASSIGN NUMBER SEMICOLON
                       | ID ASSIGN STRING SEMICOLON
                       | ID ASSIGN expression SEMICOLON'''
    pass
def p_fun_declaration(p):
    'fun_declaration : FUNCTION FUNCID LPAREN params RPAREN comp_statement'
    pass
def p_comp_statement(p): #modify
    'comp_statement : LBRACKET expression RBRACKET SEMICOLON'
    pass
def p_params_1(p):
    'params : params COMMA param'
    pass
def p_params_2(p):
    'params : param'
    pass
def p_param(p):
    '''param : ID
             | NUMBER
             | STRING
             | empty
            '''
    pass

def p_expression(p):
    'expression : additive_expression'
    pass
def p_additive_expression(p):
    '''additive_expression : additive_expression opsum term
                         | term'''
    pass
def p_opsum(p):
    '''opsum : PLUS
             | MINUS'''
    pass
def p_opmult(p):
    '''opmult : MULTIPLY
             | DIVIDE'''
    pass
def p_term(p):
    '''term : term opmult factor
          | factor '''
    pass
def p_factor(p):
    '''factor : LPAREN expression RPAREN
              | NUMBER
              | ID
    '''
    pass
def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(t.lexer.lineno))
	else:
		raise Exception('syntax', 'error')
def p_empty(p):
    'empty :'
lexer = lex.lex()
parser = yacc.yacc()
input = 1

if __name__ == '__main__':
    if not input:
        if (len(sys.argv) > 1):
            fin = sys.argv[1]
        else:
            fin = 'prueba.txt'
        f = open(fin, 'r')
        data = f.read()
        s = lex.input(data)
        print data
        parser.parse(data, debug = True, tracking=True)
    else:
        while True:
           try:
               s = raw_input('hannibal_parser > ')
           except EOFError:
               break
           if not s: continue
           result = parser.parse(s, debug = True, tracking=True)
           print(result)
