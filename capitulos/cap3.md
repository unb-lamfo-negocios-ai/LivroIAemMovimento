# Capítulo 3 – Estratégias de Construção e Operação

Criar uma solução de Inteligência Artificial vai muito além de treinar modelos.  
É preciso pensar em **estratégia, operação, custos, governança e sustentabilidade do produto**.  
Neste capítulo, discutiremos como avaliar diferentes caminhos, modelos de negócio e abordagens operacionais ao desenvolver soluções de IA.  

---

## Build vs. Buy — Modelo Pronto ou Desenvolvido

Um dos primeiros dilemas estratégicos é decidir entre **desenvolver internamente (build)** ou **adotar soluções prontas (buy)**:  

- **Build (desenvolver internamente)**  
  - Maior controle sobre o produto, incluindo dados, algoritmos e personalizações.  
  - Possibilidade de criar **vantagem competitiva sustentável**, difícil de replicar por concorrentes.  
  - Exige **investimento elevado em infraestrutura** e **formação de equipe técnica especializada**.  

- **Buy (usar soluções prontas, como APIs e serviços de nuvem)**  
  - Reduz tempo de entrada no mercado (*time-to-market*).  
  - Menor custo inicial, já que a infraestrutura é terceirizada.  
  - Cria **dependência de fornecedores externos**, o que pode impactar custos e flexibilidade a longo prazo {cite}`choudhury2023`.  

Na prática, muitas organizações adotam um **modelo híbrido**, combinando APIs externas para funcionalidades padrão (ex.: tradução, OCR) e desenvolvimento interno para os diferenciais estratégicos.  

:::{note}
Um banco pode comprar um serviço de reconhecimento facial via API (buy), mas desenvolver internamente um motor de decisão de crédito com base em seu histórico exclusivo de clientes (build).  
:::

-----FELIPE ------
## Build vs. Buy - modelo pronto ou desenvolvimento interno?

- No caminho para criar um negócio com Inteligência Artificial, uma das primeiras e mais importantes decisões estratégicas é definir se a empresa irá desenvolver uma tecnologia própria (build) ou se irá utilizar uma solução já existente no mercado (buy). Essa escolha impacta diretamente o orçamento, o tempo de lançamento do produto e, principalmente, onde residirá o diferencial competitivo. Não se trata de uma decisão puramente técnica, mas fundamentalmente de uma decisão de negócio.
- A abordagem "Buy": usando um modelo pronto
     
    Optar por “comprar” significa utilizar a tecnologia de ponta desenvolvida por grandes provedores (como os modelos GPT da OpenAI, Claude da Anthropic e Gemini do Google via API) ou empregar modelos de código aberto (open-source) já treinados, como os da família Llama (Meta) ou Mixtral (Mistral AI). 
    
    A grande vantagem dessa abordagem é a velocidade de implementação e o acesso a um poder computacional de ponta sem o investimento inicial em Pesquisa & Desenvolvimento. O problema central reside no risco de lock-in (dependência de um fornecedor) e na dificuldade de criar um diferencial tecnológico profundo, visto que concorrentes podem acessar a mesma tecnologia.
- A abordagem "Build": desenvolvendo um modelo proprietário
    
    
    “Construir” não se limita a criar um modelo do zero, um processo extremamente raro e custoso. Na prática atual, a abordagem "Build" manifesta-se principalmente através do ajuste fino (fine-tuning) de modelos open-source de alta performance com dados proprietários da empresa. Os motivadores para essa decisão são variados e estratégicos.
    
    - Motivadores Estratégicos para a Abordagem "Build":
        - Hiper-especialização e Vantagem Competitiva: Um modelo genérico, por mais poderoso que seja, não supera um modelo menor e mais ágil treinado exaustivamente para uma única tarefa. É o caso do Harvey AI, que ajustou modelos da família GPT para se tornar um especialista em análise de documentos jurídicos, criando uma vantagem competitiva sustentável em seu nicho.
        - Soberania de Dados, Segurança e Conformidade: Para setores como o financeiro, saúde ou governamental, enviar dados de clientes para uma API de terceiros pode ser inviável por razões regulatórias (LGPD/GDPR) e de segurança. A solução é uma abordagem "Build". Um exemplo recente é a iniciativa do governo francês, que [em 2024 anunciou a  criação da agência AMIAD, de infraestrutura classificada para IA de defesa para desenvolver modelos de IA soberanos,](https://www.defense.gouv.fr/actualites/sebastien-lecornu-lance-strategie-ministerielle-lintelligence-artificielle) assim como criação de [ferramentas destinadas ao serviço público no gera](https://www.info.gouv.fr/actualite/ia-simplification-et-debureaucratisation-pour-transformer-letat?utm_source=chatgpt.com)l, garantindo que dados sensíveis permaneçam em infraestrutura controlada.
        - Otimização de Custo e Latência em Escala: Utilizar uma API de ponta tem um custo variável que pode aumentar expressivamente com o volume de uso. Empresas como a DoorDash publicaram estudos em 2024 mostrando como desenvolveram seus próprios modelos para tarefas específicas, como [a estimativa de tempo de entrega](https://careersatdoordash.com/blog/deep-learning-for-smarter-eta-predictions/?utm_source=chatgpt.com). O modelo customizado, embora menos versátil que um GPT-4o, é drasticamente mais rápido e mais econômico para sua única e repetitiva função.
- A Questão da Propriedade Intelectual e das Licenças
    - É crucial entender que ao fazer o fine-tuning de um modelo open-source como o Llama 3, a empresa não se torna dona do modelo base. A propriedade intelectual, e o verdadeiro ativo, reside nos "pesos" – a camada matemática de conhecimento resultante do ajuste fino – e, principalmente, no conjunto de dados proprietário utilizado para o treinamento. A licença do modelo original ainda se aplica, mas a especialização que torna o modelo único pertence à empresa.
    - Adicionalmente, é vital para a estratégia de negócio analisar o tipo de licença do modelo open-source. Nem todo "código aberto" é igual. As licenças podem ser divididas em duas categorias principais, com implicações diretas no uso comercial:
        - Licenças Permissivas (ex: Apache 2.0, MIT): Estas licenças oferecem máxima flexibilidade. Elas permitem que uma empresa modifique, distribua e comercialize o modelo e seus derivados com pouquíssimas restrições. A Mistral AI, por exemplo, estrategicamente lança seus modelos sob a licença Apache 2.0, incentivando a adoção comercial irrestrita para competir com modelos de código fechado.
        - Licenças Customizadas com Restrições (ex: Llama 3 License): Grandes empresas como a Meta criam suas próprias licenças. A licença do Llama 3, por exemplo, embora permita uso comercial, impõe uma "Política de Uso Aceitável" que proíbe a utilização do modelo para fins ilegais ou antiéticos. Mais importante, a licença estipula que empresas com mais de 700 milhões de usuários ativos mensais no momento do lançamento do modelo precisam solicitar uma licença especial da Meta. Isso efetivamente permite que startups e empresas de médio porte o utilizem livremente, mas impede que concorrentes diretos de escala global o usem sem um acordo específico.
    - Portanto, a análise jurídica da licença de um modelo não é um mero detalhe técnico, mas um passo mandatório que pode definir a viabilidade e a escalabilidade de um produto construído sobre essa tecnologia.
- A Decisão Estratégica Final
A escolha entre "Build" e "Buy" não deve ser vista como uma questão binária, mas como um espectro de opções. A pergunta estratégica central a ser feita é: A funcionalidade de IA precisa ser uma fonte de diferenciação defensável para o negócio?
    
    Mesmo que a IA não seja o produto principal, ela pode ser um componente crítico para o sucesso. O sistema de recomendação da Netflix ou do Spotify não é o produto em si (que é o acesso ao conteúdo), mas é uma funcionalidade tão determinante para a experiência e retenção dos usuários que exigiu uma abordagem "Build" para sua criação. Isso permitiu que ambas as empresas estabelecessem uma vantagem de mercado significativa.
    
    Portanto, a decisão se alinha a um espectro: começa com o uso de uma API pronta (Buy), avança para o ajuste fino de um modelo open-source (um híbrido de Buy+Build) e pode chegar à construção de um modelo customizado (Build puro). A escolha correta depende de onde a empresa precisa, estrategicamente, ser não apenas boa, mas excepcionalmente única.
  
---

## Estruturas de Precificação para IA

Definir o preço de soluções baseadas em IA é um desafio porque envolve **custos variáveis e infraestrutura intensiva**. Alguns modelos comuns incluem:  

- **Preço por uso** (*pay-per-use*): clientes pagam proporcionalmente ao consumo, típico em APIs de IA generativa.  
- **Assinaturas mensais ou anuais**: acesso recorrente a funcionalidades, modelo muito usado em SaaS.  
- **Licenciamento corporativo**: contratos personalizados para grandes organizações que exigem escala, integração e suporte dedicado.  

A precificação deve equilibrar **custo operacional (treinamento de modelos, armazenamento, servidores, equipe)** e **valor percebido pelo cliente**.  

Exemplo: uma API de transcrição de áudio pode cobrar por minuto processado, enquanto uma plataforma de análise de documentos pode usar planos por número de usuários ativos.  

---
---FELIPE---INICIO-----------------
- No modelo “pay-as-you-go” via API, empresas como OpenAI, Anthropic e Google disponibilizam diversos endpoints de inferência, cada um oferecendo um conjunto de modelos (por exemplo, GPT-4o, o3, Claude 3.5, Claude 4, Gemini 2.5, etc.) com razões custo-benefício diferentes. Você é cobrado por unidade de consumo (geralmente por milhão de tokens de entrada e saída), o que possibilita:
    - Escalabilidade imediata: basta chamar a API, sem se preocupar em gerenciar servidores ou clusters de GPU.
    - Flexibilidade de escolha: selecione o modelo mais barato para tarefas simples (como Gemini 2.0 Flash) ou um mais caro e preciso (como Gemini 2.5 Pro) conforme a necessidade de qualidade e latência.
- Existem dois problemas centrais desse modelo:
    - Oscilação de custos: Se seu tráfego varia muito, a fatura pode subir de forma imprevisível no mês em que há picos de uso. Modelos maiores (mais parâmetros) custam várias vezes mais por token. Por exemplo, imagine que você oferece uma ferramenta SaaS que resume documentos, e sua assinatura custa $20/mês. Um "cliente casual" resume 10 artigos curtos, consumindo um total de 50.000 tokens no mês, o que gera um custo de API para você de apenas $0.15. Já um "cliente intensivo" resume 30 relatórios longos, consumindo 3.000.000 de tokens, o que gera um custo de $9.00. Se no mês seguinte esse cliente intensivo dobrar o uso, seu custo direto com ele sobe para $18, eliminando quase toda a sua margem de lucro.
    - Lock-in ao provedor:
        - Endpoints e bibliotecas proprietárias: seu código faz chamadas específicas (URLs, formatos de requisição e autenticação) que não são idênticas entre OpenAI, Anthropic ou Vertex AI. Migrar exige refatorar toda a camada de integração.
        - Tokenização e embeddings: cada provedor usa seu próprio esquema de tokenização e vetorização; embeddings gerados em um serviço podem não ser 100 % compatíveis com outro.
        - Políticas de dados e egressos: para mudar de nuvem (por exemplo, de Vertex AI para um deployment self-hosted), você pagará taxas de “data egress” e precisará garantir conformidade (LGPD/GDPR) no novo ambiente.
        - Descontos por uso comprometido: ao fechar um contrato de consumo mínimo para obter desconto (committed-use), você reduz custos, mas fica vinculado a aquele provedor até o fim do período acordado. Romper antes pode acarretar multas ou perda do benefício.
        
        Como mitigar o lock-in:
        
        - Padrões abertos: estruture suas chamadas de inferência usando a especificação OpenAI ou OpenAPI, facilitando a troca de backend.
        - Abstração de modelos: desenvolva uma camada de serviço interna que encapsule detalhes de API, de modo que trocar o provedor seja uma simples configuração, não uma reescrita de código.
        - Cache e fallback: armazene respostas em cache para reduzir chamadas diretas à API e implemente lógica de fallback para usar um modelo alternativo (por exemplo, um checkpoint open-source hospedado internamente) quando o custo ou a latência do endpoint principal estiverem altos. Dessa forma, você aproveita toda a flexibilidade e poder dos serviços pay-as-you-go, sem ficar refém de um único provedor.
        
- Exemplos do uso metrado via API (pay-as-you-go):
    - **Anthropic:**  [https://www.anthropic.com/api](https://www.anthropic.com/pricing#api)
    - **Google:**  [https://cloud.google.com/vertex-ai/pricing](https://ai.google.dev/gemini-api/docs/pricing)
    - **Groq Cloud:** https://groq.com/pricing
    - **SambaNova Suite** –  https://sambanova.ai/
    - **OpenRouter** – Plataforma agregadora que oferece modelos diversos com preços variados por token, claramente exibidos no site. [https://openrouter.ai/pricing](https://openrouter.ai/)
 
---FELIPE--FIM------------------------------------------

----ERIC --- INICIO
## Modelos de Monetização

As soluções de IA podem gerar receita de diferentes formas, dependendo do público-alvo e da proposta de valor:  

- **SaaS (Software as a Service)**: o modelo mais difundido, baseado em assinaturas recorrentes.  
- **Micro-SaaS**: soluções enxutas, criadas para nichos muito específicos {cite}`hogan2021`.  
- **Freemium**: versão gratuita com limitações e versão paga com recursos avançados.  
- **Marketplace de IA**: disponibilizar modelos, datasets ou APIs em plataformas de terceiros (ex.: Hugging Face, AWS Marketplace).  

Cada modelo pode ser combinado em diferentes estágios de crescimento: **freemium** para atrair usuários, seguido por **SaaS corporativo** para clientes que exigem escala.  

---

## SaaS e Micro-SaaS

O modelo **SaaS** permite escalar rapidamente, gerar receita previsível e atualizar soluções continuamente.  
É amplamente utilizado em setores que demandam **flexibilidade e segurança**, como gestão financeira, RH ou marketing.  

O **Micro-SaaS**, por sua vez, é indicado para empreendedores e equipes enxutas que desejam resolver **problemas muito específicos**, com baixa concorrência e custos reduzidos.  

Exemplo prático:  
- Um SaaS de análise preditiva para o varejo.  
- Um micro-SaaS que gera **descrições automáticas para produtos de e-commerce** usando IA generativa.  

Esse último pode ser criado por um pequeno time ou até por um único desenvolvedor, alcançando rentabilidade em mercados de nicho. 

----ERIC--FIM----
---

