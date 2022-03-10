print('ELEIÇÕES 2020')
print('Justiça Eleitoral')
print('=-' * 19)
 
def menu():
  print('\n')
  print('Candidatos:')
  print('João do gás | Número: 18')
  print('Ronaldo dono do bar | Número: 20')
  print('Titio Dinho | Número: 12')
  print('Digite 0 para encerra a sessão de votação')
  return 
 
 
nJ = 0
nR = 0
nT = 0
vB = 0
vN = 0
 
while True:
  menu()
  print('\n')
  voto = input('Digite o número do seu candidato: ')
  if voto == '18':
    confirmar = input('Deseja confirmar seu voto? Sim ou Não: ')
    if confirmar == 'Sim':
      print('Você votou em João do gás ')
      nJ += 1
    elif confirmar == 'Não':
      continue
 
##=-=-=-=-= LINHA SEPARADORA DE CODIGO =-=-=-=-=##    
 
  elif voto == '20':
    confirmar = input('Deseja confirmar seu voto? Sim ou Não: ')
    if confirmar == 'Sim':
      print('Você votou em Ronaldo dono do bar ')
      nR += 1
    elif confirmar == 'Não':
      continue
 
##=-=-=-=-= LINHA SEPARADORA DE CODIGO =-=-=-=-=##  
 
 
  elif voto == '12':
    confirmar = input('Deseja confirmar seu voto? Sim ou Não: ')
    if confirmar == 'Sim':
       print('Você votou em Titio Dinho ')
       nT += 1
    elif confirmar == 'Não':
      continue
 
##=-=-=-=-= LINHA SEPARADORA DE CODIGO =-=-=-=-=## 
 
 
  elif voto == '':
    confirmar = input('Deseja confirmar seu voto? Sim ou Não: ')
    if confirmar == 'Sim':
       print('Você votou em branco ')
       vB += 1
    elif confirmar == 'Não':
      continue
 
##=-=-=-=-= LINHA SEPARADORA DE CODIGO =-=-=-=-=## 
 
  elif voto != 18 and 20 and 12 and 0:
    confirmar = input('Deseja confirmar seu voto? Sim ou Não: ')
    if confirmar == 'Sim':
       print('Você votou Nulo ')
       vN += 1
    elif confirmar == 'Não':
      continue
  
 
  elif voto == '0':
    break
 
 
def resultado():
  if nJ > nR and nJ > nT:
    print('\n\n')
    print('João do gás é o novo Prefeito com', nJ, 'voto(s)')
    print('Voto(s) Ronaldo do bar', nR)
    print('Voto(s) Titio Dinho', nT)
    print('Voto(s) nulos', vN)
    print('Voto(s) em branco', vB)
    print('Total de votos: ', nJ + nR + nT + vB + vN)
  elif nR > nJ and nR > nT:
    print('Ronaldo do bar é o novo Prefeito com', nR, 'votos')
    print('Voto(s) João do gás', nJ)
    print('Voto(s) Titio Dinho', nT)
    print('Voto(s) nulos', vN)
    print('Voto(s) em branco', vB)
    print('Total de votos: ', nJ + nR + nT + vB + vN)
  elif nT > nJ and nT > nR:
    print('Titio Dinho é o novo Prefeito com', nT, 'votos')
    print('Voto(s) João do gás', nJ)
    print('Voto(s) Ronaldo do bar', nR)
    print('Voto(s) nulos', vN)
    print('Voto(s) em branco', vB)
    print('Total de votos: ', nJ + nR + nT + vB + vN)
 
print('=-=-=-= RESULTADOS =-=-=-=')
 
resultado()