import ply.lex as lex
from time import sleep

# Define the tokens that our lexer will recognize
tokens = (
    'TYPE',
    'COMMENTARY',
    'FOR_LOOP',
    'IN',
    'IF',
    'ELSE',
    'FUNCTION',
    #'PROGRAM',
    'NUMBER',
    'COMMENTARYOPEN',
    'COMMENTARYCLOSE',
    'TEXT',
    'RANGE',
    'WHILE',
    'ID'
)

# erals are characters or strings that represent themselves as tokens
literals = (',',';','=','(',')','{','}','<','>','[',']',r'+',r'-','/',r'*')

states = (
    ('COMM','exclusive'), # para no caso dos comentarios
)


# there is another way of doing this
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_TYPE(t):
    r'int|float|char|string|boolean'
    return t

def t_FOR_LOOP(t):
    r'for'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_IN(t):
    r'in'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_ID(t):
    r'[_a-zA-Z]\w*'
    return t

def t_RANGE(t):
    r'\.\.' # [1..9]
    return t


def t_FUNCTION(t):
    r'function'
    return t

def t_COMMENTARYOPEN(t):
    r'/\*'
    t.lexer.begin('COMM')
    return t # ??

def t_COMM_COMMENTARYCLOSE(t):
    r'\*/'
    t.lexer.begin('INITIAL')
    return t

def t_COMMENTARY(t):
    r'//.*'
    pass

def t_COMM_TEXT(t):
    r'.|\n'
    pass


t_ANY_ignore = ' \t\n'


def t_ANY_error(t):
    print("Caracter invalido: ", t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()



data1 = """
/* factorial.p
-- 2023-03-20 
-- by jcr
*/
int i;
// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}
// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
"""

data2 = """
/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/
int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};
// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}
"""

data3="""
/* 
Isto aqui e` so para testar comentarios
*/
// sera que funciono ou nao
"""

data = [data1,data2,data3]

for d in data:
    lexer.input(d)
    for tok in lexer:
        #if(tok.value == 'STOP') : quit()
        print(tok)
    print("\n--------------------------------------------------\n")
    sleep(5)
