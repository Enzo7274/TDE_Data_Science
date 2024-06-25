# TDE - Data Science
Projeto desenvolvido por Enzo dos Anjos e João Matheus e submetido como TDE da disciplina de Data Science, ministrada por Prof. Me. Gledston Carneiro, no 5º semestre do curso de Análise e Desenvolvimento de Sistemas pela UNIFAN.

Neste repositório encontram-se os arquivos em python com o código elaborado para a realização do projeto.
Para executar os arquivos será necessário instalar as bibliotecas especificadas no item a seguir.

### Bibliotecas utilizadas
- numpy
- pandas
- scikit-learn

### Conteúdo do repositório
- **itch-analytics.csv:** uma fonte de dados em .csv (comma-separated values) que contém o análitico dos últimos 30 dias da plataforma virtual de vendas.
- **tcc_analiticas_panda.py:** uma aplicação CLI feita para visualizar e comparar as informações da tabela .csv.
- **tcc-ml-random-forest-mse.py:** uma aplicação CLI que emite o erro quadrático médio usando o algoritmo de floresta randômica.
- **tcc-model-comparison:** uma aplicação CLI que compara os diferentes algoritimos de machile learning e seus resultados possíveis.
- **tcc-model-tuning:** uma aplicação CLI que utiliza métodos de machine learning para aperfeiçoar o resultado do MSE (mean squared error).

## Modelo de Projeto: Análise e Previsão de Desempenho de Jogos Digitais em Plataforma Online
### Etapa 1: Descrição do Projeto
1. Objetivo do Projeto
  - Descrição: Este projeto busca comparar as estatísticas do desempenho de alguns jogos produzidos ao longo do semestre, enviados na plataforma online itch.io. 
  - Importância: Um dos projetos, Defiant Strife, foi projetado e desenvolvido como requisito para o artigo escrito para a disciplina de Trabalho de Conclusão de Curso do mesmo semestre. Neste artigo, foi escrita uma seção dedicada ao uso dessa plataforma para distribuição do jogo, e dados detalhes sobre o impacto da escolha para esse serviço online no projeto final. Portanto esse projeto de Data Science foi uma oportunidade de avaliar de que forma os pontos de vista trazidos no texto correlacionam com as informações disponíveis para nós, além de medir o desempenho em comparação com projetos feitos anteriormente.
2. Fontes de Dados
  - Dados do Analítico do itch.io: a página de usuário (dashboard) do site itch.io dispõe de várias informações úteis e estatísticas relacionadas com os projetos que nós já tenhamos enviado na plataforma. Essas informações serão suficientes para gerar uma amostra que virá a ser usada a seguir pelas aplicações em python. 
3. Métodos a Serem Utilizados
  - Floresta Aleatória: é um método bastante flexível que pode ser usado quando temos acesso a informações distintas que não necessáriamente precisam estar interligadas embora façam parte de um mesmo contexto.
  - Modelagem Preditiva: através de tentativas em sucessão, testando e comparando métodos e algoritmos diferentes, podemos obter a confirmação de um valor mais acurado de acordo com a quantidade de dados que dispomos e descartar discrepâncias que possam levar a conclusões precipitadas.
4. Impacto Esperado
  - Identificar como o que os números que são passados para nós, como desenvolvedores de software, pode ser correlacionado com o sucesso relativo pela aplicação em si.
  - Avaliar o impacto que jogos desenvolvidos de forma independente conseguem ter quando a publicação e divugação dos mesmoes também é feita pela mesma equipe, não dispondo de amplos recursos financeiros externos ᴏᴜ de marketing que possam influenciar no resultado.

### Etapa 2: Desenvolvimento do Projeto

  Para realização dessa tarefa, o primeiro passo é obter as informações. Apesar de ser a fonte das informações, o dashboard do itch.io não conta atualmente com uma funcionalidade nativa para o download desses dados, sendo necessário solicitar a equipe de suporte do site ou realizar a coleta manualmente. Porém através de uma aplicação já existente em python, foi possível extrair as informações presentes no dashboard no itch.io. Esses dados são processados em um arquivo .csv que pode posteriormente ser manipulado pelo pandas e pelo scikit-learn. O arquivo dispõe em uma tabela as seguintes informações: data, nome, número de vezes em que foram jogados, downloads, e visualizações.

  Inicializamos o projeto importando a biblioteca pandas para efetivar as operações de manipulação dos dados da planilha. Logo, checamos se existe o arquivo dos dados extraídos do website dentro do diretório do algoritmo, para assim podermos realizar uma varredura que informa quantas células estão preenchidas em cada coluna. A partir disso, fomos inserindo outras funções de organização de dados. Assim, concluímos o projeto inicial com um arquivo em python que é capaz de realizar as seguintes funcionalidades:
- Emitir as 5 primeiras linhas de cada coluna
- Emitir as 5 últimas linhas de cada coluna
- Emitir o tipo de dados de cada coluna
- Exibir o número de linhas e colunas dos dados
- Exibir a quantidade de células vazias em cada coluna
- Exibir a quantidade de valores únicos em cada coluna
- Obrter um relatório contendo estatísticas dos dados obtidos como média e valores mínimos e máximos encontrados
- Correlacionar as colunas
- Obter a soma final de todos os valores em cada coluna
- Obter a soma total dos valores categorizados por jogo
- Emitir as 5 primeiras e últimas linhas 
- Emitir o total de linhas e colunas dos dados
- Emitir a quantidade de células sem valores em cada coluna
- Emitir a quantidade de células com valores únicos em cada coluna

Cada uma dessas funções pode ser acessada através do arquivo **tcc_analiticas_panda.py** encontrado na raiz do repositório.]

Depois, buscamos usar as informações obtidas como parte do processo de machine learning. Para isso, foi feito uso intensivo da biblioteca scikit-learn, em três métodos diferentes.

No arquivo **tcc-ml-random-forest-mse.py**, conseguimos obter o resultado do erro quadrático médio através do algoritmo floresta randômica, que como explicado anteriormente, é ideal para fontes de dados como a utilizada neste projeto.
Depois, fomos atrás de testar as informações do relatório gerado pela aplicação de floresta randômica, com outros algoritmos de machine learning disponíveis em nosso alcance que façam sentido com a quantidade de dados e variaveis que possuímos. O resultado dessas comparações poderá ser obtido no arquivo **tcc-model-comparison.py**. Por fim, para garantir maior acurácia em nossos testes, implementamos uma variação do código anterior que procura automáticamente revisar o resultado do erro quadrático médio com outros métodos da biblioteca scikit-learn, e o código pode ser encontrado no arquivo **tcc-model-tuning**.

### Etapa 3: Relatório Final

vale destacar também a criação de uma segunda base de dados que extrai apenas os valores numéricos contidos da planilha para então simular uma média de flutuação de valor para cada coluna
ex: se na coluna de visualizações, a cada dia que passa a quantidade de visualização tende a aumentar ou diminuir 

para poder entregar um relatório compreensível que contabilize o total de visualizações, downloads e pesquisas do jogo nos últimos 31 dias (totalizando aproximadamente um mês inteiro), realizamos uma categorização da base de dados baseados por cada título de jogo, assim conseguimos contabilizar a quantidade de visualizações, downloads e demonstrações jogadas respectivamente
