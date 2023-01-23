# Proojeto_web_craping_v2

Esta é a Segunda versão do projeto de web scraping do site Mercado Livre

# Afinal de contas, o que é e qual a finalidade de se fazer web scraping:

Web scraping é uma habilidade valiosa para quem trabalha com dados, pois permite coletar dados de fontes na internet que não estão facilmente disponíveis. Isso inclui sites de comércio eletrônico, redes sociais, notícias e outras fontes de dados não estruturadas. Além disso, as técnicas de web scraping também podem ser usadas para automatizar a coleta de dados de fontes que são atualizadas frequentemente, como preços de produtos ou notícias.

Com essa capacidade de coletar e processar esses dados, podemos identificar tendências, fazer previsões e tomar decisões baseadas em dados mais recentes e precisos. Isso é especialmente importante em um mundo cada vez mais conectado, onde a quantidade de informações disponíveis é cada vez maior. A habilidade de extrair essas informações de forma eficiente e precisa é crucial para a tomada de decisões informadas. Portanto, é omportante para o analista de dados estar familiarizado com a técnica de web scraping para aproveitar ao máximo as informações disponíveis.

# Explicando o código 
Para este exemplo usamos o termo de pesquisa 'Bicicleta", no arquivomain.py definimos um link da pesquisa, em seguida é solcitado qual produto desejamos pesquisar. A estrutura dentro site Mecado livre
é padrão, por isso cosneguimos pesquisar ppor uma infinidade de produtos, em seguida é solicitado o número de paginas a ser pesquisada
por via de regra, o site apresenta até 40 paginas,porém caso a pessoa queira pesquisar por menos, também é possível.

Após digitar o número de paginas, o programa irá percorrer cada pagina do site em busca das seguintes informações: nome do produto, link do produto, preço do produto e se possui frete gratis ou não, irá fazer isso para uma pagina em seguida com a próxima, fará isso de acordo com o número de paginas definido no inicio da pesquisa, deixamos o tempo de um segundo entre uma pesquisa e outra pra não corrermos o risco de sermos bloqueados. após realizar a pesquisa, deixamos duas opções, ou a pesquisa é apresentado na tela ou salvo em um arquivo do Excel, basta comentar ou descomentar a ultima e penultimas linhas deste código.

# Análise dados

Agora temos a parte de análise dos dados, geramos um notebook, onde analisamos os dados coletados, porém antes da análise tivemos que tratar a variavel preço do produto, pois a mesma estava sendo tratada como um objeto enquanto deveria se comportar como valor. Segumos dentro do nosso notebook da seguinte maneira:

 -> *importamos os dados*

 -> *Verificamos nosso DataFrame, quais os tipos de dados estamos trabalhaando*

 -> *Tratamento dos dados tranformando a ##variavel### "preço do produto" do tipo object para tipo float*

  -> *mostramos qual produto foi o mais recorrente dentro do nosso conjunto de dados*

 -> *Ordemanos os dez produtos de maior vaalor dentro do nosso conjunto de dados*

 -> *Ordenamos os dez valores de menor valor dentro do nosso conjunto de dados*

 -> *Por ultimo estamos verificando quantos produtos possuem frete gratis ou não, dentro do nosso conjunto de dados*
 
### Resultado da análise pode ser visto acessando o arquivo "analise_dados_coletatos.ipynb"

