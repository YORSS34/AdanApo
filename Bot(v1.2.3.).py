#BOT

from nltk.chat.util import Chat, reflections

#Presentacion

print('.        █████╗ ██████╗   █████╗ ███╗   ██╗ ')
print('.       ██╔══██╗██╔══██╗██╔══██╗████╗  ██║ ')
print('.       ███████║██║  ██║███████║██╔██╗ ██║ ')
print ('.       ██╔══██║██║  ██║██╔══██║██║╚██╗██║ ')
print('.       ██║  ██║██████╔╝██║  ██║██║ ╚████║')
print('.       ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ .')
print('============================================================')
print('.........Ｖ１.０.０.０.6..........')
print('')
print('')
print('>MI NOMBRE ES ADAN Y SERÉ TU ASISTENTE૮₍´˶ᵔ ᵕ ᵔ⑅ ₎ა')

#Variables

pairs = [['mi nombre es (.*)', ['Hola %1,¿Cómo estás?૮₍´˶•⁠ᴗ⁠•⑅ ₎ა']],
['bien|Vien|Fino|Piola|fino|piola|toi ready|toi redi|toi chulo|ando tranqui|good|Bien',['¡Me alegro!,¿Qué puedo hacer por tí hoy?૮₍´ ˶^ - ^ ⑅ ₎ა']],
['(.*) saber sobre(.*)',['Me especializo en 17 áreas, aquí las secciones: Programación, Historia, Geografía, esperando más resultados...૮₍´˶ᵔ ᵕ ᵔ⑅ ₎ა']],
['Meh|mjm|ay|Ai|ai|pf|Pfff',['¿Qué le ocurre?૮₍´˶• . • ⑅ ₎ა']],['Mal|Terrible|Creo que nada bien|no sé como me siento', ['Lamento saberlo,¿Quiéres qué te ayude a sentirte mejor?૮₍´⇀⁠‸⁠↼⁠‶⑅ ₎ა']],
['(Hola|Ola|ola|hola|(.*)uenos días|(.*)uenas tardes)',['Hola, ¿En qué puedo ayudarte?૮₍´˶•⁠ᴗ⁠•⑅ ₎ა']],
['qué (.*) quieres', ['Quiero ayudarte en lo que necesites']],
['(.*) creado', ['Fui creado el Sábado 15 de Junio de 2024 a las 1500 horas ૮₍´˶ᵔ ᵕ ᵔ⑅ ₎ა']],
['(.*) programado', ['Fui programado en python ૮₍´♡ ᵕ ♡ ⑅ ₎ა']],
['salir', ['Adiós! Espero haber sido de ayuda૮₍´ ˶^ - ^ ⑅ ₎ა']],
['(.*) creó|(.*)creo|(.*)kreo',['Me creó YorSS01 ૮₍´˶☆ - ☆⑅ ₎ა']],
['(.*) nombre|(.*) llamas',['Mi nombre ha sido asignado por Yorss01 y es: Adan ૮₍´˶ᵔ ᵕ ᵔ⑅ ₎ა']],['(.*) lindo|(.*) linda',['Si,mucho૮₍´˶ᵔ ᵕ ᵔ⑅ ₎ა']],
['(.*) veo hoy',['Creo que te debes ver bien૮₍´˶•⁠ᴗ⁠•⑅ ₎ა']],
#Posibles preguntas
['(.*)istoria',['¿Qué exactamente quisieras saber del tema?૮₍´˶• . • ⑅ ₎ა']],
['',['']],
['',['']],
['',['']],
['',['']],
['',['']],
['',['']],
['',['']],
['',['']],
['',['']],
['',['']],
['',['']],
['',['']],
['',['']],
['',['']],
['',['']],
['',['']],
['',['']],

]

#Funcion

def chatbot():
   
   print('el bot ha sido inicializado')
chat = Chat(pairs, reflections)
chat.converse()