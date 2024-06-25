# TDE - Data Science
Projeto desenvolvido por Enzo dos Anjos e João Matheus e submetido como TDE da disciplina de Data Science, ministrada por Prof. Me. Gledston Carneiro, no 5º semestre do curso de Análise e Desenvolvimento de Sistemas pela UNIFAN.

Neste repositório encontram-se os arquivos em python com o código elaborado para a realização do projeto.

## Bibliotecas utilizadas
- numpy
- pandas
- scikit-learn

## Modelo de Projeto: Análise e Previsão de Desempenho de Jogos Digitais em Plataforma Online
### Etapa 1: Descrição do Projeto
1. Objetivo do Projeto
  - Descrição
  - Importância
2. Fontes de Dados
  -
  -
3. Métodos a Serem Utilizados
  -
  -
4. Impacto Esperado
  -
  -

### Etapa 2: Projeto
inicializamos o projeto importando a biblioteca pandas para efetivar as operações de manipulação dos dados da planilha

logo, checamos se existe o arquivo dos dados extraídos do website dentro do diretório do algoritmo, para assim podermos realizar uma varredura que informa quantas células estão preenchidas em cada coluna
A partir disso, fomos inserindo outras funções de organização de dados
dentre elas estão
emitir as 5 primeiras e últimas linhas de cada coluna
emitir o total de linhas e colunas dos dados
emitir a quantidade de células sem valores em cada coluna
emitir a quantidade de células com valores únicos em cada coluna
emitir um relatório contendo estatísticas dos dados obtidos como média e valores mínimos e máximos encontrados

vale destacar também a criação de uma segunda base de dados que extrai apenas os valores numéricos contidos da planilha para então simular uma média de flutuação de valor para cada coluna
ex: se na coluna de visualizações, a cada dia que passa a quantidade de visualização tende a aumentar ou diminuir 

para poder entregar um relatório compreensível que contabilize o total de visualizações, downloads e pesquisas do jogo nos últimos 31 dias (totalizando aproximadamente um mês inteiro), realizamos uma categorização da base de dados baseados por cada título de jogo, assim conseguimos contabilizar a quantidade de visualizações, downloads e demonstrações jogadas respectivamente
