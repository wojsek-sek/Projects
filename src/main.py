import ply.lex as lex
import ply.yacc as yacc
import webbrowser
import os


tokens = (
    'OPERATE',
    'WHATOPEN',
    'NAME',
)

def t_OPERATE(t):
    r'TURNON | turnon | Turnon | START | Start |start | RUN | Run | run | EXIT | Exit | exit | TURNOFF | Turn off | turnoff | CLOSE | Close | close '
    return t

def t_WHATOPEN(t):
    r'Internet|INTERNET|internet|NET|Net|net|PROGRAM|Program|program'
    if t.value =='Internet' or 'INTERNET' or 'internet' or 'NET' or 'Net' or 'net':
        t.value = 1
    elif t.value == 'program' or 'PROGRAM' or 'Program':
        t.value = 2
    return t

def t_NAME(t):
    r'\w+'
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


t_ignore = ' \t'

def p_command(p):
    'command : OPERATE WHATOPEN NAME'

    if p[1] == 'TURNON' or 'turnon' or 'Turnon' or 'START' or 'Start' or 'start' or 'RUN' or 'Run' or 'run':
        if p[2] == 1:
            website = p[3]
            print(f'{website} on !')
            webbrowser.open(f'https://www.{website}.com/')
        elif p[2] == 2:
             file = p[3]
             print(f'{file} on !')
             os.system(f'{file}.exe')
    elif p[1] == 'EXIT' or 'Exit' or 'exit' or 'TURNOFF' or 'Turn off' or 'turnoff' or 'CLOSE' or 'Close' or 'close':
        if p[2] == 1:
             website = p[3]
             print(f'{website} off')
             os.system("taskkill /im chrome.exe /f")
        elif p[2] == 2:
            file = p[3]
            print(f'{file} off')
            os.system(f'taskkill /f /im {file}.exe')


def p_error(p):
    print("Syntax error in input!")


lexer = lex.lex()

parser = yacc.yacc()

while True:
    q = input('How can I help you ?\n')
    if q == 'End for today':
        break
    parser.parse(q)







