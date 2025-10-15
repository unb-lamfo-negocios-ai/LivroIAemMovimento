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
```

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

O n8n é, essencialmente, **um orquestrador de automações**. Sua função principal é conectar diferentes ferramentas e sistemas para que eles “conversem” entre si — e essa comunicação só é possível graças às APIs abertas desses serviços.

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

### O que é autenticação em APIs?

Autenticação é o processo de **validar quem está fazendo a requisição** à API. Sem autenticação, qualquer um poderia acessar, alterar ou deletar dados sensíveis.

**Tipos de Autenticação mais comuns em APIs**

|**Tipo**	|**Como funciona**|	**Exemplo de uso**|
|-------|-------------|---------------|
|API Key|	Chave única que identifica o usuário|	<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">api_key=XYZ123</span>? no link ou cabeçalho|
|Bearer Token (OAuth2)	|Token de acesso temporário	|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Authorization: Bearer abc.def.ghi</span>|
|Basic Auth	|Usuário + senha codificados em Base64	|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Authorization: Basic dXNlcjpwYXNz</span>|
|OAuth2 (3-legged)	|Redireciona o usuário para login	|Usado no Google, Facebook, Microsoft|
|Header Customizado|	API exige chave em cabeçalho com nome específico	|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">X-API-KEY: sua-chave-aqui</span>|
|Session Cookie / JWT|	Cookies de sessão ou tokens JWT	|Sessões autenticadas de forma segura|

#### Como autenticação se aplica no n8n?

No n8n, você configura autenticação em dois lugares:

1. Credenciais do Node:
   - **Exemplo**: Google Sheets, Gmail, WhatsApp, Supabase, Notion
   - Você usa **OAuth2** ou **API Key** cadastradas no menu de credenciais
2. Node HTTP Request (genérico):
   - Ideal para APIs sem nodes prontos
   - Você pode usar:
     - <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Header Auth</span> (com Bearer, Token, etc)
     - <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Query Auth</span>
(API Key na URL)
     - <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Basic Auth</span>
(usuário/senha codificados)
     - <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Custom Headers</span>
(nome + valor da chave)

## Credenciais

Ao trabalhar com automações no **n8n**, é comum se conectar a serviços externos, como Gmail, Google Sheets, WhatsApp, Slack, bancos de dados, APIs, entre muitos outros. Para que o n8n consiga interagir com esses serviços de forma segura e autorizada, ele precisa de algo chamado **credenciais**.

Credenciais são **informações de acesso seguras** que permitem que o n8n “fale” com outras ferramentas ou plataformas, em nome do usuário. Essas informações podem variar dependendo do serviço, mas geralmente incluem:

```{admonition} Exemplos de credenciais
:class: exemplo
- **Tokens de acesso** (como chaves secretas)
- **Usuário e senha**
- **Client ID e Client Secret**
- **Chaves de API (API Keys)**
- **URLs de autenticação**
```

Ou seja, as credenciais **funcionam como uma ponte segura** entre o n8n e o serviço externo com o qual se deseja interagir.

### Como as credenciais atuam no n8n?

No n8n, as credenciais são criadas e armazenadas separadamente dos workflows. Isso permite que você as reutilize em múltiplos fluxos de automação de forma prática, sem precisar configurar novamente o acesso sempre que for utilizar o mesmo serviço.

```{admonition} O processo é simples:
:class: note
1. O usuário cria uma nova credencial no painel do n8n.
2. Ele informa os dados necessários para autenticação com o serviço desejado.
3. Ao montar um fluxo (workflow), ele seleciona essa credencial nos nós (nodes) que precisam dela.
4. O n8n utiliza essas informações nos bastidores para autenticar e fazer as requisições necessárias.
```
Isso evita que o usuário precise se preocupar com a lógica de segurança a cada passo da automação.

```{admonition} Benefícios ao usar credenciais
:class: hint
- **Segurança**: os dados de autenticação ficam armazenados em local protegido.
- **Padronização**: vários workflows podem utilizar a mesma credencial.
- **Facilidade de manutenção**: se a senha ou chave de API mudar, é possível atualizar a credencial em um único lugar.
- **Controle de acesso**: em ambientes com múltiplos usuários, é possível restringir quem pode usar ou editar certas credenciais.
```
## Tipos de autenticação comuns no n8n

A segurança e a proteção de dados são fundamentais ao integrar diferentes serviços e APIs em seus workflows de automação. O **n8n** oferece suporte robusto a diversos métodos de autenticação, permitindo que você conecte seus workflows a praticamente qualquer serviço externo de forma segura e confiável. Cada método de autenticação é adequado para diferentes tipos de integrações e níveis de segurança, desde simples chaves de API até protocolos mais complexos como OAuth2. Compreender esses métodos é essencial para configurar conexões seguras e garantir que suas automações funcionem adequadamente respeitando as políticas de segurança de cada plataforma.

### Exemplos de métodos de autenticação

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

```{admonition} Exemplo Prático: Integração Gmail + Slack
:class: exemplo
Imagine que você deseja criar um fluxo no n8n que envia uma mensagem no Slack sempre que receber um e-mail. Para isso, você precisa que o n8n consiga acessar:

- Sua conta do Gmail (para ler e-mails)
- Sua conta do Slack (para enviar mensagens)

Isso exige duas credenciais:

- Uma para o **Gmail** (via OAuth2)
- Uma para o **Slack** (geralmente via Webhook ou token)

Com essas credenciais criadas e salvas, basta vinculá-las aos respectivos nós no seu fluxo — e pronto! O n8n saberá como se comunicar com cada serviço.
```


## Nodes de Gatilhos

Os Trigger Nodes são responsáveis por iniciar um fluxo automaticamente. Eles fazem com que o n8n espere por um evento externo — como o recebimento de um e-mail, uma nova linha em uma planilha ou uma mensagem em um chat — antes de executar as próximas etapas do workflow.

Sem um gatilho configurado, o fluxo precisa ser iniciado manualmente. Com um trigger, o n8n passa a reagir de forma automática e inteligente, tornando o processo contínuo e dinâmico.


|Tipo de Node Trigger	|Finalidade	|Exemplo|
|-----------------------|-----------|-------|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Webhook</span>|Ativado por uma requisição HTTP|	Um sistema externo envia um POST e inicia o fluxo|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Form Trigger</span>	|Ativado quando alguém preenche um formulário	|Lead preenche dados de contato|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Cron</span>	|Executa em horários definidos	|Enviar relatório toda segunda às 8h|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Google Drive Trigger</span>	|Ativado quando um arquivo é criado/atualizado em uma pasta do Drive	|Novo contrato adicionado no Drive|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Telegram Trigger</span>	|Reage a mensagens recebidas no bot do Telegram	|Cliente envia “Oi” e inicia atendimento|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Email Trigger (IMAP)</span>	|Dispara ao receber um e-mail	|Processar anexos de e-mails automaticamente|
|<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Shopify Trigger, Notion Trigger, etc.</span>	|Ativam fluxos com base em eventos de plataformas específicas|	Novo pedido na loja, nova nota criada|

## Nodes Essenciais

**Nodes essenciais** são os blocos fundamentais que **não dependem de integrações externas** (como Gmail, WhatsApp, Notion...) e que **manipulam dados, controlam o fluxo e estruturam a lógica** do seu workflow.

```{admonition} Os nodes são universais
:class: note
Os nodes são usados em quase todos os tipos de automações e fazem parte do "cérebro" da automação, funcionando como:

- **Variáveis** (<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Set`</span>)
- **Condições** (<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`IF`</span>, <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Switch`</span>)
- **Regras e lógica** (<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Function`</span>, <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Code`</span>)
- **Controle de tempo** (<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Wait`</span>)
- **Divisão e união de dados** (<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Split`</span>, <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Merge`</span>)
```

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

## Node Set
        
O node <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">Set</span> serve para **criar, modificar ou excluir dados no seu fluxo**, sem depender de fontes externas. Ele é um dos **nodes essenciais** do n8n.
    
```{admonition}
:class: hint
Pense no Node Set como um "bloco de notas" onde você define ou ajusta valores antes de enviar para um e-mail, API, IA ou planilha.
```

**Principais usos do Set**

|Objetivo|	Exemplo|
|--------|----------|
|Criar variáveis	|Criar <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">status: "novo"</span> ou <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">tipo: "lead quente"</span>|
|Editar campos	|Alterar o nome de uma variável, como <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">telefone → WhatsApp</span>|
|Renomear dados recebidos	|Padronizar nomes de campos antes de enviar a outro sistema|
|Deixar o dado pronto para IA/API	|Juntar nome + empresa num só campo|

```{admonition} Como funciona na prática
:class: note

No node <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Set`</span> você define:

- **O nome do campo**: ex. <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`mensagem`</span>
- **O valor**: ex. <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`"Olá, {{ $json['nome'] }}. Tudo bem?"`</span>
```

Você pode usar **expressões dinâmicas**, como:

```{code-block} text
Olá {{ $json['nome'] }}, sua empresa {{ $json['empresa'] }} foi registrada com sucesso!
```

```{admonition} **Dica de ouro**
:class: tip

Você pode marcar **“Keep Only Set”** se quiser **remover todos os outros campos** e manter **somente os definidos no <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Set`</span>**. Isso é útil para simplificar o payload antes de enviar para um e-mail, API ou IA.
```

## Node Filter

O **Filter** serve para **filtrar dados** que passam pelo seu workflow, ou seja, **permitir apenas itens que atendam a certas condições** continuarem para os próximos nodes.

Itens que **não passam pelo filtro** são descartados (não seguem adiante no fluxo).

```{admonition} Quando usar o Filter?
:class: tip
- Quando você só quer continuar o fluxo com itens que correspondem a critérios específicos.
- Para separar leads qualificados de não qualificados, por exemplo.
- Para processar apenas registros com status específico, valores mínimos/máximos, campos preenchidos, etc.
```

```{admonition} Como funciona?
:class: note
1. **Entrada:** Recebe uma lista de itens (ex: vários leads, pedidos, respostas de API...).
2. **Condições:** Você define as regras (ex: “status” igual a “aprovado” ou “valor” maior que 1000).
3. **Saída:** Só os itens que **passam nas condições** seguem para os próximos nodes.
```

**Exemplo prático**: Suponha que você tem vários leads:

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

## Node Agreggate
    
O Aggregate Node é utilizado para **combinar e resumir dados** provenientes de várias entradas dentro de um fluxo no n8n. Ele permite reunir informações dispersas e transformá-las em um único resultado consolidado, facilitando análises, relatórios e integrações posteriores.

```{admonition} Com o Node Agreggate é possível:
:class: note

- Juntar textos de vários registros em uma única string.

- Somar valores ou calcular médias de campos numéricos.

- Criar listas agrupadas ou com valores únicos.

- Gerar estatísticas básicas, como máximo, mínimo e contagem.

- Transformar múltiplos itens em um único item, útil para gerar resumos, relatórios ou arquivos consolidados.
```

```{admonition} Como funciona na prática?
:class: note

- **Entrada:** Recebe vários itens (ex: linhas do Google Sheets, respostas de API, vários leads).

- **Configuração:**

  - Você escolhe qual campo quer agregar (ex: <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`nome`</span>, <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`valor`</span>, <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`mensagem`</span>).
  
  - Define a operação: **somar**, **contar**, **juntar**, **média**, **min/max** ou **customizada**.

- **Saída:** Entrega **um ou poucos itens** já agregados/resumidos.
```

```{admonition} Exemplos práticos
:class: note
```

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

```{admonition} Use o node **Aggregate** sempre que quiser, para:
:class: tip
- Fazer relatórios resumidos
- Mandar um único e-mail com dados agrupados
- Preparar dados para dashboards ou integrações externas
```

## Node HTTP Request
     
O **HTTP Request** é como um “mensageiro digital” que faz o n8n **conversar com outros sites, sistemas ou aplicativos na internet**.
    
Ele serve para **buscar informações** em outros lugares (ex: previsão do tempo, dados de clientes, valores de moedas), **enviar dados** (ex: criar um lead, registrar uma compra), ou **fazer qualquer ação** que esses sistemas permitam via internet.

```{admonition}  Como funciona na prática?
:class: note
    
Imagine que você quer saber a previsão do tempo. Você:
    
1. Abre um navegador,
2. Digita um endereço (URL) e,
3. Vê a resposta (previsão) na tela.
```
    
No n8n, o **node HTTP Request** faz isso automaticamente e pode:
    
- Buscar informações para você,
- Enviar formulários,
- Integrar com APIs de bancos, e-commerces, WhatsApp, Google, e qualquer outro sistema.


**Passos básicos de uso**:

1. Escolher o endereço (URL)
    
    Onde o n8n vai buscar ou enviar informação. Exemplo: `https://api.exemplo.com/usuarios`
    
2. Escolher a ação (verbo HTTP)
    - <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`GET`</span> = Buscar dados
    - <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`POST`</span> = Enviar/criar dados
    - <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`PUT/PATCH`</span> = Atualizar dados
    - <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`DELETE`</span> = Apagar dados
3. (Opcional) Enviar dados junto
    
    Por exemplo, se for um formulário ou cadastro.
    
4. Receber a resposta
    
    O node traz os dados do site/aplicativo, que podem ser usados nos próximos passos do fluxo.

```{admonition} Para que serve no dia a dia?
:class: note

- Integrar com sistemas que **não têm node próprio** no n8n
- Buscar ou enviar dados em **APIs públicas ou privadas**
- Criar automações sob medida com qualquer serviço online
```

### Exemplo bem simples

Você quer buscar o preço do dólar hoje:

- Node HTTP Request com URL de uma API de câmbio e método <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`GET`</span>
- O n8n traz a cotação para o seu fluxo, pronta para ser usada.

## Node Respond to Webhook
    
O **Respond to Webhook** é como um **"balcão de respostas"** do seu fluxo de automação.
    
Ele serve para **enviar uma resposta automática para quem chamou o seu workflow**.

```{admonition}  Como funciona na prática?
:class: note
    
Imagine que seu fluxo do n8n recebe um pedido de fora (de um site, sistema ou aplicativo) usando um **Webhook** (um “sininho” que escuta quando algo acontece).
    
- O **Webhook** recebe a mensagem (ex: dados de um formulário enviado).
- O seu fluxo faz tudo o que precisa (salva, calcula, consulta, etc.).
- **No final**, você usa o node **Respond to Webhook** para **responder de volta** (confirmando que deu certo, enviando dados, etc).
```

```{admonition}  Para que serve?
:class: note    
 - Enviar confirmações automáticas para integrações externas.
 - Responder sistemas, sites, chatbots, apps ou pessoas que aguardam uma resposta rápida.
 - Retornar dados processados pelo n8n (por exemplo, status, valores, cálculos).
 ```
    
 ```{admonition}
:class: tip
    
 Se não usar o **Respond to Webhook**, quem chamou o seu fluxo pode **ficar esperando** e não receber resposta nenhuma, ou receber uma mensagem padrão de erro.
```

### Exemplo de uso: Respondendo a pedidos automaticamente

Imagine que você tem um site onde os visitantes podem solicitar um orçamento. Assim que eles preenchem o formulário, você quer que uma **resposta automática** apareça imediatamente na tela, confirmando o recebimento.

O **Node Respond to Webhook** que permite **enviar uma resposta imediata ao navegador do usuário** assim que o fluxo termina sua execução.

```{admonition} Fluxo no n8n
:class: exemplo

1. O **Webhook Node** recebe os dados enviados pelo formulário do site.  
2. O fluxo realiza os cálculos necessários — como consultar preços, aplicar regras ou compor uma resposta personalizada.  
3. O **Respond to Webhook Node** envia a resposta automática de volta ao site, por exemplo:  
   _“Orçamento recebido! Em breve, entraremos em contato.”_
```

Esse tipo de resposta em tempo real **melhora a experiência do usuário**, evita redirecionamentos e torna a automação muito mais fluida e interativa.


## Nodes de Aplicativo

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

  ```{admonition} Exemplo
  :class: exemplo
  O node do Google Sheets permite criar, ler, atualizar e deletar linhas; o node do WhatsApp pode enviar mensagens de texto, imagem, áudio, etc.
  ```

5. **Tratamento de Erros**:
    
Caso o app externo retorne um erro (ex: falha de autenticação, dados inválidos, limite atingido), o node pode exibir esse erro no painel ou permitir o uso de nodes de controle (como o IF) para tratar falhas e tomar decisões alternativas no fluxo.
    
6. **Personalização**:
    
Os nodes de aplicativo geralmente permitem **personalizar mensagens, campos e payloads** usando expressões dinâmicas do n8n, tornando cada automação adaptada ao contexto do lead ou usuário.

```{admonition} Exemplo prático de sequência:
:class: exemplo

Um formulário captura dados do lead, que são gravados em uma planilha via Node de Aplicativo (Google Sheets). Em seguida, outro Node envia uma mensagem personalizada pelo WhatsApp e, por fim, um terceiro notifica o time comercial por Gmail.

> Formulário → Google Sheets (grava dados) → WhatsApp (mensagem personalizada) → Gmail (notificação comercial).
```

## Linguagem JSON

**JSON (JavaScript Object Notation)** é um formato leve de troca de dados, baseado em texto. Ele é utilizado para **armazenar e transmitir informações estruturadas** entre sistemas, especialmente em APIs e integrações como as feitas no **n8n**.

```{code-block} json
{
  "nome": "Lucas",
  "idade": 30,
  "ativo": true}
```

- As **chaves** são sempre entre aspas
- Os **valores** podem ser string, número, booleano, objeto, array, ou `null`

### Os blocos básicos do JSON

Os blocos são as unidades estruturais do JSON que organizam informações em padrões específicos. 

- Um bloco de objeto {} agrupa pares de chave-valor, permitindo organizar dados relacionados—por exemplo, um bloco contendo "nome": "João" e "email": "joao@email.com".
- Um bloco de array [] armazena listas de elementos em sequência, ideal para coleções como múltiplos leads ou mensagens.

Cada bloco pode conter diferentes tipos de dados: strings (texto), números (inteiros e decimais), booleanos (verdadeiro/falso) e null (vazio). Esses tipos garantem que as informações sejam processadas corretamente quando fluem entre Nodes de Aplicativo—um array de objetos, por exemplo, permite que um Node envie múltiplos contatos ao WhatsApp em uma única operação de IA.

```{code-block} json{
  "nome": "João",
  "email": "joao@email.com",
  "ativo": true,
  "contatos": [
    {"telefone": "11999999999", "plataforma": "whatsapp"},
    {"telefone": "11988888888", "plataforma": "sms"}
  ]
}
```

```{admonition} Os blocos de objeto e array são complementares:
:class: note
objetos organizam dados relacionados horizontalmente, enquanto arrays os organizam verticalmente em sequência.
```

### Tipos de Dados

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

**JSON alinhado: Um objeto dentro do outro**

Quando precisamos representar informações hierárquicas ou relacionadas, podemos aninhar objetos JSON uns dentro dos outros, criando uma estrutura de dados mais rica e organizada.

```{code-block} json
    {
      "usuario": {
        "nome": "Ana",
        "contato": {
          "email": "ana@exemplo.com",
          "telefone": "123456"
        }
  }

```

No exemplo acima temos objetos dentro de outros objetos. Acessar isso no n8n exige navegação com <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">usuario.contato.email</span>.

### JSON vs. XML vs. CSV

|Formato|	Legibilidade|	Peso	|Uso moderno|
|-------|---------------|-----------|-----------|
|JSON|	Alta	|Leve|	🔥 Amplamente usado|
|XML	|Verboso	|Pesado	|Usado em sistemas antigos|
|CSV|	Simples	|Muito leve	|Ideal para planilhas|


```{admonition}
:class: note
JSON é preferido em APIs e automações como as do n8n.
```

### Como o JSON é usado no n8n?

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


### Configurações no Node

Todo Node possui configurações extras além das básicas. Estas opções são fundamentais para cenários específicos e otimizam o funcionamento da automação.

Na configuração de um node, sempre haverá configurações extras, que podem ser importantes em situações específicas. Vamos explicar algumas dessas opções: 👇
```{figure} imagens/conf_parameter.png
:align: center
:name: conf_parameter
```
## Always Output Data

**Always Output Data** é uma configuração que garante a continuidade do fluxo de automação, mesmo quando ocorrem falhas.

```{admonition} Como funciona
:class: note

- **Comportamento padrão:** Quando um Node encontra um erro, ele interrompe a execução e não envia dados para os próximos passos da sequência.

- **Com Always Output Data ativado:** O Node continua a cadeia de automação mesmo após uma falha, passando os dados disponíveis para o próximo Node.
```

```{admonition} O que é transmitido
:class: note
Os dados enviados podem incluir:
- Mensagens de erro
- Valores parciais processados
- Informações de status da operação
```

```{admonition} Benefícios
:class: tip

Esta configuração permite:
- **Tratamento de falhas:** Criar lógicas alternativas para lidar com erros
- **Logging de erros:** Registrar problemas para análise posterior
- **Fluxos alternativos:** Direcionar a automação por caminhos diferentes conforme o resultado
```

### Funcionamento da Opção Always Output Data

```{admonition} Comportamento sem Always Output Data
:class: note
Quando esta opção está **desativada**:
- Um Node que falha bloqueia toda a sequência de automação
- Os dados não são transmitidos para os próximos Nodes
- **Exemplo:** Se um Node do Google Sheets não consegue gravar dados, nenhuma informação segue para o Node do WhatsApp
```

```{admonition} Comportamento com Always Output Data
:class: note

Quando esta opção está **ativada**:
- Mesmo com a falha, o Node continua alimentando a cadeia
- Os dados disponíveis são transmitidos para os próximos Nodes
- A automação não é interrompida completamente
```

```{admonition} Possibilidades de tratamento
:class: note
Com os dados transmitidos, os Nodes posteriores podem:
- Registrar o erro em um banco de dados
- Enviar alertas para a equipe
- Executar ações de contingência
- Redirecionar o fluxo para caminhos alternativos
```

```{admonition} Vantagens
class: note
- **Maior resiliência:** Automações que continuam funcionando mesmo com falhas pontuais
- **Melhor controle:** Gerenciamento detalhado de cenários de erro
- **Confiabilidade:** Essencial para operações críticas de IA que não podem ser simplesmente interrompidas
```

Quando habilitada, o nó sempre enviará uma saída, mesmo nas seguintes situações:

- **Sem dados de entrada**: Se o nó não receber dados de um nó anterior no fluxo.
- **Falha na execução**: Se ocorrer um erro durante a execução do nó.
- **Saída vazia**: Se o nó não tiver dados para enviar após sua execução.

### Configuração no n8n️

Para ativar Always Output Data em um nó:

1. Abra as configurações do nó desejado no editor de fluxo do n8n.
2. Procure pela opção **"Always Output Data"** ou similar nas configurações do nó.
3. Habilite esta opção conforme necessário.

```{admonition} Exemplo Prático
:class: exemplo

- **Cenário**: Um nó que faz uma solicitação a uma API externa para buscar dados.
- **Uso**: Com Always Output Data ativado, o fluxo continuará mesmo se a solicitação à API falhar, garantindo que etapas subsequentes possam processar os dados disponíveis ou lidar com a falha de forma adequada.
```

## Execute Once

**Execute Once** é uma configuração que limita a execução de um Node a apenas uma vez, independentemente de quantas vezes a condição de acionamento seja atingida.

```{admonition} Como funciona
:class: note
- Quando **habilitado**, o Node será executado **somente na primeira vez** após o acionamento inicial do fluxo
- Execuções subsequentes que normalmente ativariam o Node são ignoradas
- A restrição permanece ativa durante toda a sessão do fluxo
```

```{admonition} Exemplo prático
:class: exemplo
Imagine um fluxo acionado por um webhook de um sistema externo:

- **Sem Execute Once:** Cada requisição recebida pelo webhook executa o Node novamente
- **Com Execute Once:** Apenas a primeira requisição aciona o Node, mesmo que o sistema externo envie múltiplas solicitações
```

### Por que usar Execute Once?

**Prevenção de execuções duplicadas**
- Evita processamentos redundantes da mesma operação
- Mantém a integridade dos dados ao impedir registros duplicados
- Garante que ações críticas ocorram apenas uma vez

**Economia de recursos**
- Reduz o consumo de recursos computacionais
- Diminui custos operacionais ao evitar execuções desnecessárias
- Otimiza o desempenho geral do fluxo de automação

**Quando aplicar**

Esta configuração é especialmente útil em:
- Integrações com sistemas externos que podem enviar requisições duplicadas
- Operações de gravação em bancos de dados
- Envio de notificações ou alertas únicos
- Processamentos que devem ocorrer apenas na inicialização do fluxo

### Configuração no n8n️

Para ativar **Execute Once** em um nó:

1. Abra as configurações do nó desejado no editor de fluxo do n8n.
2. Procure pela opção **"Execute Once"** ou similar nas configurações do nó.
3. Habilite esta opção para garantir que o nó seja executado apenas uma vez após o acionamento inicial do fluxo.

```{admonition} Exemplo Prático
:class: exemplo

- **Cenário**: Um webhook aciona um fluxo no n8n sempre que um novo pedido é recebido em um sistema de e-commerce.
- **Uso de Execute Once**: Com Execute Once ativado, o fluxo será acionado apenas na primeira vez que o webhook for recebido para processar o novo pedido, independentemente de quantas vezes o webhook seja acionado pelo sistema de e-commerce.
```

## Retry on Fail

**Retry on Fail** é uma configuração que permite ao Node tentar executar uma operação novamente após uma falha inicial, aumentando a resiliência do fluxo de automação.

```{admonition} Como funciona
:class: note
- Quando **habilitado**, o Node realiza novas tentativas automaticamente após uma falha
- As tentativas ocorrem após intervalos de tempo configuráveis
- O processo se repete até obter sucesso ou atingir o número máximo de tentativas
```

**Quando é útil**

Esta configuração é especialmente eficaz para lidar com:
- Problemas temporários de conexão
- Timeouts de rede
- Instabilidades momentâneas em APIs externas
- Erros transitórios que tendem a se resolver rapidamente

```{admonition} Exemplo prático
:class: exemplo
Imagine um fluxo onde um Node faz uma solicitação a uma API externa:

- **Primeira tentativa:** Falha devido a um problema momentâneo de rede
- **Com Retry on Fail:** O Node aguarda um intervalo e tenta novamente automaticamente
- **Resultado:** A operação é concluída com sucesso na segunda ou terceira tentativa
```

### Por que usar Retry on Fail?

**Redução de erros transitórios**
- Supera problemas temporários que não são persistentes
- Elimina falhas causadas por instabilidades pontuais
- Aumenta a taxa de sucesso das operações

**Garantia de entrega**
- Aumenta a confiabilidade do fluxo de automação
- Garante que operações críticas sejam concluídas mesmo em condições adversas
- Reduz a necessidade de intervenção manual

**Melhoria na experiência do usuário**
- Evita interrupções no serviço para o usuário final
- Resolve automaticamente problemas temporários de forma transparente
- Mantém a continuidade das operações sem impacto perceptível

```{admonition} Boas práticas
:class: hint
- Configure intervalos adequados entre as tentativas para não sobrecarregar sistemas
- Defina um número máximo razoável de tentativas
- Combine com **Always Output Data** para registrar falhas persistentes
- Use em operações suscetíveis a erros temporários, não para problemas estruturais
```

### Configuração no n8n️

Para ativar **Retry on Fail** em um nó:

1. Abra as configurações do nó desejado no editor de fluxo do n8n.
2. Procure pela opção **"Retry on Fail"** ou similar nas configurações do nó.
3. Habilite esta opção e configure o **número máximo de tentativas** e o **intervalo de tempo entre as tentativas** conforme necessário.

```{admonition} Exemplo Prático
:class: exemplo

- **Cenário**: Um nó faz uma solicitação a uma API externa para buscar dados, mas a API está temporariamente fora do ar.
- **Uso de Retry on Fail**: Com Retry on Fail ativado, o nó tentará novamente automaticamente após uma falha inicial de conexão, permitindo que o fluxo continue mesmo em condições adversas.
```

## Comportamento do workflow com erros

Quando um Node encontra uma falha durante a execução, você pode definir como o fluxo de automação deve reagir. Existem três estratégias principais para gerenciar erros, cada uma adequada a diferentes necessidades e cenários. 

```{figure} ../imagens/fig_workflow.png
---
height: 150px
name: fig_workflow
---
Estratégias para gerenciar erros.
```

### 1. Stop Workflow

**O que faz:**
- Interrompe o fluxo inteiro imediatamente quando o Node específico falha
- Nenhum Node subsequente é executado
- A execução é encerrada no ponto de falha

**Quando usar:**
- Operações críticas onde erros não podem ser tolerados
- Processos que dependem estritamente do sucesso de cada etapa
- Situações onde continuar após um erro causaria inconsistências graves

**Benefícios:**
- Evita que a falha se propague para outras partes do sistema
- Garante que apenas operações completamente seguras sejam concluídas
- Mantém a integridade dos dados ao impedir processamentos parciais

```{admonition} Exemplo prático
:class: exemplo

Em um fluxo de pagamento online:
- Se houver falha na confirmação do pagamento, o fluxo é interrompido imediatamente
- Isso evita que o pedido seja processado incorretamente
- Previne cobranças duplicadas ou entregas sem pagamento confirmado
```

### 2. Continue

**O que faz:**
- O fluxo continua normalmente para os próximos Nodes
- A falha é registrada, mas não bloqueia a execução
- Nodes subsequentes são executados como se nada tivesse acontecido

**Quando usar:**
- Operações não-críticas que podem falhar sem comprometer o fluxo principal
- Processos onde algumas etapas são opcionais
- Situações onde a continuidade é mais importante que o sucesso de cada Node

**Benefícios:**
- Evita interrupções desnecessárias no fluxo
- Permite que operações críticas subsequentes continuem sendo executadas
- Aumenta a robustez do fluxo em ambientes instáveis

```{admonition} Exemplo prático:
:class: exemplo
Em um fluxo de automação de e-commerce:
- Se um Node de envio de e-mail de confirmação falhar, o fluxo continua
- O próximo Node atualiza o status do pedido normalmente
- O cliente pode receber o produto mesmo se o e-mail não for enviado
```

### 3. Continue (using Error Output) 

**O que faz:**
- O fluxo continua, mas utiliza a saída de erro do Node que falhou
- As informações do erro são passadas para os próximos Nodes
- Permite criar caminhos alternativos específicos para tratamento de erros

**Quando usar:**
- Situações que exigem tratamento personalizado de erros
- Processos onde você precisa registrar, notificar ou remediar falhas
- Fluxos que necessitam de ações específicas baseadas no tipo de erro

**Benefícios:**
- Permite tratamento controlado e inteligente de erros
- Possibilita usar informações detalhadas do erro para tomar decisões
- Combina resiliência com visibilidade sobre problemas

```{admonition} Exemplo prático:

Em um fluxo de validação de dados:
- Se um Node de validação falhar, você captura os detalhes do erro
- Com essas informações, você pode:
  - Enviar um e-mail de notificação à equipe técnica
  - Registrar o problema em um sistema de logs
  - Acionar um Node de tratamento específico para aquele tipo de erro
  - Criar relatórios detalhados sobre falhas recorrentes
```

A tabela abaixo resume as principais diferenças entre as três estratégias, facilitando a escolha da abordagem mais adequada para cada situação:

| Estratégia | Continua o Fluxo? | Usa Dados do Erro? | Melhor Para |
|------------|-------------------|--------------------| ------------|
| **Stop Workflow** | ❌ Não | ❌ Não | Operações críticas |
| **Continue** | ✅ Sim | ❌ Não | Operações não-críticas |
| **Continue (Error Output)** | ✅ Sim | ✅ Sim | Tratamento inteligente de erros |Tentar novamenteClaude ainda não tem a capacidade de executar o código que gera.

### Resolvendo erros

Ao começar a utilizar o n8n para criar automações, é comum encontrar dificuldades relacionadas ao funcionamento dos **nodes** (os blocos que compõem o fluxo). Muitos dos erros enfrentados por iniciantes são causados por configurações incorretas, dados mal estruturados ou falta de compreensão sobre o fluxo de informações entre os nodes.

A seguir, estão listados os **principais erros que ocorrem nos nodes** e dicas práticas para evitá-los.

#### 1. Campos obrigatórios não preenchidos

Alguns nodes exigem campos obrigatórios como URLs, credenciais, IDs de planilhas, ou chaves de API. Caso não preenchidos corretamente, o node falha.

:::{tip}
Sempre revise campos marcados com "*", leia as dicas no rodapé e use as opções de ajuda ao lado de cada campo no editor.
:::


#### 2. Falta de credenciais configuradas

Muitos nodes de integração (ex: Gmail, Google Sheets, Notion, Trello) dependem de credenciais autenticadas. Esquecer de configurá-las ou vinculá-las ao node gera erro de autenticação.

:::{tip}

Configure as credenciais antes de executar e certifique-se de que estão ativas e conectadas corretamente.
:::


#### 3. Formato de dados incompatível
Um node pode esperar um tipo de dado (ex: número, string ou objeto JSON), mas receber outro formato. Isso gera falhas silenciosas ou erros visíveis.

```{admonition} Exemplo
:class: exemplo

Passar um número onde se espera texto ou enviar um array quando se espera um único item.
```

:::{tip}
Use o **Set Node** ou **Function Node** para ajustar dados antes de enviá-los a outros nodes.
:::

#### 4. Dados ausentes ou campos inexistentes

Ao tentar acessar um campo com <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`{{$json.campoInexistente}}`</span>, o n8n retorna <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`undefined`</span> e pode gerar erro ou resultado inesperado.

:::{tip}
Use o botão de **"Executar o Node"** anterior e visualize a aba **"Output"** para confirmar se os dados esperados realmente existem.
:::

#### 5. Expressões mal escritas
Expressões em JavaScript mal formatadas ou com erro de sintaxe podem impedir o node de funcionar.

**Exemplo de erro:**
```{code-block} json
{{ $json.valor + 10 // falta fechar o parêntese ou chave }}
```
:::{tip}
Use <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">{{(() => { ... })()}}</span> para expressões mais complexas e valide com pequenas execuções antes de usar em produção.
:::

#### 6. Acesso incorreto a dados de outros nodes

Tentar acessar outro node da forma errada, como <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`$('Node-Errado')`</span>, ou usando o nome incorreto, gera erro ou dados vazios.

:::{tip}
Use o autocompletador (<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Cmd/Ctrl + Espaço`</span>) ao escrever expressões ou clique com botão direito no campo e selecione "Add Expression" → "Nodes".
:::

#### 7. Não verificar se o item atual existe em arrays

Ao processar arrays, é comum esquecer que o node está tratando cada item individualmente, o que pode gerar tentativas de acessar dados que não existem naquele item.

:::{tip}
Use expressões com <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`if`</span> ou <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`try-catch`</span> para evitar que itens incompletos quebrem o fluxo.
:::

**Exemplo:**

```{code-block} json
{{ $json?.meuCampo || 'valor padrão' }}
```

#### 8. Looping excessivo ou mal controlado

Usar loops mal configurados (como <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`SplitInBatches`</span> com muitos itens ou <span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Merge`</span> mal estruturado) pode criar lentidão, travamentos ou comportamento inesperado.

:::{tip}
Sempre teste com poucos itens e verifique a saída de cada nó antes de escalar.
:::

#### 9. Esquecer de ativar o workflow

Após testar, o workflow funciona, mas o usuário esquece de clicar em “Ativar”, então ele nunca executa automaticamente.

:::{tip}
Sempre verifique o estado do workflow após testes locais.
:::

#### 10. Não salvar alterações antes de executar

Executar um node sem salvar alterações recentes pode causar execução com configurações antigas.

:::{tip}
Salve sempre antes de testar (<span style="background-color: #f2f2f2; border-radius: 5px; padding: 2px 6px; font-family: monospace; color: #d6336c; border: 1px solid #f2f2f2;">`Ctrl + S`</span> ou botão "Save").
:::

#### Códigos de erro mais comuns em APIs

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

## GPT n8n

O **n8n** oferece integração nativa com modelos de linguagem GPT, permitindo que você incorpore inteligência artificial generativa diretamente em seus fluxos de automação. Com essa funcionalidade, é possível criar automações que processam linguagem natural, geram conteúdo automaticamente, analisam textos, respondem perguntas de forma inteligente e tomam decisões baseadas em contexto. Essa integração transforma fluxos de trabalho simples em soluções sofisticadas que combinam automação tradicional com as capacidades avançadas de IA, abrindo possibilidades desde chatbots inteligentes até análise automatizada de documentos e geração de conteúdo personalizado em escala.

### GPT Assistente do n8n

Durante o processo de aprendizado e uso da plataforma **n8n**, contar com o apoio de ferramentas baseadas em inteligência artificial pode representar um ganho significativo em produtividade, compreensão e autonomia. 

```{admonition} O **N8N A.I Assistant (by Nskha)**
:class: exemplo

Um exemplo disso é o uso de assistentes especializados, como o **N8N A.I Assistant (by Nskha)**, uma versão do GPT treinada especificamente para auxiliar usuários da plataforma n8n.

Ao clicar no link abaixo você pode ter a experiência de usar o N8N A.I Assistant (by Nskha):
[n8n Assistant](https://chatgpt.com/g/g-SVatmGSdQ-n8n-assistant-by-nskha?model=gpt-4o)
```

Abaixo estão relacionados os principais motivos pelos quais esse tipo de assistente desempenha um papel importante no processo de construção de conhecimento:

#### 1. Conhecimento especializado sobre o n8n

Ao contrário de assistentes genéricos, o N8N A.I Assistant é treinado com foco total na estrutura e funcionamento do n8n. 

Ele possui **conhecimento atualizado** sobre:

- Os principais nós (nodes) disponíveis na plataforma;
- Criação e uso de expressões;
- Integração com APIs e serviços externos;
- Tratamento de dados e manipulação de campos;
- Identificação e correção de erros comuns.


Esse domínio técnico permite ao assistente fornecer orientações precisas e contextualizadas.

#### 2. Aprendizado guiado e personalizado

Ao interagir com o assistente, é possível obter explicações adaptadas ao nível de conhecimento do usuário (iniciante ou avançado), facilitando a compreensão de conceitos como:

- Criação de workflows do zero;
- Aplicação prática de lógica condicional e expressões;
- Estratégias para otimização e organização de automações.

Isso transforma o aprendizado em uma experiência mais interativa e eficiente.

#### 3. Suporte técnico em tempo real

Além do aspecto didático, o assistente também pode ser utilizado como ferramenta de apoio técnico. 

Ele é capaz de:

- Sugerir melhorias em fluxos existentes;
- Gerar workflows em formato JSON, prontos para importação;
- Criar expressões complexas com base em requisitos específicos;
- Explicar a origem de erros e orientar sobre possíveis soluções.

Essa funcionalidade reduz a curva de aprendizado e evita que o usuário fique travado em problemas técnicos.

O uso de uma inteligência artificial especializada no n8n representa uma importante estratégia de apoio no processo de aprendizagem. Ela atua como um **tutor digital**, capaz de acelerar o entendimento da plataforma, orientar boas práticas e ajudar a resolver desafios técnicos de forma prática e acessível.

Ao incorporar essa ferramenta no estudo e uso diário do n8n, o usuário potencializa sua capacidade de aprender, experimentar e evoluir na criação de automações mais robustas e eficientes.

## Templates

Os templates no n8n são, essencialmente, fluxos de automação (workflows) pré-construídos e prontos para uso. Eles funcionam como modelos que resolvem problemas comuns e integram diferentes aplicações de maneira lógica. Em vez de começar um workflow do zero, um usuário pode simplesmente selecionar um template, conectar suas próprias credenciais (como contas de email, APIs, planilhas) e ativar a automação em questão de minutos.

```{admonition} Esses templates cobrem uma vasta gama de casos de uso, como:
:class: note
- **Sincronização de Dados:** Manter informações consistentes entre um CRM (como o HubSpot) e uma planilha do Google Sheets.
- **Notificações Inteligentes:** Enviar uma mensagem customizada no Slack ou Discord sempre que um novo cliente se cadastra na sua plataforma.
- **Marketing e Vendas:** Adicionar automaticamente leads de um formulário do Typeform a uma lista de email no Mailchimp.
- **Gestão de Projetos:** Criar um card no Trello a partir de um email recebido que contenha palavras-chave específicas.
```

A grande vantagem é que eles são totalmente customizáveis. Um template serve como um ponto de partida robusto, que pode ser expandido, modificado e adaptado para atender às necessidades exatas de um projeto, economizando um tempo de desenvolvimento significativo e expondo o usuário a boas práticas de construção de workflows.

```{admonition} Comece agora com Templates
:class: seealso
Para facilitar seus primeiros passos e acelerar a criação de automações, disponibilizamos uma planilha com templates prontos para uso!

Baixe aqui a planilha [Templates_n8n.xlsx](https://github.com/unb-lamfo-negocios-ai/LivroIAemMovimento/blob/main/Templates_n8n.xlsx) e explore exemplos práticos que você pode adaptar às suas necessidades.
```

## Como Usar n8n Gratuitamente

O **n8n** é uma ferramenta de código aberto, o que significa que você pode utilizá-la completamente **gratuita** através da modalidade **self-hosted** (auto-hospedagem). Nessa abordagem, você instala e executa o n8n em sua própria infraestrutura, seja no seu computador local, em um servidor próprio ou em serviços de nuvem. Além de economizar custos, o self-hosting oferece controle total sobre seus dados, privacidade e personalização completa da plataforma.

### Pré-requisitos

Para executar o n8n gratuitamente em seu ambiente local, você precisará instalar o **Docker**, que é a solução de containerização mais utilizada por desenvolvedores e equipes para executar aplicações de forma isolada e consistente.

**Instale o Docker:**
- Acesse o site oficial: [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Baixe e instale a versão adequada para seu sistema operacional (Windows, macOS ou Linux)
- Siga as instruções de instalação fornecidas pelo instalador

### Executando n8n com Docker

Após instalar o Docker, você pode executar o n8n com um único comando no terminal:

:::{code-block} bash
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n
:::

**O que este comando faz:**
- `-it`: Executa o container em modo interativo
- `--rm`: Remove o container automaticamente quando você pará-lo
- `--name n8n`: Nomeia o container como "n8n"
- `-p 5678:5678`: Mapeia a porta 5678 para acessar a interface
- `-v ~/.n8n:/home/node/.n8n`: Persiste seus workflows e configurações localmente

**Acessando a interface:**
- Abra seu navegador e acesse: `http://localhost:5678`
- Crie sua conta local (os dados ficam apenas na sua máquina)
- Comece a criar seus workflows!

### Outras Opções de Self-Hosting

Além do Docker Desktop local, você pode hospedar o n8n de outras formas gratuitas:

#### Serviços de Nuvem Gratuitos
- **Railway**: Oferece tier gratuito com recursos suficientes para começar
- **Render**: Plano gratuito com sleep após inatividade
- **Google Cloud Run**: Tier gratuito generoso para aplicações containerizadas
- **AWS Free Tier**: 12 meses gratuitos com recursos limitados

#### Servidores Próprios
- Servidor VPS pessoal (como DigitalOcean, Linode, Vultr)
- Servidor doméstico (Raspberry Pi, computador antigo)
- Ambiente de desenvolvimento local permanente

### Documentação Oficial

Para instruções detalhadas sobre diferentes métodos de instalação, configurações avançadas e melhores práticas de self-hosting, consulte:

📚 [Guia Oficial de Self-Hosting do n8n](https://docs.n8n.io/hosting/?_gl=1*9qdgvv*_gcl_aw*R0NMLjE3NDkxNTA2MzAuQ2owS0NRandnSVhDQmhEQkFSSXNBRUxDOVppTXFma29NREM0em1TaU1lN05YVnc0dVZqWU1DTGYzZXNmcE91YklXR1phOERIb0ZCLUlJMGFBbHdjRUFMd193Y0I.*_gcl_au*MTAwMjExMjc2MS4xNzUwMDk4ODcz*_ga*NDMwODU3NTU0LjE3NTAwOTg2MzY.*_ga_0SC4FF2FH9*czE3NTAxMTQ4OTIkbzMkZzEkdDE3NTAxMTU1MzQkajYwJGwwJGgw)

### Vantagens do Self-Hosting Gratuito

#### Controle Total
- Seus dados permanecem completamente sob seu controle
- Sem limites de workflows ou execuções
- Personalização completa da plataforma

#### Privacidade e Segurança
- Dados sensíveis não saem do seu ambiente
- Ideal para projetos corporativos com requisitos de compliance
- Nenhuma informação compartilhada com terceiros

#### Aprendizado e Experimentação
- Ambiente perfeito para aprender e testar
- Sem preocupações com custos ou limites de uso
- Possibilidade de explorar todas as funcionalidades

#### Flexibilidade
- Execute em qualquer lugar que suporte Docker
- Escalável conforme suas necessidades crescem
- Migração fácil entre diferentes ambientes

:::{admonition} Dica para Iniciantes
:class: tip

Se você está começando, recomendamos iniciar com o Docker Desktop no seu computador local. É a forma mais rápida de testar o n8n sem custos e sem complicações. Depois que se familiarizar com a ferramenta, você pode considerar migrar para uma solução em nuvem se precisar de acesso remoto ou maior disponibilidade.
:::

:::{admonition} Atenção
:class: warning

Ao usar o n8n gratuitamente via self-hosting, você é responsável por:
- Manter o software atualizado
- Fazer backups dos seus workflows
- Garantir a segurança do ambiente
- Gerenciar recursos computacionais (memória, processamento, armazenamento)
:::


Para uma demonstração prática e visual de como configurar o n8n usando Docker, recomendamos o vídeo tutorial que apresenta o processo completo de instalação passo a passo. O vídeo mostra desde a instalação do Docker Desktop até a execução do primeiro workflow no n8n, incluindo dicas de configuração e troubleshooting. É um recurso excelente tanto para iniciantes quanto para quem deseja revisar o processo de setup de forma rápida e didática.

<iframe width="100%" height="315" src="https://www.youtube.com/embed/8hQ1u0TAyAc?start=5" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


