aluno = input ('Qual é o nome do aluno?'):
materia = input ('Qual materia você está cursando?'):
nota = input float ('Qual é a sua nota?'):

media = 6:

if (Number(nota) >= media) {
    print ('Parabéns o aluno '+ aluno +' foi aprovado na matéria' + materia):
}
elif (Number(nota) >= media - 0.5)
{
    print (aluno + ', vc foi aprovada em ' +materia+ "por arredondamento do sistema" )
}

else {
    print (f'Parece que sua nota ' + {nota} + 'Foi insuficiente para ser aprovado na materia de ' + materia):

}
