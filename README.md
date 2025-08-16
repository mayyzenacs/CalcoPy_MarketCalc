# 📊 CalcoPy MktCalc  

![Interface](https://i.imgur.com/6Oi0NvX.png)

## 🔎 O que é um preço comercial?  
Um **preço comercial** é um valor atrativo para o cliente, geralmente arredondado ou psicológico, como **39,90** ou **99,99**, que transmite a percepção de um preço menor.  
Esse recurso é muito utilizado em marketplaces como o **Mercado Livre**.  

---

## ⚙️ Como o programa funciona?  

### 🟡 Cálculo de Preço Comercial  
O **CalcoPy MktCalc** facilita a criação de preços comerciais para marketplaces, inspirado na precificação do **Mercado Livre**.  
O usuário define um valor desejado (ex.: `39,90`) e escolhe uma porcentagem de desconto.  
O programa calcula automaticamente **qual deve ser o preço base** para que, ao aplicar o desconto no marketplace, o valor final exibido seja o desejado.  

📌 **Exemplo:**  
- Valor desejado: `39,90`  
- Desconto: `10%`  
- O programa descobre qual valor **“de”** resulta em `39,90` após o desconto → esse é o valor que você deve cadastrar no marketplace.  

---

### 📦 Cálculo de Envio de Estoque (Full)  
O Mercado Livre oferece o sistema **Full**, onde vendedores enviam estoque para centros de distribuição a fim de agilizar entregas.  
Para evitar falta de produtos, o programa calcula automaticamente **quantas unidades devem ser enviadas**, com base no número de vendas semanais e no período de cobertura desejado.  

📌 **Exemplo:**  
- Vendas nos últimos 7 dias: `25 unidades`  
- Cobertura desejada: `6 semanas`  
- O programa calcula: `25 × 6 = 150 unidades`  

Assim, o vendedor mantém o estoque equilibrado e não perde vendas.  

---

## 🖥️ Como usar  

⚠️ *Aviso*: o programa não possui licença. O **Windows Defender** pode detectar um falso positivo — adicione às exceções caso necessário.  

![Exemplo de Interface](https://i.imgur.com/HXlPNAN.png)

### 🧾 Campos da Interface  

1. **Seleção de desconto** – escolha a porcentagem aplicada no cálculo.  
2. **Valor desejado** – insira o valor que deseja exibir no marketplace (ex.: `39,90`).  
3. **Calcular** – gera o valor base para cadastro.  
4. **Resultado (valor de)** – mostra qual preço deve ser inserido para chegar ao valor final.  
5. **Copiar resultado** – copia o valor do campo anterior.  
6. **Valor com 3% OFF** – calcula automaticamente um preço promocional adicional.  
7. **Semanas de estoque** – insira quantas semanas deseja cobrir.  
8. **Vendas (últimos 7 dias)** – insira o total vendido no período.  
9. **Botão Full** – calcula automaticamente o estoque necessário.  
10. **Resultado Full** – exibe quantas unidades devem ser enviadas.  
11. **Limpar campos** – reinicia os dados inseridos.  
12. **Exportar histórico** – salva todas as operações em um arquivo **Excel**.  

---

✨ **Resumo:**  
O **CalcoPy MktCalc** é uma ferramenta prática para vendedores de marketplaces, ajudando na **precificação estratégica** e no **planejamento de estoque** de forma rápida e automatizada.  
