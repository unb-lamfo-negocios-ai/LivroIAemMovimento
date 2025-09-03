## O que é IA

- A Inteligência Artificial (IA) é um campo de estudos dedicado à construção de sistemas capazes de raciocinar, aprender e agir de maneira que tradicionalmente exigiria inteligência humana. Em termos mais práticos, a IA representa um conjunto de tecnologias baseadas principalmente em machine learning e deep learning, utilizadas para análise de dados, previsões, processamento de linguagem natural, categorização de objetos, recomendações inteligentes etc.
- A IA engloba diversas disciplinas, incluindo ciência da computação, análise de dados, estatística, engenharia de hardware e software, linguística, neurociência e até filosofia e psicologia.
- Fundamentalmente, a IA gira em torno de dados; os modelos de IA aprendem e melhoram através da exposição a grandes quantidades de dados, identificando seus padrões e relações.

## Modelos de IA

- Modelos de IA são as estruturas computacionais e os algoritmos que formam o "cérebro" de um sistema de inteligência artificial, permitindo que ele aprenda com dados, identifique padrões e tome decisões ou faça previsões. A forma como esses modelos são construídos e treinados define suas capacidades e aplicações.

## Prompt Engineering, Retrieval-Augmented Generation (RAG) e Fine-tuning & LoRA

## Build vs. Buy - modelo pronto ou desenvolvimento interno?

- No caminho para criar um negócio com Inteligência Artificial, uma das primeiras e mais importantes decisões estratégicas é definir se a empresa irá desenvolver uma tecnologia própria (build) ou se irá utilizar uma solução já existente no mercado (buy). Essa escolha impacta diretamente o orçamento, o tempo de lançamento do produto e, principalmente, onde residirá o diferencial competitivo. Não se trata de uma decisão puramente técnica, mas fundamentalmente de uma decisão de negócio.
- A abordagem "Buy": usando um modelo pronto
    
    
    Optar por “comprar” significa utilizar a tecnologia de ponta desenvolvida por grandes provedores (como os modelos GPT da OpenAI, Claude da Anthropic e Gemini do Google via API) ou empregar modelos de código aberto (open-source) já treinados, como os da família Llama (Meta) ou Mixtral (Mistral AI). 
    
    A grande vantagem dessa abordagem é a velocidade de implementação e o acesso a um poder computacional de ponta sem o investimento inicial em Pesquisa & Desenvolvimento. O problema central reside no risco de lock-in (dependência de um fornecedor) e na dificuldade de criar um diferencial tecnológico profundo, visto que concorrentes podem acessar a mesma tecnologia.
    
- A abordagem "Build": desenvolvendo um modelo proprietário
    
    
    “Construir” não se limita a criar um modelo do zero, um processo extremamente raro e custoso. Na prática atual, a abordagem "Build" manifesta-se principalmente através do ajuste fino (fine-tuning) de modelos open-source de alta performance com dados proprietários da empresa. Os motivadores para essa decisão são variados e estratégicos.
    
    - Motivadores Estratégicos para a Abordagem "Build":
        - Hiper-especialização e Vantagem Competitiva: Um modelo genérico, por mais poderoso que seja, não supera um modelo menor e mais ágil treinado exaustivamente para uma única tarefa. É o caso do Harvey AI, que ajustou modelos da família GPT para se tornar um especialista em análise de documentos jurídicos, criando uma vantagem competitiva sustentável em seu nicho.
        - Soberania de Dados, Segurança e Conformidade: Para setores como o financeiro, saúde ou governamental, enviar dados de clientes para uma API de terceiros pode ser inviável por razões regulatórias (LGPD/GDPR) e de segurança. A solução é uma abordagem "Build". Um exemplo recente é a iniciativa do governo francês, que em 2024 anunciou a criação de um "commando AI" para desenvolver modelos de IA soberanos, garantindo que dados sensíveis permaneçam em infraestrutura controlada.
        - Otimização de Custo e Latência em Escala: Utilizar uma API de ponta tem um custo variável que pode aumentar expressivamente com o volume de uso. Empresas como a DoorDash publicaram estudos em 2024 mostrando como desenvolveram seus próprios modelos para tarefas específicas, como a estimativa de tempo de entrega. O modelo customizado, embora menos versátil que um GPT-4o, é drasticamente mais rápido e mais econômico (com reduções de custo que podem superar 90%) para sua única e repetitiva função.
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
    

## Rodar localmente vs. cloud computing

## Estruturas de precificação para IA

- Uso metrado via API (pay-as-you-go)
    - No modelo “pay-as-you-go” via API, empresas como OpenAI, Anthropic e Google disponibilizam diversos endpoints de inferência, cada um oferecendo um conjunto de modelos (por exemplo, GPT-4o, o3, Claude 3.5, Claude 4, Gemini 2.5, etc.) com razões custo-benefício diferentes. Você é cobrado por unidade de consumo (geralmente por milhão de tokens de entrada e saída), o que possibilita:
        - Escalabilidade imediata: basta chamar a API, sem se preocupar em gerenciar servidores ou clusters de GPU.
        - Flexibilidade de escolha: selecione o modelo mais barato para tarefas simples (como Gemini 2.0 Flash) ou um mais caro e preciso (como Gemini 2.5 Pro) conforme a necessidade de qualidade e latência.
    - Existem dois problemas centrais desse modelo:
        - Oscilação de custos: Se seu tráfego varia muito, a fatura pode subir de forma imprevisível no mês em que há picos de uso. Modelos maiores (mais parâmetros) custam várias vezes mais por token. Por exemplo…
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

## Frontend vs. backend @Mateus Macedo

- NoCode / LowCode

## UX de IA - interação humano-sistema

## API e integração @Mateus Macedo

## LLMs e IA Generativa

- LLM Leaderboard: https://lmarena.ai/leaderboard ou https://huggingface.co/spaces/lmarena-ai/chatbot-arena-leaderboard
- Protocolos como MCP @paulo oliveira
- Vibe Coding
- “Vibe coding” é um estilo de programação que procura tornar o processo mais leve, acessível e criativo. Em lugar de seguir o caminho tradicional baseado em planejamento extenso e etapas técnicas rígidas, o programador simplesmente descreve o que deseja e deixa que a inteligência artificial traduza essa ideia em código em questão de segundos. Isso significa que o vibe coder não precisa dominar linguagens ou bibliotecas complexas: basta conversar com o modelo de IA e ir moldando o projeto conforme as necessidades surgem. A grande vantagem é a prototipagem rápida. Em poucas horas (às vezes minutos) é possível ter um app, uma automação ou uma ferramenta simples funcionando, avaliar sua utilidade e, se necessário, aprimorá-la com o próprio auxílio da IA. Caso não dê certo, o custo do erro é mínimo, pois todo o código foi gerado em tempo quase real. 
Essa abordagem chama atenção porque elimina barreiras históricas de entrada: qualquer pessoa pode sair de uma ideia abstrata para um protótipo funcional sem meses de estudo prévio. Além disso, ela incentiva a liberdade criativa; não há “modo correto” de começar, apenas o objetivo de colocar algo para rodar. No entanto, nem tudo são flores. Quando se salta etapas de arquitetura, o código pode crescer frágil e se tornar difícil de manter ou escalar. É comum acumular dependências sugeridas pela IA sem e`m`ntender versões ou licenças, o que cria um débito técnico invisível. Também há riscos de qualidade e segurança, já que os trechos gerados podem conter falhas de desempenho ou vulnerabilidades que passam despercebidas sem auditoria humana. Outro ponto crítico é a dependência da ferramenta: deixar todo o raciocínio a cargo do modelo pode impedir que o desenvolvedor aprenda fundamentos essenciais. Por fim, a velocidade inicial pode ser ilusória: transformar um protótipo relâmpago em produto robusto exige testes, documentação, versionamento e boas práticas de engenharia. 
Em síntese, vibe coding abre portas e democratiza a criação de soluções com IA ao reduzir o medo de começar errado e permitir entregas relâmpago. Por outro lado, cada atalho cobra seu preço mais adiante. Resta, portanto, a reflexão: até que ponto vale trocar profundidade por velocidade e em quais projetos esse compromisso faz sentido? Encontrar esse equilíbrio será, provavelmente, o próximo grande desafio de quem deseja construir com IA de forma realmente sustentável.

## SaaS e micro-SaaS

- SaaS (Software as a Service)
    - Modelo de negócio baseado em software distribuído como serviço
    - Acesso via navegador ou aplicativo, geralmente com assinatura recorrente
    - O cliente paga mensal ou anualmente para acessar uma aplicação em nuvem que embute IA. A receita é previsível (ARR) e se mede pela expansão de contas (net revenue retention). Margem bruta depende do custo de GPU em nuvem: reservar instâncias ou aderir a saving plans pode cortar 30 % do COGS.
    - Exemplos:
        - Grammarly Premium - https://www.grammarly.com/
        - 
- Micro-SaaS
    - Versão especializada e focada de um SaaS tradicional
    - Geralmente desenvolvido por equipes pequenas ou individuais

## Ética e viés @Maisa Kely Melo

## Casos de uso exemplares por setor (EXCLUIR)

## Modelos de monetização