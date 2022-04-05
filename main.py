contador = 0  # É responsável por calcular os acertos
print('Quiz de God of War')

# Perguntas
question1 = input('1 - Quem é o pai de Kratos?\n'  # Recebe a respostado jogador
                  'A) Hades\n'
                  'B) Ares\n'
                  'C) Zeus\n'
                  'D) Leonidas\n\n')
# Verifica se o jogador acertou ou errou
if question1 == 'c':
    print('Acertou\n')
    contador += 1
elif question1 != 'c':
    print('Errou\n')

question2 = input('2 - Quem foi o primeiro Deus que Kratos matou em God of War 3?\n'
                  'A) Zeus\n'
                  'B) Poseidon\n'
                  'C) Hércules\n'
                  'D) Hades\n\n')
if question2 == 'b':
    print('Acertou\n')
    contador += 1
elif question2 != 'b':
    print('Errou\n')

question3 = input('3 - Qual é a arma mais forte do Olimpo?\n'
                  'A) Lamina do Caos\n'
                  'B) Lamina do Olimpo\n'
                  'C) Tridende do Poseidon\n'
                  'D) Machado Leviatan\n\n')
if question3 == 'b':
    print('Acertou\n')
    contador += 1
elif question3 != 'b':
    print('Errou\n')

question4 = input('4 - Porquê Kratos queria matar ares?\n'
                  'A) Porque ele fez Kratos matar sua família\n'
                  'B) Porque ares matou a filha dele\n'
                  'C) Porque ares mentiu para ele.\n'
                  'D) Porque ele matou seu exército\n\n')
if question4 == 'a':
    print('Acertou\n')
    contador += 1
elif question4 != 'a':
    print('Errou\n')

question5 = input('5 - Qual o nome da filha de Kratos?\n'
                  'A) Ártemis\n'
                  'B) Calíope\n'
                  'C) Pesérfone\n'
                  'D) Pandora\n\n')
if question5 == 'b':
    print('Acertou\n')
    contador += 1
elif question5 != 'b':
    print('Errou\n')

question6 = input('6 - Qual é a mitologia do God of War 4?\n'
                  'A) Astéca\n'
                  'B) Grega\n'
                  'C) Egípicia\n'
                  'D) Nórdica\n\n')
if question6 == 'd':
    print('Acertou\n')
    contador += 1
elif question6 != 'd':
    print('Errou\n')

question7 = input('7 - Qual é o nome do filho de Kratos?\n'
                  'A) Atreus\n'
                  'B) Garoto\n'
                  'C) Baldur\n'
                  'D) Magni\n\n')
if question7 == 'a':
    print('Acertou')
    contador += 1
elif question7 != 'a':
    print('Errou')

question8 = input('8 - Qual o nome do irmão de Kratos?\n'
                  'A) Thor\n'
                  'B) Hades\n'
                  'C) Hermes\n'
                  'D) Deimos\n\n')
if question8 == 'd':
    print('Acertou')
    contador += 1
elif question8 != 'd':
    print('Errou')

question9 = input('9 - Qual god of war foi considerado o jogo do ano?\n'
                  'A) God of War 2\n'
                  'B) God of War 4\n'
                  'C) God of War Ascencion\n'
                  'D) God of War 3\n\n')
if question9 == 'b':
    print('Acertou')
    contador += 1
elif question9 != 'b':
    print('Errou')

question10 = input('10 - Qual foi o primeiro god of war por ordem cronológica?\n'
                   'A) God of War Chains of Olympus\n'
                   'B) God of War Ghost of Sparta\n'
                   'C) God of War Ascension\n'
                   'D) God of War 1\n\n')
if question10 == 'c':
    print('Acertou')
    contador += 1
elif question10 != 'c':
    print('Errou')

# Resultado
# Calcula o total de acertos e retorna o resultado do quiz

if contador >= 9:
    print('Você acertou {}/10'.format(contador))
    print('Você é um expert no assunto')

if contador >= 7 and contador <= 8:
    print('Você acertou {}/10'.format(contador))
    print('Você tem um bom conhecimento no assunto')

if contador >= 5 and contador <= 6:
    print('Você acertou {}/10'.format(contador))
    print('Você tem um certo conhecimento no assunto')

if contador >= 3 and contador <= 4:
    print('Você acertou {}/10'.format(contador))
    print('Seu conhecimento é básico')

if contador >= 0 and contador <= 2:
    print('Você acertou {}/10'.format(contador))
    print('Você é um noob nesse assunto')
