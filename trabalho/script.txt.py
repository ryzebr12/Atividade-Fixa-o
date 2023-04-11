import sys
from os import path

dirname = path.dirname(__file__)

def readFile(filename):
  try:
    filepath = path.join(dirname, 'arquivo_entrada', filename)
    with open(filepath) as file:
        data = file.readlines()
        return data
  except:
    print('erro ao ler arquivo')

def createDisciplineFile(filename, data): 
  try:
    with open(path.join(dirname, 'arquivo_saida', filename), 'w') as file:
      for line in data:
        file.write(f'{line[0]};{line[1]}')
        file.write('\n')
  except :
    print('erro ao criar o arquivo')

def createAverageFile(filename, data): 
  try:
    with open(path.join(dirname, 'arquivo_saida', filename), 'w') as file:
      for line in data:
        av1 = float(f'{line[3][0:2]}.{line[3][2:3]}')
        av2 = float(f'{line[3][3:5]}.{line[3][5:6]}')
        av3 = float(f'{line[3][6:8]}.{line[3][8:9]}')
        avg = average(av1, av2, av3)
        status = 'Aprovado' if avg >= 7 else 'Reprovado'
        file.write(f'{line[0]};{line[1]};{av1};{av2};{av3};{avg};{status}')
        file.write('\n')
  except :
    e = sys.exc_info()[0]
    print('erro ao criar o arquivo', e)


def extractDisciplines():
  try:
    disciplines = []
    data = readFile('2023.csv')
    for line in data:
      item = line.strip().split(';')
      if item[2] not in disciplines:
        disciplines.append(item[2])
    return disciplines
  except: 
    return []
  
def extractStudents(discipline):
  try:
    students = []
    data = readFile('2023.csv')
    for line in data:
      item = line.strip().split(';')
      if item[2] == discipline:
        students.append(item)
    return students
  except: 
    return []  

def average(av1, av2, av3):
  if av1 >= av2 and av2 >= av3:
    return (av1 + av2 ) / 2
  elif av1 >= av2 and av2 <= av3:
    return (av1 + av3 ) / 2
  else:
    return (av2 + av3 ) / 2

for d in extractDisciplines():
  s = extractStudents(d)
  # print(d, s)
  createDisciplineFile(f'{d}.csv', s)
  createAverageFile(f'{d}_notas.csv', s)
def criar_pasta_aprovados_reprovados(disciplina, estudantes):
    try:
        aprovados_dir = path.join(dirname, 'arquivo_saida', disciplina, 'aprovados')
        reprovados_dir = path.join(dirname, 'arquivo_saida', disciplina, 'reprovados')
        makedirs(aprovados_dir)
        makedirs(reprovados_dir)

        for estudante in estudantes:
            matricula = estudante[0]
            nome = estudante[1]
            media = float(estudante[5])
            if media >= 7.0:
                arquivo = f"{matricula} {nome}.txt"
                with open(path.join(aprovados_dir, arquivo), 'w') as file:
                    file.write(f"Matrícula: {matricula}")
            else:
                arquivo = f"{matricula} {nome}.txt"
                with open(path.join(reprovados_dir, arquivo), 'w') as file:
                    file.write(f"Matrícula: {matricula}")
    except:
        e = sys.exc_info()[0]
        print('Erro ao criar pasta aprovados/reprovados', e)
  