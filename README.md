# Web Scrapper

Projeto desenvolvido em python, sobre tudo com Selenium, BeautifulSoup e Pandas é um web scrapper que puxa uma tabela com as principais empresas listadas na bolsa, no site fundamentus e após isso aplica uma série de filtros que são úteis no mundo dos investimentos. 

## Componentes
Esse projeto é dividido em 4 partes básicas, sendo elas:
- main_scrapper.py
- filter_data.py
- advanced_scrapper.py
- utils.py

### main_scrapper
Esse código é responsável por pegar os principais dados das empresas listadas na bolsa disponíveis no site fundamentus. Esse dados são transformados em um Data Frame pandas e depois disso ele salva em um arquivo Excel, chamado output.xlsx na pasta excel tables

### filter_data
Essa parte do código é responsável por aplicar alguns filtros no output gerado. Removendo empresas com baixa liquides, empresas com Mrg. Ebit negativa e empresas do ramo financeiro, como seguradoras, bancos, etc. Após isso ele ordena por Ev/Ebit. 
Uma vez que os dados saíram desse filtro, eles já podem ser consultados para saber quais empresas podem ser investidas , levando em consideração as 30 primeiras

(Lembrando que isso foi por meio de algumas pesquisas e eu não posso dizer que você terá lucro nisso, reforçando que a intenção aqui é mostrar o código em python e não uma maneira de ganhar dinheiro)

### advanced_scrapper
Essa parte aqui é avançada não por ser código complexos, mas a meu ver foi mais chata de fazer, além de que é a parte do código que mais demora. Nele, eu pego todos os papeis das ações e faço consultas individualizadas para buscar o valor atual ação, lpa e vpa. Após isso, eu uso a fórmula de Ben Graham para calcular o valor intrínseco da empresa (Eu zero as que estiverem com LPA ou VPA negativo, pois preciso calcular uma raíz quadrada). Uma vez que o loop foi finalizado, eu vou gerar um novo data frame apenas com as informações de LPA, VPA, VAlUE e VALUATION (valor intriseco) e gero uma saída em um novo arquivo excel

## Para rodar
É necessários os seguintes elementos:
- Python
- Pandas
- Selenium
- bs4
- chrome driver (o ques tá presente no pacote é para versão especifica do navegador que uso, mas pode baixar a vesão compatível com seu navegador no seguinte link: [Chrome Driver](https://chromedriver.chromium.org/downloads)) 

```
mkdir resultados; cd webscrapper; chmod +x *; ./main_scrapper.py 
```

## Considerações Finais
para testar o programa por completo, pode ser que demore bastante pois o advanced scrapper consome muito tempo para buscar todas informações, caso queira ver ele rodando por completo. Sugiro que após executar o primeiro arquivo, você abra o output.xlsx e deixe apenas umas 10-20 linhas que ele executará o programa por completo mais rápido, além disso, após finalizado cada programa, ele vai automaticamente chamar o próximo do fluxo, então tem que ter um pouquinho de atenção.

Toda susgestão é bem vinda, pois é meu primeiro projeto nessa área então não entendo muito das boas práticas ou algo que possa melhorar, etc
