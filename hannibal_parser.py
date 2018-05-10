import ply.yacc as yacc
from hannibal_lexer import tokens
import hannibal_lexer
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
    '''var_declaration : ID ASSIGN NUMBER
                       | ID ASSIGN STRING
                       | expression'''
    pass
def p_fun_declaration(p):
    'fun_declaration : FUNCTION LPAREN RPAREN'
    pass
def p_expression(p):
    'expression : additive_expression'
def p_additive_expression(p):
    '''additive_expression : additive_expression opsum term
                         | term'''
def p_opsum(p):
    '''opsum : PLUS
             | MINUS'''
def p_opmult(p):
    '''opmult : MULTIPLY
             | DIVIDE'''
def p_term(p):
    '''term : term opmult factor
          | factor '''
def p_factor(p):
    '''factor : LPAREN expression RPAREN
              | NUMBER
              | ID
    '''
def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(cminus_lexer.lexer.lineno))
	else:
		raise Exception('syntax', 'error')

parser = yacc.yacc()


if __name__ == '__main__':
    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'prueba.txt'
    f = open(fin, 'r')
    data = f.read()

    parser.parse(data)
