# Arquitetura Integrada de Funil de Vendas: Saúde Integrativa
**Estrutura Multi-Ticket: Infoproduto Front-End ➔ Produto Físico (Order Bump/Upsell) ➔ Mentoria High Ticket**

---

## 1. Visão Geral da Estratégia

O ecossistema é baseado no modelo de **Funil de Múltiplos Níveis de Ticket (LTV Maximization)**. O objetivo principal é utilizar um produto digital de entrada para cobrir os custos de aquisição de tráfego (CAC Zero ou Positivo), monetizar imediatamente com a conveniência do produto físico próprio e qualificar os clientes de maior valor para o programa de alto ticket.

### Os Três Pilares do Ecossistema:

1. **Front-End / Low Ticket (`Desparasitação Descomplicada`):**
   * **Objetivo:** Aquisição massiva de novos clientes com baixíssima barreira de entrada.
   * **Promessa:** Método claro, seguro e didático de limpeza intestinal e desparasitação natural.
   * **Formato:** Infoproduto (Curso/E-book na Kiwify).
2. **Cross-Sell de Conveniência / Produto Físico (`Kit Desparasitação DI Raízes`):**
   * **Objetivo:** Elevar o Ticket Médio (AOV) no checkout e gerar resultado rápido/prático ao aluno.
   * **Posicionamento:** Não é um "item obrigatório para o curso funcionar", mas sim o **atalho de conveniência** com a pureza, dosagem e praticidade das ervas e tinturas padronizadas pelo próprio profissional.
   * **Formato:** Produto Físico enviado para a casa do aluno.
3. **Back-End / High Ticket (`Ressurgir`):**
   * **Objetivo:** Maximizar a margem de lucro (LTV) oferecendo acompanhamento profundo e individualizado.
   * **Público-Alvo:** Alunos do Low Ticket com sintomas crônicos, dores profundas ou que buscam acompanhamento especializado contínuo.
   * **Formato:** Mentoria, programa de saúde integrativa ou acompanhamento individual/em grupo.

---

## 2. Desenho do Fluxo de Conversão (User Journey)

```text
[ Tráfego Pago: Meta Ads & Google Ads ]
                  │
                  ▼
[ Página de Vendas (LP): Desparasitação Descomplicada ]
                  │
          ( Checkout Kiwify )
                  │
      ┌───────────┴───────────┐
      │ (Order Bump)          │ (Compra Básica)
      ▼                       ▼
[ Kit Físico DI Raízes ]     [ Acesso ao Curso Digital ]
      │                       │
      └───────────┬───────────┘
                  │
   ( Página de Obrigado / Upsell 1-Click )
                  │
                  ▼
   [ Formulário de Onboarding / Pesquisa de Saúde ]
                  │
   ┌──────────────┴──────────────┐
   │ (Lead Padrão)               │ (Lead Qualificado / Sintomas Crônicos)
   ▼                             ▼
[ Consumo do Curso ]         [ Tag: High Ticket Potential ]
                                 │
                                 ▼
                     [ Automação CRM (WhatsApp/Email) ]
                                 │
                                 ▼
                     [ Convite: Aula / Sessão Estratégica ]
                                 │
                                 ▼
                     [ Oferta High Ticket: Ressurgir ]
```

---

## 3. Matriz de Posicionamento e Quebra de Objeções

| Produto | Função Principal | Ângulo de Venda (Copy) | Prevenção da sensação de "Produto Incompleto" |
| :--- | :--- | :--- | :--- |
| **Desparasitação Descomplicada** | Conhecimento & Autonomia | "Aprenda a fórmula, os protocolos e como desparasitar seu corpo com segurança." | O curso entrega 100% da lista de ingredientes e ensinará a comprar em qualquer farmácia de manipulação. |
| **Kit DI Raízes** | Praticidade & Garantia de Qualidade | "Economize tempo, evite manipular errado e receba os insumos com a exata pureza recomendada." | Apresentado como *Fast-Track* (conveniência), e não como item bloqueador da execução do método. |
| **Ressurgir** | Acompanhamento & Transformação Profunda | "Para quem tem sintomas crônicos persistentes e precisa de um acompanhamento integrativo guiado." | Posicionado para o próximo nível de saúde, após o protocolo inicial de limpeza ter sido feito. |

---

## 4. Estrutura de KPIs e Métricas para o Dashboard de Marketing

O dashboard gerencial a ser desenvolvido pelo Claude deve consolidar os dados das plataformas (Kiwify, Meta Ads, CRM/WhatsApp) em 4 blocos operacionais:

### Bloco 1: Tráfego & Aquisição (Front-End)
* **Ad Spend:** Investimento total em tráfego pago.
* **Cost Per Click (CPC) & CPM:** Custos de atração.
* **Checkout Rate:** % de visitantes da LP que vão para o checkout.
* **Conversion Rate (LP):** Vendas do Low Ticket / Visitantes Únicos.
* **CPA Front-End:** Custo por aquisição de cada aluno do curso digital.

### Bloco 2: Monetização Imediata (Order Bump & Upsell Físico)
* **Take Rate do Order Bump (%):** % de compradores que marcam a caixa do Kit no checkout.
* **Take Rate do Upsell (%):** % de compradores que aceitam a oferta do Kit na página de obrigado.
* **Average Order Value (AOV):** Faturamento Total do Checkout / Vendas Totais do Curso.
* **ROAS Imediato (Front-End):** Faturamento do Curso + Kit / Investimento em Anúncios.
* *Meta Estratégica:* ROAS ≥ 1.0 (O Front-End financia totalmente a aquisição de clientes).

### Bloco 3: Qualificação & Meio do Funil
* **Taxa de Resposta ao Onboarding (%):** Alunos que preenchem a anamnese inicial na área de membros.
* **Volume de Leads Tier A (Qualificados):** Alunos com alto interesse/necessidade de mentoria.
* **Engajamento nas Automações:** Taxa de abertura de e-mails e respostas no WhatsApp.

### Bloco 4: Performance de Vendas (High Ticket)
* **Aplicações / Agendamentos:** Leads que solicitaram atendimento para o *Ressurgir*.
* **Taxa de Conversão High Ticket (%):** Vendas do Ressurgir / Aplicações.
* **Lifetime Value (LTV):** Receita total média gerada por um cliente somando todas as etapas (Curso + Kit + Mentoria).
* **Lucro Líquido Consolidado:** Margem final da operação.

---

## 5. Prompt Prontinho para Enviar ao Claude (Dashboard Builder)

> *"Claude, preciso que você construa o código de um **Dashboard Interativo em React com Tailwind CSS e Lucide Icons** para acompanhar uma operação de Marketing e Vendas de Saúde Integrativa baseada em um Funil de 3 Etapas:*
>
> 1. **Low Ticket Digital:** Desparasitação Descomplicada (Curso).
> 2. **Cross-Sell Físico:** Kit Desparasitação DI Raízes (Order Bump/Upsell).
> 3. **High Ticket Back-End:** Ressurgir (Mentoria de Alto Valor).
>
> **O Dashboard deve conter:**
> - **Filtros por Período:** Hoje, 7 dias, 30 dias.
> - **Cards de KPIs Principais:** Investimento em Ads, Faturamento Total, ROAS Consolidado, AOV (Ticket Médio), LTV e CPA.
> - **Gráfico de Retudo/Funil de Conversão:** Visualização da taxa de conversão passo a passo (Tráfego ➔ Compra Curso ➔ Adição Kit Físico ➔ Resposta Onboarding ➔ Venda High Ticket).
> - **Painel de Monetização (Front-End vs. Back-End):** Comparativo visual da receita gerada pelo Curso, pelo Kit Físico e pela Mentoria Ressurgir.
> - **Tabela de Acompanhamento das Campanhas:** Lista com métricas simuladas por canal (Meta Ads, Google Ads, E-mail, WhatsApp).
>
> Crie uma interface limpa, moderna, responsiva e com dados fictícios bem coerentes para que a visualização pareça um sistema SaaS de alta performance."*