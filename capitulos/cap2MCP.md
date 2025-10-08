# Protocolos de Integração entre Modelos Computacionais

Protocolos para conectar modelos computacionais distintos são conjuntos de regras, formatos e padrões que permitem a integração, comunicação e interoperabilidade entre diferentes sistemas, algoritmos ou arquiteturas de modelagem. Eles atuam como pontes semânticas e estruturais, garantindo que os modelos compartilhem informações contextuais, metadados, entradas e saídas, mesmo quando desenvolvidos com linguagens, objetivos ou arquiteturas diferentes. Esses protocolos são fundamentais em cenários como sistemas multiagentes, gêmeos digitais, orquestração de modelos de IA, fluxos RAG e infraestruturas de MLOps, onde é necessário manter consistência, rastreabilidade e colaboração inteligente entre os diversos componentes do sistema.

```{figure} imagens/protocolo.jpeg
:alt: Representação visual dos protocolos de integração entre agentes de IA
:align: center
:name: protocolo

Fluxograma ilustrando os protocolos de integração entre agentes de IA.
```

Antes de abordarmos os protocolos de integração entre modelos computacionais, é importante garantir a compreensão de alguns conceitos fundamentais relacionados a redes, APIs, agentes inteligentes e fluxo de dados.

```{admonition} Conhecimentos recomendáveis:
:class: note
- **Programação Básica**: Ter familiaridade com pelo menos uma linguagem de programação. *Python* será a linguagem utilizada nos exemplos.  
- **Conceitos de APIs**: Entender como funcionam APIs, requisições e respostas. Consulte também nossa seção sobre APIs para reforçar esse conhecimento.  
- **JSON**: Conhecer o formato *JSON*, muito utilizado para troca de dados entre sistemas.  
- **Arquitetura Cliente-Servidor**: Compreender como clientes e servidores se comunicam no modelo tradicional da web.  
- **Outros**: Conhecimentos adicionais que podem ajudar incluem *APIs REST*, protocolo *HTTP/HTTPS*, noções básicas de segurança web, *Inteligência Artificial* e *LLMs*.  
```

Além dos conhecimentos teóricos, também é recomendável familiaridade com determinadas ferramentas e bibliotecas que viabilizam a implementação prática desses protocolos, como plataformas de orquestração, frameworks de agentes e ambientes de teste com suporte à integração por API.

```{admonition} Ferramentas necessárias
:class: note

- **Python 3.8 ou superior** – linguagem utilizada nos exemplos.
- **Editor de texto ou IDE** de sua preferência (ex: VS Code, PyCharm, JupyterLab).
- **Acesso à internet** para instalação de pacotes e uso de APIs.
- **Ambiente virtual** configurado (ex: `venv` ou `conda`) para gerenciar dependências.
- **Bibliotecas essenciais de IA** como `requests`, `openai`, `langchain` e `transformers`.
- **Conta gratuita** ou acesso a **APIs externas** utilizadas nos exemplos.
- **Ferramentas de versionamento** (como `Git`) para organizar e acompanhar o código.
- **Terminal ou shell** configurado para execução dos scripts.
```
Alguns **protocolos de integração entre agentes de IA e sistemas computacionais** vêm sendo desenvolvidos com o objetivo de padronizar a comunicação entre modelos, agentes e ambientes. Entre os principais, destacam-se:

- [`OpenAi Function Calling`](https://platform.openai.com/docs/guides/function-calling)
- [`LangChain Agents Protocol`](https://github.com/langchain-ai/agent-protocol?ref=blog.langchain.com)
- [`Agent2Agent protocol`](https://a2aprotocol.ai/)

Neste e-book, optamos por aprofundar o **Model Context Protocol (MCP)** por três motivos principais:

- Ele propõe uma **estrutura simples e modular** para orquestração de agentes em fluxos complexos.
- Permite organizar a troca de informações em **blocos reutilizáveis e interpretáveis**, facilitando o rastreamento do raciocínio do agente.
- Está alinhado com práticas modernas de construção de **sistemas multiagentes baseados em linguagem natural**.
  
## Model Context Protocol

O [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) (MCP) é uma iniciativa aberta e recente que busca padronizar a comunicação entre modelos de linguagem e aplicações. Seu objetivo central é permitir que diferentes agentes de IA interajam com fontes de dados, APIs e sistemas legados de forma segura, consistente e escalável — sem a necessidade de integrações manuais e fragmentadas.

Imagine que você tem um assistente de IA superinteligente (como o ChatGPT ou o Claude), mas ele está isolado, sem acesso aos seus arquivos, e-mails, agendas ou sistemas corporativos. O MCP funciona como uma “ponte universal”, que permite conectar esse assistente a tudo isso, garantindo controle, segurança e estrutura na troca de informações.

Essa padronização torna-se essencial em ecossistemas mais complexos, nos quais coexistem LLMs proprietários, aplicações empresariais, repositórios sensíveis e ferramentas de automação. Ao criar uma interface comum entre esses elementos, o MCP promove interoperabilidade real e reduz drasticamente os atritos técnicos.

Além disso, o protocolo foi desenvolvido com foco em modularidade e clareza. Em vez de construir integrações do zero para cada agente, você pode utilizar os blocos definidos no MCP para orquestrar fluxos, registrar raciocínios e controlar interações com outros sistemas.

Você pode se aprofundar acessando a [documentação oficial do Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) ou outras fontes como {cite}`mcp_workshop_youtube,norahsakal_mcp_explained`.

### Por que o MCP Existe?

```{list-table}
:header-rows: 1
:widths: 50 50

* - **O Problema Antes do MCP**
  - **A Solução do MCP**
* - 
  - 
* - Cada empresa criava sua própria forma de conectar IA aos seus sistemas  
  - Um padrão único que funciona para todas as aplicações de IA
* - Muito trabalho duplicado e incompatibilidade entre soluções  
  - Qualquer ferramenta que implemente MCP pode ser usada por qualquer aplicação de IA compatível
* - Desenvolvedores precisavam criar integrações específicas para cada ferramenta  
  - Redução drástica do tempo de desenvolvimento
* - Usuários ficavam limitados aos sistemas que cada aplicação de IA conseguia acessar  
  - Maior segurança e controle sobre as integrações
```


### A Filosofia e Motivação por Trás do MCP

A motivação central por trás do MCP, especialmente para a [Anthropic](https://www.youtube.com/watch?v=kQmXtrmQ5Zg), é a premissa de que "modelos são tão bons quanto o contexto que lhes fornecemos". Há alguns anos, a integração de contexto em chatbots ou aplicações de IA era muitas vezes feita por meio de copiar e colar ou digitação manual. No entanto, a evolução levou a sistemas onde os modelos precisam de "ganchos" diretos em seus dados e contexto, tornando-os mais poderosos e personalizados.

O que a Anthropic observou antes do MCP era uma grande fragmentação na forma como as empresas e equipes construíam sistemas de IA. Cada equipe criava suas próprias implementações personalizadas para conectar LLMs a dados e ferramentas, com lógicas de prompt e formas de federação de acesso diferentes. Isso resultava em um problema "N vezes M", onde havia inúmeras permutações para a interação entre aplicações cliente e servidores.

O MCP nasceu para padronizar esse desenvolvimento de IA, atuando como uma camada intermediária que "achata" essa complexidade. Ele busca ser para as aplicações de IA o que as APIs foram para a interação entre frontend e backend da web, ou o que o Language Server Protocol (LSP) é para a padronização da interação de IDEs com ferramentas específicas de linguagem.

```{figure} imagens/mcp_protocol.png
:align: center
:name: mcp_protocol
```

### MCP versus Outras Soluções

Para entender melhor o valor do MCP, vamos compará-lo com outras abordagens existentes:

| Aspecto | MCP | APIs REST Tradicionais | Webhooks | Plugins Específicos |
|---------|-----|------------------------|-----------|---------------------|
| **Padronização** | Protocolo único | Cada API é diferente |  Implementação varia |  Específico por aplicação |
| **Bidirecionalidade** |  Cliente ↔ Servidor |  Principalmente Cliente → Servidor |  Servidor → Cliente |  Varia |
| **Tempo Real** |  Suporte nativo |  Polling necessário |  Push notifications |  Varia |
| **Descoberta Automática** |  Capacidades expostas | Documentação manual | Configuração manual | Manual |
| **Controle de Acesso** | Granular e padronizado | Varia por API | Limitado | Varia |
| **Facilidade de Integração** | Uma vez implementado, funciona com todos | Integração por API | Configuração por webhook | Por aplicação |

Para ajudar na escolha do protocolo mais adequado ao seu cenário, a tabela a seguir compara MCP, APIs REST, Webhooks e Plugins Específicos em diferentes situações de uso. Ela mostra, de forma visual, onde cada abordagem é recomendada ✅, possível mas com limitações ⚠️ ou não recomendada ❌.

| Situação de Uso | MCP | APIs REST | Webhooks | Plugins Específicos |
|------------------|-----|------------|----------|----------------------|
| Conectar IA a múltiplos sistemas | ✅ | ❌ | ❌ | ❌ |
| Solução padronizada e reutilizável | ✅ | ❌ | ❌ | ❌ |
| Aproveitar ecossistema existente | ✅ | ❌ | ❌ | ❌ |
| Comunicação bidirecional em tempo real | ✅ | ❌ | ⚠️ (limitada) | ❌ |
| Integração simples e específica | ❌ | ✅ | ⚠️ | ✅ |
| Sem necessidade de IA avançada | ❌ | ✅ | ✅ | ✅ |
| Já existe API REST disponível | ❌ | ✅ | ❌ | ❌ |
| Notificações simples | ❌ | ❌ | ✅ | ❌ |
| Comunicação unidirecional | ❌ | ✅ | ✅ | ✅ |
| Requisitos específicos de tempo real | ❌ | ❌ | ✅ | ❌ |
| Aplicação única | ❌ | ✅ | ✅ | ✅ |
| Funcionalidades muito específicas | ❌ | ⚠️ | ✅ | ✅ |
| Aplicação sem suporte a MCP | ❌ | ✅ | ✅ | ✅ |

### Arquitetura Central do MCP

A arquitetura central do MCP se baseia em uma estrutura cliente-servidor robusta e modular, projetada para facilitar a integração entre modelos de IA e sistemas externos. Para quem deseja se aprofundar nos detalhes dessa arquitetura, recomendamos a leitura da documentação oficial e de recursos complementares disponíveis em {cite}`mcp_official_docs, deeplearning_mcp_course, microsoft_mcp_tutorial`.

```{admonition} No MCP com o modelo cliente-servidor:
:class: note

- **Hosts MCP** executam os modelos de IA
- **Clientes MCP** iniciam solicitações
- **Servidores MCP** fornecem contexto, ferramentas e capacidades
```

```{admonition} **Componentes principais:**
:class: note

- **Recursos**: Dados estáticos ou dinâmicos para os modelos

- **Prompts**: Fluxos de trabalho predefinidos para geração guiada

- **Ferramentas**: Funções executáveis como busca, cálculos

- **Amostragem**: Comportamento agente por meio de interações recursivas
```

#### [Componentes Detalhados](https://modelcontextprotocol.io/docs/getting-started/intro)

- **MCP Host (Anfitrião)**:
  - É a aplicação ou ferramenta que o usuário interage diretamente.

```{admonition} Exemplos de MCP Host
:class: exemplo
[Claude Code](https://claude.com/product/claude-code) ou [Claude Desktop](https://claude.ai/download), IDEs (como Cursor ou Windsurf).
```
 
- **MCP Client (Cliente):**
  - Componente interno do MCP Host
  - Mantém conexões um-para-um com os servidores MCP
      
- **MCP Server (Servidor):**
  - Programa leve que atua como "wrapper" para sistemas externos
  - Pode ser executado localmente ou remotamente
       
```{admonition}{Responsabilidades}
:class: note
- **MCP Host**
  - Gerenciar a configuração do usuário
  - Iniciar conexões com servidores MCP
  - Orquestrar a interação com o LLM
  - Apresentar resultados ao usuário
- **MCP Client**
  - Descobrir capacidades dos servidores
  - Gerenciar autenticação
  - Traduzir requisições entre Host e Server
  - Manter estado das conexões
- **MCP Server**
  - Expor ferramentas, recursos e prompts
  - Implementar lógica de negócio específica
  - Gerenciar acesso a sistemas externos
  - Manter segurança e permissões
```
### Fluxo de Comunicação

1. **Inicialização:** Host inicia e configura conexões com servidores
2. **Descoberta:** Cliente solicita capacidades de cada servidor
3. **Disponibilização:** Servidor informa suas ferramentas, recursos e prompts
4. **Uso:** Usuário interage com Host, que decide quando usar cada capacidade
5. **Execução:** Cliente invoca ferramentas do servidor conforme necessário
6. **Resultado:** Servidor processa e retorna resultados ao cliente/host

```{figure} imagens/client_server_arq.png
:alt: Client server Architecture
:align: center
:name: client_server_arq

Exemplo visual da arquitetura

<span style="font-size: 0.8em; color: gray;">Fonte: https://learn.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic/lesson/xtt6w/mcp-architecture</span>
```

Na prática:

```{figure} imagens/mcp_na_pratica.png
:alt: Client server Architecture
:align: center
:name: mcp_na_pratica

MCP na prática

<span style="font-size: 0.8em; color: gray;">Fonte: [https://learn.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic/lesson/xtt6w/mcp-architecture](https://norahsakal.com/blog/mcp-vs-api-model-context-protocol-explained/)</span>
```

#### Componentes Primários do protocolo

O MCP padroniza as interações em três interfaces principais, além de outras funcionalidades:

##### 1. **Ferramentas (Tools)**
 
As **ferramentas** no contexto do **Model Context Protocol (MCP)** são funcionalidades expostas pelo **servidor MCP** que podem ser utilizadas pelos modelos de linguagem (LLMs) durante a execução de tarefas. Elas funcionam como extensões das capacidades do modelo, permitindo que ele interaja com o mundo externo de maneira programada.

- **O que são:** São _funções executáveis_ que podem ser chamadas pelo LLM para realizar ações (como buscar dados, consultar sistemas, fazer cálculos, enviar mensagens, etc.).
- **Controle:** A decisão de usar ou não uma ferramenta é tomada **autonomamente pelo modelo**, com base no contexto da conversa ou tarefa em andamento.
- **Função:** Ampliar o poder do modelo, permitindo que ele **recupere informações externas** ou **execute comandos** no ambiente do usuário, de forma segura e contextualizada.

Essas ferramentas são o que transformam um modelo estático em um **agente dinâmico e funcional**, capaz de realizar operações complexas, acessar bancos de dados, interagir com APIs, ou controlar outros sistemas integrados.

```{admonition} **Características das Ferramentas:**
:class: note
- **Invocação Automática**: O LLM decide quando usar
- **Parâmetros Estruturados**: Definidos via JSON Schema
- **Resposta Estruturada**: Retorno padronizado
- **Assincronia**: Podem executar operações longas
```

**Exemplos de Ferramentas:**

```json
{
  "name": "send_email",
  "description": "Enviar email para um destinatário",
  "inputSchema": {
    "type": "object",
    "properties": {
      "to": {
        "type": "string",
        "description": "Email do destinatário"
      },
      "subject": {
        "type": "string",
        "description": "Assunto do email"
      },
      "body": {
        "type": "string",
        "description": "Corpo do email"
      }
    },
    "required": ["to", "subject", "body"]
  }
}
```

```{admonition} **Casos de Uso Comuns:**
:class: exemplo

- Integrações com GitHub (listar issues, criar PRs)
- Asana (adicionar tarefas, atualizar status)
- Brave (pesquisar na web)
- Sistemas de arquivos (ler/escrever arquivos)
- APIs diversas (Stripe, Cloudflare, etc.)
```

##### 2. **Recursos (_Resources_)**
   
Os **recursos** no contexto do MCP são **dados disponibilizados pela aplicação** (ou **MCP Host**) para enriquecer o contexto da conversa. Diferentemente das ferramentas, os recursos **não são invocados diretamente pelo LLM**. Em vez disso, são **anexados ao contexto** de forma automática, fornecendo informações adicionais que auxiliam o modelo a gerar respostas mais completas e contextualizadas.

- **Controle:** Controlados pela **aplicação** (o **MCP Host**).  
- **Função:** São **dados expostos à aplicação**, incorporados ao contexto para **melhorar a compreensão e relevância** das respostas geradas pelo modelo.  

```{admonition} **Tipos de Recursos:**
:class: note

- **Estáticos**: Arquivos JSON, documentos, configurações
- **Dinâmicos**: Dados interpolados com informações do usuário/sistema
- **Streaming**: Recursos que atualizam em tempo real
```

**Exemplos de Recursos:**
```json
{

"uri": "file:///home/user/project/README.md",

"name": "Project Documentation",

"description": "Documentação principal do projeto",

"mimeType": "text/markdown"

}
```

```{admonition} **Casos de Uso:**
:class: exemplo

- **Anexos em um chat:** como imagens enviadas pelo usuário ou documentos em PDF.  
- **Logs de sistema em tempo real:** permitindo que o modelo acompanhe eventos e status do sistema enquanto responde.  
- **Configurações de projeto:** parâmetros ou preferências definidos pelo usuário que orientam o comportamento do modelo.  
- **Dados de contexto do usuário:** informações como idioma, localização ou permissões ativas.  
- **Arquivos de referência:** textos, planilhas ou relatórios que o modelo pode consultar para fundamentar respostas.  
```

##### 3. **_Prompts_**

Os **prompts** funcionam como **templates configuráveis** ou **atalhos inteligentes** que os usuários podem utilizar para iniciar fluxos específicos de conversa com o modelo. Eles encapsulam instruções complexas em comandos simples, semelhantes a _"comandos de barra"_ (ex: `/resumir-documento` ou `/gerar-relatório`), permitindo ao usuário acionar comportamentos predefinidos de forma rápida e consistente.

- **Controle:** definidos e acionados pelo **usuário**
- **Função:** atuam como **modelos predefinidos** de interação para tarefas recorrentes

```{admonition} **Características dos Prompts:**
:class: note

- **Invocação Manual**: Usuário escolhe quando usar (ex: /summarize)
- **Parametrizáveis**: Aceitam entradas personalizadas (ex: idioma, extensão do resumo)
- **Contextuais**: Utilizam dados disponíveis no ambiente atual da conversa
- **Reutilizáveis**: Mesmo prompt funciona em diferentes contextos
```

**Estrutura de um Prompt:**

```json
{
  "name": "summarize_code",
  "description": "Resumir arquivos de código do projeto",
  "arguments": [
    {
      "name": "file_pattern",
      "description": "Padrão de arquivos a resumir (ex: *.py)",
      "required": false
    }
  ]
}
```

```{admonition} **Exemplos de comandos:**
:class: note

- `/summarize` - Resumir documentos ou conversas
- `/translate` - Traduzir texto para outro idioma
- `/code-review` - Revisar código com padrões da empresa
- `/meeting-notes` - Extrair ações de notas de reunião
```

## Exemplos de Mensagens Comuns

Antes de entender os exemplos, é importante saber **o que são essas mensagens**.

No MCP, a comunicação entre o **Cliente** (como um agente de IA ou aplicativo) e o **Servidor** (que fornece dados, como papers ou APIs) ocorre por meio de um protocolo padronizado chamado **JSON-RPC**.

Esse formato define com precisão **como as mensagens devem ser estruturadas, enviadas e interpretadas**, permitindo que diferentes sistemas se comuniquem de forma segura e padronizada.

:::{tip}
Pense no JSON-RPC como um "idioma comum" entre o cliente e o servidor.
:::

**Analogia para Entender**

Imagine um atendimento em um **drive-thru**:

- **Você (Cliente):** “Quero um hambúrguer com queijo.”
- **Atendente (Servidor):** “Certo! São R$ 15,00. Seu pedido está sendo preparado.”

Assim também funciona a comunicação no MCP:

- O **Cliente** envia uma **requisição JSON** pedindo algo.
- O **Servidor** retorna uma **resposta estruturada**, com o resultado, confirmação ou erro.

Todas as mensagens seguem esse padrão de "pergunta → resposta".

---

### Estrutura Básica das Mensagens

Toda mensagem JSON-RPC tem estes elementos:

```json
{
  "jsonrpc": "2.0",
  "id": "1",
  "method": "fazer_algo",
  "params": {
    "dado1": "valor1"
  }
}
```

```{admonition} **Campos principais:**
:class: note

- `jsonrpc`: Versão do protocolo (sempre 2.0)
- `id`: Identificador único da mensagem
- `method`: O que você quer fazer
- `params`: Parâmetros/dados necessários
```

1. **Inicialização da Conexão**

Antes de qualquer troca de dados úteis, cliente e servidor precisam se reconhecer e alinhar capacidades. É nesse momento que ocorre a inicialização da conexão, uma etapa essencial para estabelecer uma comunicação clara e segura.

```{admonition} **O que acontece aqui?**
:class: note

Esta é a **primeira mensagem** trocada quando o cliente se conecta ao servidor. É como um "aperto de mãos" digital onde ambos dizem:
- "Oi, eu sou o Cliente, versão 1.0.0"
- "Olá, eu sou o Servidor, versão 1.0.0, e posso fazer X, Y e Z"

Cliente pergunta: "Quem é você e o que pode fazer?"
```

A seguir, apresentamos o **script em formato JSON** que representa essa etapa inicial de comunicação, onde cliente e servidor trocam suas primeiras informações para estabelecer a conexão.

```json
{
  "jsonrpc": "2.0",
  "id": "1",
  "method": "initialize",
  "params": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "tools": {},
      "resources": {},
      "prompts": {}
    },
    "clientInfo": {
      "name": "ExampleClient",
      "version": "1.0.0"
    }
  }
}
```

**Tradução em português:**

```
Cliente: "Olá servidor! Sou o ExampleClient versão 1.0.0.
         Uso o protocolo MCP versão 2024-11-05.
         Posso trabalhar com ferramentas, recursos e prompts.
         Você pode me responder?"
```

```{admonition} **Explicação dos campos:**
:class: note

- `method: "initialize"` → Estou iniciando a conexão
- `protocolVersion` → Versão do MCP que estou usando
- `capabilities` → O que eu (cliente) consigo fazer
- `clientInfo` → Meu nome e versão
```
Servidor responde: "Oi! Eu posso fazer isso..."

```json
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "tools": {
        "listChanged": true
      },
      "resources": {
        "subscribe": true,
        "listChanged": true
      },
      "prompts": {
        "listChanged": true
      }
    },
    "serverInfo": {
      "name": "ExampleServer",
      "version": "1.0.0"
    }
  }
}
```

**Tradução em português:**

```
Servidor: "Olá ExampleClient! Sou o ExampleServer versão 1.0.0.
           Também uso o protocolo MCP versão 2024-11-05.
           
           Minhas capacidades:
           ✅ Ferramentas: Posso notificar quando a lista mudar
           ✅ Recursos: Você pode se inscrever e serei notificado sobre mudanças
           ✅ Prompts: Posso notificar quando a lista mudar
           
           Estamos conectados!"
```

```{admonition} **Explicação dos campos:**
:class: note

- `result` → Resposta bem-sucedida (não é erro)
- `capabilities` → O que EU (servidor) consigo fazer
- `listChanged: true` → Posso avisar quando algo mudar
- `subscribe: true` → Você pode se inscrever para receber atualizações
- `serverInfo` → Meu nome e versão
```

2. **Listagem de Ferramentas Disponíveis**

Após o processo de inicialização, o próximo passo é a **descoberta de capacidades**.

Neste momento, o **cliente envia uma solicitação ao servidor perguntando quais ferramentas estão disponíveis** para uso. Essa listagem permite que o modelo saiba o que está ao seu alcance — funções, integrações e recursos que pode utilizar durante uma interação.

:::tip Analogia
É como entrar em uma oficina e perguntar:  
**"Quais ferramentas vocês têm aí? Martelo? Chave de fenda? Furadeira?"**  
O servidor responde com a lista do que tem disponível, e o modelo decide como usar essas ferramentas conforme necessário.
:::

Cliente pergunta: "Que ferramentas você oferece?"

```json
{
  "jsonrpc": "2.0",
  "id": "2",
  "method": "tools/list"
}
```

**Tradução em português:**

```
Cliente: "Me mostre a lista de todas as ferramentas disponíveis."
```

```{admonition} **Explicação:**
:class: note

- `method: "tools/list"` → Quero ver a lista de ferramentas
- `id: "2"` → Esta é minha segunda mensagem (a primeira foi o initialize)
- Sem `params` porque não preciso enviar dados extras
```

Servidor responde: "Tenho estas ferramentas..."

```json
{
  "jsonrpc": "2.0",
  "id": "2",
  "result": {
    "tools": [
      {
        "name": "get_weather",
        "description": "Obter informações meteorológicas",
        "inputSchema": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "Cidade para consultar o clima"
            }
          },
          "required": ["location"]
        }
      }
    ]
  }
}
```

**Tradução em português:**

```
Servidor: "Tenho 1 ferramenta disponível:

           📍 Nome: get_weather
           📝 O que faz: Busca informações sobre o clima
           
           Como usar:
           - Você DEVE me dar: 'location' (nome da cidade)
           - location deve ser texto (string)
           - Exemplo: 'São Paulo', 'Rio de Janeiro'
           
           Pronto! É só chamar essa ferramenta quando precisar."
```

```{admonition} **Explicação dos campos:**
:class: note

- `tools` → Array (lista) com todas as ferramentas
- `name` → Nome único da ferramenta (usado para chamá-la)
- `description` → Explicação do que a ferramenta faz
- `inputSchema` → "Contrato" de como usar a ferramenta
  - `properties` → Parâmetros que você pode enviar
  - `required` → Parâmetros obrigatórios
  - `type: "string"` → Tipo de dado (texto, número, etc.)
```


3. **Execução de uma Ferramenta**

Após conhecer as ferramentas disponíveis, o **cliente pode invocar uma delas** para executar uma ação específica.  
Essa etapa representa o momento em que o modelo **passa da descoberta para a execução**, colocando em prática uma funcionalidade oferecida pelo servidor.

Por exemplo, se entre as ferramentas listadas há uma chamada `get_weather`, o cliente pode enviar uma solicitação como:  

> “Quero usar a ferramenta `get_weather` para consultar a previsão do tempo em São Paulo.”

Esse processo é essencial para que o **LLM realize operações externas**, como consultas a APIs, cálculos personalizados ou acesso a sistemas, expandindo suas capacidades além do texto gerado localmente.

:::tip Analogia  
É como estar em uma oficina: depois de saber que há um **termômetro**, você diz —  
**"Ok, quero usar essa ferramenta para medir a temperatura agora!"**  
O servidor então executa a função e retorna o resultado solicitado.  
:::

Veja os comandos utilizados para uma execução em JSON:

Cliente chama: "Use a ferramenta X com estes dados"

```json
{
  "jsonrpc": "2.0",
  "id": "3",
  "method": "tools/call",
  "params": {
    "name": "get_weather",
    "arguments": {
      "location": "São Paulo"
    }
  }
}
```

**Tradução em português:**

```
Cliente: "Quero EXECUTAR a ferramenta 'get_weather'.
         
         Os dados que estou enviando são:
         📍 location: 'São Paulo'
         
         Me retorne o resultado, por favor!"
```

```{admonition} **Explicação dos campos**
:class: note

- `method: "tools/call"` → Quero executar uma ferramenta
- `params.name` → Nome da ferramenta que quero usar
- `params.arguments` → Os dados necessários (conforme o inputSchema)
- `arguments.location` → Parâmetro obrigatório definido no schema
```

Servidor responde: "Aqui está o resultado!"

```json
{
  "jsonrpc": "2.0",
  "id": "3",
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Clima em São Paulo: 25°C, ensolarado, umidade 60%"
      }
    ]
  }
}
```

**Tradução em português:**

```
Servidor: "Executei a ferramenta 'get_weather' para São Paulo.
           
           Resultado:
           🌡️ Temperatura: 25°C
           ☀️ Condição: Ensolarado
           💧 Umidade: 60%
           
           Tudo certo!"
```

```{admonition} **Explicação dos campos:**
:class: note

- `result.content` → O conteúdo da resposta (pode ser texto, imagem, etc.)
- `type: "text"` → O resultado é texto puro
- `text` → O resultado em si
```

### Exemplo Real do Nosso Projeto

A seguir, apresentamos um exemplo real extraído do nosso projeto, ilustrando como o cliente pode chamar uma ferramenta de busca de papers para recuperar informações acadêmicas. Este é um exemplo prático de comunicação entre cliente e servidor utilizando o MCP, a troca de mensagens segue o padrão **JSON-RPC**.


**Cliente pede:**

```json
{
  "jsonrpc": "2.0",
  "id": "3",
  "method": "tools/call",
  "params": {
    "name": "search_papers",
    "arguments": {
      "query": "artificial intelligence",
      "max_results": 3
    }
  }
}
```

O cliente está solicitando ao servidor que execute uma **ferramenta chamada `search_papers`**, com os seguintes argumentos:

- `"query": "artificial intelligence"` → tema da busca.
- `"max_results": 3` → quantidade de resultados desejados.

Essa chamada equivale a dizer:  
> “Servidor, por favor, busque 3 artigos sobre inteligência artificial.”

**Servidor responde:**

```json
{
  "jsonrpc": "2.0",
  "id": "3",
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Encontrados 3 papers sobre 'artificial intelligence':\n\n1. Deep Learning Advances (2024)\n   Autores: John Smith, Jane Doe\n   ArXiv: 2409.12345\n\n2. Neural Networks Review (2024)\n   Autores: Bob Johnson\n   ArXiv: 2409.54321\n\n3. AI Ethics Study (2024)\n   Autores: Alice Brown\n   ArXiv: 2409.98765"
      }
    ]
  }
}
```
O servidor compreendeu a solicitação e devolveu um resultado com 3 artigos, contendo:

- Título do artigo
- Nome dos autores
- Identificador ArXiv
---

## Tratamento de Erros

O que acontece se algo sair do esperado?

Quando ocorre uma falha durante a comunicação, o **servidor não retorna um campo `result`**, como em uma resposta bem-sucedida.  
Em vez disso, ele envia uma **mensagem de erro estruturada**, contendo informações sobre o que deu errado.

Isso permite que o cliente trate adequadamente a situação — por exemplo, exibindo uma mensagem ao usuário ou tentando novamente com outros parâmetros.

**Exemplo: Ferramenta não encontrada**

```json
{
  "jsonrpc": "2.0",
  "id": "3",
  "error": {
    "code": -32601,
    "message": "Method not found",
    "data": {
      "detail": "A ferramenta 'get_clima' não existe. Ferramentas disponíveis: get_weather"
    }
  }
}
```

**Tradução:**

```
Servidor: "ERRO! A ferramenta que você pediu não existe.
           
           🔴 Código do erro: -32601 (Método não encontrado)
           📝 Mensagem: Method not found
           ℹ️ Detalhes: A ferramenta 'get_clima' não existe.
                       Ferramentas disponíveis: get_weather"
```

```{admonition} **Códigos de erro comuns:**
:class: note

- `-32700` → JSON inválido (erro de sintaxe)
- `-32600` → Requisição inválida
- `-32601` → Método/ferramenta não encontrado
- `-32602` → Parâmetros inválidos
- `-32603` → Erro interno do servidor
```

---

## Fluxo Completo de Comunicação

Sequência típica de uso:

```
1. INICIALIZAÇÃO
   Cliente: "initialize" → Servidor: "Ok, conectado!"

2. DESCOBERTA
   Cliente: "tools/list" → Servidor: "Tenho estas ferramentas..."

3. EXECUÇÃO (pode repetir várias vezes)
   Cliente: "tools/call get_weather" → Servidor: "25°C, sol"
   Cliente: "tools/call search_papers" → Servidor: "Encontrei 5 papers"
   Cliente: "tools/call analyze_papers" → Servidor: "Análise completa..."

4. FINALIZAÇÃO
   Cliente fecha a conexão
```

### Diagrama Visual

```
┌─────────┐                           ┌─────────┐
│ CLIENTE │                           │SERVIDOR │
└────┬────┘                           └────┬────┘
     │                                     │
     │  1. initialize                      │
     │────────────────────────────────────>│
     │                                     │
     │  2. Conectado + Capacidades         │
     │<────────────────────────────────────│
     │                                     │
     │  3. tools/list                      │
     │────────────────────────────────────>│
     │                                     │
     │  4. Lista de ferramentas            │
     │<────────────────────────────────────│
     │                                     │
     │  5. tools/call "get_weather"        │
     │────────────────────────────────────>│
     │                                     │
     │  6. Resultado: "25°C, sol"          │
     │<────────────────────────────────────│
     │                                     │
```

---

## Resumo para Leigos

```{admonition} O que você precisa entender:
:class: tip

1. **JSON-RPC** é só um formato padronizado de mensagens
2. Sempre há um **id** para identificar cada conversa
3. **Cliente pergunta** (`method`) → **Servidor responde** (`result` ou `error`)
4. Tudo começa com `initialize` (apresentação)
5. Depois vem `tools/list` (ver o que tem disponível)
6. Por fim `tools/call` (usar uma ferramenta específica)
```

## Analogia Final: Restaurante

```
1. INITIALIZE = Entrar no restaurante e ser recebido
   "Boa noite! Bem-vindo ao restaurante!"

2. TOOLS/LIST = Pedir o cardápio
   "Aqui está nosso menu: pizza, hambúrguer, salada..."

3. TOOLS/CALL = Fazer o pedido
   "Quero uma pizza margherita"
   → "Sua pizza está pronta!"
```

---

## Dicas Práticas

Antes de finalizar, vale destacar algumas **boas práticas** tanto para quem **desenvolve** quanto para quem **utiliza** integrações com o MCP.  

```{admonition} Para Desenvolvedores:
:class: tip

 ✅ Sempre valide o `inputSchema` antes de chamar ferramentas
 ✅ Use `id` único para cada mensagem
 ✅ Implemente timeout (não espere eternamente por resposta)
 ✅ Trate todos os códigos de erro possíveis
 ✅ Teste com ferramentas simples primeiro
```

```{admonition} Para Usuários:
:class: tip

 ✅ Se ver erro `-32601`: A ferramenta não existe
 ✅ Se ver erro `-32602`: Faltou algum parâmetro obrigatório
 ✅ Se ver erro `-32603`: Problema no servidor (tente novamente)
 ✅ Verifique os logs para detalhes dos erros
```

---

## Recursos Adicionais

Abaixo estão listados alguns **recursos úteis** para aprofundar o entendimento e aplicar na prática o que foi apresentado até o momento. Esses materiais complementares ajudam tanto no domínio da estrutura de mensagens quanto na validação e aplicação real do MCP:

- **[Especificação JSON-RPC 2.0](https://www.jsonrpc.org/specification)**  
  Documento oficial que define como funciona o protocolo de comunicação usado entre cliente e servidor.

- **[Documentação Oficial do MCP](https://modelcontextprotocol.io)**  
  Página com exemplos, especificações e guia completo sobre o Model Context Protocol.

- **[Validador de JSON Online](https://jsonlint.com)**  
  Ferramenta prática para testar se os scripts JSON estão corretos e bem formatados.



## Outras Capacidades Essenciais

O MCP oferece ainda um conjunto de capacidades avançadas que ampliam sua flexibilidade e inteligência. Elas tornam possível controlar o comportamento do modelo, organizar fluxos de interação e extrair informações de forma mais precisa e estruturada. Para se aprofundar nesses conceitos, recomendamos a leitura dos materiais {cite}`mcp_workshop_youtube, mcp_official_docs`.

### **1. Composability (Componibilidade)**

Uma característica poderosa do MCP é que qualquer aplicação, API ou agente pode ser tanto um cliente MCP quanto um servidor MCP simultaneamente. Isso permite criar arquiteturas complexas e em camadas.

```{admonition} Exemplo de Arquitetura Composta
:class: exemplo

Agent de Pesquisa (Cliente + Servidor):
```
```{list-table}
:header-rows: 1
:widths: 50 50

* - **Como Cliente, usa:**
  - **Como Servidor, expõe:**
* - Web Search MCP Server  
  - research_topic()
* - Database MCP Server  
  - summarize_findings()
* - File System MCP Server  
  - generate_report()
```

```{admonition} Benefícios da Componibilidade
:class: note

- **Especialização:** Cada camada foca em uma responsabilidade específica
- **Reutilização:** Componentes podem ser usados em diferentes contextos
- **Escalabilidade:** Fácil adicionar novas capacidades
- **Manutenibilidade:** Mudanças isoladas por componente
```

### **2. Sampling (Amostragem)**

Permite que um servidor MCP solicite inferências (chamadas de LLM) do cliente, sem precisar hospedar seu próprio modelo.

```{admonition} **Como Funciona:**
:class: note

1. Servidor precisa de inteligência para uma decisão
2. Solicita ao cliente para fazer uma inferência
3. Cliente usa seu LLM e retorna resultado
4. Servidor usa o resultado para continuar processamento
```

```{admonition} Exemplo: Servidor -> Cliente (solicitando inferência)
:class: note
**Resumo do Fluxo:**

1. Você pede: "Organize minha caixa de entrada"

2. Servidor lê email e precisa classificar urgência

3. Servidor ****pede ao llm****: "Esse email é urgente?"

4. llm analisa e responde: "URGENTE - Requer ação imediata"

5. Servidor executa ação: move para pasta "Urgentes" e notifica você
```

**Por que isso é poderoso?**

1. **Simplicidade no servidor**  
   O servidor permanece leve e direto, sem precisar incorporar capacidades próprias de IA.

2. **Controle total**  
   Você mantém o controle sobre os custos e a privacidade, já que toda a inteligência vem do seu próprio modelo de linguagem (LLM).

O script abaixo cria uma **solicitação de amostragem (sampling)** para o modelo de linguagem, pedindo que ele **classifique um e-mail** em uma das três categorias — *urgente*, *normal* ou *baixa prioridade* —, utilizando o modelo preferencial **Claude 3 Sonnet**.

```json
{
  "jsonrpc": "2.0",
  "method": "sampling/createMessage",
  "params": {
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "Classifique este email como urgente, normal ou baixa prioridade: [email content...]"
        }
      }
    ],
    "modelPreferences": {
      "hints": [
        {
          "name": "claude-3-sonnet"
        }
      ]
    }
  }
}
```

```{admonition} **Vantagens:**
:class: tip

- Servidor não precisa gerenciar LLM próprio
- Cliente mantém controle sobre custos e privacidade
- Consistência no modelo usado em toda a aplicação
```

### 3. Elicitation (Elicitação)

Capacidade que permite ao servidor solicitar informações adicionais dos usuários durante a execução de uma ferramenta.

```{admonition} **Casos de Uso:**
:class: exemplo

- Confirmar ações críticas (deletar arquivos, fazer pagamentos)
- Coletar informações adicionais necessárias
- Obter permissões específicas
```

```{admonition} **Exemplo**
:class: exemplo


O script abaixo representa um fluxo durante execução de uma ferramenta de reserva.
```
```json
{
  "jsonrpc": "2.0",
  "method": "elicitation/request",
  "params": {
    "prompt": "Confirmar reserva do restaurante X para 4 pessoas às 19h?",
    "options": ["Confirmar", "Cancelar", "Alterar horário"]
    }
 }
```

### 4. Completions (Conclusões/Sugestões)

O MCP suporta autocompletar para argumentos de prompt e parâmetros de recursos.

Implementação:

Cliente solicita sugestões

```json
{
  "jsonrpc": "2.0",
  "id": "4",
  "method": "completion/complete",
  "params": {
    "ref": {
      "type": "prompt",
      "name": "analyze_data"
    },
    "argument": {
      "name": "data_source",
      "value": "sales_"
    }
  }
}
```

Servidor retorna sugestões

```json
{
  "jsonrpc": "2.0",
  "id": "4",
  "result": {
    "completion": {
      "values": [
        "sales_2024",
        "sales_monthly",
        "sales_quarterly"
      ],
      "total": 3,
      "hasMore": false
    }
  }
}
```

### 5. Authentication (Autenticação)

Os servidores MCP podem implementar OAuth 2.0/2.1 para acessar recursos protegidos.

```{admonition} **Fluxo de Autenticação:**
:class: note

1. Servidor inicia processo OAuth
2. Cliente redireciona usuário para provedor
3. Usuário autentica e autoriza
4. Servidor recebe token OAuth
5. Cliente recebe token de sessão para uso futuro
```

Exemplo de configuração:

```json
{
  "mcpServers": {
    "google-drive": {
      "command": "mcp-server-google-drive",
      "env": {
        "GOOGLE_CLIENT_ID": "your-client-id",
        "GOOGLE_CLIENT_SECRET": "your-client-secret"
      }
    }
  }
}
```

### 6. Notifications (Notificações)

Servidores podem enviar notificações para clientes sobre mudanças de estado.

```{admonition} **Tipos de Notificações:**
:class: note

- `resources/updated`: Recurso foi modificado
- `tools/list_changed`: Lista de ferramentas mudou
- `prompts/list_changed`: Lista de prompts mudou
```

O script do exemplo abaixo envia uma **notificação ao servidor** informando que o **recurso localizado no URI `file:///project/config.json` foi atualizado**, permitindo que o servidor reaja a essa mudança se necessário (como recarregar o arquivo ou ajustar o contexto).

```{admonition} **Exemplo de notificação ao servidor:**
:class: exemplo
```
```json
{
   "jsonrpc": "2.0",
   "method": "notifications/resources/updated",
   "params": {
      "uri": "file:///project/config.json"
    }
}
```

### 7. Transports (Transportes)

O MCP suporta diferentes mecanismos de comunicação:

```{list-table}
:header-rows: 1
:widths: 50 50

* - **Transporte Local (STDIO)**
  - **Transporte Remoto (HTTP/SSE)**
* - - Comunicação via entrada/saída padrão  
    - Ideal para servidores locais  
    - Baixa latência, alta segurança
  - - Comunicação via HTTP com Server-Sent Events  
    - Permite servidores remotos  
    - Suporte a múltiplos clientes
```


**Configuração de Transporte:**

```json
{
  "mcpServers": {
    "local-server": {
      "command": "python",
      "args": [
        "server.py"
      ],
      "transport": "stdio"
    },
    "remote-server": {
      "url": "https://api.example.com/mcp",
      "transport": "http"
    }
  }
}
```

## Limitações e Considerações de Segurança

As implementações do MCP trazem avanços significativos em interoperabilidade e integração entre modelos de IA, mas é essencial compreender suas **limitações técnicas** e **riscos de segurança**.  Antes de aplicar o MCP em ambientes produtivos, recomenda-se avaliar aspectos como **exposição de dados sensíveis**, **controle de acesso**, **auditoria de logs** e **tratamento de falhas**, garantindo que a adoção do protocolo seja feita de forma segura e escalável. 
Para saber mais sobre limitações e considerações de segurança consulte, {cite}`dsacademy_mcp_blog, neo4j_mcp_blog`.

###  1. Limitações do MCP

```{list-table}
:header-rows: 1
:widths: 50 50

* - **Limitações de Performance**
  - **Limitações Funcionais**
* - **Latência de Rede**: Servidores remotos podem ter latência alta  
  - **Stateless**: Servidores MCP são geralmente stateless entre requisições
* - **Throughput**: Limitado pela capacidade do transporte (HTTP vs STDIO)  
  - **Transações**: Não há suporte nativo para transações distribuídas
* - **Concorrência**: Nem todos os servidores suportam requisições paralelas  
  - **Streaming de Dados**: Limitado para grandes volumes de dados
* - **Timeout**: Operações longas podem exceder limites de timeout  
  - **Compatibilidade**: Nem todas as ferramentas/APIs têm servidor MCP
```



```{admonition} Quando NÃO Usar MCP:
:class: warning

- Aplicações que precisam de latência ultra-baixa
- Sistemas que requerem transações ACID complexas
- Integrações simples que não justificam a complexidade
- Ambientes com restrições severas de recursos
```

### 2. Considerações de Segurança

Antes de implementar qualquer integração baseada em MCP, é fundamental compreender as **considerações de segurança** que garantem o uso confiável do protocolo. A proteção de dados sensíveis e o controle de acesso são pilares para manter a integridade e a confidencialidade do sistema.  

#### Autenticação e Autorização

```{admonition} Exemplo 
:class: exemplo

Configuração segura:
```
```json
{
  "mcpServers": {
    "database-server": {
      "command": "mcp-database-server",
      "env": {
        "DB_CONNECTION": "postgresql://user:pass@localhost/db",
        "ALLOWED_OPERATIONS": "SELECT, INSERT",
        "MAX_ROWS": "1000"
      }
    }
  }
}
```

```{admonition} **Validação de Entrada:**
:class: note

- Sempre validar parâmetros de ferramentas
- Sanitizar dados antes de usar em queries/comandos
- Implementar rate limiting para prevenir abuso
- Usar schemas JSON rigorosos
```

#### Controle de Acesso

Exemplo de verificação de permissões

```python
def verify_permissions(operation, resource):
    if operation == "DELETE" and not user.has_permission("admin"):
        raise PermissionError("Operação DELETE requer permissão de admin")
    if resource.startswith("/system/") and not user.has_permission("system"):
        raise PermissionError("Acesso a recursos do sistema negado")
```

#### Isolamento e Sandboxing

- Execute servidores MCP em containers ou ambientes isolados
- Use usuários com privilégios limitados
- Implemente timeouts para prevenir operações infinitas
- Monitore recursos (CPU, memória, disco)

#### Auditoria e Logging

Sistema de registro que monitora e documenta todas as operações realizadas através do MCP. É como ter um "diário detalhado" de tudo que acontece entre cliente e servidor. 

```{admonition} Por que é importante
:class: note

- **Rastreabilidade**: Saber exatamente quem fez o quê e quando
- **Debugging**: Identificar problemas e entender falhas
- **Segurança**: Detectar uso inadequado ou tentativas de acesso não autorizado
- **Compliance**: Atender requisitos legais de auditoria
```

#### Informações Registradas

Durante as interações no contexto do MCP, é essencial registrar detalhes operacionais para garantir segurança, rastreabilidade e auditoria adequada. Abaixo estão os principais elementos recomendados para registro:

- ⏰ **Timestamp**: momento exato em que a operação foi realizada  
- 🔧 **Ferramenta/recurso acessado**: nome da funcionalidade ou recurso utilizado  
- 👤 **Usuário que realizou a ação**: identificação do agente ou usuário solicitante  
- 📋 **Parâmetros enviados**: dados ou argumentos fornecidos na chamada  
- ✅/❌ **Status do resultado**: indicação de sucesso ou erro da operação 

**Exemplo Prático:**
```python
import logging
from datetime import datetime

def log_mcp_operation(tool_name, params, user_id, result_status):
    logging.info({
        "timestamp": datetime.utcnow().isoformat(),
        "tool": tool_name,
        "user": user_id,
        "params": params,
        "status": result_status,
        "type": "mcp_operation"
    })
```

```{admonition} Boas Práticas de Segurança
:class: tip

1. **Princípio do Menor Privilégio:** Conceda apenas as permissões mínimas necessárias
2. **Defesa em Profundidade:** Múltiplas camadas de segurança
3. **Monitoramento Contínuo:** Logs e alertas para atividades suspeitas
4. **Atualizações Regulares:** Mantenha servidores MCP atualizados
5. **Testes de Segurança:** Auditorias regulares e testes de penetração
```

## Benefícios do MCP

O MCP oferece vantagens significativas para todo o ecossistema de IA:

#### 1. Para Desenvolvedores de Aplicações

- **Desenvolvimento Acelerado:** Uma vez que o cliente é compatível com MCP, pode conectar a qualquer servidor sem trabalho adicional
- **Foco na Lógica Principal:** Desenvolvedores se concentram na lógica do agente em vez de integrações específicas
- **Ecossistema Rico:** Aproveitar servidores MCP existentes da comunidade
- **Manutenção Simplificada:** Updates centralizados no protocolo beneficiam todos

#### 2. Para Provedores de Ferramentas/APIs

- **Alcance Ampliado:** Um servidor MCP funciona com múltiplas aplicações de IA
- **Padronização:** Não precisa criar integrações específicas para cada cliente
- **Descoberta Automática:** Ferramentas são automaticamente descobertas por aplicações compatíveis
- **Monetização:** Oportunidades de criar serviços MCP premium

#### 3. Para Usuários Finais

- **Experiência Unificada:** Mesmo assistente IA acessa múltiplos sistemas
- **Personalização Avançada:** IA com acesso a dados pessoais e preferências
- **Automação Poderosa:** Fluxos de trabalho complexos executados automaticamente
- **Controle Granular:** Permissões específicas por ferramenta/recurso

#### 4. Para Empresas

- **Separação de Responsabilidades:** Diferentes equipes podem gerenciar diferentes servidores MCP
- **Governança Centralizada:** Controle unificado sobre integrações de IA
- **ROI Acelerado:** Implementação mais rápida de soluções de IA
- **Interoperabilidade:** Redução de silos entre sistemas

#### 5. Para o Ecossistema de IA

- **Padronização da Indústria:** Protocolo comum para toda a indústria
- **Inovação Acelerada:** Foco em capacidades específicas em vez de integrações
- **Redução de Fragmentação:** Menos duplicação de esforços
- **Crescimento Sustentável:** Base sólida para evolução futura

## Aplicação Prática: Sistema MCP para Busca e Análise de Papers Acadêmicos

Agora que compreendemos os conceitos e estruturas fundamentais do MCP, é hora de visualizar esses conhecimentos em ação. A seguir, apresentaremos uma **aplicação prática desenvolvida pelos autores deste e-book**, que demonstra passo a passo como implementar as funcionalidades do MCP em um cenário real.

Trata-se de um **Sistema MCP para Busca e Análise de Papers Acadêmicos** — uma solução completa que permite **buscar, analisar e interagir com artigos científicos** utilizando o protocolo MCP aliado à inteligência artificial. Esse exemplo mostra como integrar agentes com ferramentas externas, manipulando dados em tempo real e simulando conversas orientadas por LLMs.

Você pode conciliar a leitura e implementação deste projeto com os conteúdos aprofundados disponíveis no curso {cite}`deeplearning_mcp_course`.

**O que é este projeto?** Este é um sistema que permite:

- **Buscar** artigos científicos no ArXiv (maior repositório de artigos acadêmicos).
- **Ler detalhes** completos de qualquer artigo encontrado.
- **Analisar** automaticamente com IA (resumos, tendências, comparações).
- **Conversar** sobre os artigos com um assistente inteligente.
- **Cache inteligente** para respostas mais rápidas.

**Como funciona?** O sistema possui duas partes:

1. **Servidor MCP** (`mcp_papers_server.py`): O "cérebro" que busca artigos e usa IA
2. **Cliente MCP** (`mcp_papers_client.py`): A interface que você usa para interagir

```
Você → Cliente → Servidor → ArXiv/Gemini IA
                    ↓
              Resultados
                    ↓
              Você recebe
```

---

### Requisitos

Antes de iniciar a aplicação, certifique-se de que os seguintes requisitos estão atendidos no seu ambiente:

- **Python 3.8 ou superior** — [Baixe aqui](https://www.python.org/downloads/)
- **pip** — Gerenciador de pacotes do Python (já incluído na instalação padrão)
- **Chave de API do Google Gemini** — [Obtenha gratuitamente aqui](https://makersuite.google.com/app/apikey)
  
## Instalação Completa (Passo a Passo)

### Passo 1: Preparar o Ambiente

#### 1.1 Criar a estrutura de pastas

Crie uma pasta para o projeto:

```bash
# Windows (no prompt de comando)
mkdir CHATBOT-PAPERS
cd CHATBOT-PAPERS
mkdir Servidores
mkdir Servidores\logs

# Linux/Mac (no terminal)
mkdir -p CHATBOT-PAPERS/Servidores/logs
cd CHATBOT-PAPERS
```

Estrutura final:

```
CHATBOT-PAPERS/
├── .venv/                      # Ambiente virtual (será criado)
├── Servidores/
│   ├── logs/                   # Logs do sistema
│   ├── .env                    # Configurações (criar)
│   ├── mcp_papers_server.py    # Servidor (criar)
│   ├── mcp_papers_client.py    # Cliente (criar)
│   └── requirements.txt        # Dependências (criar)
```

#### 1.2 Criar ambiente virtual

**Por que fazer isso?** Para isolar as dependências do projeto e não bagunçar seu Python.

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

```{admonition}
:class: tip
Você verá `(.venv)` no início da linha do terminal quando ativado.
```

### Passo 2: Instalar Dependências

#### 2.1 Criar arquivo `requirements.txt`

Na pasta `Servidores`, crie o arquivo `requirements.txt`:

```txt
# Dependências principais
fastmcp>=0.1.0
arxiv>=2.0.0
google-generativeai>=0.3.0
python-dotenv>=1.0.0

# Dependências do cliente
mcp>=0.1.0
colorama>=0.4.6

# Ferramentas de desenvolvimento (opcional)
mcp-inspector>=0.1.0
```

#### 2.2 Instalar tudo de uma vez

```bash
cd Servidores
pip install -r requirements.txt
```
```{admonition}
:class: tip
⏳ Isso pode levar alguns minutos. Aguarde até finalizar.
```

### Passo 3: Configurar API Key

#### 3.1 Obter sua chave API do Google Gemini

1. Acesse: https://makersuite.google.com/app/apikey
2. Faça login com sua conta Google
3. Clique em "Create API Key"
4. Copie a chave gerada

#### 3.2 Criar arquivo `.env`

Na pasta `Servidores`, crie o arquivo `.env`:

```env
# Chave da API do Google Gemini (OBRIGATÓRIO)
GOOGLE_API_KEY=sua_chave_api_aqui

# Configurações opcionais
MCP_SERVER_NAME=papers-academic-server
MCP_LOG_LEVEL=INFO
```

```{admonition} IMPORTANTE
:class: warning

- Substitua `sua_chave_api_aqui` pela chave real
- **NUNCA compartilhe** este arquivo publicamente
- Adicione `.env` ao `.gitignore` se usar Git
```

### Passo 4: Adicionar os Códigos

#### 4.1 Criar o servidor (`mcp_papers_server.py`)

Cole o código do servidor fornecido anteriormente.

#### 4.2 Criar o cliente (`mcp_papers_client.py`)

Cole o código do cliente fornecido anteriormente.

---

## Como Usar

### Método 1: Modo Simples (Recomendado para Iniciantes)

Basta executar o cliente, que iniciará tudo automaticamente:

```bash
# Na pasta Servidores, com ambiente ativado
python mcp_papers_client.py
```

### Método 2: Modo Avançado (Debug)

Execute servidor e cliente separadamente para ver logs detalhados:

**Terminal 1 - Servidor:**

```bash
cd CHATBOT-PAPERS/Servidores
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # Linux/Mac
python mcp_papers_server.py
```

**Terminal 2 - Cliente:**

```bash
cd CHATBOT-PAPERS/Servidores
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # Linux/Mac
python mcp_papers_client.py
```

---

## Guia de Uso Interativo

### Menu Principal

Quando você executar o cliente, verá:

```
📚 Cliente MCP de Papers Acadêmicos
=================================

🔌 Conectando ao servidor MCP...
✅ Conectado com sucesso!
📦 6 ferramentas disponíveis

📋 Menu de Opções
========================================
  1 - Buscar papers
  2 - Ver detalhes de um paper
  3 - Analisar papers (resumo)
  4 - Analisar papers (tendências)
  5 - Analisar papers (comparação)
  6 - Chat sobre papers
  7 - Informações do cache
  8 - Limpar cache
  9 - Ajuda
  0 - Sair
========================================

Escolha uma opção:
```

### Exemplo de Uso Completo

#### Buscar Papers sobre Inteligência Artificial

```
Escolha uma opção: 1
Digite os termos de busca: artificial intelligence ethics
Número de resultados (1-10, padrão 5): 5

🔍 Buscando papers...
✅ Encontrados 5 papers!

📄 Paper 1:
   Título: Ethics in AI: A Comprehensive Review
   Autores: John Smith, Jane Doe
   Data: 2024-09-15
   ArXiv ID: 2409.12345
```

#### Ver Detalhes de um Paper

```
Escolha uma opção: 2
Digite o número do paper (1-5): 1

📄 Detalhes do Paper
========================================
Título: Ethics in AI: A Comprehensive Review
Autores: John Smith, Jane Doe
Data de Publicação: 2024-09-15
ArXiv ID: 2409.12345
Link: https://arxiv.org/abs/2409.12345

📝 Resumo:
This paper reviews ethical considerations in artificial
intelligence systems, focusing on bias, transparency,
and accountability...
```

#### Gerar Análise Inteligente

```
Escolha uma opção: 3
🤖 Gerando análise com IA...

📊 RESUMO EXECUTIVO
========================================
Com base nos 5 papers analisados sobre ética em IA:

🔑 Principais Descobertas:
- Viés algorítmico é o tema mais recorrente
- Necessidade de frameworks regulatórios
- Importância da transparência em sistemas críticos

📈 Tendências:
- Crescente preocupação com privacidade
- Desenvolvimento de IA explicável (XAI)
- Foco em IA centrada no ser humano
```

#### Chat Interativo

```
Escolha uma opção: 6
Digite sua pergunta (ou 'voltar' para menu):
> Quais metodologias são mais usadas para detectar viés?

🤖 Resposta:
Baseado nos papers analisados, as principais metodologias
incluem:

1. Análise estatística de disparidade de impacto
2. Testes de fairness (equidade) em diferentes grupos
3. Auditoria algorítmica com datasets de teste
4. Métodos de interpretabilidade como SHAP e LIME

Os papers recomendam usar uma combinação de técnicas...

Digite sua pergunta (ou 'voltar' para menu):
> voltar
```

---

## Funcionalidades Detalhadas

### 1. Busca de Papers (`search_papers`)

**O que faz:** Busca artigos no ArXiv

**Parâmetros:**
- `query`: Termos de busca (ex: "machine learning", "quantum computing")
- `max_results`: Quantidade de resultados (1-10)

```{admonition} Dica
:class: tip
Use termos em inglês para melhores resultados.
```

### 2. Detalhes do Paper (`get_paper_details`)

**O que faz:** Mostra informações completas de um artigo

**Informações exibidas:**
- Título completo
- Lista de autores
- Data de publicação
- Resumo (abstract)
- Link direto para o ArXiv

### 3. Análise com IA (`analyze_papers`)

**O que faz:** Usa Gemini para analisar os papers encontrados

**Tipos de análise:**
- **Summary**: Resumo executivo geral
- **Trends**: Identifica tendências e padrões
- **Comparison**: Compara metodologias e resultados

### 4. Chat Inteligente (`chat_about_papers`)

**O que faz:** Conversa sobre os papers em linguagem natural

```{admonition} Exemplos de perguntas
:class: exemplo
- "Quais são as limitações apontadas?"
- "Que datasets foram usados?"
- "Como os métodos se comparam?"
- "Quais as aplicações práticas?"
```

### 5. Gerenciamento de Cache

**O que é cache?** Memória temporária que acelera respostas repetidas.

**Comandos:**
- `get_cache_info`: Ver quantos papers estão em cache
- `clear_cache`: Limpar cache (útil para buscas novas)

---

## Monitoramento e Logs

### Visualizar Logs em Tempo Real

**Windows:**

```bash
# Em um novo terminal
cd CHATBOT-PAPERS\Servidores
type logs\mcp_server.log
```

**Linux/Mac:**

```bash
# Visualização contínua
tail -f Servidores/logs/mcp_server.log
```

### Entender os Logs

Formato dos logs:

```
2025-09-30 14:32:15 - INFO - Searching for: machine learning
2025-09-30 14:32:17 - INFO - Found 5 papers
2025-09-30 14:32:20 - ERROR - API key invalid
```

```{admonition} Níveis:
:class: note
- `INFO`: Informações normais
- `WARNING`: Avisos (não crítico)
- `ERROR`: Erros que precisam atenção
```

---

## Casos de Uso Práticos

### 1. Revisão Bibliográfica Rápida

```{admonition} Objetivo: Revisar literatura sobre um tema
:class: note
Fluxo:
1. Buscar papers (opção 1)
2. Ver detalhes dos mais relevantes (opção 2)
3. Gerar resumo executivo (opção 3)
4. Fazer perguntas específicas (opção 6)
```

### 2. Identificar Tendências de Pesquisa

```{admonition} Objetivo: Entender direções da área
:class: note
Fluxo:
1. Buscar papers recentes (opção 1)
2. Análise de tendências (opção 4)
3. Chat sobre metodologias emergentes (opção 6)
```

### 3. Comparar Abordagens

```{admonition}Objetivo: Comparar diferentes métodos
:class: note
Fluxo:
1. Buscar papers sobre métodos específicos
2. Análise comparativa (opção 5)
3. Perguntar sobre vantagens/desvantagens
```

---

## Segurança e Boas Práticas

```{admonition} Faça:
:class: tip

- Mantenha seu `.env` privado
- Use `.gitignore` se versionar o código
- Atualize dependências regularmente: `pip install -U -r requirements.txt`
- Faça backup dos logs importantes
- Monitore uso da API Gemini
```

```{admonition} Não Faça:
:class: warning

- Compartilhar sua API key
- Commitar `.env` no Git
- Fazer milhares de requisições seguidas (rate limit)
- Usar em produção sem autenticação adicional
- Ignorar mensagens de erro nos logs
```

### Arquivo `.gitignore` recomendado

Para manter seu repositório limpo e evitar o versionamento de arquivos desnecessários, recomendamos utilizar um arquivo `.gitignore` adequado ao projeto.

```gitignore
# Ambiente virtual
.venv/
venv_mcp/

# Configurações sensíveis
.env
*.env

# Logs
logs/
*.log

# Python
__pycache__/
*.pyc
*.pyo
*.pyd

# IDE
.vscode/
.idea/
*.swp
```

---

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

##  Recursos Úteis

Durante a implementação e aprofundamento no uso do MCP, é importante ter à mão algumas ferramentas e documentações de apoio. Abaixo estão links úteis que podem acelerar o desenvolvimento e facilitar a integração com APIs e modelos de IA:

- **Documentação FastMCP**: https://github.com/jlowin/fastmcp
- **ArXiv API**: https://arxiv.org/help/api
- **Google Gemini**: https://ai.google.dev/
- **Python.org**: https://docs.python.org/3/

---

## Créditos

Desenvolvido com:

- **FastMCP**: Framework MCP
- **ArXiv API**: Busca de papers
- **Google Gemini**: Análise com IA
- **Python**: Linguagem de programação

---
