'''
1. Controle de cotas de disco. A ACME Inc., uma organização com mais de 1500 funcionários,
está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver
este problema, o Administrador de Rede precisa saber qual o espaço em disco ocupado pelas
contas dos usuários, e identificar os usuários com maior espaço ocupado. Através de um aplicativo
baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado 'usuarios.txt':


alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o primeiro campo corresponde ao login do usuário e o segundo ao espaço em disco ocupado pelo seu diretório home. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado relatório.txt, no seguinte formato:


ACME Inc.           Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB            16,85%
2    anderson       1187,99 MB            46,02%
3    antonio         117,73 MB             4,56%
4    carlos           87,03 MB             3,37%
5    cesar             0,94 MB             0,04%
6    rosemary        752,88 MB            29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.
'''

writeUser = open("usuarios.txt", "r")

# INCIO
lst = [i.replace("\n", "") for i in writeUser]
userName = [i.rsplit(" ", 1)[0] for i in lst]
userStorage = [int(i.rsplit()[1]) for i in lst]

# CONVERSÃO
userStorageInMb = [round((float(i) / 1048576), 2) for i in userStorage]
userTotalStorageInMb = round((sum(userStorage) / 1048576), 2)
userMedStorageInMb = round((sum(userStorage) / 1048576) / len(userStorageInMb), 2)
userStorageInMb_Space = []

# PORCENTAGEM
userStroagePercent = [round((i / userTotalStorageInMb) * 100, 2) for i in userStorageInMb]
userStroagePercent_Space = []

# lINHAS
lineCount = []
# VARIAVEIS FIXAS
countLine = 0
line = []
spaceAdd = []

# CORRIGIR ESPAÇOS
for i in range(1, len(lst)):
    line.append(i)
else:
    line.append(i + 1)

for i in line:
    charCount = len(str(i))
    if charCount <= 5:
        spaceAdd.append(" " * (5 - charCount))

for i in userStorageInMb:
    charCount = len(str(i))
    if charCount <= 10:
        userStorageInMb_Space.append(" " * (10 - charCount) + str(i))
for i in userStroagePercent:
    charCount = len(str(i))
    if charCount <= 6:
        userStroagePercent_Space.append(" " * (6 - charCount) + str(i))

with open("relatorio.txt", "w") as writeRel:
    writeRel.write("ACME Inc.           Uso do espaço em disco pelos usuários\n")
    writeRel.write("---------------------------------------------------------\n")
    writeRel.write(("Nr.{}  Usuário        Espaço utilizado     % do uso\n").format(spaceAdd[countLine]))
    for i in lst:
        writeRel.write(
            ("{}{}    {}   {} MB      {}%\n").format(line[countLine], spaceAdd[countLine], userName[countLine],
                                                     userStorageInMb_Space[countLine],
                                                     userStroagePercent_Space[countLine]))
        countLine += 1
    else:
        writeRel.write(("\nEspaço total ocupado: {} MB\n").format(userTotalStorageInMb))
        writeRel.write(("Espaço médio ocupado: {} MB\n").format(userMedStorageInMb))