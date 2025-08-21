# 📊 CalcoPy MktCalc  

  

<img width="1890" height="749" alt="calcopy_png" src="https://github.com/user-attachments/assets/27547a4a-4888-4f9c-9c4a-aed7239d9da6" />

  

## 🔎 O que é um preço comercial?  

Um *preço comercial* é um valor atrativo para o cliente, geralmente arredondado ou psicológico, como *39,90* ou *99,99*, que transmite a percepção de um preço menor.  

Esse recurso é muito utilizado em marketplaces como o *Mercado Livre* para precificação de produtos.

  

### 🏷️ Quando vemos um produto anunciado como "de 539 por 299", temos dois elementos estratégicos:

- Um **desconto comercial** aplicado para criar a percepção de vantagem.  

- Um **preço comercial** (299), pensado para transmitir ao cliente a sensação de ser mais acessível.  

  

A *CalcoPy* automatiza esse processo: ela calcula automaticamente qual deve ser o **preço base ("de")** que, ao aplicar uma porcentagem de desconto, resulta exatamente no **preço final ("por")** desejado.  

Assim, o vendedor garante uma oferta **atrativa e estratégica**, sem precisar calcular manualmente.

  

---

  

## ⚙ Como o programa funciona?  

  

### 🟡 Cálculo de Preço Comercial  

O usuário define um valor desejado (ex.: 39,90) e escolhe uma porcentagem de desconto.  

O programa calcula automaticamente *qual deve ser o preço base* para que, ao aplicar o desconto no marketplace, o valor final exibido seja o desejado. O valor desejado (preço por) é o valor de venda/desconto para o cliente, o valor base (preço de) é o valor cortado que aparece para o cliente como valor anterior.

  

<img width="350" height="249" alt="precode" src="https://github.com/user-attachments/assets/b061c5e8-bdd6-46f6-b16b-414a1d9cc458" />

  
  

📌 *Exemplo:*  

- Valor desejado: 39,90  

- Desconto: 10%  

- O programa descobre qual valor *“de”* resulta em 39,90 após o desconto → O valor "preço de" que deve ser cadastrado no martkeplace e descontado a porcentagem desejada de acordo com a interface do marketplace.

  

---

  

### 📦 Cálculo de Envio de Estoque (Full)  

O Mercado Livre oferece o sistema *Full*, onde vendedores enviam estoque para centros de distribuição a fim de agilizar entregas e aumentar as vendas.

Para evitar défict de produtos e perca de vendas, o programa calcula automaticamente *quantas unidades devem ser enviadas*, com base no número de vendas semanais e no período de cobertura desejado.  

  

📌 *Exemplo:*  

- Vendas nos últimos 7 dias: 25 unidades  

- Cobertura desejada: 6 semanas  

- O programa calcula: 25 × 6 = 150 unidades

Resultado: Envio de 150 unidades para cobrir 6 semanas de estoque.

  

Assim, o vendedor mantém o estoque equilibrado e não perde vendas.  

  

---

  

## 🖥 Como usar  

- Baixe o último executável da CalcoPy MktCalc nas releases.

⚠ Aviso: o programa não possui licença. O *Windows Defender* pode detectar um falso positivo — adicione às exceções caso necessário. CalcoPy é totalmente segura e de código aberto.

  

<img width="474" height="477" alt="Screenshot_1" src="https://github.com/user-attachments/assets/79ca8bea-c59d-4195-88a7-13b1b06304ed" />

  

### 🧾 Campos da Interface  

  

#### Preço Comercial

1. *Seleção de desconto* – escolha a porcentagem aplicada no cálculo.  

2. *Valor desejado* – insira o valor que deseja exibir no marketplace (ex.: 39,90)

3. *Calcular* – gera o valor base para cadastro.

4. *Resultado (valor de)* – mostra qual preço deve ser inserido para chegar ao valor final.  

5. *Copiar resultado* – copia o valor do campo anterior.  

6. *Valor com 3% OFF* – calcula automaticamente um preço promocional adicional.  

#### Cálculo Full

7. *Semanas de estoque* – insira quantas semanas deseja cobrir.  

8. *Vendas (últimos 7 dias)* – insira o total vendido no período.  

9. *Botão Full* – calcula automaticamente o estoque necessário.  

10. *Resultado Full* – exibe quantas unidades devem ser enviadas.  

#### Outras funções

11. *Limpar campos* – reinicia os dados inseridos.  

12. *Exportar histórico* – salva todas as operações em um arquivo *Excel*.  

  

---

  

✨ *Resumo:*  

O *CalcoPy MktCalc* é uma ferramenta prática para vendedores de marketplaces, ajudando na *precificação estratégica* e no *planejamento de estoque* de forma rápida e automatizada.

  

## Dev Infos

  

### 🔧 Como rodar o projeto  

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
python -m source.window
```

O histórico de operaçoes (history.json) é salvo automaticamente em:

```
users\user_name\appData\local
```


## ⚠️ Possíveis Problemas  

  

### Falso positivo do Windows Defender 

- Adicione a pasta do projeto ou o arquivo executável nas exceções do Windows defender.

  

### no module named pandas

- Rode dentro de um ambiente virtual e instale diretamente o pandas com ´pip install pandas´

  

### no module named source

- Rode pelo terminal ´python -m source.window´

