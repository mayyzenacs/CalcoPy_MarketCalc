# CalcoPy MktCalc | Calculadora de Preços Comerciais

<div align="center">
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow)
![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=flat)
![pandas Badge](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=fff&style=flat)
![JSON Badge](https://img.shields.io/badge/JSON-000?logo=json&logoColor=fff&style=flat)
![Python Badge](https://img.shields.io/badge/Tkinter-3776AB?logo=python&logoColor=fff&style=flat)
</div>

<img width="1890" height="749" alt="calcopy_png" src="https://github.com/user-attachments/assets/27547a4a-4888-4f9c-9c4a-aed7239d9da6" />

## 🔎 O que é um preço comercial?  

Um _preço comercial_ é um valor atrativo para o cliente, geralmente arredondado ou psicológico, como _39,90_ ou _99,99_, que transmite a percepção de um preço menor.

Esse recurso é muito utilizado em marketplaces como o _Mercado Livre_ para precificação de produtos.

### Quando vemos um produto anunciado como "de 539 por 299", temos dois elementos estratégicos:

- Um **desconto comercial** aplicado para criar a percepção de vantagem.

- Um **preço comercial** (299), pensado para transmitir ao cliente a sensação de ser mais acessível.

A _CalcoPy_ automatiza esse processo: ela calcula automaticamente qual deve ser o **preço base ("de")** que, ao aplicar uma porcentagem de desconto, resulta exatamente no **preço final ("por")** desejado.

Assim, o vendedor garante uma oferta **atrativa e estratégica**, sem precisar calcular manualmente.

## ⚙ Como o programa funciona?  

### 🏷️ Cálculo de Preço Comercial  

O usuário define um valor desejado (ex.: 39,90) e escolhe uma porcentagem de desconto.

O programa calcula automaticamente _qual deve ser o preço base_ para que, ao aplicar o desconto no marketplace, o valor final exibido seja o desejado. O valor desejado (preço por) é o valor de venda/desconto para o cliente, o valor base (preço de) é o valor cortado que aparece para o cliente como valor anterior.

<img width="350" height="249" alt="precode" src="https://github.com/user-attachments/assets/b061c5e8-bdd6-46f6-b16b-414a1d9cc458" />

_Exemplo:_

- Valor desejado: 39,90

- Desconto: 10%

- O programa descobre qual valor _“de”_ resulta em 39,90 após o desconto → O valor "preço de" que deve ser cadastrado no martkeplace e descontado a porcentagem desejada de acordo com a interface do marketplace.

### 📦 Cálculo de Envio de Estoque (Full)  

O Mercado Livre oferece o sistema _Full_, onde vendedores enviam estoque para centros de distribuição a fim de agilizar entregas e aumentar as vendas.

Para evitar défict de produtos e perca de vendas, o programa calcula automaticamente _quantas unidades devem ser enviadas_, com base no número de vendas semanais e no período de cobertura desejado.

_Exemplo:_

- Vendas nos últimos 7 dias: 25 unidades

- Cobertura desejada: 6 semanas

- O programa calcula: 25 × 6 = 150 unidades

Resultado: Envio de 150 unidades para cobrir 6 semanas de estoque.

Assim, o vendedor mantém o estoque equilibrado e não perde vendas.

## 🖥 Como usar  

- Baixe o último executável da CalcoPy MktCalc nas releases.

⚠ Aviso: o programa não possui licença. O _Windows Defender_ pode detectar um falso positivo — adicione às exceções caso necessário. CalcoPy é totalmente segura e de código aberto.

<img width="474" height="477" alt="Screenshot_1" src="https://github.com/user-attachments/assets/79ca8bea-c59d-4195-88a7-13b1b06304ed" />

### Campos da Interface  

#### Preço Comercial

1. _Seleção de desconto_ – escolha a porcentagem aplicada no cálculo.

2. _Valor desejado_ – insira o valor que deseja exibir no marketplace (ex.: 39,90)

3. _Calcular_ – gera o valor base para cadastro.

4. _Resultado (valor de)_ – mostra qual preço deve ser inserido para chegar ao valor final.

5. _Copiar resultado_ – copia o valor do campo anterior.

6. _Valor com 3% OFF_ – calcula automaticamente um preço promocional adicional.

#### Cálculo Full

7. _Semanas de estoque_ – insira quantas semanas deseja cobrir.

8. _Vendas (últimos 7 dias)_ – insira o total vendido no período.

9. _Botão Full_ – calcula automaticamente o estoque necessário.

10. _Resultado Full_ – exibe quantas unidades devem ser enviadas.

#### Outras funções

11. _Limpar campos_ – reinicia os dados inseridos.

12. _Exportar histórico_ – salva todas as operações em um arquivo _Excel_.

## Dev Infos

### Como rodar o projeto  

1. Crie e ative um ambiente virtual:

```
python -m venv venv
```

```
source venv/bin/activate   # Linux/Mac
```

```
venv\Scripts\activate      # Windows
```

2. Instale as dependências:

```
pip install -r requirements.txt
```

3. Rode o programa:

```
python -m src.interface
```

O histórico de operaçoes (history.json) é salvo automaticamente em:

```
users\user_name\appData\local          # Windows

/home/user_name/.local/share           # Linux/Mac
```

## ⚠️ Possíveis Problemas  

### Falso positivo do Windows Defender

- Adicione a pasta do projeto ou o arquivo executável nas exceções do Windows defender.

### no module named 'pandas'

- Rode dentro de um ambiente virtual e instale diretamente o pandas com 'pip install pandas'

### no module named src

- Rode pelo terminal 'python -m src.interface'

---
