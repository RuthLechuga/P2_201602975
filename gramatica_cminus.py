reservadas = {
    'int': 'INT',
    'char': 'CHAR',
    'double': 'DOUBLE',
    'float': 'FLOAT',
    'printf': 'PRINTF',
    'struct': 'STRUCT',
    'if': 'IF',
    'else': 'ELSE',
    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',
    'while': 'WHILE',
    'do': 'DO',
    'for': 'FOR',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
    'void': 'VOID',
    'sizeof': 'SIZEOF',
    'scanf': 'SCANF',
    'goto': 'GOTO'
}

tokens  = [
    'PTCOMA',
    'DPUNTOS',
    'COMA',
    'PIZQ',
    'PDER',
    'CIZQ',
    'CDER',
    'LLIZQ',
    'LLDER',
    'PUNTO',
    'ASIG',
    'INCREMENTO',
    'DECREMENTO',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'MODULO',
    'BBIZQ',
    'BBDER',
    'MENOR_IGUAL_QUE',
    'MAYOR_IGUAL_QUE',
    'MENOR_QUE',
    'MAYOR_QUE',
    'IGUAL_QUE',
    'MAS_ASIG',
    'MENOS_ASIG',
    'POR_ASIG',
    'DIV_ASIG',
    'MOD_ASIG',
    'IZQ_ASIG',
    'DER_ASIG',
    'AND_ASIG',
    'OR_ASIG',
    'XOR_ASIG',
    'NOT',
    'AND',
    'OR',
    'BBNOT',
    'BBAND',
    'BBOR',
    'BBXOR',
    'DESIGUAL_QUE',
    'TERNARIO',
    'DECIMAL',
    'ENTERO',
    'IDENTIFICADOR',
    'CADENA',
    'CARACTER'
] + list(reservadas.values())

# Tokens
t_PTCOMA            = r';'
t_DPUNTOS           = r':'
t_COMA              = r','
t_PIZQ              = r'\('
t_PDER              = r'\)'
t_CIZQ              = r'\['
t_CDER              = r']'
t_LLIZQ             = r'\{'
t_LLDER             = r'\}'
t_PUNTO             = r'.'
t_ASIG              = r'\='
t_INCREMENTO        = r'\+\+'
t_DECREMENTO        = r'\-\-'
t_MAS               = r'\+'
t_MENOS             = r'\-'
t_POR               = r'\*'
t_DIVIDIDO          = r'\/'
t_MODULO            = r'\%'
t_BBIZQ             = r'<<'
t_BBDER             = r'>>'
t_MENOR_IGUAL_QUE   = r'\<\='
t_MAYOR_IGUAL_QUE   = r'\>\='
t_MENOR_QUE         = r'\<'
t_MAYOR_QUE         = r'\>'
t_IGUAL_QUE         = r'\=\='
t_MAS_ASIG          = r'\+\='
t_MENOS_ASIG        = r'-\='
t_POR_ASIG          = r'\*\='
t_DIV_ASIG          = r'/\='
t_MOD_ASIG          = r'%\='
t_IZQ_ASIG          = r'\<\<\='
t_DER_ASIG          = r'\>\>\='
t_AND_ASIG          = r'\&\='
t_OR_ASIG           = r'\|\='
t_XOR_ASIG          = r'\^\='
t_NOT               = r'\!'
t_AND               = r'\&\&'
t_OR                = r'\|\|'
t_BBNOT             = r'~'
t_BBAND             = r'\&'
t_BBOR              = r'\|'
t_BBXOR             = r'\^'
t_DESIGUAL_QUE      = r'!\='
t_TERNARIO          = r'\?'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        global mensajes
        mensajes.append(Mensaje(TIPO_MENSAJE.LEXICO,'Valor decimal muy largo para almacenar en: '+t.value+'.',t.lexer.lineno,0))
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        global mensajes
        mensajes.append(Mensaje(TIPO_MENSAJE.LEXICO,'Valor entero muy largo para almacenar en: '+t.value+'.',t.lexer.lineno,0))
        t.value = 0
    return t

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(),'IDENTIFICADOR')
    return t

def t_CADENA(t):
    r'(\".*?\")'
    t.value = t.value[1:-1]
    return t 

def t_CARACTER(t):
    r'(\'.?\')'
    t.value = t.value[1:-1]
    return t 

def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_COMENTARIO_SIMPLE(t):
    r'//.*\n'
    t.lexer.lineno += 1

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
   
def t_error(t):
    global mensajes
    mensajes.append(Mensaje(TIPO_MENSAJE.LEXICO,'Caracter no válido: '+t.value[0]+'.',t.lexer.lineno,0))
    t.lexer.skip(1)

import ply.lex as lex
from Arbol.Mensaje import *
from Arbol.Asignacion import *
from Arbol.Break import *
from Arbol.Case import *
from Arbol.Continue import *
from Arbol.Declaracion import *
from Arbol.DoWhile import *
from Arbol.Elseif import *
from Arbol.EtiquetasAgust import *
from Arbol.Expresion import *
from Arbol.For import *
from Arbol.Funcion import *
from Arbol.If import *
from Arbol.Printf import *
from Arbol.Scanf import *
from Arbol.Simbolo import *
from Arbol.Switch import *
from Arbol.While import *

lexer = lex.lex()

#---------------------------------------------PRECEDENCIA-----------------------------------------------#
precedence = (
    ('left','BBIZQ','BBDER'),
    ('left','OR','BBOR'),
    ('left','AND','BBAND'),
    ('left','BBXOR'),
    ('left','IGUAL_QUE','DESIGUAL_QUE'),
    ('left','MENOR_IGUAL_QUE','MAYOR_IGUAL_QUE','MENOR_QUE','MAYOR_QUE'),
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO','MODULO'),
    ('right','NOT','BBNOT')
)

#-------------------------------------------INICIO GRAMATICA---------------------------------------------#
def p_init(t) :
    'init            :  instrucciones_globales'
    reporte_gramatical.append(['init -> instrucciones_globales','t[0] = t[1]'])
    t[0] = t[1]

def p_instrucciones_globales_instrucciones(t):
    'instrucciones_globales : instrucciones_globales instruccion_global'
    reporte_gramatical.append(['instrucciones_globales -> instrucciones_globales instruccion_global','t[1].extend(t[2])\nt[0] = t[1]'])
    t[1].extend(t[2])
    t[0] = t[1]

def p_instrucciones_global_instruccion(t):
    'instrucciones_globales : instruccion_global'
    reporte_gramatical.append(['instrucciones_globales -> instruccion_global','t[0] = t[1]'])
    t[0] = t[1]

#---------------------------------------GRAMATICA DECLARACION---------------------------------------------#
def p_instruccion_global_decl(t):
    'instruccion_global : declaracion PTCOMA'
    reporte_gramatical.append(['instruccion_global -> declaracion PTCOMA','t[0] = t[1]'])
    t[0] = t[1]

def p_declaracion(t):
    'declaracion : tipo lista_asignaciones_dec'
    reporte_gramatical.append(['declaracion -> tipo lista_asignaciones_dec PTCOMA','t[0] = t[2]'])
    global temporal_tipo
    temporal_tipo = ''
    t[0] = t[2]

def p_lista_asignaciones_dec(t):
    'lista_asignaciones_dec : lista_asignaciones_dec COMA asignacion_dec'
    reporte_gramatical.append(['lista_asignaciones_dec -> lista_asignaciones_dec COMA asignacion_dec','t[1].append(t[3])\nt[0] = t[1]'])
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_asignacion_dec(t):
    'lista_asignaciones_dec : asignacion_dec'
    reporte_gramatical.append(['lista_asignaciones_dec -> asignacion_dec','t[0] = [t[1]]'])
    t[0] = [t[1]]

def p_asignacion_dec_id(t):
    'asignacion_dec : IDENTIFICADOR'
    reporte_gramatical.append(['asignacion_dec -> IDENTIFICADOR','t[0] = Declaracion(TIPO_DATO.ENTERO,t[1],None,None,t.lineno(1),find_column(entrada, t.slice[1]))'])
    global temporal_tipo
    temporal_tipo = t[-1] if temporal_tipo == '' else temporal_tipo
    if temporal_tipo=='int' : t[0] = Declaracion(TIPO_DATO.ENTERO,t[1],None,None,t.lineno(1),find_column(entrada, t.slice[1]))
    elif temporal_tipo=='char' : t[0] = Declaracion(TIPO_DATO.CARACTER,t[1],None,None,t.lineno(1),find_column(entrada, t.slice[1]))
    elif temporal_tipo=='double' : t[0] = Declaracion(TIPO_DATO.DECIMAL,t[1],None,None,t.lineno(1),find_column(entrada, t.slice[1]))
    elif temporal_tipo=='float' : t[0] = Declaracion(TIPO_DATO.DECIMAL,t[1],None,None,t.lineno(1),find_column(entrada, t.slice[1]))

def p_asignacion_dec_expresion(t):
    'asignacion_dec : IDENTIFICADOR ASIG expresion'
    reporte_gramatical.append(['asignacion_dec -> IDENTIFICADOR sig_asig expresion','t[0] = Declaracion(TIPO_DATO.ENTERO,t[1],None,t[3],t.lineno(1),find_column(entrada, t.slice[1]))'])
    global temporal_tipo
    temporal_tipo = t[-1] if temporal_tipo == '' else temporal_tipo
    if temporal_tipo=='int' : t[0] = Declaracion(TIPO_DATO.ENTERO,t[1],None,t[3],t.lineno(1),find_column(entrada, t.slice[1]))
    elif temporal_tipo=='char' : t[0] = Declaracion(TIPO_DATO.CARACTER,t[1],None,t[3],t.lineno(1),find_column(entrada, t.slice[1]))
    elif temporal_tipo=='double' : t[0] = Declaracion(TIPO_DATO.DECIMAL,t[1],None,t[3],t.lineno(1),find_column(entrada, t.slice[1]))
    elif temporal_tipo=='float' : t[0] = Declaracion(TIPO_DATO.DECIMAL,t[1],None,t[3],t.lineno(1),find_column(entrada, t.slice[1]))

def p_asignacion_dec_accesos(t):
    'asignacion_dec : IDENTIFICADOR accesos'
    reporte_gramatical.append(['asignacion_dec -> IDENTIFICADOR accesos',''])

def p_asignacion_dec_accesos_expresion(t):
    'asignacion_dec : IDENTIFICADOR accesos ASIG expresion'
    reporte_gramatical.append(['asignacion_dec -> IDENTIFICADOR sig_asig expresion',''])

def p_signos_asignacion(t):
    '''sig_asig : ASIG
                | AND_ASIG
                | DER_ASIG
                | DIV_ASIG
                | IZQ_ASIG
                | MAS_ASIG
                | MENOS_ASIG
                | MOD_ASIG
                | OR_ASIG
                | POR_ASIG
                | XOR_ASIG
    '''
    reporte_gramatical.append(['sig_asig -> '+t[1],'t[0] = t[1]'])
    t[0] = t[1]

def p_tipo(t):
    ''' tipo : INT
            | CHAR
            | DOUBLE
            | FLOAT
    '''
    reporte_gramatical.append(['tipo -> '+t[1],'t[0] = t[1]'])
    t[0] = t[1]

def p_accesos(t):
    ' accesos : accesos acceso'
    reporte_gramatical.append([' accesos -> accesos acceso', ''])

def p_accesos_acceso(t):
    ' accesos : acceso '
    reporte_gramatical.append([' accesos -> acceso', ''])

def p_acceso(t):
    ' acceso : CIZQ expresion CDER'
    reporte_gramatical.append([' acceso -> CIZQ expresion CDER',''])

def p_acceso_vacio(t):
    ' acceso : CIZQ CDER'
    reporte_gramatical.append([' acceso -> CIZQ CDER',''])

#-------------------------------GRAMATICA DECLARACION STRUCTS---------------------------------------------#
def p_instruccion_global_struct(t):
    'instruccion_global : def_struct PTCOMA'
    reporte_gramatical.append(['instruccion_global -> decl_struct PTCOMA',''])

def p_definicion_struct(t):
    'def_struct : STRUCT IDENTIFICADOR LLIZQ struct_lista_decl LLDER '
    reporte_gramatical.append(['decl_struct -> STRUCT IDENTIFICADOR LLIZQ struct_lista_decl LLDER ',''])

def p_struct_lista(t):
    'struct_lista_decl : struct_lista_decl struct_decl'
    reporte_gramatical.append(['struct_lista_decl -> struct_lista_decl struct_decl',''])

def p_struct_lista_decl(t):
    'struct_lista_decl : struct_decl'
    reporte_gramatical.append(['struct_lista_decl -> struct_decl',''])

def p_struct_decl(t):
    'struct_decl : tipo lista_id_struct PTCOMA'
    reporte_gramatical.append(['struct_decl -> tipo lista_id_struct PTCOMA',''])

def p_lista_ids_struct(t):
    'lista_id_struct : lista_id_struct COMA id_struct'
    reporte_gramatical.append(['lista_id_struct -> lista_id_struct COMA id_struct',''])

def p_lista_id(t):
    'lista_id_struct : id_struct'
    reporte_gramatical.append(['lista_id_struct -> id_struct',''])

def p_id_struct(t):
    'id_struct : IDENTIFICADOR'
    reporte_gramatical.append(['id_struct -> IDENTIFICADOR',''])

def p_id_struct_acceso(t):
    'id_struct : IDENTIFICADOR accesos'
    reporte_gramatical.append(['id_struct -> IDENTIFICADOR accesos',''])

#--------------------------------------GRAMATICA DECL. STRUCT---------------------------------------------#
def p_instruccion_global_declaracion_struct(t):
    'instruccion_global : declaracion_struct PTCOMA'
    reporte_gramatical.append(['instruccion_global -> declaracion_struct PTCOMA',''])

def p_declaracion_struct(t):
    'declaracion_struct : STRUCT IDENTIFICADOR IDENTIFICADOR'
    reporte_gramatical.append(['declaracion_struct -> STRUCT IDENTIFICADOR IDENTIFICADOR',''])

def p_declaracion_struct_accesos(t):
    'declaracion_struct : STRUCT IDENTIFICADOR IDENTIFICADOR accesos'
    reporte_gramatical.append(['declaracion_struct -> STRUCT IDENTIFICADOR IDENTIFICADOR accesos',''])

#---------------------------------------GRAMATICA DE METODOS---------------------------------------------#
def p_instruccion_global_metodo(t):
    'instruccion_global : metodo '
    reporte_gramatical.append(['instruccion_global -> metodo','t[0] = [t[1]]'])
    t[0] = [t[1]]

def p_metodo_void_param(t):
    'metodo : VOID IDENTIFICADOR PIZQ lista_parametros PDER LLIZQ instrucciones LLDER'
    reporte_gramatical.append(['metodo -> VOID IDENTIFICADOR PIZQ lista_parametros PDER LLIZQ instrucciones LLDER','t[0] = Funcion(TIPO_FUNCION.VOID,t[2],t[4],t[7],t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = Funcion(TIPO_FUNCION.VOID,t[2],t[4],t[7],t.lineno(1),find_column(entrada, t.slice[1]))

def p_metodo_void(t):
    'metodo : VOID IDENTIFICADOR PIZQ PDER LLIZQ instrucciones LLDER'
    reporte_gramatical.append(['metodo -> VOID IDENTIFICADOR PIZQ PDER LLIZQ instrucciones LLDER','t[0] = Funcion(TIPO_FUNCION.VOID,t[2],None,t[6],t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = Funcion(TIPO_FUNCION.VOID,t[2],None,t[6],t.lineno(1),find_column(entrada, t.slice[1]))

def p_metodo_tipo_param(t):
    'metodo : tipo IDENTIFICADOR PIZQ lista_parametros PDER LLIZQ instrucciones LLDER'
    reporte_gramatical.append(['metodo -> tipo IDENTIFICADOR PIZQ lista_parametros PDER LLIZQ instrucciones LLDER','t[0] = Funcion(tipo,t[2],t[4],t[7],t.lineno(2),find_column(entrada, t.slice[2]))'])
    tipo = ''
    if t[1]=='int': tipo = TIPO_FUNCION.ENTERO
    elif t[1]=='double' or t[1]=='float': tipo = TIPO_FUNCION.DECIMAL
    elif t[1]=='char': tipo = TIPO_FUNCION.CARACTER
    t[0] = Funcion(tipo,t[2],t[4],t[7],t.lineno(2),find_column(entrada, t.slice[2]))

def p_metodo_tipo(t):
    'metodo : tipo IDENTIFICADOR PIZQ PDER LLIZQ instrucciones LLDER'
    reporte_gramatical.append(['metodo -> tipo IDENTIFICADOR PIZQ PDER LLIZQ instrucciones LLDER','t[0] = Funcion(tipo,t[2],None,t[6],t.lineno(2),find_column(entrada, t.slice[2]))'])
    tipo = ''
    if t[1]=='int': tipo = TIPO_FUNCION.ENTERO
    elif t[1]=='double' or t[1]=='float': tipo = TIPO_FUNCION.DECIMAL
    elif t[1]=='char': tipo = TIPO_FUNCION.CARACTER
    t[0] = Funcion(tipo,t[2],None,t[6],t.lineno(2),find_column(entrada, t.slice[2]))

def p_lista_parametros(t):
    'lista_parametros : lista_parametros COMA parametro'
    reporte_gramatical.append(['lista_parametros -> lista_parametros COMA parametro','t[1].append(t[3])\nt[0] = t[1]'])
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_parametros_parametro(t):
    'lista_parametros : parametro'
    reporte_gramatical.append(['lista_parametros -> parametro','t[0] = [t[1]]'])
    t[0] = [t[1]]

def p_parametro(t):
    'parametro : tipo IDENTIFICADOR'
    reporte_gramatical.append(['parametro -> tipo IDENTIFICADOR','t[0] = Declaracion(tipo,t[2],None,None,t.lineno(2),find_column(entrada, t.slice[2]))'])
    tipo = ''
    if t[1]=='int': tipo = TIPO_DATO.ENTERO
    elif t[1]=='double' or t[1]=='float': tipo = TIPO_DATO.DECIMAL
    elif t[1]=='char': tipo = TIPO_DATO.CARACTER
    t[0] = Declaracion(tipo,t[2],None,None,t.lineno(2),find_column(entrada, t.slice[2]))

def p_parametro_acceso(t):
    'parametro : tipo IDENTIFICADOR accesos'
    reporte_gramatical.append(['parametro -> tipo IDENTIFICADOR accesos',''])

def p_instrucciones(t):
    'instrucciones : instrucciones instruccion'
    reporte_gramatical.append(['instrucciones -> instrucciones instruccion','t[1].extend(t[2])\nt[0] = t[1]'])
    t[1].extend(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t):
    'instrucciones : instruccion'
    reporte_gramatical.append(['instrucciones -> instruccion','t[0] = t[1]'])
    t[0] = t[1]

def p_instruccion(t):
    'instruccion : declaracion PTCOMA'
    reporte_gramatical.append(['instruccion -> declaracion PTCOMA','t[0] = t[1]'])
    t[0] = t[1]

def p_instruccion_struct(t):
    'instruccion : def_struct PTCOMA'
    reporte_gramatical.append(['instruccion -> decl_struct PTCOMA',''])

def p_instruccion_declaracion_struct(t):
    'instruccion : declaracion_struct PTCOMA'
    reporte_gramatical.append(['instruccion -> declaracion_struct PTCOMA',''])

def p_instruccion_goto(t):
    'instruccion : GOTO IDENTIFICADOR PTCOMA'
    t[0] = [EtiquetasAgust('goto '+t[2]+';\n')]

def p_instruccion_label(t):
    'instruccion : IDENTIFICADOR DPUNTOS'
    t[0] = [EtiquetasAgust(t[1]+':\n')]

#---------------------------------------GRAMATICA PRINTF---------------------------------------------#
def p_printf(t):
    'instruccion : PRINTF PIZQ CADENA COMA lista_param_printf PDER PTCOMA'
    reporte_gramatical.append(['instruccion -> PRINTF PIZQ CADENA COMA lista_param_printf PDER PTCOMA','t[0] = [Printf(t[3],t[5],t.lineno(2),find_column(entrada, t.slice[2]))]'])
    t[0] = [Printf(t[3],t[5],t.lineno(2),find_column(entrada, t.slice[2]))]

def p_printf_cadena(t):
    'instruccion : PRINTF PIZQ CADENA PDER PTCOMA'
    reporte_gramatical.append(['instruccion -> PRINTF PIZQ CADENA PDER PTCOMA','t[0] = Printf(t[3],None,t.lineno(2),find_column(entrada, t.slice[2]))'])
    t[0] = [Printf(t[3],None,t.lineno(2),find_column(entrada, t.slice[2]))]

def p_lista_param_printf(t):
    'lista_param_printf : lista_param_printf COMA expresion'
    reporte_gramatical.append(['lista_param_printf -> lista_param_printf COMA expresion','t[1].append(t[3])\nt[0] = t[1]'])
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_param_printf_param(t):
    'lista_param_printf : expresion'
    reporte_gramatical.append(['lista_param_printf -> expresion','t[0] = [t[1]]'])
    t[0] = [t[1]]

#----------------------------------------GRAMATICA ASIGNACION---------------------------------------------#
def p_instruccion_asignacion(t):
    'instruccion : asignacion PTCOMA'
    reporte_gramatical.append(['instruccion -> asignacion','t[0] = [t[1]]'])
    t[0] = [t[1]]

def p_asignacion(t):
    'asignacion : IDENTIFICADOR sig_asig expresion'
    reporte_gramatical.append(['asignacion -> IDENTIFICADOR sig_asig expresion','t[0] = Asignacion(t[1],None,t[2],t[3],t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = Asignacion(t[1],None,t[2],t[3],t.lineno(1),find_column(entrada, t.slice[1]))

def p_asignacion_accesos(t):
    'asignacion : IDENTIFICADOR accesos sig_asig expresion'
    reporte_gramatical.append(['asignacion -> IDENTIFICADOR accesos sig_asig expresion',''])

def p_asignacion_punto(t):
    'asignacion : IDENTIFICADOR lista_punto sig_asig expresion'
    reporte_gramatical.append(['asignacion -> IDENTIFICADOR lista_punto sig_asig expresion',''])

def p_asignacion_punto_acceso(t):
    'asignacion : IDENTIFICADOR accesos lista_punto sig_asig expresion'
    reporte_gramatical.append(['asignacion -> IDENTIFICADOR accesos lista_punto sig_asig expresion',''])

def p_asignacion_lista_punto(t):
    'lista_punto : lista_punto PUNTO valor'
    reporte_gramatical.append(['lista_punto -> lista_punto PUNTO valor',''])

def p_asignacion_lista_punto_punto(t):
    'lista_punto : PUNTO valor'
    reporte_gramatical.append(['lista_punto -> PUNTO valor',''])

def p_lista_punto_valor_id(t):
    'valor : IDENTIFICADOR'
    reporte_gramatical.append(['valor -> IDENTIFICADOR',''])

def p_lista_punto_valor_acceso(t):
    'valor : IDENTIFICADOR accesos'
    reporte_gramatical.append(['valor -> IDENTIFICADOR accesos',''])
    
#-------------------------------------------GRAMATICA IF--------------------------------------------------#
def p_instruccion_if(t):
    'instruccion : if'
    reporte_gramatical.append(['instruccion -> if','t[0] = [t[1]]'])
    t[0] = [t[1]]

def p_if(t):
    'if : IF PIZQ expresion PDER LLIZQ instrucciones LLDER'
    reporte_gramatical.append(['if -> IF PIZQ expresion PDER LLIZQ instrucciones LLDER','lista = [Elseif(t[3],t[6],t.lineno(1),find_column(entrada, t.slice[1]))]\nt[0] = If(lista)'])
    lista = [Elseif(t[3],t[6],t.lineno(1),find_column(entrada, t.slice[1]))]
    t[0] = If(lista)

def p_if_else(t):
    'if : IF PIZQ expresion PDER LLIZQ instrucciones LLDER ELSE LLIZQ instrucciones LLDER'
    reporte_gramatical.append(['if -> IF PIZQ expresion PDER LLIZQ instrucciones LLDER ELSE LLIZQ instrucciones LLDER','lista = [Elseif(t[3],t[6],t.lineno(1),find_column(entrada, t.slice[1]))]\nlista.append(Elseif(None,t[10],t.lineno(1),find_column(entrada, t.slice[1])))\nt[0] = If(lista)'])
    lista = [Elseif(t[3],t[6],t.lineno(1),find_column(entrada, t.slice[1]))]
    lista.append(Elseif(None,t[10],t.lineno(1),find_column(entrada, t.slice[1])))
    t[0] = If(lista)
    
def p_if_der(t):
    'if : IF PIZQ expresion PDER LLIZQ instrucciones LLDER ELSE if'
    reporte_gramatical.append(['if -> IF PIZQ expresion PDER LLIZQ instrucciones LLDER ELSE if','t[9].lista_if.insert(0,Elseif(t[3],t[6],t.lineno(1),find_column(entrada, t.slice[1])))\nt[0] = t[9]'])
    t[9].lista_if.insert(0,Elseif(t[3],t[6],t.lineno(1),find_column(entrada, t.slice[1])))
    t[0] = t[9]

#-------------------------------------------GRAMATICA SWITCH--------------------------------------------------#
def p_instruccion_switch(t):
    'instruccion : switch_ins'
    reporte_gramatical.append(['instruccion -> switch','t[0] = [t[1]]'])
    t[0] = [t[1]]

def p_switch(t):
    'switch_ins : SWITCH PIZQ expresion PDER LLIZQ lista_cases LLDER'
    reporte_gramatical.append(['switch -> SWITCH PIZQ expresion PDER LLIZQ lista_cases LLDER','t[0] = Switch(t[3],t[6],t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = Switch(t[3],t[6],t.lineno(1),find_column(entrada, t.slice[1]))

def p_switch_default(t):
    'switch_ins : SWITCH PIZQ expresion PDER LLIZQ lista_cases default LLDER'
    reporte_gramatical.append(['switch_ins -> SWITCH PIZQ expresion PDER LLIZQ lista_cases default LLDER','t[6].append(t[7])\nt[0] = Switch(t[3],t[6],t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[6].append(t[7])
    t[0] = Switch(t[3],t[6],t.lineno(1),find_column(entrada, t.slice[1]))

def p_lista_cases(t):
    'lista_cases : lista_cases case'
    reporte_gramatical.append(['lista_cases -> lista_cases case','t[1].append(t[2])\nt[0] = t[1]'])
    t[1].append(t[2])
    t[0] = t[1]

def p_lista_case(t):
    'lista_cases : case'
    reporte_gramatical.append(['lista_cases -> case','t[0] = t[1]'])
    t[0] = [t[1]]

def p_case(t):
    'case : CASE expresion DPUNTOS instrucciones' 
    reporte_gramatical.append(['case -> CASE expresion DPUNTOS instrucciones','t[0] = Case(t[2],t[4],t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = Case(t[2],t[4],t.lineno(1),find_column(entrada, t.slice[1]))

def p_case_epsilon(t):
    'case : CASE expresion DPUNTOS' 
    reporte_gramatical.append(['case -> CASE expresion DPUNTOS instrucciones','t[0] = Case(t[2],[],t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = Case(t[2],[],t.lineno(1),find_column(entrada, t.slice[1]))

def p_default(t):
    'default : DEFAULT DPUNTOS instrucciones'
    reporte_gramatical.append(['default -> DEFAULT DPUNTOS instrucciones','t[0] = Case(None,t[4],t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = Case(None,t[3],t.lineno(1),find_column(entrada, t.slice[1]))

#------------------------------------------GRAMATICA WHILE------------------------------------------------#
def p_instruccion_while(t):
    'instruccion : while'
    reporte_gramatical.append(['instruccion -> while','t[0] = [t[1]]'])
    t[0] = [t[1]]

def p_while(t):
    'while : WHILE PIZQ expresion PDER LLIZQ instrucciones LLDER'
    reporte_gramatical.append(['while -> WHILE PIZQ expresion PDER LLIZQ instrucciones LLDER','t[0] = While(t[3],t[6],t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = While(t[3],t[6],t.lineno(1),find_column(entrada, t.slice[1]))

#----------------------------------------GRAMATICA DO WHILE------------------------------------------------#
def p_instruccion_do_while(t):
    'instruccion : do_while'
    reporte_gramatical.append(['instruccion -> do_while','t[0] = [t[1]]'])
    t[0] = [t[1]]

def p_do_while(t):
    'do_while : DO LLIZQ instrucciones LLDER WHILE PIZQ expresion PDER PTCOMA'
    reporte_gramatical.append(['do_while : DO LLIZQ instrucciones LLDER WHILE PIZQ expresion PDER PTCOMA','t[0] = DoWhile(t[7],t[3],t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = DoWhile(t[7],t[3],t.lineno(1),find_column(entrada, t.slice[1]))

#------------------------------------------GRAMATICA FOR---------------------------------------------------#
def p_instruccion_for(t):
    'instruccion : for'
    reporte_gramatical.append(['instruccion -> for','t[0] = [t[1]]'])
    t[0] = [t[1]]

def p_for(t):
    'for : FOR PIZQ for_ini PTCOMA for_exp PTCOMA for_inc PDER LLIZQ instrucciones LLDER '
    reporte_gramatical.append(['for -> FOR PIZQ for_ini PTCOMA for_exp PTCOMA for_inc PDER LLIZQ instrucciones LLDER ','t[0] = For(t[3],t[5],t[7],t[10],t.lineno(1),find_column(entrada, t.slice[1]))'])
    t[0] = For(t[3],t[5],t[7],t[10],t.lineno(1),find_column(entrada, t.slice[1]))

def p_for_ini(t):
    'for_ini : IDENTIFICADOR'
    reporte_gramatical.append(['for_ini -> IDENTIFICADOR','t[0] = t[1]'])
    t[0] = t[1]

def p_for_ini_dec(t):
    'for_ini : declaracion'
    reporte_gramatical.append(['for_ini -> declaracion','t[0] = t[1]'])
    t[0] = t[1][0]

def p_for_init_asig(t):
    'for_ini : asignacion'
    reporte_gramatical.append(['for_ini -> asignacion','t[0] = t[1]'])
    t[0] = t[1]

def p_for_ini_epsilon(t):
    'for_ini : '
    reporte_gramatical.append(['for_ini -> ','t[0] = None'])
    t[0] = None

def p_for_exp(t):
    'for_exp : expresion'
    reporte_gramatical.append(['for_exp -> expresion','t[0] = t[1]'])
    t[0] = t[1]

def p_for_exp_epsilon(t):
    'for_exp : '
    reporte_gramatical.append(['for_exp -> ','t[0] = None'])
    t[0] = None

def p_for_incremento(t):
    'for_inc : asignacion'
    reporte_gramatical.append(['for_inc -> asignacion','t[0] = t[1][0]'])
    t[0] = t[1]

def p_for_operadores(t):
    'for_inc : inc_dec'
    reporte_gramatical.append(['for_inc -> inc_dec','t[0] = t[1][0]'])
    t[0] = t[1]

def p_for_inc_epsilon(t):
    'for_inc : '
    reporte_gramatical.append(['for_inc -> ','t[0] = None'])
    t[0] = None

#------------------------------------------GRAMATICA BREAK------------------------------------------------#
def p_instruccion_break(t):
    'instruccion : BREAK PTCOMA'
    reporte_gramatical.append(['instruccion -> BREAK PTCOMA','t[0] = [Break()]'])
    t[0] = [Break()]

#------------------------------------------GRAMATICA CONTINUE------------------------------------------------#
def p_instruccion_continue(t):
    'instruccion : CONTINUE PTCOMA'
    reporte_gramatical.append(['instruccion -> CONTINUE PTCOMA','t[0] = [Continue()]'])
    t[0] = [Continue()]

#------------------------------------------GRAMATICA RETURN------------------------------------------------#
def p_instruccion_return(t):
    'instruccion : RETURN PTCOMA'
    reporte_gramatical.append(['instruccion -> RETURN PTCOMA',''])

def p_instruccion_return_exp(t):
    'instruccion : RETURN expresion PTCOMA'
    reporte_gramatical.append(['instruccion -> RETURN expresion PTCOMA',''])

#------------------------------------------GRAMATICA INCREMENTOS------------------------------------------------#
def p_ins_inc_dec(t):
    'instruccion : inc_dec PTCOMA'
    reporte_gramatical.append(['instruccion -> inc_dec PTCOMA','t[0] = t[1]'])
    t[0] = [t[1]]

def p_ins_inc_pre(t):
    'inc_dec : INCREMENTO IDENTIFICADOR'
    reporte_gramatical.append(['inc_dec -> INCREMENTO IDENTIFICADOR','exp = Expresion(t[2],Expresion(1,None,TIPO_OPERACION.ENTERO,t.lineno(1),find_column(entrada, t.slice[1])),TIPO_OPERACION.SUMA,t.lineno(1),find_column(entrada, t.slice[1]))\nt[0] = Asignacion(t[2],None,\'=\',exp,t.lineno(1),find_column(entrada, t.slice[1]))'])
    exp_id = Expresion(t[2],None,TIPO_OPERACION.IDENTIFICADOR,t.lineno(1),find_column(entrada, t.slice[1]))
    exp_1 = Expresion(1,None,TIPO_OPERACION.ENTERO,t.lineno(1),find_column(entrada, t.slice[1]))
    exp = Expresion(exp_id,exp_1,TIPO_OPERACION.SUMA,t.lineno(1),find_column(entrada, t.slice[1]),'+')
    t[0] = Asignacion(t[2],None,'=',exp,t.lineno(1),find_column(entrada, t.slice[1]))

def p_ins_inc_post(t):
    'inc_dec : IDENTIFICADOR INCREMENTO'
    reporte_gramatical.append(['inc_dec -> IDENTIFICADOR INCREMENTO','exp = Expresion(t[1],Expresion(1,None,TIPO_OPERACION.ENTERO,t.lineno(1),find_column(entrada, t.slice[1])),TIPO_OPERACION.SUMA,t.lineno(1),find_column(entrada, t.slice[1]))\nt[0] = Asignacion(t[1],None,\'=\',exp,t.lineno(1),find_column(entrada, t.slice[1]))'])
    exp_id = Expresion(t[1],None,TIPO_OPERACION.IDENTIFICADOR,t.lineno(1),find_column(entrada, t.slice[1]))
    exp_1 = Expresion(1,None,TIPO_OPERACION.ENTERO,t.lineno(1),find_column(entrada, t.slice[1]))
    exp = Expresion(exp_id,exp_1,TIPO_OPERACION.SUMA,t.lineno(1),find_column(entrada, t.slice[1]),'+')
    t[0] = Asignacion(t[1],None,'=',exp,t.lineno(1),find_column(entrada, t.slice[1]))

def p_ins_dec_pre(t):
    'inc_dec : DECREMENTO IDENTIFICADOR'
    reporte_gramatical.append(['inc_dec -> DECREMENTO IDENTIFICADOR','exp = Expresion(t[2],Expresion(1,None,TIPO_OPERACION.ENTERO,t.lineno(1),find_column(entrada, t.slice[1])),TIPO_OPERACION.RESTA,t.lineno(1),find_column(entrada, t.slice[1]))\nt[0] = Asignacion(t[2],None,\'=\',exp,t.lineno(1),find_column(entrada, t.slice[1]))'])
    exp_id = Expresion(t[2],None,TIPO_OPERACION.IDENTIFICADOR,t.lineno(1),find_column(entrada, t.slice[1]))
    exp_1 = Expresion(1,None,TIPO_OPERACION.ENTERO,t.lineno(1),find_column(entrada, t.slice[1]))
    exp = Expresion(exp_id,exp_1,TIPO_OPERACION.RESTA,t.lineno(1),find_column(entrada, t.slice[1]),'-')
    t[0] = Asignacion(t[2],None,'=',exp,t.lineno(1),find_column(entrada, t.slice[1]))

def p_ins_dec_post(t):
    'inc_dec : IDENTIFICADOR DECREMENTO'
    reporte_gramatical.append(['inc_dec -> IDENTIFICADOR DECREMENTO','exp = Expresion(t[1],Expresion(1,None,TIPO_OPERACION.ENTERO,t.lineno(1),find_column(entrada, t.slice[1])),TIPO_OPERACION.RESTA,t.lineno(1),find_column(entrada, t.slice[1]))\nt[0] = Asignacion(t[1],None,\'=\',exp,t.lineno(1),find_column(entrada, t.slice[1]))'])
    exp_id = Expresion(t[1],None,TIPO_OPERACION.IDENTIFICADOR,t.lineno(1),find_column(entrada, t.slice[1]))
    exp_1 = Expresion(1,None,TIPO_OPERACION.ENTERO,t.lineno(1),find_column(entrada, t.slice[1]))
    exp = Expresion(exp_id,exp_1,TIPO_OPERACION.RESTA,t.lineno(1),find_column(entrada, t.slice[1]),'-')
    t[0] = Asignacion(t[1],None,'=',exp,t.lineno(1),find_column(entrada, t.slice[1]))

#---------------------------------------GRAMATICA EXPRESIONES---------------------------------------------#
def p_expresion_3(t):
    ''' expresion : expresion MAS expresion
                | expresion MENOS expresion
                | expresion POR expresion
                | expresion DIVIDIDO expresion
                | expresion MODULO expresion
                | expresion AND expresion
                | expresion OR expresion
                | expresion BBAND expresion
                | expresion BBOR expresion
                | expresion BBXOR expresion
                | expresion BBIZQ expresion
                | expresion BBDER expresion
                | expresion IGUAL_QUE expresion
                | expresion DESIGUAL_QUE expresion
                | expresion MENOR_QUE expresion
                | expresion MAYOR_QUE expresion
                | expresion MENOR_IGUAL_QUE expresion
                | expresion MAYOR_IGUAL_QUE expresion
    '''
    reporte_gramatical.append([' expresion -> expresion '+t[2]+' expresion',''])
    if t[2]=='+': t[0] = Expresion(t[1],t[3],TIPO_OPERACION.SUMA,t.lineno(2),find_column(entrada, t.slice[2]),t[2])
    if t[2]=='-': t[0] = Expresion(t[1],t[3],TIPO_OPERACION.RESTA,t.lineno(2),find_column(entrada, t.slice[2]),t[2])
    if t[2]=='*': t[0] = Expresion(t[1],t[3],TIPO_OPERACION.MULTIPLICACION,t.lineno(2),find_column(entrada, t.slice[2]),t[2])
    if t[2]=='/': t[0] = Expresion(t[1],t[3],TIPO_OPERACION.DIVISION,t.lineno(2),find_column(entrada, t.slice[2]),t[2])
    if t[2]=='%': t[0] = Expresion(t[1],t[3],TIPO_OPERACION.RESIDUO,t.lineno(2),find_column(entrada, t.slice[2]),t[2])
    if t[2]=='<': t[0] = Expresion(t[1],t[3],TIPO_OPERACION.MENOR_QUE,t.lineno(2),find_column(entrada, t.slice[2]),t[2])
    if t[2]=='>': t[0] = Expresion(t[1],t[3],TIPO_OPERACION.MAYOR_QUE,t.lineno(2),find_column(entrada, t.slice[2]),t[2])
    if t[2]=='<=': t[0] = Expresion(t[1],t[3],TIPO_OPERACION.MENOR_IGUAL_QUE,t.lineno(2),find_column(entrada, t.slice[2]),t[2])
    if t[2]=='>=': t[0] = Expresion(t[1],t[3],TIPO_OPERACION.MAYOR_IGUAL_QUE,t.lineno(2),find_column(entrada, t.slice[2]),t[2])
    if t[2]=='==': t[0] = Expresion(t[1],t[3],TIPO_OPERACION.IGUAL_QUE,t.lineno(2),find_column(entrada, t.slice[2]),t[2])
    if t[2]=='!=': t[0] = Expresion(t[1],t[3],TIPO_OPERACION.DISTINTO_QUE,t.lineno(2),find_column(entrada, t.slice[2]),t[2])
    if t[2]=='&&': t[0] = Expresion(t[1],t[3],TIPO_OPERACION.AND,t.lineno(2),find_column(entrada, t.slice[2]),t[2])
    if t[2]=='||': t[0] = Expresion(t[1],t[3],TIPO_OPERACION.OR,t.lineno(2),find_column(entrada, t.slice[2]),t[2])
    if t[2]=='&': t[0] = Expresion(t[1],t[3],TIPO_OPERACION.BBAND,t.lineno(2),find_column(entrada, t.slice[2]),t[2])
    if t[2]=='|': t[0] = Expresion(t[1],t[3],TIPO_OPERACION.BBOR,t.lineno(2),find_column(entrada, t.slice[2]),t[2])
    if t[2]=='^': t[0] = Expresion(t[1],t[3],TIPO_OPERACION.BBXOR,t.lineno(2),find_column(entrada, t.slice[2]),t[2])
    if t[2]=='<<': t[0] = Expresion(t[1],t[3],TIPO_OPERACION.BBIZQ,t.lineno(2),find_column(entrada, t.slice[2]),t[2])
    if t[2]=='>>': t[0] = Expresion(t[1],t[3],TIPO_OPERACION.BBDER,t.lineno(2),find_column(entrada, t.slice[2]),t[2])

def p_expresion_2(t):
    ''' expresion : BBNOT expresion
                    | NOT expresion
                    | MENOS expresion
                    | INCREMENTO IDENTIFICADOR
                    | DECREMENTO IDENTIFICADOR
                    | BBAND expresion
    '''
    reporte_gramatical.append([' expresion -> '+t[1]+' expresion',''])
    if t[1]=='!': t[0] = Expresion(t[2],None,TIPO_OPERACION.NOT,t.lineno(1),find_column(entrada, t.slice[1]),t[1])
    if t[1]=='~': t[0] = Expresion(t[2],None,TIPO_OPERACION.BBNOT,t.lineno(1),find_column(entrada, t.slice[1]),t[1])
    if t[1]=='-': t[0] = Expresion(t[2],None,TIPO_OPERACION.MENOS_UNARIO,t.lineno(1),find_column(entrada, t.slice[1]),t[1])

def p_expresion_2_post(t):
    ''' expresion : IDENTIFICADOR INCREMENTO
                | IDENTIFICADOR DECREMENTO
    '''
    reporte_gramatical.append([' expresion -> expresion '+t[2],''])

def p_expresion_2_accesos(t):
    'expresion : IDENTIFICADOR accesos'
    reporte_gramatical.append([' expresion -> IDENTIFICADOR accesos',''])

def p_expresion_2_lista_punto(t):
    'expresion : IDENTIFICADOR lista_punto'
    reporte_gramatical.append([' expresion -> IDENTIFICADOR lista_punto',''])

def p_expresion_3_acceso_lista_punto(t):
    'expresion : IDENTIFICADOR accesos lista_punto'
    reporte_gramatical.append([' expresion -> IDENTIFICADOR accesos lista_punto',''])

def p_expresion_1_entero(t):
    ''' expresion : ENTERO '''
    reporte_gramatical.append([' expresion -> ENTERO',''])
    t[0] = Expresion(t[1],None,TIPO_OPERACION.ENTERO,t.lineno(1),find_column(entrada, t.slice[1]))

def p_expresion_1_cadena(t):
    'expresion : CADENA '
    reporte_gramatical.append([' expresion -> CADENA',''])
    t[0] = Expresion(t[1],None,TIPO_OPERACION.CADENA,t.lineno(1),find_column(entrada, t.slice[1]))

def p_expresion_1_decimal(t):
    'expresion : DECIMAL '
    reporte_gramatical.append([' expresion -> DECIMAL',''])
    t[0] = Expresion(t[1],None,TIPO_OPERACION.DECIMAL,t.lineno(1),find_column(entrada, t.slice[1]))

def p_expresion_1_caracter(t):
    'expresion : CARACTER'
    reporte_gramatical.append([' expresion -> CARACTER',''])
    t[0] = Expresion(t[1],None,TIPO_OPERACION.CARACTER,t.lineno(1),find_column(entrada, t.slice[1]))

def p_expresion_1_identificador(t):
    'expresion : IDENTIFICADOR '
    reporte_gramatical.append([' expresion -> IDENTIFICADOR',''])
    t[0] = Expresion(t[1],None,TIPO_OPERACION.IDENTIFICADOR,t.lineno(1),find_column(entrada, t.slice[1]))

def p_expresion_1_llamada(t):
    'expresion : llamada '
    reporte_gramatical.append([' expresion -> llamada',''])

def p_expresion_1_scanf(t):
    'expresion : SCANF PIZQ PDER'
    t[0] = Scanf(t.lineno(1),find_column(entrada, t.slice[1]))

def p_expresion_par(t):
    ''' expresion : PIZQ expresion PDER '''
    reporte_gramatical.append([' expresion -> ( expresion )','t[0] = t[2]'])
    t[0] = t[2]

def p_operador_ternario(t):
    ' expresion : expresion TERNARIO expresion DPUNTOS expresion '
    reporte_gramatical.append([' expresion -> expresion TERNARIO expresion DPUNTOS expresion ',''])

def p_sizeof(t):
    ' expresion : SIZEOF PIZQ expresion PDER'
    reporte_gramatical.append([' expresion -> SIZEOF PIZQ expresion PDER',''])

def p_sizeof_TIPO(t):
    ' expresion : SIZEOF PIZQ tipo PDER'
    reporte_gramatical.append([' expresion -> SIZEOF PIZQ tipo PDER',''])

def p_casteos(t):
    ' expresion : PIZQ tipo PDER expresion'
    reporte_gramatical.append([' expresion -> PIZQ tipo PDER expresion',''])

#---------------------------------------GRAMATICA LLAMADA FUNCIONES----------------------------------------#
def p_instruccion_llamada(t):
    'instruccion : llamada PTCOMA'
    reporte_gramatical.append([ 'instruccion -> llamada PTCOMA',''])

def p_llamada(t):
    'llamada : IDENTIFICADOR PIZQ PDER'
    reporte_gramatical.append([' expresion -> IDENTIFICADOR PIZQ PDER ',''])

def p_llamada_parametros(t):
    'llamada : IDENTIFICADOR PIZQ lista_expresiones PDER'
    reporte_gramatical.append([' expresion -> IDENTIFICADOR PIZQ lista_expresiones PDER ',''])

def p_lista_expresiones(t):
    'lista_expresiones : lista_expresiones COMA expresion'
    reporte_gramatical.append(['lista_expresiones -> lista_expresiones COMA expresion',''])

def p_lista_expresiones_expresion(t):
    'lista_expresiones : expresion'
    reporte_gramatical.append(['lista_expresiones -> expresion',''])

#---------------------------------------METODOS DE HERRAMIENTA---------------------------------------------#
def p_error(t):
    if not t:
        mensajes.append(Mensaje(TIPO_MENSAJE.SINTACTICO,'Error sintáctico irrecuperable.',0,0))    
        return

    mensajes.append(Mensaje(TIPO_MENSAJE.SINTACTICO,'Error sintáctico en: '+str(t.value)+'.',t.lineno,find_column(entrada, t)))    
    while True:
        tok = parser.token()
        if not tok or tok.type == 'PTCOMA': 
            break
    parser.restart()

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return ((token.lexpos - line_start) + 1)

import ply.yacc as yacc
parser = yacc.yacc()

entrada = ''
mensajes = []
reporte_gramatical = []
temporal_tipo = ''

def parsec(input) :
    global entrada
    entrada = input
    return parser.parse(input)