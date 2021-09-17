import ply.lex as lex
import ply.yacc as yacc
import webbrowser
import os
import ctypes
import speech_recognition as sr

tokens = (
    'OPERATE',
    'WHATOPEN',
    'NAME',
)

def t_OPERATE(t):
    r'TURNON | turnon | Turnon | START | Start |start | RUN | Run | run | EXIT | Exit | exit | TURNOFF | Turn off | turnoff | CLOSE | Close | close|OPEN|Open|open |Change|CHANGE|change'
    return t

def t_WHATOPEN(t):
    r'Internet|INTERNET|internet|NET|Net|net|PROGRAM|Program|program|FILE|file|File|WALLPAPER|Wallpaper|wallpaper'
    if t.value =='Internet' or t.value =='INTERNET' or t.value =='internet' or t.value =='NET' or t.value =='Net' or t.value =='net':
        t.value = 1
    elif t.value == 'program' or t.value == 'PROGRAM' or t.value =='Program':
        t.value = 2
    elif t.value == 'FILE' or t.value == 'file' or t.value == 'File':
        t.value = 3
    elif t.value == 'WALLPAPER' or t.value == 'Wallpaper' or t.value == 'wallpaper':
        t.value = 4
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

    if p[1] == 'TURNON' or p[1] =='turnon' or p[1] =='Turnon' or p[1] =='START' or p[1] =='Start' or p[1] =='start' or p[1] =='RUN' or p[1] =='Run' or p[1] =='run' or p[1] =='OPEN' or p[1] =='Open' or p[1] =='open' or p[1] =='CHANGE' or p[1]=='Change' or p[1]=='change':
        if p[2] == 1:
            website = p[3]
            print(f'{website} on !')
            webbrowser.open(f'https://www.{website}.com/')
        elif p[2] == 2:
             program = p[3]
             print(f'{program} on !')
             os.system(f'{program}.exe')
        elif p[2] == 3:
             file = p[3]
             print(f'{file} on !')
             f = open("tekst",'r')
             print(f.read())
        elif p[2] == 4:
             wallpaper = p[3]
             print(f'{wallpaper} changed !')
            # if this doesn't work u will need put there absolute path to this img - and it will be work !!!
             if wallpaper == 'sun':
                ctypes.windll.user32.SystemParametersInfoW(20, 0, 'sun1.jpg', 0)
             elif wallpaper == 'rain':
                 ctypes.windll.user32.SystemParametersInfoW(20, 0, 'rain1.jpg', 0)
             elif wallpaper == 'snow':
                 ctypes.windll.user32.SystemParametersInfoW(20, 0, 'snow1.jpg', 0)


    elif p[1] == 'EXIT' or p[1] =='Exit' or p[1] =='exit' or p[1] =='TURNOFF' or p[1] =='Turn off' or p[1] =='turnoff' or p[1] =='CLOSE' or p[1] =='Close' or p[1] =='close':
        if p[2] == 1:
             website = p[3]
             print(f'{website} off')
             os.system("taskkill /im chrome.exe /f")
        elif p[2] == 2:
            program = p[3]
            print(f'{program} off')
            os.system(f'taskkill /f /im {program}.exe')
        elif p[2] == 3:
            file = p[3]
            print(f'{file} off')


def p_error(p):
    print("Syntax error in input!")


lexer = lex.lex()

parser = yacc.yacc()

while True:
    q = input('How can I help you ?\n')
    if q == 'End for today':
        break
    elif q == 'How are you today':
        print('I am fine, I m here to help you :D')
    elif q =='voice mode on':

        sr1 = sr.Recognizer()
        sr2 = sr.Recognizer()

        with sr.Microphone() as source:
            print('Hi !')
            audio = sr1.listen(source)
            speak = ''

        if 'hi' in sr2.recognize_google(audio):
            while True:
                sr2 = sr.Recognizer()
                with sr.Microphone() as source:
                    print('If you want some help i\'m here for you, talk to me i\'m a bit bored')
                    audio = sr2.listen(source)

                    try:
                        speak = sr2.recognize_google(audio)
                        print(f'Sorry, do you said {speak}, no problem I will help you with that :) !')
                        if speak == 'bye' or speak == 'Bye':
                            break
                        parser.parse(speak)
                    except sr.UnknownValueError:
                        print('Error')


    parser.parse(q)







