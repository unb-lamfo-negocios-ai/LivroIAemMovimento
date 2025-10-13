# Fundamentos de Inteligência Artificial

A Inteligência Artificial (IA) é um campo da ciência da computação dedicado a criar sistemas capazes de executar tarefas que, tradicionalmente, exigiriam inteligência humana. Esses sistemas podem **reconhecer padrões, aprender com dados, tomar decisões e interagir com pessoas** {cite}`russell2021`.  

Mais do que um conjunto de algoritmos, a IA é hoje um **instrumento estratégico** que redefine modelos de negócios, práticas sociais e até mesmo a forma como nos relacionamos com a informação e o conhecimento.  

## O que é IA?

A ideia de criar máquinas capazes de pensar como seres humanos surgiu na década de 1950, marcando o início de uma revolução tecnológica e científica {cite}`turing1950`. Dois nomes se destacam nesse contexto: **Alan Turing**, que levantou a questão central sobre a capacidade de pensamento das máquinas, e **John McCarthy**, que cunhou o termo que hoje conhecemos como *Inteligência Artificial*.

```{admonition} Teste de Turing
:class: note

- Alan Turing propôs o que ficou conhecido como **Teste de Turing**:

> um experimento  para avaliar se uma máquina consegue se passar por um ser humano em uma conversa textual.

- Se o interlocutor humano não conseguir distinguir se está conversando com uma pessoa ou com uma máquina, considera-se que o sistema passou no teste.
- Essa proposta lançou as bases filosóficas e práticas da Inteligência Artificial.
```

```{admonition} O surgimento do termo *Artificial Intelligence*
:class: note

- O termo **Inteligência Artificial** foi utilizado pela primeira vez por **John McCarthy** durante a **Conferência de Dartmouth** em 1956.
- Considerada o marco zero da IA, a conferência reuniu cientistas para discutir como construir máquinas capazes de simular aspectos da inteligência humana.
- Esse encontro deu origem a uma nova área de pesquisa que evolui até os dias atuais.

```

Desde então, a inteligência artificial deixou de ser apenas uma tecnologia futurista para se tornar parte integrante do nosso dia a dia. Ela está presente em soluções que facilitam tarefas cotidianas, otimizam processos e tomam decisões com base em grandes volumes de dados.

```{admonition} Exemplos de algumas aplicabilidades de IA no dia a dia:
:class: exemplo

**Assistentes virtuais**, como Alexa e Siri, que reconhecem comandos de voz e executam ações;

**Sistemas de recomendação em plataformas de streaming e e-commerce**, que sugerem filmes, músicas ou produtos com base no comportamento do usuário;

**Carros autônomos**, que interpretam o ambiente e tomam decisões em tempo real;

**Diagnósticos médicos** assistidos por computador, capazes de identificar padrões em exames de imagem;

**Análises preditivas em negócios**, que ajudam empresas a antecipar tendências, melhorar estratégias e reduzir riscos.
```

Para compreender melhor os diferentes níveis de capacidade da inteligência artificial, é útil distinguir entre dois grandes grupos: IA fraca e IA forte. Essa classificação nos ajuda a entender até onde as máquinas conseguem simular comportamentos inteligentes e em que medida elas realmente compreendem o que estão fazendo.

```{admonition} **IA fraca (ou estreita)**
:class: note
  - Projetada para executar tarefas específicas com **alto desempenho**, mas **sem consciência** ou compreensão real.  
  - **Exemplos**: assistentes virtuais (Alexa, Siri), sistemas de recomendação da Netflix, algoritmos de classificação de imagens no Instagram.  
  - **Característica**: extremamente eficiente em **um domínio específico**, mas incapaz de transferir esse aprendizado para outras áreas.  
  - **Situação atual**: é a forma de IA predominante hoje, presente em quase todos os produtos e serviços inteligentes disponíveis no mercado.
```

```{admonition} **IA forte (ou geral)**
:class: note
  - Ainda hipotética, busca replicar a inteligência humana em sua plenitude, incluindo **raciocínio abstrato, criatividade, senso comum e adaptabilidade em múltiplos contextos**.  
  - **Exemplo teórico**: uma máquina que pudesse aprender qualquer tarefa cognitiva com a mesma flexibilidade de um ser humano.  
  - **Desafios**: exigiria avanços em **consciência artificial, compreensão contextual profunda e autonomia de aprendizado**.  
  - **Situação atual**: permanece como **um objetivo de longo prazo**, alvo de debates filosóficos, éticos e científicos.
```

Uma forma simples de diferenciar é pensar que a **IA fraca** é como um **especialista em uma única área**, enquanto a **IA forte** seria um **generalista versátil**, capaz de aprender e se adaptar a qualquer desafio cognitivo.  


## Modelos de IA

Para navegar no cenário da inteligência artificial moderna, é crucial compreender a terminologia e as relações entre seus componentes. Muitas vezes usados de forma intercambiável, os termos-chave na verdade representam camadas de uma hierarquia tecnológica. No topo está a **Inteligência Artificial (IA)**, o campo abrangente dedicado a criar máquinas que podem imitar o comportamento humano inteligente.

O motor por trás da Inteligência Artificial são os **modelos computacionais** — estruturas matemáticas que aprendem padrões a partir de dados e generalizam esse conhecimento para novos cenários. A grande diferença em relação ao software tradicional é o "como" eles operam. Em vez de seguir regras explícitas e fixas programadas por um humano (se X, então Y), um modelo de IA aprende suas próprias regras e padrões ao analisar os dados. 

```{admonition} **“Tradutores” da realidade**
:class: note

Os modelos computacionais atuam como tradutores da realidade:
- observam exemplos;
- identificam regularidades;
- passam a **prever ou decidir** com base nessas regularidades.
```

Existem inúmeros tipos de modelos, desde os preditivos (que estimam a probabilidade de um cliente cancelar um serviço) até os revolucionários modelos generativos (como os LLMs que escrevem textos ou criam imagens), que são o foco principal deste material. Em qualquer um dos casos, o modelo é, em última análise, o ativo central e o motor de valor de um negócio construído sobre Inteligência Artificial.

Entre as principais técnicas, destacam-se:

```{admonition} **Machine Learning (ML)**
:class: note
  - Algoritmos que aprendem a partir de exemplos e melhoram com a experiência {cite}`goodfellow2016`.  
  - **Exemplo prático**: um sistema de detecção de fraudes em cartões de crédito pode ser treinado com transações históricas, aprendendo a identificar padrões incomuns e gerar alertas em tempo real.  
  - **Limitação**: depende fortemente da qualidade dos dados — se o conjunto de treinamento contiver vieses, o modelo pode reproduzi-los.  
```

```{admonition} **Deep Learning (DL)**
:class: note
  - Redes neurais profundas compostas por várias camadas de processamento, que extraem representações complexas dos dados.  
  - **Avanços notáveis**:  
    - **Visão computacional**: reconhecimento facial em smartphones, análise de imagens médicas, identificação automática de objetos em fotos.  
    - **Processamento de linguagem natural (PLN)**: tradução automática, assistentes virtuais, análise de sentimentos em redes sociais.  
  - **Limitação**: exige grandes volumes de dados e poder computacional elevado, o que pode dificultar a adoção por pequenas organizações.
```

Essas abordagens sustentam aplicações cada vez mais presentes no cotidiano, como:  

- **Chatbots** que respondem perguntas de clientes em tempo real.  
- **Sistemas de tradução automática** que permitem comunicação entre idiomas.  
- **Modelos de previsão de demanda** usados no varejo e na logística.  
- **Modelos climáticos** capazes de projetar cenários de aquecimento global com base em dados ambientais.  

**Comparação entre Machine Learning e Deep Learning**

| Aspecto                | Machine Learning (ML)                                                                 | Deep Learning (DL)                                                                 |
|-------------------------|---------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| **Dependência de Dados** | Funciona bem com **volumes moderados de dados**.                                      | Requer **grandes volumes de dados** para treinar modelos eficazes.                  |
| **Complexidade**        | Algoritmos mais simples (árvores de decisão, regressões, SVMs).                        | Estruturas complexas de redes neurais com muitas camadas.                           |
| **Explicabilidade**     | Geralmente mais fácil de interpretar e explicar.                                       | Considerado uma “caixa-preta”, com menor interpretabilidade.                        |
| **Requisitos Computacionais** | Pode rodar em computadores convencionais.                                             | Demanda GPUs e infraestrutura robusta.                                             |
| **Exemplos de Aplicação** | Previsão de churn de clientes, detecção de fraudes, recomendação de produtos.          | Reconhecimento facial, tradução automática, geração de texto e imagem.              |
| **Curva de Adoção**     | Mais acessível para pequenas e médias empresas.                                        | Predominante em grandes organizações, laboratórios de pesquisa e startups de ponta. |

---

:::{note}
De forma simples: o **Machine Learning** pode ser visto como um **professor que treina a máquina com exemplos**, enquanto o **Deep Learning** é como uma **rede de especialistas**, que refina o conhecimento em múltiplas camadas até chegar a uma decisão.  
:::

## LLMs e IA Generativa

A evolução recente da inteligência artificial trouxe uma nova classe de tecnologias capazes de **gerar conteúdo novo** — estamos falando da **IA Generativa**, um campo amplo que inclui diversas modalidades, como texto, imagem, áudio e vídeo. Em paralelo, ganharam destaque os **Modelos de Linguagem de Grande Escala (LLMs, do inglês *Large Language Models*)**. Os LLMs são os "motores" especializados, treinados em quantidades massivas de dados de texto, que capacitam as aplicações de IA Generativa a compreender, processar e gerar linguagem humana {cite}`brown2020`. 

### Diferença entre LLM e IA Generativa

É essencial entender que um LLM é a tecnologia subjacente que executa tarefas de Processamento de Linguagem Natural (PLN), como classificação de texto e análise de sentimento, enquanto a IA Generativa é a aplicação mais ampla que usa essa análise para criar uma nova saída.

```{admonition} IA Generativa: o conceito mais amplo
:class: note
A **IA Generativa** engloba qualquer sistema de inteligência artificial capaz de **criar conteúdo original**. Ela pode utilizar diferentes tipos de modelos, dependendo do formato da entrada e da saída.
```

```{admonition} LLM: uma especialização da IA Generativa
:class: note

- LLMs são uma tecnologia dentro do guarda-chuva da IA Generativa.
- Eles são como o "motor" que impulsiona aplicações de geração e compreensão de texto.
- Eles são capazes de **compreender e gerar linguagem natural** e estão por trás de ferramentas como:

- [ChatGPT (OpenAI)](https://chat.openai.com)
- [Claude (Anthropic)](https://www.anthropic.com)
- [Gemini (Google)](https://deepmind.google/technologies/gemini/)
- [Mistral](https://mistral.ai/)
- [LLaMA (Meta)](https://ai.meta.com/llama/)

Esses modelos alimentam **chatbots**, **assistentes virtuais**, **sistemas de recomendação de código**, entre muitas outras aplicações textuais.
```

Essa distinção revela um paradigma fundamental para a compreensão do ecossistema de IA: 

> o do "motor versus veículo".

Um LLM, como o GPT-4 da OpenAI, pode ser visto como um motor de alto desempenho, uma peça de tecnologia complexa e poderosa. A IA Generativa, por outro lado, é o veículo que utiliza esse motor para uma finalidade específica. Assim como um motor pode ser instalado em um carro (para transporte), um barco (para navegação) ou um avião (para voo), um único LLM pode alimentar uma variedade de aplicações: um chatbot para atendimento ao cliente, uma ferramenta para redação de e-mails de marketing ou um assistente para geração de código de programação. Essa separação entre a tecnologia central (o motor) e sua aplicação (o veículo) explica por que a inovação em um único LLM pode levar a uma explosão de novas e diversas ferramentas de IA Generativa.

Concluindo, podemos dizer que a hierarquia da Inteligência Artificial pode ser entendida como um sistema de camadas interligadas, onde cada nível representa uma especialização maior do anterior. No topo está a IA como campo geral, seguida pelas Redes Neurais e, dentro delas, o Deep Learning, que impulsiona a IA Generativa. Essa organização hierárquica pode ser vista na imagem abaixo. Ela apresenta camadas que vão do geral ao específico:

- **Inteligência Artificial**: A camada mais externa, incluindo todas as tecnologias que envolvem comportamento inteligente.

- **Aprendizado de Máquinas**: Algoritmos que aprendem com dados.

- **Redes Neurais**: Estruturas inspiradas no cérebro que formam a base do deep learning.

- **Aprendizado Profundo**: Aplicações com múltiplas camadas de redes neurais para tarefas complexas.

- **IA Generativa**: Modelos capazes de criar novos dados como textos, imagens e sons (ex: GPT, BERT, GANs).

A imagem também destaca subtemas importantes em cada categoria, como:

- **Em Machine Learning**: regressão logística, KNN, K-means.

- **Em Neural Networks**: Perceptron, Backpropagation.

- **Em Deep Learning**: LSTM, CNN, RNN.

- **Em IA Generativa**: Transformers, LLM, LangChain, Foundation Models, Multimodal AI, RLHF, QLoRA, etc.

```{figure} imagens/hierarquia_de_IAs.jpeg
:name: hierarquia_de_IAs
:alt: Diagrama em camadas que mostra a hierarquia da Inteligência Artificial, com destaque para IA, Machine Learning, Deep Learning, Redes Neurais e IA Generativa.
:align: center
:figclass: align-center
**Figura – Como a IA Generativa se Encaixa no Universo da IA.**  
Fonte: Inspirado em {cite}`chapman2023linkedin`.
```

![Como a IA Generativa se Encaixa no Universo da IA](imagens/hierarquia_de_IAs.jpeg)

![Como a IA Generativa se Encaixa no Universo da IA](https://github.com/unb-lamfo-negocios-ai/LivroIAemMovimento/blob/9862fb242173b8c67864ae9c20e0472c55fa3205/imagens/hierarquia_de_IAs.jpeg)

### **Como os LLMs Funcionam: Dos Dados ao Diálogo**

O termo "Grande" em Grandes Modelos de Linguagem refere-se a duas dimensões de escala. A primeira é o tamanho monumental do conjunto de dados de treinamento, que pode incluir bilhões ou até trilhões de palavras extraídas de livros, artigos, sites e outras fontes da internet. A segunda é o número de parâmetros do modelo, que são essencialmente os "botões" internos que o modelo ajusta durante o treinamento para capturar os padrões nos dados. 

```{admonition}
:class: exemplo
O modelo GPT-3 possui 175 bilhões de parâmetros, uma escala que lhe permite aprender nuances linguísticas incrivelmente complexas.
```

Apesar de sua complexidade, o mecanismo central de um LLM é baseado em um princípio surpreendentemente simples: a previsão probabilística. Em vez de "pensar" ou "entender" no sentido humano, um LLM funciona como uma máquina de reconhecimento de padrões extremamente sofisticada. Quando recebe um texto de entrada (um "prompt"), ele calcula a probabilidade da próxima palavra (ou, mais precisamente, do próximo "token", que pode ser uma palavra ou parte de uma palavra) que deveria seguir na sequência, com base nos padrões que aprendeu durante o treinamento. Ele então seleciona a palavra mais provável, anexa-a ao texto e repete o processo, gerando sentenças e parágrafos inteiros, uma palavra de cada vez. Este mecanismo fundamental explica tanto a notável fluência e coerência dos LLMs quanto sua tendência a "alucinar", inventar fatos ou informações que parecem plausíveis, mas não são verdadeiros, pois o modelo está otimizando para a probabilidade linguística, não para a veracidade factual.

A inovação arquitetônica que tornou os LLMs modernos possíveis é conhecida como **Transformer**. Introduzida em 2017, essa arquitetura de rede neural permite que o modelo pese a importância de diferentes palavras na entrada, independentemente de sua distância umas das outras. Isso lhe confere uma compreensão superior do contexto em longas sequências de texto, superando as limitações de arquiteturas mais antigas.

O ciclo de vida de um LLM normalmente envolve duas fases principais. A primeira é o **pré-treinamento**, um processo de aprendizado não supervisionado no qual o modelo é alimentado com o vasto conjunto de dados de texto sem rótulos ou instruções explícitas, aprendendo a gramática, os fatos, os estilos de raciocínio e os vieses contidos nos dados. A segunda fase é o **ajuste fino (fine-tuning)**, onde o modelo pré-treinado é treinado adicionalmente em um conjunto de dados menor e mais específico, muitas vezes com supervisão humana, para alinhá-lo a tarefas específicas (como responder a perguntas) e a comportamentos desejados (como ser útil e inofensivo).

### **O Ecossistema da IA Generativa: Um Universo de Criação**

A IA Generativa transcende os *chatbots* e representa um campo vasto de criação de conteúdo em múltiplas modalidades. Sua versatilidade está redefinindo indústrias e processos criativos.


```{admonition} Universo de criação da IA generativa
:class: note

- **Geração de Texto:** A aplicação mais conhecida, onde os LLMs são usados para criar uma ampla gama de conteúdos escritos. Isso inclui tarefas práticas como redigir e-mails, resumir relatórios longos e criar postagens para redes sociais, bem como tarefas criativas como escrever poemas, roteiros e artigos.
- **Geração de Imagem:** Modelos como DALL-E, Midjourney e Stable Diffusion podem traduzir descrições textuais em imagens visuais ricas e detalhadas. Eles podem gerar desde imagens fotorrealistas até ilustrações em estilos artísticos específicos, oferecendo uma ferramenta poderosa para designers, profissionais de marketing e artistas.
- **Geração de Código:** A IA Generativa pode escrever, depurar, otimizar e traduzir código em várias linguagens de programação. Ferramentas como o GitHub Copilot atuam como um "parceiro de programação", sugerindo trechos de código e funções inteiras, o que aumenta drasticamente a produtividade dos desenvolvedores.
- **Geração de Áudio e Música:** Modelos generativos podem sintetizar fala com som natural para assistentes de voz e narrações, além de compor peças musicais originais em diversos gêneros, imitando a estrutura e o som de composições profissionais.
- **Geração de Vídeo:** Uma fronteira emergente e em rápida evolução, onde a IA pode criar clipes de vídeo curtos a partir de prompts de texto ou imagens estáticas. Essa tecnologia tem o potencial de revolucionar a produção de conteúdo, animação e efeitos especiais.
```

O impacto dessa tecnologia é sentido em praticamente todos os setores. No mundo dos negócios, a IA Generativa é usada para melhorar a **experiência do cliente** por meio de chatbots mais inteligentes e personalização em escala; aumentar a **produtividade dos funcionários** ao automatizar a geração de relatórios e auxiliar na criação de conteúdo; e otimizar **processos de negócios** complexos, como análise de documentos, detecção de fraudes e otimização da cadeia de suprimentos.

> A interação do usuário com todas essas modalidades converge para um único conceito: o **prompt**.

Seja para gerar um soneto, uma imagem de um astronauta em um cavalo ou uma função em Python, a entrada do usuário é quase sempre uma instrução em linguagem natural. Isso aponta para uma transformação mais profunda na interação humano-computador. A IA Generativa está se tornando um "tradutor universal da intenção humana". Ela pega o desejo humano, expresso na linguagem ambígua e rica em nuances que nos é natural, e o traduz em uma saída estruturada e específica, seja ela um poema, uma imagem ou um programa de computador. Nesse novo paradigma, a habilidade de formular prompts claros e eficazes, conhecida como "engenharia de prompt", torna-se uma competência fundamental para extrair o máximo valor desses sistemas poderosos.

```{admonition} Exemplos de ferramentas de IA generativa:
:class: exemplo

- **Texto (LLMs)**: [ChatGPT](https://chat.openai.com), [Claude](https://www.anthropic.com/index/claude), [Gemini](https://deepmind.google/technologies/gemini/)
- **Imagem**: [DALL·E](https://openai.com/dall-e), [Midjourney](https://www.midjourney.com/), [Stable Diffusion](https://stability.ai/)
- **Voz**: [ElevenLabs](https://www.elevenlabs.io/)
- **Multimodal**: [GPT-4V (Vision)](https://openai.com/gpt-4), [Gemini 1.5](https://deepmind.google/technologies/gemini/)
```

**Por que a IA generativa importa na criação de negócios?**

Durante décadas, criar um negócio dependia de habilidades como:

- Saber programar ou contratar programadores
- Saber escrever ou contratar redatores
- Saber desenhar ou contratar designers
- Ter tempo e recursos para montar, testar e lançar algo novo

Hoje, com LLMs e IA generativa, **muitas dessas barreiras caíram.** Isso significa que **mais pessoas podem tirar ideias do papel com mais rapidez e menos custo.**

### Casos de uso práticos para empreendedores

Aqui estão formas reais de usar LLMs e IA generativa **na criação de um negócio:**

| Área                | O que a IA pode fazer                                                                 | 
|-------------------------|---------------------------------------------------------------------------------------|
| **Validação de ideias** | Simular personas, criar pesquisas, testar propostas de valor                                     |
| **Copywriting**        | Criar textos para landing pages, anúncios, e-mails                       |
| **Naming & branding**     | Gerar nomes de empresas, slogans, ideias de posicionamento                                      |
| **Desenvolvimento de produto** | Gerar código, wireframes, fluxos, documentações                                            |
| **Marketing de conteúdo** | Criar posts de blog, redes sociais, ebooks, newsletters          |
| **Pitch de vendas**     | Criar roteiros, argumentos, respostas a objeções                                        |
|**Atendimento e suporte** | Criar FAQs, chatbots, respostas automáticas, assistente virtual inteligente |
| **Automação de tarefas** | Usar IA combinada com ferramentas no-code para fluxos inteligentes |

```{admonition} Limitações e Cuidados
:class: caution

- **Alucinações:** LLMs podem inventar fatos. Sempre revise conteúdo crítico.  
- **Privacidade:** Evite inserir dados sensíveis.  
- **Qualidade:** Nem todo conteúdo gerado é bom — o olho humano ainda manda.  
- **Dependência:** A IA é ferramenta, não muleta. Desenvolva também sua intuição de negócio.
```

### Acompanhando a batalha das IAs em tempo real

Podemos dizer que a evolução dos LLMs e da IA Generativa está acontecendo em um ritmo vertiginoso. Novos modelos, melhorias de desempenho e abordagens mais avançadas são lançadas quase semanalmente. Empresas como [**OpenAI**](https://openai.com/), [**Anthropic**](https://www.anthropic.com/), [**Google DeepMind**](https://deepmind.google/), [**Meta**](https://www.meta.ai/) e [**Mistral**](https://mistral.ai/) lideram essa corrida tecnológica, disputando não apenas a supremacia técnica, mas também a preferência de desenvolvedores e usuários.

Para acompanhar de perto esse cenário em constante transformação, duas plataformas se destacam como **arenas públicas e vitrines de desempenho** dos modelos mais avançados:

```{admonition} [LMArena Leaderboard](https://lmarena.ai/)
:class: tip
Uma plataforma onde modelos de IA generativa competem em duelos de perguntas e respostas. Os resultados são baseados em **votações humanas cegas**, o que garante um reflexo fiel da experiência de uso. A arena oferece:
- Comparações diretas entre modelos como GPT-4, Claude 2, Mistral, Llama 2, entre outros;
- Atualizações contínuas conforme novos modelos são lançados;
- Dados úteis para avaliar desempenho em tarefas reais.
```

```{admonition} [Hugging Face — Chatbot Arena Leaderboard](https://huggingface.co/spaces/lmarena-ai/chatbot-arena-leaderboard)
:class: tip
Esta é a versão da LMArena hospedada na Hugging Face, com acesso fácil ao código e visualizações interativas. É ideal para quem quer:
- Testar os modelos diretamente no navegador;
- Explorar rankings e estatísticas;
- Usar o ambiente como referência para experimentações próprias.
```

Esses espaços são valiosos para qualquer profissional, pesquisador ou empreendedor que deseje:
- **acompanhar tendências** no desempenho dos LLMs;
- **escolher os melhores modelos** para suas soluções;
- **entender os diferenciais competitivos** em termos de geração, contexto, criatividade e raciocínio.

```{admonition}
:class: hint
> Em um cenário de evolução tão veloz, manter-se informado não é apenas útil — é estratégico.
```



## Ética e Viés MAISA FAZER

Apesar do potencial transformador, a IA traz consigo desafios importantes:  

- **Viés algorítmico**: sistemas podem reproduzir preconceitos existentes nos dados de treinamento. Um exemplo clássico é o de sistemas de recrutamento que penalizaram candidatos por padrões de gênero ou etnia presentes em bases históricas.  
- **Privacidade e uso de dados**: a coleta massiva de informações pessoais levanta preocupações sobre proteção, consentimento e transparência.  
- **Impacto no trabalho**: a automação pode substituir funções repetitivas, exigindo **requalificação e adaptação** da força de trabalho.  
- **Responsabilidade e accountability**: quem deve responder por erros de decisão — a empresa que utiliza a IA, os desenvolvedores ou o próprio sistema?  

Diversas iniciativas de pesquisa e regulação buscam garantir o uso **responsável, ético e transparente** da IA {cite}`jobin2019`. Governos, empresas e sociedade civil têm buscado criar normas que equilibrem **inovação** e **proteção social**.  

---

:::{tip}
Sempre que encontrar um conceito desafiador neste livro, consulte os materiais de apoio e faça paralelos com exemplos da sua realidade. A melhor forma de entender IA é **relacionando teoria, prática e impacto social**.
:::
