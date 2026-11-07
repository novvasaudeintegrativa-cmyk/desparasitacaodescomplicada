# Escopo — Landing page do Método Raízes - Desparasitação Descomplicada

Página de vendas de alta conversão, com VSL, que leva ao checkout na **Kiwify**. Base: o site desparasitacao-descomplicada.vercel.app, com o conteúdo reorganizado em ordem de persuasão. Arquivo: [index.html](index.html), um único arquivo, sem instalação.

## 1. Objetivo
Vender o curso (R$ 97) a quem chega por anúncio ou perfil, com uma página que educa, quebra objeções e leva ao botão de compra, **sem promessa de cura** (categoria sensível no Meta).

## 2. Visual
- **Verde e menta da Clínica Corpo Terra:** teal profundo #00454d, menta #00dcc0, verde #00716f, fundo claro #f1f8f7 e creme #fdeee3. Fonte Outfit.
- **Laranja só nos botões de compra** (#e0600a), para o olho ir direto à ação. A clínica não tem laranja próprio; este tom é escolha minha e é uma variável no topo do CSS (`--cta`).
- Mobile primeiro: botão fixo na parte de baixo do celular.

## 3. Estrutura da página (em ordem de persuasão)
| # | Bloco | Função |
| :--- | :--- | :--- |
| 1 | Topo com Roma + **VSL** + botão | Promessa clara e vídeo logo na primeira tela |
| 2 | Faixa de números | Prova rápida: 30 dias, 9 materiais, 20 anos |
| 3 | Identificação | "Você se reconhece?", em terceira pessoa, sem afirmar condição |
| 4 | O verdadeiro problema | Jeito comum x jeito organizado; a culpa não é dela |
| 5 | Método Raízes | 6 etapas da jornada de 30 dias |
| 6 | O que você recebe | 9 entregáveis |
| 7 | Quem conduz | Foto e credenciais do Luís |
| 8 | Para quem é / avaliação antes | Segurança e filtro do público |
| 9 | Depoimentos | **Modelos**, trocar por relatos reais autorizados |
| 10 | Quebra de objeções | 8 objeções, com empatia e resposta |
| 11 | Oferta | Preço, entregáveis, botão, selo de segurança |
| 12 | Garantia | Incondicional (7, 14 ou 30 dias) |
| 13 | FAQ | 10 perguntas |
| 14 | Chamada final + rodapé | Fechamento e aviso legal |

## 4. Integração com a Kiwify
No fim do arquivo há três variáveis para preencher:
- `CHECKOUT`: link da oferta na Kiwify. Todos os botões passam a levar ao checkout, e os UTMs da página são repassados.
- `VSL_EMBED`: link de incorporação do vídeo (YouTube, Vimeo, etc.). Sem ele, aparece o pôster com o botão de play.
- `GARANTIA_DIAS`: 7, 14 ou 30. O selo e os textos mudam sozinhos.

**Na Kiwify:** order bump com o Kit DI Raízes, upsell de 1 clique na página de obrigado, página de obrigado com o primeiro passo (anamnese) e e-mail de acesso.

## 5. Rastreamento
- Espaço reservado no `<head>` para o pixel da Meta e a tag do Google.
- O clique nos botões já dispara o evento `InitiateCheckout` quando o pixel existir.
- Padronizar UTMs em todos os links de anúncio.

## 6. O que preciso para publicar
| Item | Situação |
| :--- | :--- |
| Link do checkout da Kiwify | Pendente |
| Vídeo da VSL (roteiro já existe) | Pendente: gravar e hospedar |
| Foto do Luís (`landing/img/luis.jpg`) | Pendente; sem ela aparece "LM" |
| Depoimentos reais com autorização por escrito | Pendente; hoje são modelos marcados |
| Preço: **R$ 97 na página**, mas o site atual mostra R$ 87 | Confirmar e corrigir o site |
| Comprovação dos "20 anos" e das credenciais | Confirmar antes de publicar |
| Termos de uso, política de privacidade e contato | Pendente: criar e ligar os links do rodapé |
| Prazo da garantia | Definir (7, 14 ou 30 dias) |
| Formas de pagamento e parcelamento | Confirmar na Kiwify |
| Domínio | Pendente |

## 7. Regras de conformidade (Meta e saúde)
- Nada de "cura", "elimina", "trata", antes e depois ou diagnóstico.
- Nenhum texto afirma condição de saúde de quem lê.
- Aviso legal no rodapé e no corpo da página.
- **Sem urgência falsa:** não há contador nem "últimas vagas". Escassez só se for real.
- O número "0 promessa de cura" da faixa é intencional: reforça a confiança e protege o anúncio.
- A palavra "desparasitação" aparece só como nome do produto, não nas promessas.

## 8. Fora deste escopo
Gravação da VSL, produção de fotos, criação dos anúncios, configuração da conta Kiwify e o 2º lançamento (Ressurgir).
