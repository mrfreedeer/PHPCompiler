import ply.yacc as yacc
from hannibal_lexer import tokens
import hannibal_lexer
import sys as

def p_error(p):
    print "Error Sintáctico"
def p_echo():
    'echo: ECHO STRING'
    pass
def p_var_declaration():
    '''var_declaration: ID ASSIGN NUMBER
                    |ID ASSIGN STRING'''

yacc.yacc()


if __name__ == '__main__':
        while True:
            try:
                s = input('expresion > ')
            except EOFError:
                break
            if not s:
                continue
            # Almacena la operacion en s

            yacc.parse(s)
