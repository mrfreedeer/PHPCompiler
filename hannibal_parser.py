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
    '''declaration : declaration var_declaration
                   | declaration fun_declaration
                   | declaration echo
                   | declaration conditional
                   | declaration iterative
                   | declaration incremental_expression
                   | empty'''
    pass
def p_declaration2(p):
    '''declaration2 : declaration2 var_declaration
                    | declaration2 echo
                    | declaration2 conditional
                    | declaration2 iterative
                    | declaration2 incremental_expression
                    | empty'''
    pass
def p_echo(p):
    '''echo : ECHO STRING SEMICOLON
            | ECHO ID SEMICOLON'''
    pass
def p_var_declaration(p):
    '''var_declaration : ID ASSIGN NUMBER SEMICOLON
                       | ID ASSIGN STRING SEMICOLON
                       | ID ASSIGN expression SEMICOLON'''
    pass
def p_var_declaration2(p):
    '''var_declaration2 : ID ASSIGN NUMBER
                        | ID ASSIGN expression'''
    pass
def p_fun_declaration(p):
    'fun_declaration : FUNCTION FUNCID LPAREN params RPAREN LBRACKET declaration2 RBRACKET'
    pass
def p_fun_declaration_2(p):
    'fun_declaration : FUNCTION FUNCID LPAREN params RPAREN LBRACKET declaration2 return_statement RBRACKET'
    pass
def p_return_statement(p):
    '''return_statement : RETURN expression SEMICOLON
                      | RETURN expression2 SEMICOLON
                      | RETURN incremental_expression'''
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
def p_conditional(p):
    '''conditional : IF LPAREN expression2 RPAREN LBRACKET declaration2 RBRACKET SEMICOLON
                   | IF LPAREN expression2 RPAREN LBRACKET declaration2 RBRACKET ENDIF SEMICOLON
                   |  IF LPAREN expression2 RPAREN LBRACKET declaration2 RBRACKET ELSE LBRACKET declaration2 RBRACKET '''
def p_iterative(p):
    '''iterative : WHILE LPAREN expression2 RPAREN LBRACKET declaration2 RBRACKET
                 | FOR LPAREN var_declaration2 SEMICOLON simple_expression SEMICOLON iterative_expression RPAREN LBRACKET declaration2 RBRACKET'''
    pass
def p_iterative_expression(p):
    '''iterative_expression : ID INCREASE
                            | ID DECREASE
                            | ID POSITIVEINCREASE additive_expression
                            | ID NEGATIVEINCREASE additive_expression
                            | ID MULTIPLIINCREASE additive_expression
                            | ID DIVIDEINCREASE additive_expression'''
    pass
def p_incremental_expression(p):
    '''incremental_expression : iterative_expression SEMICOLON'''
    pass
def p_expression(p):
    '''expression : additive_expression
                | simple_expression'''
    pass
def p_expression2(p):
    '''expression2 : simple_expression
                 | ID '''
    pass

def p_simple_expression(p):
    'simple_expression : additive_expression compop additive_expression'
def p_compop(p):
    '''compop : LT
              | LE
              | GT
              | GE
              | EQUAL
              | NEQUAL
              | IDENTICAL'''
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
input = 0

if __name__ == '__main__':
    if not input:
        if (len(sys.argv) > 1):
            fin = sys.argv[1]
        else:
            fin = 'prueba2.txt'
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
