# Integrando com n8n

O **n8n** é uma ferramenta de automação **low-code** que conecta diferentes serviços por meio de **workflows visuais**.  

```{admonition} Utilidade do n8n no contexto de IA
:class: note 
Automatizar e orquestrar tarefas complexas, como:

- **Monitorar mensagens de clientes** e acionar respostas automáticas com base em regras ou IA.
- **Classificar tickets de suporte** utilizando modelos de NLP.
- **Conectar LLMs a bancos de dados ou sistemas corporativos**, como CRMs e ERPs.
- **Automatizar tarefas repetitivas**, reduzindo erros manuais e economizando tempo.
- **Integrar com diferentes aplicativos e bancos de dados**, mesmo que não possuam integrações nativas, por meio de requisições HTTP/API.
- **Criar fluxos inteligentes**, combinando lógica condicional, código personalizado, APIs e modelos de IA generativa.
```

 ```{admonition} Exemplo: Análise automática para menções no Twitter
 :class: exemplo
Uma empresa pode criar um fluxo onde menções no Twitter são analisadas por IA e classificadas em “elogio”, “crítica” ou “pedido de suporte”, com resposta automática ou encaminhamento interno {cite}`n8n2020`.
```

```{admonition} Pronúncia
:class: tip
O **n8n** diz-se "n-eight-n", de “*node to node*”.

```{admonition} Principais Características
:class: note

- **Open source:** você pode usar, adaptar e hospedar gratuitamente
- **Interface visual drag-and-drop:** fácil de montar e visualizar fluxos (“workflows”)
- **Nodes prontos para centenas de apps:** WhatsApp, Google, Telegram, Slack, Notion, bancos SQL, etc.
- **Permite lógica condicional, loops, código customizado**
- **Extensível:** aceita plugins, scripts, integrações customizadas
- **Funciona local, em cloud, em servidor VPS, Docker...**
- **Muito usado para automação com IA** (OpenAI, Gemini, DeepSeek...)
```

## Como o n8n usa APIs

O n8n é, essencialmente, um orquestrador de automações. Sua função principal é conectar diferentes ferramentas e sistemas para que eles “conversem” entre si — e essa comunicação só é possível graças às APIs abertas desses serviços.

APIs (Interfaces de Programação de Aplicações) funcionam como pontes que permitem o envio, recebimento e manipulação de dados entre sistemas distintos. 

```{admonition} No caso do n8n, as APIs são fundamentais para:
:class: note
- Enviar dados gerados dentro de um fluxo para sistemas externos (como um CRM ou planilha).

- Receber dados de serviços externos e utilizá-los em etapas subsequentes do fluxo.

- Executar ações remotas, como cadastrar um novo cliente, consultar informações, ou deletar arquivos automaticamente.
```

Com o uso de APIs, o n8n se torna ainda mais poderoso, pois permite:

- Automatizar ferramentas que não possuem nodes nativos no n8n.

- Acessar recursos avançados que os nodes prontos não oferecem.

- Criar integrações personalizadas, conectando qualquer sistema que suporte API REST.

### Verbos HTTP (métodos de requisição)

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

**Entrada:** Recebe vários itens (ex: linhas do Google Sheets, respostas de API, vários leads).
**Configuração:**
- Você escolhe qual campo quer agregar (ex: <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`nome`</span>, <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`valor`</span>, <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`mensagem`</span>).
- Define a operação: **somar**, **contar**, **juntar**, **média**, **min/max** ou **customizada**.
**Saída:**
Entrega **um ou poucos itens** já agregados/resumidos.

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

**JSON Aninhado: Um objeto dentro do outro**

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

```{admonition} Erros comuns com JSON
:class: warning

- Esquecer aspas em **chaves**
- Vírgula sobrando no final
- Usar **aspas simples** em vez de **duplas**
- Acessar caminho que não existe → erro `undefined`
- Enviar JSON mal formatado em um `POST` via HTTP
```

---

### Configurações no Node

Na configuração de um Node, sempre haverá configurações extras, que podem ser importantes em situações específicas. Vamos explicar algumas dessas opções: 👇
```{figure} imagens/conf_parameter.png
:align: center
:name: conf_parameter
```
#### Always Output Data**

**Funcionamento da Opção Always Output Data**

Quando habilitada, o nó sempre enviará uma saída, mesmo nas seguintes situações:

- 📉 **Sem dados de entrada**: Se o nó não receber dados de um nó anterior no fluxo.
- ❌ **Falha na execução**: Se ocorrer um erro durante a execução do nó.
- 🚫 **Saída vazia**: Se o nó não tiver dados para enviar após sua execução.

**Por que usar Always Output Data?**

- **Garantia de fluxo**: Mantém a consistência do fluxo, permitindo que ele continue mesmo em condições adversas.
- **Tratamento de erros**: Ajuda a lidar com erros de forma mais controlada, podendo incluir ações de contingência ou tratamento posterior.
- **Transparência e depuração**: Facilita a depuração do fluxo, permitindo visualizar onde ocorrem falhas ou lacunas nos dados.

Configuração no n8n ⚙️

Para ativar Always Output Data em um nó:

1. Abra as configurações do nó desejado no editor de fluxo do n8n.
2. Procure pela opção **"Always Output Data"** ou similar nas configurações do nó.
3. Habilite esta opção conforme necessário.

Exemplo Prático 🔍

- **Cenário**: Um nó que faz uma solicitação a uma API externa para buscar dados.
- **Uso**: Com Always Output Data ativado, o fluxo continuará mesmo se a solicitação à API falhar, garantindo que etapas subsequentes possam processar os dados disponíveis ou lidar com a falha de forma adequada.

#### Execute Once

Funcionamento do **Execute Once** 🔄

- **Quando habilitado**, o nó só será executado **uma única vez** após o acionamento inicial do fluxo, mesmo que a condição normalmente desencadeasse múltiplas execuções.
- **Cenário comum**: Imagine um fluxo que é acionado por um webhook de um sistema externo. Com **Execute Once** ativado, o nó será acionado apenas na primeira vez que o webhook for recebido, mesmo que o sistema externo envie múltiplas solicitações ao webhook.

Por que usar **Execute Once**? 🎯

- **Prevenção de execuções duplicadas**: Evita processamentos redundantes e mantém a integridade dos dados.
- **Economia de recursos**: Reduz o consumo de recursos do sistema ao limitar execuções desnecessárias do fluxo.

Configuração no n8n ⚙️

Para ativar **Execute Once** em um nó:

1. Abra as configurações do nó desejado no editor de fluxo do n8n.
2. Procure pela opção **"Execute Once"** ou similar nas configurações do nó.
3. Habilite esta opção para garantir que o nó seja executado apenas uma vez após o acionamento inicial do fluxo.

Exemplo Prático 🔍

- **Cenário**: Um webhook aciona um fluxo no n8n sempre que um novo pedido é recebido em um sistema de e-commerce.
- **Uso de Execute Once**: Com Execute Once ativado, o fluxo será acionado apenas na primeira vez que o webhook for recebido para processar o novo pedido, independentemente de quantas vezes o webhook seja acionado pelo sistema de e-commerce.

#### Retry on Fail

Funcionamento do **Retry on Fail** 🔄

- **Quando habilitado**, o nó tentará **executar a operação novamente** após uma falha inicial. Isso é útil para lidar com erros temporários, como problemas de conexão ou timeout de rede.
- **Cenário comum**: Imagine um fluxo onde um nó faz uma solicitação a uma API externa. Se houver uma falha na primeira tentativa devido a um problema de rede, o **Retry on Fail** permitirá que o nó tente novamente após um curto intervalo de tempo.

Por que usar **Retry on Fail**? 🎯

- **Redução de erros transitórios**: Ajuda a superar problemas temporários que não são persistentes.
- **Garantia de entrega**: Aumenta a confiabilidade do fluxo, garantindo que as operações sejam concluídas mesmo em condições adversas.
- **Melhoria na experiência do usuário**: Evita interrupções no serviço ao tentar resolver automaticamente problemas temporários.

Configuração no n8n ⚙️

Para ativar **Retry on Fail** em um nó:

1. Abra as configurações do nó desejado no editor de fluxo do n8n.
2. Procure pela opção **"Retry on Fail"** ou similar nas configurações do nó.
3. Habilite esta opção e configure o **número máximo de tentativas** e o **intervalo de tempo entre as tentativas** conforme necessário.

Exemplo Prático 🔍

- **Cenário**: Um nó faz uma solicitação a uma API externa para buscar dados, mas a API está temporariamente fora do ar.
- **Uso de Retry on Fail**: Com Retry on Fail ativado, o nó tentará novamente automaticamente após uma falha inicial de conexão, permitindo que o fluxo continue mesmo em condições adversas.

```{figure} imagens/retry_on_fail.png
:align: center
:name: retry_on_fail
```

Comportamento do Workflow com erros

```{figure} imagens/fig_workflow.png
:align: center
:name: fig_workflow

```
Comportamentos em Caso de Erro de um Node Específico

**Stop Workflow** ⛔

- **Descrição**: O fluxo inteiro é interrompido imediatamente quando o node específico falha.
- **Benefícios**: Evita que a falha se propague para outras partes do sistema, garantindo que apenas operações seguras sejam concluídas.
- **Cenário**: Em um fluxo de pagamento online, se houver uma falha na confirmação de pagamento, o fluxo pode ser interrompido para evitar que o pedido seja processado incorretamente.

**Continue** 🔄

- **Descrição**: O fluxo continua normalmente, mesmo que o node específico falhe.
- **Benefícios**: Evita interrupções no fluxo, permitindo que operações críticas continuem sendo executadas.
- **Cenário**: Em um fluxo de automação de e-commerce, se um node de envio de e-mail falhar, o fluxo continua para o próximo node, como atualização de status do pedido.

**Continue (using Error Output)** 🚀

- **Descrição**: O fluxo continua, usando a saída de erro do node específico para tomar ações adicionais.
- **Benefícios**: Permite que você trate erros de forma mais controlada, usando as informações do erro para tomar decisões específicas.
- **Cenário**: Se um node de validação de dados falhar, você pode usar as informações do erro para enviar um e-mail de notificação ou registrar o problema em um sistema de logs.

---

#### Resolvendo erros

Principais Erros em Workflows do n8n: O Que Observar nos Nodes

Ao começar a utilizar o n8n para criar automações, é comum encontrar dificuldades relacionadas ao funcionamento dos **nodes** (os blocos que compõem o fluxo). Muitos dos erros enfrentados por iniciantes são causados por configurações incorretas, dados mal estruturados ou falta de compreensão sobre o fluxo de informações entre os nodes.

A seguir, estão listados os **principais erros que ocorrem nos nodes** e dicas práticas para evitá-los.

---

1. ❌ Campos obrigatórios não preenchidos

**Descrição:**

Alguns nodes exigem campos obrigatórios como URLs, credenciais, IDs de planilhas, ou chaves de API. Caso não preenchidos corretamente, o node falha.

:::{tip}
Sempre revise campos marcados com "*", leia as dicas no rodapé e use as opções de ajuda ao lado de cada campo no editor.
:::
---

2. ❌ Falta de credenciais configuradas

**Descrição:**

Muitos nodes de integração (ex: Gmail, Google Sheets, Notion, Trello) dependem de credenciais autenticadas. Esquecer de configurá-las ou vinculá-las ao node gera erro de autenticação.

:::{tip}

Configure as credenciais antes de executar e certifique-se de que estão ativas e conectadas corretamente.
:::
---

3. ❌ Formato de dados incompatível

**Descrição:**

Um node pode esperar um tipo de dado (ex: número, string ou objeto JSON), mas receber outro formato. Isso gera falhas silenciosas ou erros visíveis.

**Exemplo:**

Passar um número onde se espera um texto ou enviar um array quando se espera um único item.

:::{tip}
Use o **Set Node** ou **Function Node** para ajustar dados antes de enviá-los a outros nodes.
:::

### 4. ❌ Dados ausentes ou campos inexistentes

**Descrição:**

Ao tentar acessar um campo com <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`{{$json.campoInexistente}}`</span>, o n8n retorna <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`undefined`</span> e pode gerar erro ou resultado inesperado.

:::{tip}
Use o botão de **"Executar o Node"** anterior e visualize a aba **"Output"** para confirmar se os dados esperados realmente existem.
:::

5. ❌ Expressões mal escritas

**Descrição:**

Expressões em JavaScript mal formatadas ou com erro de sintaxe podem impedir o node de funcionar.

**Exemplo de erro:**
```{code-block} json
{{ $json.valor + 10 // falta fechar o parêntese ou chave }}
```
:::{tip}
Use <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">{{(() => { ... })()}}</span> para expressões mais complexas e valide com pequenas execuções antes de usar em produção.
:::

6. ❌ Acesso incorreto a dados de outros nodes

**Descrição:**

Tentar acessar outro node da forma errada, como <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`$('Node-Errado')`</span>, ou usando o nome incorreto, gera erro ou dados vazios.

:::{tip}
Use o autocompletador (<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Cmd/Ctrl + Espaço`</span>) ao escrever expressões ou clique com botão direito no campo e selecione "Add Expression" → "Nodes".
:::

7. ❌ Não verificar se o item atual existe em arrays

**Descrição:**

Ao processar arrays, é comum esquecer que o node está tratando cada item individualmente, o que pode gerar tentativas de acessar dados que não existem naquele item.

:::{tip}
Use expressões com <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`if`</span> ou <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`try-catch`</span> para evitar que itens incompletos quebrem o fluxo.
:::

Exemplo:

```{code-block} json
{{ $json?.meuCampo || 'valor padrão' }}
```

8. ❌ Looping excessivo ou mal controlado

**Descrição:**

Usar loops mal configurados (como <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`SplitInBatches`</span> com muitos itens ou <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Merge`</span> mal estruturado) pode criar lentidão, travamentos ou comportamento inesperado.

:::{tip}
Sempre teste com poucos itens e verifique a saída de cada nó antes de escalar.
:::

---

9. ❌ Esquecer de ativar o workflow

**Descrição:**

Após testar, o workflow funciona, mas o usuário esquece de clicar em “Ativar”, então ele nunca executa automaticamente.

:::{tip}
Sempre verifique o estado do workflow após testes locais.
:::

10. ❌ Não salvar alterações antes de executar

**Descrição:**

Executar um node sem salvar alterações recentes pode causar execução com configurações antigas.

:::{tip}
Salve sempre antes de testar (<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Ctrl + S`</span> ou botão "Save").
:::

Códigos de erro mais comuns em APIs

|Código|	Significado|	Quando acontece?|
|------|---------------|--------------------|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">200 OK</span>	|Requisição bem-sucedida	|Tudo funcionou|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">201 Created</span>|Recurso criado com sucesso	|Ao fazer um POST com sucesso|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">204 No Content</span>|	Requisição bem-sucedida, sem retorno	|Ex: deletar algo|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">400 Bad Request</span>|	Erro na sua requisição	|Campos inválidos ou formato errado|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">401 Unauthorized</span>	|Falta de autenticação	|Token errado ou ausente|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">403 Forbidden</span>	|Autenticado, mas sem permissão	|Acesso negado mesmo com login|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">404 Not Found</span>	|Endpoint ou recurso não existe	|URL errada ou item inexistente|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">409 Conflict</span>	|Conflito com o estado atual	|Criar um item que já existe, por exemplo|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">422 Unprocessable Entity</span>|	Dados válidos, mas com erro lógico	|Formato certo, mas info errada (ex: CPF inválido)|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">429 Too Many Requests</span>|	Limite de chamadas atingido	|Você bateu no rate limit da API|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">500 Internal Server Error</span>	|Erro no servidor da API	|Falha interna da aplicação externa|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">502 Bad Gateway</span>	|Gateway da API falhou	|Normal em sistemas com proxies|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">503 Service Unavailable</span>|	API está fora do ar ou sobrecarregada	|Muita demanda ou manutenção|

#### # GPT n8n

💻GPT Assistente do n8n

[n8n Assistant](https://chatgpt.com/g/g-SVatmGSdQ-n8n-assistant-by-nskha?model=gpt-4o)

O Papel da Inteligência Artificial no Aprendizado do n8n

Durante o processo de aprendizado e uso da plataforma **n8n**, contar com o apoio de ferramentas baseadas em inteligência artificial pode representar um ganho significativo em produtividade, compreensão e autonomia. Um exemplo disso é o uso de assistentes especializados, como o **N8N A.I Assistant (by Nskha)**, uma versão do GPT treinada especificamente para auxiliar usuários da plataforma n8n.

Esse tipo de assistente desempenha um papel importante no processo de construção de conhecimento por diversos motivos:

1. Conhecimento especializado sobre o n8n

Ao contrário de assistentes genéricos, o N8N A.I Assistant é treinado com foco total na estrutura e funcionamento do n8n. Ele possui conhecimento atualizado sobre:

- Os principais nós (nodes) disponíveis na plataforma;
- Criação e uso de expressões;
- Integração com APIs e serviços externos;
- Tratamento de dados e manipulação de campos;
- Identificação e correção de erros comuns.

Esse domínio técnico permite ao assistente fornecer orientações precisas e contextualizadas.

2. Aprendizado guiado e personalizado

Ao interagir com o assistente, é possível obter explicações adaptadas ao nível de conhecimento do usuário (iniciante ou avançado), facilitando a compreensão de conceitos como:

- Criação de workflows do zero;
- Aplicação prática de lógica condicional e expressões;
- Estratégias para otimização e organização de automações.

Isso transforma o aprendizado em uma experiência mais interativa e eficiente.

3. Suporte técnico em tempo real

Além do aspecto didático, o assistente também pode ser utilizado como ferramenta de apoio técnico. Ele é capaz de:

- Sugerir melhorias em fluxos existentes;
- Gerar workflows em formato JSON, prontos para importação;
- Criar expressões complexas com base em requisitos específicos;
- Explicar a origem de erros e orientar sobre possíveis soluções.

Essa funcionalidade reduz a curva de aprendizado e evita que o usuário fique travado em problemas técnicos.

O uso de uma inteligência artificial especializada no n8n representa uma importante estratégia de apoio no processo de aprendizagem. Ela atua como um **tutor digital**, capaz de acelerar o entendimento da plataforma, orientar boas práticas e ajudar a resolver desafios técnicos de forma prática e acessível.

Ao incorporar essa ferramenta no estudo e uso diário do n8n, o usuário potencializa sua capacidade de aprender, experimentar e evoluir na criação de automações mais robustas e eficientes.

#### Templates

Os templates no n8n são, essencialmente, fluxos de automação (workflows) pré-construídos e prontos para uso. Eles funcionam como modelos que resolvem problemas comuns e integram diferentes aplicações de maneira lógica. Em vez de começar um workflow do zero, um usuário pode simplesmente selecionar um template, conectar suas próprias credenciais (como contas de email, APIs, planilhas) e ativar a automação em questão de minutos.

Esses templates cobrem uma vasta gama de casos de uso, como:

- **Sincronização de Dados:** Manter informações consistentes entre um CRM (como o HubSpot) e uma planilha do Google Sheets.
- **Notificações Inteligentes:** Enviar uma mensagem customizada no Slack ou Discord sempre que um novo cliente se cadastra na sua plataforma.
- **Marketing e Vendas:** Adicionar automaticamente leads de um formulário do Typeform a uma lista de email no Mailchimp.
- **Gestão de Projetos:** Criar um card no Trello a partir de um email recebido que contenha palavras-chave específicas.

A grande vantagem é que eles são totalmente customizáveis. Um template serve como um ponto de partida robusto, que pode ser expandido, modificado e adaptado para atender às necessidades exatas de um projeto, economizando um tempo de desenvolvimento significativo e expondo o usuário a boas práticas de construção de workflows.

[Baixe aqui a planilha Templates_n8n.xlsx](https://github.com/unb-lamfo-negocios-ai/LivroIAemMovimento/blob/main/Templates_n8n.xlsx)


#### Como usar n8n de graça

[Guia Self-Host n8n]([https://exemplo.com/caminho/para/planilha/Templates_n8n.xlsx](https://docs.n8n.io/hosting/?_gl=1*9qdgvv*_gcl_aw*R0NMLjE3NDkxNTA2MzAuQ2owS0NRandnSVhDQmhEQkFSSXNBRUxDOVppTXFma29NREM0em1TaU1lN05YVnc0dVZqWU1DTGYzZXNmcE91YklXR1phOERIb0ZCLUlJMGFBbHdjRUFMd193Y0I.*_gcl_au*MTAwMjExMjc2MS4xNzUwMDk4ODcz*_ga*NDMwODU3NTU0LjE3NTAwOTg2MzY.*_ga_0SC4FF2FH9*czE3NTAxMTQ4OTIkbzMkZzEkdDE3NTAxMTU1MzQkajYwJGwwJGgw))

Instalar o Docker 🐳  [The #1 containerization software for developers and teams](https://www.docker.com/products/docker-desktop/)

```{figure} imagens/docker_n8n.png
:alt: Docker n8n.
:align: center
:name: docker_n8n

```

```{admonition} Lembrando
:class: note

Isso é um atalho para utilizar a ferramenta gratuitamente, o que inclui certas limitações. Por isso, após se especializar, é interessante assinar a plataforma para uma melhor performance das suas automações. A plataforma também sempre oferece 14 dias de teste gratuito.

Qualquer dúvida ao rodar os códigos no terminal e na instalação, pergunte ao ChatGPT! Alguns detalhes são imprevisíveis.
```

<iframe width="560" height="315" src="https://www.youtube.com/embed/8hQ1u0TAyAc&t=5s" 
title="Instalação n8n via Docker" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>

#### Credenciais

O que são credenciais no n8n e como elas funcionam?

Ao trabalhar com automações no **n8n**, é comum se conectar a serviços externos, como Gmail, Google Sheets, WhatsApp, Slack, bancos de dados, APIs, entre muitos outros. Para que o n8n consiga interagir com esses serviços de forma segura e autorizada, ele precisa de algo chamado **credenciais**.

🧠 Mas o que são credenciais?

Credenciais são **informações de acesso seguras** que permitem que o n8n “fale” com outras ferramentas ou plataformas, em nome do usuário. Essas informações podem variar dependendo do serviço, mas geralmente incluem:

- **Tokens de acesso** (como chaves secretas)
- **Usuário e senha**
- **Client ID e Client Secret**
- **Chaves de API (API Keys)**
- **URLs de autenticação**

Ou seja, as credenciais **funcionam como uma ponte segura** entre o n8n e o serviço externo com o qual se deseja interagir.

---

📦 Como as credenciais atuam no n8n?

No n8n, as credenciais são criadas e armazenadas separadamente dos workflows. Isso permite que você as reutilize em múltiplos fluxos de automação de forma prática, sem precisar configurar novamente o acesso sempre que for utilizar o mesmo serviço.

O processo é simples:

1. O usuário cria uma nova credencial no painel do n8n.
2. Ele informa os dados necessários para autenticação com o serviço desejado.
3. Ao montar um fluxo (workflow), ele seleciona essa credencial nos nós (nodes) que precisam dela.
4. O n8n utiliza essas informações nos bastidores para autenticar e fazer as requisições necessárias.

Isso evita que o usuário precise se preocupar com a lógica de segurança a cada passo da automação.

---

🔐 Por que as credenciais são importantes?

O uso de credenciais traz diversos benefícios:

- ✅ **Segurança**: os dados de autenticação ficam armazenados em local protegido.
- ✅ **Padronização**: vários workflows podem utilizar a mesma credencial.
- ✅ **Facilidade de manutenção**: se a senha ou chave de API mudar, é possível atualizar a credencial em um único lugar.
- ✅ **Controle de acesso**: em ambientes com múltiplos usuários, é possível restringir quem pode usar ou editar certas credenciais.

---

🧩 Tipos de autenticação comuns no n8n

O n8n suporta diversos métodos de autenticação, tais como:

|Tipo|	Quando é usado|
|----|----------------|
|API Key|	Serviços que usam uma chave secreta única|
|OAuth2	|Google, Microsoft, Facebook, etc.|
|Basic Auth|	Serviços que exigem usuário e senha|
|Header personalizado|	APIs que requerem tokens no cabeçalho das requisições|
|Credenciais genéricas|	Para serviços customizados via HTTP Request|

```{admonition}
:class: note
Cada tipo tem campos específicos, mas o processo no n8n é sempre semelhante: informar os dados, testar a conexão e salvar.
```

Exemplo simples

Imagine que você deseja criar um fluxo no n8n que envia uma mensagem no Slack sempre que receber um e-mail. Para isso, você precisa que o n8n consiga acessar:

- Sua conta do Gmail (para ler e-mails)
- Sua conta do Slack (para enviar mensagens)

Isso exige duas credenciais:

- Uma para o **Gmail** (via OAuth2)
- Uma para o **Slack** (geralmente via Webhook ou token)

Com essas credenciais criadas e salvas, basta vinculá-las aos respectivos nós no seu fluxo — e pronto! O n8n saberá como se comunicar com cada serviço.

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

## Canva

O **Canva** é uma plataforma de design que incorporou recursos de **IA generativa**, como:  
- Criação automática de imagens.  
- Sugestão de layouts e textos.  
- Geração de apresentações com base em descrições simples.  

Embora não seja uma ferramenta técnica de desenvolvimento, **democratiza a IA** para profissionais de comunicação, marketing e design, ampliando a adoção em escala {cite}`canva2023`.  
