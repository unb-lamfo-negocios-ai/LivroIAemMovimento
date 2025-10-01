# Capítulo 4 – Ecossistema de Ferramentas e Frameworks

O crescimento da Inteligência Artificial trouxe consigo um **ecossistema diverso de ferramentas e frameworks**, que aceleram a criação, teste e implantação de soluções.  
Esses recursos permitem que equipes foquem no **valor de negócio** em vez de reinventar a roda do zero.  

Neste capítulo, vamos explorar algumas das ferramentas mais utilizadas atualmente, com foco em suas aplicações práticas, pontos fortes e limitações.  

---

## LangFlow

O **LangFlow** é uma interface visual que facilita a construção de aplicações com modelos de linguagem.  
Ele funciona como um **“laboratório de fluxos”**, no qual prompts, APIs, bancos de dados e lógica de negócio podem ser conectados de forma intuitiva, sem necessidade de programação aprofundada.  

**Principais usos:**  
- Criação de protótipos de chatbots em minutos.  
- Testes rápidos de **Prompt Engineering** com diferentes entradas.  
- Construção de **Proofs of Concept (PoCs)** para validação junto a stakeholders.  

Por reduzir barreiras técnicas, é especialmente útil para **equipes multidisciplinares** (como marketing e inovação) que querem experimentar IA de forma ágil {cite}`langflow2023`.  

----TEXTO---NOTION---
O LangFlow é uma ferramenta de código aberto que permite criar fluxos de trabalho de IA visualmente, similar ao LangChain. Suas principais características incluem:

- Interface visual drag-and-drop para construção de fluxos de IA
- Compatibilidade com diversos modelos de linguagem e embeddings
- Suporte a múltiplos provedores de IA (OpenAI, Anthropic, etc)
- Exportação de fluxos como código Python

Para trabalhar com MCP (Model Context Protocol):

- Configure diferentes modelos de linguagem como nós
- Estabeleça regras de roteamento entre modelos
- Defina estratégias de fallback automático
- Monitore uso e custos por provedor

O LangFlow é ideal para prototipagem rápida de aplicações de IA e experimentação com diferentes modelos e arquiteturas de fluxo.

---

## LangChain

O **LangChain** é uma das bibliotecas mais populares para desenvolvimento de aplicações baseadas em LLMs.  
Ele oferece **componentes reutilizáveis e modulares** para:  

- Conectar modelos de linguagem a diferentes fontes de dados.  
- Gerenciar memória de conversas de longo prazo.  
- Criar cadeias de raciocínio complexas e pipelines de decisão.  

**Exemplo prático:** criar um assistente corporativo que acessa políticas internas em PDF, responde dúvidas e registra feedback dos colaboradores.  

Seu diferencial está na **flexibilidade para integrar IA em aplicações robustas**, tornando-o uma escolha comum para startups e grandes empresas {cite}`langchain2022`.  

----TEXTO----NOTION----
LangChain é um framework de código aberto que facilita o desenvolvimento de aplicações com Inteligência Artificial, especialmente para criar agentes de IA. Suas principais características incluem:

- **Componentes Modulares:** Oferece blocos de construção reutilizáveis para criar aplicações de IA personalizadas
- **Integração com LLMs:** Suporta diversos modelos de linguagem como GPT-4, Claude, PaLM e outros
- **Gerenciamento de Contexto:** Permite manipular e estruturar o contexto das conversas de forma eficiente
- **Chains:** Possibilita a criação de fluxos sequenciais de processamento de dados e lógica
- **Agents:** Facilita a construção de agentes autônomos que podem tomar decisões e executar tarefas

**Principais funcionalidades para Backend:**

- **Memory Systems:** Gerenciamento de histórico de conversas e estados
- **Prompt Templates:** Sistema robusto para gerenciar e padronizar prompts
- **Tools e Callbacks:** Integração com APIs externas e sistemas de monitoramento
- **Document Loaders:** Processamento de diferentes tipos de documentos e dados

**Vantagens para Desenvolvimento:**

- Arquitetura modular e extensível
- Grande comunidade e documentação abrangente
- Suporte a diversos backends de banco de dados
- Integração facilitada com serviços de nuvem

```{code-block} python
from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent
from langchain.memory import ConversationBufferMemory

# Exemplo básico de configuração de um agente
tools = [
    Tool(
        name="Search",
        func=search_function,
        description="Útil para buscar informações"
    )
]

memory = ConversationBufferMemory()
agent = LLMSingleActionAgent(tools=tools, memory=memory)
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    memory=memory
)
```

---

## LangGraph

O **LangGraph** é uma evolução das ideias do LangChain, mas com foco em **grafos de execução**.  
Isso permite mapear fluxos complexos de decisão como se fossem diagramas visuais, trazendo:  

- **Transparência**: acompanhamento de cada etapa do raciocínio.  
- **Governança**: auditoria mais fácil em processos críticos (como jurídico e saúde).  
- **Flexibilidade**: múltiplos caminhos de execução em um mesmo sistema.  

**Exemplo:** um sistema de triagem médica que decide se um paciente deve ser atendido por IA, direcionado a um humano ou encaminhado a um especialista.  

Essa abordagem é indicada para **sistemas críticos** que exigem rastreabilidade e controle.  

---

## Streamlit

O **Streamlit** é um framework em Python que permite criar **aplicações interativas de dados e IA** com poucas linhas de código.  

**Aplicações típicas:**  
- Dashboards dinâmicos para visualização de métricas.  
- Protótipos de interfaces para modelos de Machine Learning.  
- Ferramentas internas para análise exploratória de dados.  

**Exemplo prático:** um analista de dados pode compartilhar em minutos um app que mostra previsões de vendas com base em modelos de regressão.  

Sua simplicidade o torna muito popular em equipes de **Data Science** {cite}`streamlit2021`.  

---

## Gradio

O **Gradio** simplifica a criação de **interfaces web acessíveis** para modelos de IA.  
Com ele, é possível transformar um modelo em uma aplicação interativa em poucos minutos, sem precisar escrever HTML, CSS ou JavaScript.  

**Exemplos de uso:**  
- Uma página onde usuários fazem upload de imagens para classificação automática.  
- Um demo público de geração de voz a partir de texto.  

É bastante utilizado para **demonstrações públicas e testes de usabilidade**, além de ser integrado ao ecossistema **Hugging Face** {cite}`gradio2021`.  

---

## n8n

O **n8n** é uma ferramenta de automação **low-code** que conecta diferentes serviços por meio de **workflows visuais**.  
No contexto de IA, ele pode ser usado para:  

- Monitorar mensagens de clientes e acionar respostas automáticas.  
- Classificar tickets de suporte com modelos de NLP.  
- Conectar LLMs a bancos de dados ou sistemas corporativos (ex.: CRM).  

**Exemplo prático:** uma empresa pode criar um fluxo onde menções no Twitter são analisadas por IA e classificadas em “elogio”, “crítica” ou “pedido de suporte”, com resposta automática ou encaminhamento interno {cite}`n8n2020`.  


----INICIO---GABRIEL---------------
### O que é o **n8n**?

O **n8n** (diz-se "n-eight-n", de “*node to node*”) é uma **plataforma de automação de processos**, **integração entre sistemas** e **orquestração de dados**.

---

### 🛠️ Para que serve?

- **Automatizar tarefas repetitivas**
- **Conectar diferentes aplicativos e bancos de dados**
- **Criar fluxos inteligentes** usando lógica, código, APIs, inteligência artificial, etc.
- **Integrar com qualquer serviço** (mesmo aqueles sem integração pronta, via HTTP/API)

---

Principais Características

- **Open source:** você pode usar, adaptar e hospedar gratuitamente
- **Interface visual drag-and-drop:** fácil de montar e visualizar fluxos (“workflows”)
- **Nodes prontos para centenas de apps:** WhatsApp, Google, Telegram, Slack, Notion, bancos SQL, etc.
- **Permite lógica condicional, loops, código customizado**
- **Extensível:** aceita plugins, scripts, integrações customizadas
- **Funciona local, em cloud, em servidor VPS, Docker...**
- **Muito usado para automação com IA** (OpenAI, Gemini, DeepSeek...)

  A API permite que o n8n:

- **Envie dados para um sistema externo**
- **Receba dados de outro sistema**
- **Execute ações nesses sistemas** (como criar um lead, buscar informações, deletar arquivos...)

Por que APIs são importantes no n8n?

O n8n é um **orquestrador**. Ele conecta várias ferramentas entre si — e isso só é possível porque essas ferramentas possuem **APIs abertas**.

Com APIs, o n8n consegue:

- Automatizar processos com ferramentas que **não têm nodes prontos**
- Acessar **funcionalidades mais avançadas** do que os nodes nativos oferecem
- **Criar integrações personalizadas** com qualquer sistema que suporte API REST

Verbos HTTP (métodos de requisição)

As APIs usam verbos HTTP para definir a ação a ser tomada:

|**Verbo**|	**Significado**|**Exemplo prático no n8n**|
|-----|------------|--------------------------|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">GET</span>	|Buscar dados	|Pegar lista de clientes do CRM|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">POST</span>	|Enviar dados (criar)	|Criar novo lead, enviar formulário|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">PUT</span>	|Atualizar dados por completo	|Atualizar todos os campos de um lead|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">PATCH</span>	|Atualizar parcialmente|	Atualizar só o status do cliente|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">DELETE</span> 	|Excluir dados|	Deletar lead inativo do banco|
---

### O que é Autenticação em APIs?

Autenticação é o processo de **validar quem está fazendo a requisição** à API. Sem autenticação, qualquer um poderia acessar, alterar ou deletar dados sensíveis.

🧩 Tipos de Autenticação mais comuns em APIs

|**Tipo**	|**Como funciona**|	**Exemplo de uso**|
|-------|-------------|---------------|
|API Key|	Chave única que identifica o usuário|	<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">api_key=XYZ123</span>? no link ou cabeçalho|
|Bearer Token (OAuth2)	|Token de acesso temporário	|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Authorization: Bearer abc.def.ghi</span>|
|Basic Auth	|Usuário + senha codificados em Base64	|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Authorization: Basic dXNlcjpwYXNz</span>|
|OAuth2 (3-legged)	|Redireciona o usuário para login	|Usado no Google, Facebook, Microsoft|
|Header Customizado|	API exige chave em cabeçalho com nome específico	|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">X-API-KEY: sua-chave-aqui</span>|
|Session Cookie / JWT|	Cookies de sessão ou tokens JWT	|Sessões autenticadas de forma segura|

### Como isso se aplica no n8n?

No **n8n**, você configura autenticação em dois lugares:

1. **Credenciais do Node**:
    - Exemplo: Google Sheets, Gmail, WhatsApp, Supabase, Notion
    - Você usa **OAuth2** ou **API Key** cadastradas no menu de credenciais
2. **Node HTTP Request (genérico)**:
    - Ideal para APIs sem nodes prontos
    - Você pode usar:
      - <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Header Auth</span>
 (com Bearer, Token, etc)
      - <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Query Auth</span>
 (API Key na URL)
      - <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Basic Auth</span>
 (usuário/senha codificados)
      - <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Custom Headers</span>
 (nome + valor da chave)

### Nodes de Gatilhos

 O que são Trigger Nodes?

Triggers são usados quando você quer que o n8n **espere por um evento externo** antes de executar as próximas etapas. Sem um gatilho, o workflow só é executado manualmente.


|Tipo de Node Trigger	|Finalidade	|Exemplo|
|-----------------------|-----------|-------|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Webhook</span>|Ativado por uma requisição HTTP|	Um sistema externo envia um POST e inicia o fluxo|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Form Trigger</span>	|Ativado quando alguém preenche um formulário	|Lead preenche dados de contato|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Cron</span>	|Executa em horários definidos	|Enviar relatório toda segunda às 8h|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Google Drive Trigger</span>	|Ativado quando um arquivo é criado/atualizado em uma pasta do Drive	|Novo contrato adicionado no Drive|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Telegram Trigger</span>	|Reage a mensagens recebidas no bot do Telegram	|Cliente envia “Oi” e inicia atendimento|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Email Trigger (IMAP)</span>	|Dispara ao receber um e-mail	|Processar anexos de e-mails automaticamente|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Shopify Trigger, Notion Trigger, etc.</span>	|Ativam fluxos com base em eventos de plataformas específicas|	Novo pedido na loja, nova nota criada|

### Nodes Essenciais

O que são *Nodes Essenciais* no n8n?

**Nodes essenciais** são os blocos fundamentais que **não dependem de integrações externas** (como Gmail, WhatsApp, Notion...) e que **manipulam dados, controlam o fluxo e estruturam a lógica** do seu workflow.

Eles são universais — usados em quase todos os tipos de automações — e fazem parte do "cérebro" da automação, funcionando como:

- **Variáveis** (<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Set`</span>)
- **Condições** (<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`IF`</span>, <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Switch`</span>)
- **Regras e lógica** (<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Function`</span>, <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Code`</span>)
- **Controle de tempo** (<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Wait`</span>)
- **Divisão e união de dados** (<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Split`</span>, <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Merge`</span>)


| Tipo de Node | Finalidade | Exemplo |
|--------------|------------|---------|
| Set (<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">set</span>) | Define ou altera dados manualmente | Criar variáveis como <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">nome</span>, <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">email</span>, <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">status</span> |
| IF (<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">if</span>) | Cria ramificações lógicas (condições) | Se <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">status == aprovado</span>, siga o fluxo A |
| Switch (<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">switch</span>) | Ramifica com múltiplas condições | Redireciona com base em “tipo de cliente” |
| Merge (<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">merge</span>) | Junta dados de dois fluxos | Unir resposta de API com dados locais |
| Wait (<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">wait</span>) | Pausa o fluxo por tempo definido | Esperar 5 min antes de seguir |
| Code (<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">code</span>) | Executa código JavaScript | Validar CPF ou gerar ID aleatório |
| HTTP Request (<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">httpRequest</span>) | Faz chamadas HTTP/REST externas | Buscar dados de uma API externa |
| Function (<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">function</span>) | Executa lógica personalizada | Calcular valores, gerar token |
| Split In Batches (<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">splitInBatches</span>) | Divide itens em partes | Processar 10 leads por vez |
| Respond to Webhook | Responde uma requisição HTTP | Retornar JSON ou HTML para quem chamou o fluxo |




**Node set**
    
O que é o Node **Set** no n8n?
    
O node <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Set</span> serve para **criar, modificar ou excluir dados no seu fluxo**, sem depender de fontes externas. Ele é um dos **nodes essenciais** do n8n.
    
Pense nele como um "bloco de notas" onde você define ou ajusta valores antes de enviar para um e-mail, API, IA ou planilha.

Principais usos do Set

|Objetivo|	Exemplo|
|--------|----------|
|Criar variáveis	|Criar <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">status: "novo"</span> ou <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">tipo: "lead quente"</span>|
|Editar campos	|Alterar o nome de uma variável, como <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">telefone → WhatsApp</span>|
|Renomear dados recebidos	|Padronizar nomes de campos antes de enviar a outro sistema|
|Deixar o dado pronto para IA/API	|Juntar nome + empresa num só campo|

Como funciona na prática

No node <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Set`</span> você define:

- O nome do campo: ex. <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`mensagem`</span>
- O valor: ex. <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`"Olá, {{ $json['nome'] }}. Tudo bem?"`</span>

Você pode usar **expressões dinâmicas**, como:

```{code-block} text
Olá {{ $json['nome'] }}, sua empresa {{ $json['empresa'] }} foi registrada com sucesso!
```

```{admonition} **Dica de ouro**
:class: tip

Você pode marcar **“Keep Only Set”** se quiser **remover todos os outros campos** e manter **somente os definidos no <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Set`</span>**. Isso é útil para simplificar o payload antes de enviar para um e-mail, API ou IA.
```

O que é o Node **Filter**?

O **Filter** serve para **filtrar dados** que passam pelo seu workflow, ou seja, **permitir apenas itens que atendam a certas condições** continuarem para os próximos nodes.

Itens que **não passam pelo filtro** são descartados (não seguem adiante no fluxo).

---

Quando usar o Filter?

- Quando você só quer continuar o fluxo com itens que correspondem a critérios específicos.
- Para separar leads qualificados de não qualificados, por exemplo.
- Para processar apenas registros com status específico, valores mínimos/máximos, campos preenchidos, etc.

---

Como funciona?

1. **Entrada:** Recebe uma lista de itens (ex: vários leads, pedidos, respostas de API...).
2. **Condições:** Você define as regras (ex: “status” igual a “aprovado” ou “valor” maior que 1000).
3. **Saída:** Só os itens que **passam nas condições** seguem para os próximos nodes.

Exemplo prático:

Suponha que você tem vários leads:


```{code-block} json
[
  { "nome": "Lucas", "pontuacao": 85 },
  { "nome": "Ana", "pontuacao": 60 }
]
```

No node **Filter**, você pode definir:

**Campo:** <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`pontuacao`</span>

**Operador:** <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`maior que`</span>

**Valor:** <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`70`</span>

**Resultado:** Só o lead "Lucas" segue adiante.

```{admonition} Dica Extra
:class: tip

- Se quiser manipular o que acontece com os que NÃO passam no filtro, use o node **IF** (que permite bifurcar o fluxo).
- O node **Filter** é ótimo para automações “em lote”, onde muitos dados passam pelo mesmo fluxo.
```

- **Node Agreggate**
    
O que faz o node **Aggregate**?
    
O **Aggregate** pega **vários itens de entrada** e realiza algum tipo de **agregação**, como:
    
- **Juntar textos** de vários registros em uma única string
- **Somar** ou **calcular médias** de campos numéricos
- **Criar listas** com valores únicos ou agrupados
- **Gerar estatísticas** simples (máximo, mínimo, contagem)
- **Transformar múltiplos itens em um único item** (útil para enviar resumo, gerar arquivo, etc.)

Como funciona na prática?

1. **Entrada:** Recebe vários itens (ex: linhas do Google Sheets, respostas de API, vários leads).
2. **Configuração:**
    - Você escolhe qual campo quer agregar (ex: <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`nome`</span>, <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`valor`</span>, <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`mensagem`</span>).
    - Define a operação: **somar**, **contar**, **juntar**, **média**, **min/max** ou **customizada**.
3. **Saída:**
    - Entrega **um ou poucos itens** já agregados/resumidos.

---

Exemplos práticos

- **Juntar nomes em uma lista:**
    
    Entrada:
  
  ```{code-block} json
  [{"nome": "Lucas"}, {"nome": "Ana"}, {"nome": "João"}]
```

Saída após concatenar nomes:

 ```{code-block} json
{ "nomes": "Lucas, Ana, João" }
```

- **Somar valores de vendas:**
    
    Entrada:
  
 ```{code-block} json

[ { "valor": 200 }, { "valor": 300 } ]

```

Saída após “somar valor”:

 ```{code-block} json

{ "total": 500 }

```

- **Contar quantos itens vieram:**
    
    Entrada: 10 leads
    
    Saída:
```{code-block} json

{ "totalLeads": 10 }

```

```{admonition} Use o node **Aggregate** sempre que quiser
:class: tip

Para:
- Fazer relatórios resumidos
- Mandar um único e-mail com dados agrupados
- Preparar dados para dashboards ou integrações externas
```

- **Node HTTP Request**
    
O que é o Node HTTP Request?
    
    O **HTTP Request** é como um “mensageiro digital” que faz o n8n **conversar com outros sites, sistemas ou aplicativos na internet**.
    
    Ele serve para **buscar informações** em outros lugares (ex: previsão do tempo, dados de clientes, valores de moedas), **enviar dados** (ex: criar um lead, registrar uma compra), ou **fazer qualquer ação** que esses sistemas permitam via internet.
    
    ---
    
Como funciona na prática?
    
    Imagine que você quer saber a previsão do tempo. Você:
    
    1. Abre um navegador,
    2. Digita um endereço (URL) e,
    3. Vê a resposta (previsão) na tela.
    
    No n8n, o **node HTTP Request** faz isso automaticamente e pode:
    
    - Buscar informações para você,
    - Enviar formulários,
    - Integrar com APIs de bancos, e-commerces, WhatsApp, Google, e qualquer outro sistema.

Passos básicos de uso:

1. **Escolher o endereço (URL)**
    
    Onde o n8n vai buscar ou enviar informação. Exemplo: `https://api.exemplo.com/usuarios`
    
2. **Escolher a ação (verbo HTTP)**
    - <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`GET`</span> = Buscar dados
    - <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`POST`</span> = Enviar/criar dados
    - <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`PUT/PATCH`</span> = Atualizar dados
    - <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`DELETE`</span> = Apagar dados
3. **(Opcional) Enviar dados junto**
    
    Por exemplo, se for um formulário ou cadastro.
    
4. **Receber a resposta**
    
    O node traz os dados do site/aplicativo, que podem ser usados nos próximos passos do fluxo.

Para que serve no dia a dia?

- Integrar com sistemas que **não têm node próprio** no n8n
- Buscar ou enviar dados em **APIs públicas ou privadas**
- Criar automações sob medida com qualquer serviço online

---

### 📋 Exemplo bem simples

Você quer buscar o preço do dólar hoje:

- Node HTTP Request com URL de uma API de câmbio e método <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">'GET'</span>
- O n8n traz a cotação para o seu fluxo, pronta para ser usada.

  - **Node Respond to Webhook**
    
O que é o Node **Respond to Webhook**?
    
    O **Respond to Webhook** é como um **"balcão de respostas"** do seu fluxo de automação.
    
    Ele serve para **enviar uma resposta automática para quem chamou o seu workflow**.
    
    ---
    
Como funciona na prática?
    
    Imagine que seu fluxo do n8n recebe um pedido de fora (de um site, sistema ou aplicativo) usando um **Webhook** (um “sininho” que escuta quando algo acontece).
    
    - O **Webhook** recebe a mensagem (ex: dados de um formulário enviado).
    - O seu fluxo faz tudo o que precisa (salva, calcula, consulta, etc.).
    - **No final**, você usa o node **Respond to Webhook** para **responder de volta** (confirmando que deu certo, enviando dados, etc).
    
    ---
    
 Exemplo do dia a dia
    
    **Situação:**
    
    Um site pede orçamento e espera uma resposta automática.
    
    **No n8n:**
    
    1. Node **Webhook** recebe o pedido.
    2. O fluxo consulta preços, calcula tudo.
    3. Node **Respond to Webhook** responde na hora:
        
        “Orçamento recebido! Em breve, entraremos em contato.”
        
    
    ---
    
Para que serve?
    
    - Enviar confirmações automáticas para integrações externas.
    - Responder sistemas, sites, chatbots, apps ou pessoas que aguardam uma resposta rápida.
    - Retornar dados processados pelo n8n (por exemplo, status, valores, cálculos).
    
    ---
    
    ```{admonition}
	:class: tip
    
    Se não usar o **Respond to Webhook**, quem chamou o seu fluxo pode **ficar esperando** e não receber resposta nenhuma, ou receber uma mensagem padrão de erro.
	```

Nodes de Aplicativo

O que são *Nodes de Aplicativo*?

**Nodes de aplicativo** são os blocos que **conectam o n8n com serviços externos** — como Gmail, WhatsApp, Google Sheets, Notion, Telegram, APIs, CRMs e muito mais.

Esses nodes permitem que o n8n **envie, receba ou modifique dados fora dele**, ou seja, **são a ponte entre o n8n e o mundo real digital**.

|Aplicativo	|Node	|Exemplo de Uso|
|-----------|-------|--------------|
|WhatsApp Business API	|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">n8n-nodes-base.whatsApp</span>|	Enviar mensagem para um lead|
|Gmail|	<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">n8n-nodes-base.gmail</span>	|Disparar um e-mail com proposta|
|Google Sheets|	<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">n8n-nodes-base.googleSheets</span>|Gravar ou buscar leads salvos|
|Telegram	|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">n8n-nodes-base.telegram</span>|Responder comandos recebidos|
|Google Drive	|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">n8n-nodes-base.googleDrive</span>	|Baixar um contrato ou subir um arquivo|
|Notion	|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">n8n-nodes-base.notion</span>	|Registrar uma nova oportunidade|
|ScrapingBee|	<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">httpRequest + headers</span>	|Scraping de sites com autenticação|
|DeepSeek AI / OpenAI / Gemini|	<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">@n8n/n8n-nodes-langchain.lmChat...</span>	|Responder com IA personalizada|
|Supabase	|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">@n8n/n8n-nodes-langchain.vectorStoreSupabase</span>	|Gravar vetores de RAG|

### Como funcionam os Nodes de Aplicativo?

1. **Autenticação**: geralmente exigem que você configure uma **credencial** (OAuth, API Key...).
2. **Parâmetros**: você define o que será enviado ou buscado.
3. **Entrada/Saída**:
    
    O node consome os dados do fluxo (normalmente em formato JSON), executa uma ação no aplicativo externo (ex: enviar um WhatsApp, criar uma linha no Google Sheets, enviar um e-mail, buscar informações de uma API) e retorna a resposta dessa ação.
    
    - Essa resposta pode ser usada por outros nodes seguintes no workflow.
    - Assim, os dados podem ser transformados, salvos, encaminhados ou analisados conforme o fluxo avança.
4. **Múltiplas Operações**:
    
    Muitos nodes de aplicativo possuem **diferentes operações** além do padrão "criar" ou "buscar".
    
    - Exemplo: O node do Google Sheets permite criar, ler, atualizar e deletar linhas; o node do WhatsApp pode enviar mensagens de texto, imagem, áudio, etc.
5. **Tratamento de Erros**:
    
    Caso o app externo retorne um erro (ex: falha de autenticação, dados inválidos, limite atingido), o node pode exibir esse erro no painel ou permitir o uso de nodes de controle (como o IF) para tratar falhas e tomar decisões alternativas no fluxo.
    
6. **Personalização**:
    
    Os nodes de aplicativo geralmente permitem **personalizar mensagens, campos e payloads** usando expressões dinâmicas do n8n, tornando cada automação adaptada ao contexto do lead ou usuário.
    

---

Exemplo prático de sequência:

1. **Formulário** preenche dados do lead →
2. **Node de Aplicativo (Google Sheets)** grava os dados →
3. **Node de Aplicativo (WhatsApp)** envia uma mensagem personalizada →
4. **Node de Aplicativo (Gmail)** envia notificação para o time comercial.
## Canva

O **Canva** é uma plataforma de design que incorporou recursos de **IA generativa**, como:  
- Criação automática de imagens.  
- Sugestão de layouts e textos.  
- Geração de apresentações com base em descrições simples.  

Embora não seja uma ferramenta técnica de desenvolvimento, **democratiza a IA** para profissionais de comunicação, marketing e design, ampliando a adoção em escala {cite}`canva2023`.  

### Linguagem JSON

O que é JSON?

**JSON (JavaScript Object Notation)** é um formato leve de troca de dados, baseado em texto. Ele é utilizado para **armazenar e transmitir informações estruturadas** entre sistemas, especialmente em APIs e integrações como as feitas no **n8n**.

```{code-block} json
{
  "nome": "Lucas",
  "idade": 30,
  "ativo": true}
```

- As **chaves** são sempre entre aspas
- Os **valores** podem ser string, número, booleano, objeto, array, ou `null`

Os blocos básicos do JSON

Tipos de Dados no JSON

1. **Strings**
    
    Texto entre **aspas duplas** (`" "`).
    
    Exemplo: <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`"nome": "Fala, galera!"`</span>
    
    ✅ Usado para nomes, emails, mensagens etc.
    
2. **Números**
    
    Valores **numéricos sem aspas**, inteiros ou decimais.
    
    Exemplo: <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`"idade": 42`, `"nota": 3.14`</span>
    
    ✅ Usado para cálculos, filtros, pontuação, ID.
    
3. **Booleanos**
    
    Verdadeiro ou falso (<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`true`</span> / <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`false`</span>).
    
    Exemplo: <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`"ativo": true`</span>

    
    ✅ Útil para checagens em <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`IF`</span>, como status de pagamento.
    
4. **Arrays**
    
    Lista de valores entre colchetes `[ ]`.
    
    Exemplo: <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`"itens": ["pizza", "hambúrguer", "pastel"]`</span>
    
    ✅ Ideal para listas, múltiplos contatos, respostas múltiplas.
    
5. **Objetos**
    
    Conjunto de pares chave-valor entre chaves <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`{ }`</span>.
    
    Exemplo:

   ```{code-block} json
   {
  "nome": "João",
  "idade": 25
}
```
É a estrutura mais usada no n8n para entradas e saídas.

6. **null**
    
    Representa valor vazio ou ausente.
    
    Exemplo: <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`"dataNascimento": null`</span>
    
    ✅ Muito usado para indicar "não preenchido" ou "a definir".

JSON Aninhado: Um objeto dentro do outro

```{code-block} json
{
  "usuario": {
    "nome": "Ana",
    "contato": {
      "email": "ana@exemplo.com",
      "telefone": "123456"
    }
  }


Aqui temos objetos dentro de outros objetos. Acessar isso no n8n exige navegação com <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">usuario.contato.email</span>.
```

JSON vs. XML vs. CSV

|Formato|	Legibilidade|	Peso	|Uso moderno|
|-------|---------------|-----------|-----------|
|JSON|	Alta	|Leve|	🔥 Amplamente usado|
|XML	|Verboso	|Pesado	|Usado em sistemas antigos|
|CSV|	Simples	|Muito leve	|Ideal para planilhas|


```{admonition}
:class: note
JSON é preferido em APIs e automações como as do n8n.
```

Como o JSON é usado no n8n?

No **n8n**, praticamente **todos os dados trafegam em JSON**:

- Respostas de APIs
- Resultados de formulários
- Mensagens manipuladas
- Saídas de nodes

Você pode visualizar e editar JSON diretamente nos nodes como <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Set`</span>, <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`HTTP Request`</span>, <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Code`</span>, etc.

Como acessar dados em JSON?

Exemplo:

Se seu JSON for:

```{code-block} json
{
  "lead": {
    "nome": "João",
    "contato": {
      "whatsapp": "5599999999"
    }
  }
}
```
Você acessa no n8n assim:

```{code-block} json
{{$json["lead"]["contato"]["whatsapp"]}}
```

Ou:
```{code-block} json
{{$json.lead.contato.whatsapp}}
```

```{admonition} Erros comuns
:class: warning

### Erros comuns com JSON

- Esquecer aspas em **chaves**
- Vírgula sobrando no final
- Usar **aspas simples** em vez de **duplas**
- Acessar caminho que não existe → erro `undefined`
- Enviar JSON mal formatado em um `POST` via HTTP
```

---

### 📝 Como é a estrutura de um JSON?

A estrutura é feita por **pares de chave e valor**, e pode conter:
---

## WhatsApp API

A integração com o **WhatsApp API** permite conectar chatbots de IA diretamente ao aplicativo de mensagens mais usado no Brasil e em vários países.  

**Casos comuns de uso:**  
- Atendimento automatizado com personalização de contexto.  
- Suporte ao cliente em escala, sem perder o tom humano.  
- Campanhas de engajamento interativas, segmentadas por perfil.  

Combinada a LLMs e frameworks de orquestração, transforma o WhatsApp em um **canal estratégico de relacionamento** {cite}`meta2022`.  

---

:::{tip}
O ecossistema de ferramentas de IA está em constante expansão.  
Mais importante do que conhecer todas as opções é saber **qual ferramenta se alinha melhor ao objetivo do projeto, à maturidade da equipe e ao orçamento disponível**.  
A escolha certa pode acelerar resultados; a errada pode gerar custos e complexidade desnecessários.
:::
