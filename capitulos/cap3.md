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

---

## Vibe Coding

O conceito de **Vibe Coding** descreve uma forma emergente de criar produtos digitais em que a **IA atua como copiloto criativo**.  
Nesse modelo, a programação tradicional é complementada por **colaboração interativa com LLMs**, que sugerem código, explicações e até protótipos funcionais {cite}`wu2022`.  

Isso acelera a prototipagem e reduz barreiras técnicas, permitindo que profissionais de áreas não técnicas participem da construção de soluções digitais.  

Exemplo prático: um designer de produto pode, com o auxílio de um LLM, criar rapidamente um protótipo de aplicativo que gera imagens personalizadas para campanhas de marketing, sem escrever linhas extensas de código.  

:::{tip}
Estratégias bem definidas de **construção, precificação e operação** podem ser o diferencial entre um produto de IA promissor e um projeto que nunca ganha escala.  
O segredo está em alinhar **capacidade técnica**, **modelo de monetização** e **necessidade real do mercado**.
:::
