# Capítulo 2 – Arquiteturas, Tecnologias e Componentes Técnicos

Uma solução de Inteligência Artificial é formada por diferentes **camadas técnicas** que trabalham em conjunto para transformar dados em valor.  
Compreender essas camadas é essencial para que líderes, desenvolvedores e gestores saibam **onde aplicar esforços**, **quais tecnologias priorizar** e **como reduzir riscos**.  

Neste capítulo, você vai explorar os principais **componentes de arquitetura, tecnologias e protocolos** utilizados atualmente, com foco em aplicações práticas e decisões estratégicas.  

---

## Prompt Engineering e RAG

O **Prompt Engineering** é a prática de **escrever instruções eficazes** para guiar modelos de linguagem, como os LLMs, a gerar respostas úteis e consistentes.  
É uma habilidade comparável a **fazer a pergunta certa em uma entrevista**: quanto mais clara e bem estruturada for a questão, melhor será a resposta {cite}`liu2023`.  

Estratégias comuns incluem:  
- **Prompts contextuais**: fornecer exemplos de entrada e saída para orientar o modelo (*few-shot learning*).  
- **Cadeias de raciocínio** (*chain-of-thought*) para estimular respostas passo a passo.  
- **Prompt híbrido**: combinar instruções, contexto e restrições para maior precisão.  

Já o **Retrieval-Augmented Generation (RAG)** combina LLMs com **bases de conhecimento externas**.  
Em vez de depender apenas do que foi aprendido no treinamento, o modelo consulta documentos, bancos de dados ou APIs em tempo real {cite}`lewis2020`.  

Exemplo prático:  
- Um chatbot jurídico pode buscar em **jurisprudências atualizadas** para dar respostas confiáveis.  
- Uma assistente de saúde pode consultar **protocolos médicos recentes** em vez de depender apenas do conhecimento pré-treinado.  

Esse paradigma aumenta a precisão, reduz **alucinações** (respostas inventadas) e amplia a aplicabilidade em cenários críticos.  


--PARTE FELIPE

Um modelo de IA genérico, como o GPT ou o Llama, é como um recém-formado brilhante: possui um conhecimento geral imenso, mas não sabe nada sobre as especificidades do seu negócio. Para transformá-lo em um especialista que entenda seus produtos, clientes e processos, é preciso "educá-lo". Prompt Engineering, RAG e Fine-tuning são as três principais estratégias para essa educação, cada uma com diferentes níveis de custo, esforço e profundidade.

1.  Prompt Engineering: Dando Instruções Claras
    - O que é: É a “arte” de dar instruções (prompts) detalhadas em tempo real para guiar a IA a gerar a resposta desejada. Não altera o conhecimento do modelo, apenas a forma como ele o utiliza naquele momento. Na verdade, toda interação com um LLM é, em sua essência, engenharia de prompt.
    - A Analogia: Pense nisso como ser um bom gerente. Você não ensina seu funcionário a falar português a cada nova tarefa; você apenas dá instruções claras sobre o que precisa ser feito, o formato esperado e o público-alvo.
    - Vantagens: Custo zero (além do tempo de desenvolvimento), resultados imediatos e acessibilidade total, sem necessidade de conhecimento técnico aprofundado.
    - Desvantagens: Não ensina o modelo permanentemente, não é escalável para tarefas complexas e se limita ao conhecimento pré-treinado do modelo.
    - Quando usar: Ideal para prototipagem, tarefas pontuais de escrita e como a base para todas as interações com LLMs. As técnicas de RAG e Fine-tuning, no fundo, são formas sofisticadas de automatizar e otimizar a engenharia de prompt.
  
2.  Retrieval-Augmented Generation (RAG): Dando ao Modelo uma Base de Consulta

    - O que é: RAG é uma técnica que conecta o modelo de IA a uma base de conhecimento externa e privada (ex: seus documentos internos, catálogo de produtos). Quando um usuário pergunta algo, o sistema primeiro recupera a informação relevante dessa base e a injeta no prompt como contexto. A IA, então, usa esse material factual para formular a resposta.
    - Como Funciona (de forma simples): Para que a busca seja inteligente, seus documentos são processados e convertidos em representações numéricas (vetores) que capturam seu significado semântico. Estes vetores são armazenados em um Banco de Dados Vetorial (Vector DB). Esse banco de dados permite uma busca por significado, e não apenas por palavras-chave, encontrando o trecho mais relevante para a pergunta do usuário.
    - A Analogia: É como dar ao seu funcionário acesso a uma intranet corporativa moderna e com uma busca inteligente. Ele não precisa memorizar tudo; ele busca a informação relevante no momento exato em que precisa dela. A resposta é sempre baseada em uma fonte oficial.
    - Vantagens: Combate "alucinações" ao ancorar as respostas em fatos, permite que o conhecimento da IA esteja sempre atualizado (basta atualizar os documentos) e oferece transparência sobre a fonte da informação.
    - Desvantagens: A qualidade da resposta depende 100% da qualidade e organização da sua base de dados ("Garbage In, Garbage Out"). A implementação inicial é mais complexa, pois exige a configuração de um pipeline de dados (ingestão, fragmentação e vetorização dos documentos).
    - Quando usar: É a arquitetura padrão para a maioria dos assistentes virtuais de atendimento, assistentes de conhecimento interno e qualquer aplicação que precise responder perguntas com base em um corpo de informações específico e mutável.
      
3. Fine-tuning (Ajuste Fino): A “Pós-Graduação” da IA
- O que é: Fine-tuning é o processo de continuar o treinamento de um modelo pré-existente usando um conjunto de dados proprietário e de alta qualidade (ex: centenas de exemplos de interações de suporte ao cliente). Você está, de fato, reescrevendo parte das conexões neurais do modelo para que ele aprenda um novo comportamento, estilo ou habilidade.
- A Inovação do LoRA: Tradicionalmente, esse processo era extremamente caro. Hoje, técnicas como o LoRA (Low-Rank Adaptation) permitem ajustar o modelo de forma muito mais eficiente. Em vez de retreinar bilhões de parâmetros, o LoRA "congela" o modelo original e treina apenas uma pequena camada adicional de parâmetros. Isso reduz o custo computacional em mais de 90%, tornando o fine-tuning uma opção estratégica viável.
- A Analogia: Fine-tuning não é dar um manual ao funcionário, é mandá-lo para uma pós-graduação. Ele não está mais apenas consultando informações; ele está internalizando um conhecimento tão profundo que sua própria maneira de "pensar" sobre um assunto é permanentemente alterada. LoRA seria o equivalente a um curso de especialização intensivo e focado, em vez de um doutorado de 5 anos.
- Vantagens: Cria um ativo único e um diferencial competitivo real, é a melhor forma de ensinar à IA um tom de voz de marca específico e pode otimizar a performance e o custo para tarefas repetitivas.
- Desvantagens: Ainda é a abordagem mais complexa, exige um bom conjunto de dados de treinamento e, se mal executado, carrega o risco de "esquecimento catastrófico" (o modelo se especializa tanto que perde habilidades gerais).
- Quando usar: A distinção estratégica é clara: use RAG para ensinar à IA o que saber; use Fine-tuning para ensinar à IA como se comportar. É ideal para quando a própria habilidade da IA é o seu produto, como uma IA que aprende o estilo de um advogado para redigir rascunhos de documentos.

  |**Estratégia** | **Custo/Esforço** | **Nível de Personalização** | **Resolve o problema de ...**|
  |---------------|-------------------|-----------------------------|------------------------------|
  |Prompt Engineering|Baixo|Baixo (Guia a IA)|...dar a instrução correta|
  |RAG|Médio|Médio (Dá conhecimento)|...não saber a informação correta.|
  |Fine-tuning (com LoRA)|Alto|Alto (Muda o comportamento)|...não ter a habilidade correta.|

  :::{tip} 
A jornada mais comum é começar com Prompt Engineering, evoluir para RAG para construir um produto robusto e baseado em fatos, e usar Fine-tuning seletivamente, apenas quando a especialização do comportamento da IA for, em si, a sua maior vantagem competitiva.
:::

```{figure} imagens/jornada_prompt_felipe.png
:label: jornada_prompt_felipe
:alt: Fluxo para implementar IA: Prompt Engineering → RAG para robustez → Fine-tuning seletivo para vantagem competitiva.
:align: center

Fluxograma ilustrando a jornada recomendada para o desenvolvimento de soluções com Inteligência Artificial. 
```
---

## API e Integração

Uma **API (Application Programming Interface)** é o “idioma” que permite que sistemas diferentes **se comuniquem** {cite}`fielding2000`.  
No contexto de IA, as APIs conectam modelos a aplicativos, websites ou sistemas corporativos.  

Exemplos de aplicação:  
- **E-commerce**: uma API de visão computacional pode classificar automaticamente fotos de produtos.  
- **Atendimento ao cliente**: chatbots integrados a APIs de NLP conseguem responder dúvidas em tempo real.  
- **Indústria 4.0**: sensores conectados via API alimentam modelos de manutenção preditiva.  

As APIs tornam a IA **modular e escalável**, permitindo que empresas adicionem inteligência a sistemas já existentes sem reconstruí-los do zero.  

---

## Rodar Localmente vs. Cloud Computing

As soluções de IA podem ser executadas de duas formas principais:  

- **Localmente** (*on-premise*): oferece maior controle sobre os dados e reduz riscos de exposição, mas exige servidores robustos, equipe técnica especializada e custos elevados de manutenção.  
- **Na nuvem** (*cloud computing*): oferece escalabilidade, menor custo inicial e acesso rápido a modelos pré-treinados {cite}`armbrust2010`.  

Na prática:  
- Bancos podem preferir **on-premise** para proteger dados sensíveis de clientes.  
- Startups geralmente escolhem **cloud**, aproveitando a flexibilidade para crescer rapidamente.  

A decisão envolve equilibrar **segurança, custo e velocidade de implantação**.  

---

## Frontend vs. Backend

Toda aplicação de IA precisa de duas camadas principais:  

- **Frontend**: a interface que o usuário final vê e interage (ex.: site, aplicativo, painel de controle).  
- **Backend**: o "motor invisível" que processa dados, executa os modelos de IA e retorna os resultados.  

Separar essas camadas garante que a arquitetura seja **mais flexível e escalável**.  
Por exemplo: o usuário de um app de tradução só vê a frase traduzida no **frontend**, mas todo o processamento de linguagem natural ocorre no **backend**.  

---

## UX de IA — Interação Humano-Sistema

A **Experiência do Usuário (UX)** em sistemas de IA exige atenção especial, pois envolve lidar com **incertezas e probabilidades**.  

Boas práticas incluem {cite}`amershi2019`:  
- **Transparência**: deixar claro de onde vêm as respostas (ex.: citar fontes).  
- **Controle**: permitir que o usuário refine ou corrija resultados (ex.: ajustar parâmetros em filtros de imagem).  
- **Confiança**: comunicar limitações, graus de confiança ou margens de erro do modelo.  

:::{note}
A qualidade técnica da IA é inútil se a experiência do usuário for confusa.  
Um modelo de recomendação de filmes pode ser altamente preciso, mas se não explicar *por que* sugeriu um título, pode gerar desconfiança.  
:::

---

## Protocolos como MCP (Model Context Protocol)

O **Model Context Protocol (MCP)** é uma iniciativa recente que propõe **padronizar a comunicação entre aplicações e modelos de IA**.  
Seu objetivo é garantir que diferentes ferramentas possam se conectar de forma **segura, eficiente e consistente**, reduzindo problemas de compatibilidade e evitando integrações fragmentadas.  

Essa padronização será cada vez mais importante em um cenário onde múltiplos modelos, serviços e frameworks precisam colaborar — por exemplo, em ecossistemas empresariais que combinam **LLMs proprietários, sistemas legados e bancos de dados sensíveis**.  

---

:::{tip}
Compreender a **arquitetura e os componentes técnicos** não significa que você precise dominar a programação de cada parte.  
O essencial é ter **clareza sobre as opções disponíveis** e saber avaliar quais escolhas são mais adequadas para os seus objetivos estratégicos.
:::
