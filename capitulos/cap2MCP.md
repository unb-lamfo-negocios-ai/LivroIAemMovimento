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

- `OpenAI Function Calling`
- `LangChain Agents Protocol`
- `Open Agents Protocol (OAP)`
- `Model Context Protocol (MCP)`

- [`OpenAi Function Calling´](https://platform.openai.com/docs/guides/function-calling)
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

#### **Componentes principais:**

- **Recursos**: Dados estáticos ou dinâmicos para os modelos

- **Prompts**: Fluxos de trabalho predefinidos para geração guiada

- **Ferramentas**: Funções executáveis como busca, cálculos

- **Amostragem**: Comportamento agente por meio de interações recursivas

#### Componentes Detalhados

- [**MCP Host (Anfitrião)](https://modelcontextprotocol.io/docs/getting-started/intro):**
- É a aplicação ou ferramenta que o usuário interage diretamente

```{admonition} Exemplos de MCP host
:class: exemplo
[Claude Code](https://claude.com/product/claude-code) ou [Claude Desktop](https://claude.ai/download), IDEs (como Cursor ou Windsurf).
```

    - **Responsabilidades:**
        - Gerenciar a configuração do usuário
        - Iniciar conexões com servidores MCP
        - Orquestrar a interação com o LLM
        - Apresentar resultados ao usuário
     - **MCP Client (Cliente):**
- Componente interno do MCP Host
- Mantém conexões um-para-um com os servidores MCP
    - **Responsabilidades:**
        - Descobrir capacidades dos servidores
        - Gerenciar autenticação
        - Traduzir requisições entre Host e Server
        - Manter estado das conexões
- **MCP Server (Servidor):**
- Programa leve que atua como "wrapper" para sistemas externos
- Pode ser executado localmente ou remotamente
    - **Responsabilidades:**
        - Expor ferramentas, recursos e prompts
        - Implementar lógica de negócio específica
        - Gerenciar acesso a sistemas externos
        - Manter segurança e permissões

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

##### 1.Ferramentas(Tools)

Controle: Controladas pelo modelo (LLM)

Função: Permitem que o LLM execute ações no mundo real ou recupere dados

As ferramentas são capacidades que o servidor MCP expõe para que o LLM possa invocar quando apropriado. O modelo decide autonomamente quando e como usar cada ferramenta baseado no contexto da conversa.

**Características das Ferramentas:**

- Invocação Automática: O LLM decide quando usar
- Parâmetros Estruturados: Definidos via JSON Schema
- Resposta Estruturada: Retorno padronizado
- Assincronia: Podem executar operações longas

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

**Casos de Uso Comuns:**

- Integrações com GitHub (listar issues, criar PRs)
- Asana (adicionar tarefas, atualizar status)
- Brave (pesquisar na web)
- Sistemas de arquivos (ler/escrever arquivos)
- APIs diversas (Stripe, Cloudflare, etc.)

##### 2.Recursos (Resources)
Controle: Controlados pela aplicação (o MCP Host)

Função: São dados expostos à aplicação que podem ser anexados ao contexto

Os recursos são diferentes das ferramentas porque não são invocados pelo LLM, mas sim disponibilizados pela aplicação para enriquecer o contexto da conversa.

**Tipos de Recursos:**

- Estáticos: Arquivos JSON, documentos, configurações
- Dinâmicos: Dados interpolados com informações do usuário/sistema
- Streaming: Recursos que atualizam em tempo real

**Exemplos de Recursos:**
```json
{

"uri": "file:///home/user/project/README.md",

"name": "Project Documentation",

"description": "Documentação principal do projeto",

"mimeType": "text/markdown"

}
```
**Casos de Uso:**

- Anexos em um chat (imagens, documentos)
- Logs de sistema em tempo real
- Configurações de projeto
- Dados de contexto do usuário
- Arquivos de referência

##### # 3.Prompts

Controle: Controlados pelo usuário

Função: Modelos predefinidos para interações comuns

Os prompts são como "templates" ou "comandos de barra" que os usuários podem invocar para executar operações complexas predefinidas.

**Características dos Prompts:**

- Invocação Manual: Usuário escolhe quando usar (ex: /summarize)
- Parametrizáveis: Podem receber argumentos do usuário
- Contextuais: Podem usar informações do ambiente atual
- Reutilizáveis: Mesmo prompt funciona em diferentes contextos

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

**Exemplos Práticos:**

- /summarize - Resumir documentos ou conversas
- /translate - Traduzir texto para outro idioma
- /code-review - Revisar código com padrões da empresa
- /meeting-notes - Extrair ações de notas de reunião

# Exemplos de Mensagens Comuns

##  O que são essas mensagens?

Imagine que o **Cliente** (seu programa) e o **Servidor** (que busca papers) precisam conversar. Eles usam um formato especial chamado **JSON-RPC** para se entenderem, como se fosse um idioma comum.

**Analogia:** É como pedir um lanche no drive-thru:
- **Você (Cliente):** "Quero um hambúrguer com queijo"
- **Atendente (Servidor):** "Ok, são R$ 15,00. Seu pedido está sendo preparado"

Todas as mensagens seguem esse padrão de "pergunta → resposta".

---

## 📋 Estrutura Básica das Mensagens

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

**Campos principais:**
- `jsonrpc`: Versão do protocolo (sempre 2.0)
- `id`: Identificador único da mensagem
- `method`: O que você quer fazer
- `params`: Parâmetros/dados necessários

---

## 1️⃣ Inicialização da Conexão

### 🎯 O que acontece aqui?

Esta é a **primeira mensagem** trocada quando o cliente se conecta ao servidor. É como um "aperto de mãos" digital onde ambos dizem:
- "Oi, eu sou o Cliente, versão 1.0.0"
- "Olá, eu sou o Servidor, versão 1.0.0, e posso fazer X, Y e Z"

### 📤 Cliente pergunta: "Quem é você e o que pode fazer?"

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

**Explicação dos campos:**
- `method: "initialize"` → Estou iniciando a conexão
- `protocolVersion` → Versão do MCP que estou usando
- `capabilities` → O que eu (cliente) consigo fazer
- `clientInfo` → Meu nome e versão

### 📥 Servidor responde: "Oi! Eu posso fazer isso..."

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

**Explicação dos campos:**
- `result` → Resposta bem-sucedida (não é erro)
- `capabilities` → O que EU (servidor) consigo fazer
- `listChanged: true` → Posso avisar quando algo mudar
- `subscribe: true` → Você pode se inscrever para receber atualizações
- `serverInfo` → Meu nome e versão

---

## 2️⃣ Listagem de Ferramentas Disponíveis

### 🎯 O que acontece aqui?

Depois de conectado, o cliente pergunta: **"Quais ferramentas você tem disponíveis?"**

É como entrar numa oficina e perguntar: "Quais ferramentas vocês têm aí? Martelo? Chave de fenda?"

### 📤 Cliente pergunta: "Que ferramentas você oferece?"

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

**Explicação:**
- `method: "tools/list"` → Quero ver a lista de ferramentas
- `id: "2"` → Esta é minha segunda mensagem (a primeira foi o initialize)
- Sem `params` porque não preciso enviar dados extras

### 📥 Servidor responde: "Tenho estas ferramentas..."

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

**Explicação dos campos:**
- `tools` → Array (lista) com todas as ferramentas
- `name` → Nome único da ferramenta (usado para chamá-la)
- `description` → Explicação do que a ferramenta faz
- `inputSchema` → "Contrato" de como usar a ferramenta
  - `properties` → Parâmetros que você pode enviar
  - `required` → Parâmetros obrigatórios
  - `type: "string"` → Tipo de dado (texto, número, etc.)


## 3️⃣ Execução de uma Ferramenta

### 🎯 O que acontece aqui?

Agora que o cliente sabe quais ferramentas existem, ele **usa uma delas**. É como dizer: "Ok, vi que você tem essa ferramenta 'get_weather'. Quero usar agora para São Paulo!"

### 📤 Cliente chama: "Use a ferramenta X com estes dados"

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

**Explicação dos campos:**
- `method: "tools/call"` → Quero executar uma ferramenta
- `params.name` → Nome da ferramenta que quero usar
- `params.arguments` → Os dados necessários (conforme o inputSchema)
- `arguments.location` → Parâmetro obrigatório definido no schema

### 📥 Servidor responde: "Aqui está o resultado!"

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

**Explicação dos campos:**
- `result.content` → O conteúdo da resposta (pode ser texto, imagem, etc.)
- `type: "text"` → O resultado é texto puro
- `text` → O resultado em si

### 🔍 Exemplo Real do Nosso Projeto

Chamando a ferramenta de busca de papers:

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

---

## 🚨 Tratamento de Erros

### O que acontece se der erro?

Se algo der errado, o servidor responde com um **erro** ao invés de `result`.

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

**Códigos de erro comuns:**
- `-32700` → JSON inválido (erro de sintaxe)
- `-32600` → Requisição inválida
- `-32601` → Método/ferramenta não encontrado
- `-32602` → Parâmetros inválidos
- `-32603` → Erro interno do servidor

---

## 📊 Fluxo Completo de Comunicação

### Sequência típica de uso:

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

## 🎓 Resumo para Leigos

### O que você precisa entender:

1. **JSON-RPC** é só um formato padronizado de mensagens
2. Sempre há um **id** para identificar cada conversa
3. **Cliente pergunta** (`method`) → **Servidor responde** (`result` ou `error`)
4. Tudo começa com `initialize` (apresentação)
5. Depois vem `tools/list` (ver o que tem disponível)
6. Por fim `tools/call` (usar uma ferramenta específica)

### Analogia Final: Restaurante

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

## 💡 Dicas Práticas

### Para Desenvolvedores:

- ✅ Sempre valide o `inputSchema` antes de chamar ferramentas
- ✅ Use `id` único para cada mensagem
- ✅ Implemente timeout (não espere eternamente por resposta)
- ✅ Trate todos os códigos de erro possíveis
- ✅ Teste com ferramentas simples primeiro

### Para Usuários:

- ✅ Se ver erro `-32601`: A ferramenta não existe
- ✅ Se ver erro `-32602`: Faltou algum parâmetro obrigatório
- ✅ Se ver erro `-32603`: Problema no servidor (tente novamente)
- ✅ Verifique os logs para detalhes dos erros

---

## 🔗 Recursos Adicionais

- **Especificação JSON-RPC 2.0**: https://www.jsonrpc.org/specification
- **Documentação MCP**: https://modelcontextprotocol.io
- **Validador JSON**: https://jsonlint.com

---


### Outras Capacidades Essenciais{cite}`mcp_workshop_youtube, mcp_official_docs`

#### 1. Composability (Componibilidade)

Uma característica poderosa do MCP é que qualquer aplicação, API ou agente pode ser tanto um cliente MCP quanto um servidor MCP simultaneamente. Isso permite criar arquiteturas complexas e em camadas.

Exemplo de Arquitetura Composta:

Agent de Pesquisa (Cliente + Servidor)

- **Como Cliente, usa:**
- Web Search MCP Server
- Database MCP Server
- File System MCP Server
- **Como Servidor, expõe:**
- research_topic()
- summarize_findings()
- generate_report()

**Benefícios da Componibilidade:**

- **Especialização:** Cada camada foca em uma responsabilidade específica
- **Reutilização:** Componentes podem ser usados em diferentes contextos
- **Escalabilidade:** Fácil adicionar novas capacidades
- **Manutenibilidade:** Mudanças isoladas por componente

#### 2. Sampling (Amostragem)

Permite que um servidor MCP solicite inferências (chamadas de LLM) do cliente, sem precisar hospedar seu próprio modelo.

**Como Funciona:**

1. Servidor precisa de inteligência para uma decisão
2. Solicita ao cliente para fazer uma inferência
3. Cliente usa seu LLM e retorna resultado
4. Servidor usa o resultado para continuar processamento

**Exemplo Prático:**

// Servidor -> Cliente (solicitando inferência)

- ***Resumo do Fluxo:****

1. Você pede: "Organize minha caixa de entrada"

2. Servidor lê email e precisa classificar urgência

3. Servidor ****pede ao llm****: "Esse email é urgente?"

4. llm analisa e responde: "URGENTE - Requer ação imediata"

5. Servidor executa ação: move para pasta "Urgentes" e notifica você

- ***Por que isso é poderoso?****

1.Servidor permanece simples (sem IA própria)

2.Você controla custos e privacidade (tudo via seu (llm))

veja: 

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

**Vantagens:**

- Servidor não precisa gerenciar LLM próprio
- Cliente mantém controle sobre custos e privacidade
- Consistência no modelo usado em toda a aplicação

#### 3. Elicitation (Elicitação)

Capacidade que permite ao servidor solicitar informações adicionais dos usuários durante a execução de uma ferramenta.

**Casos de Uso:**

- Confirmar ações críticas (deletar arquivos, fazer pagamentos)
- Coletar informações adicionais necessárias
- Obter permissões específicas

**Exemplo de Fluxo:**

// Durante execução de uma ferramenta de reserva
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
#### 4. Completions (Conclusões/Sugestões)

O MCP suporta autocompletar para argumentos de prompt e parâmetros de recursos.

**Implementação:**

// Cliente solicita sugestões

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

// Servidor retorna sugestões

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

#### 5. Authentication (Autenticação)

Os servidores MCP podem implementar OAuth 2.0/2.1 para acessar recursos protegidos.

**Fluxo de Autenticação:**

1. Servidor inicia processo OAuth
2. Cliente redireciona usuário para provedor
3. Usuário autentica e autoriza
4. Servidor recebe token OAuth
5. Cliente recebe token de sessão para uso futuro

**Configuração Exemplo:**

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

#### 6. Notifications (Notificações)

Servidores podem enviar notificações para clientes sobre mudanças de estado.

**Tipos de Notificações:**

- resources/updated: Recurso foi modificado
- tools/list_changed: Lista de ferramentas mudou
- prompts/list_changed: Lista de prompts mudou

**Exemplo:**
```json
{
   "jsonrpc": "2.0",
   "method": "notifications/resources/updated",
   "params": {
      "uri": "file:///project/config.json"
    }
}
```
#### 7. Transports (Transportes)

O MCP suporta diferentes mecanismos de comunicação:

**Transporte Local (STDIO):**

- Comunicação via entrada/saída padrão
- Ideal para servidores locais
- Baixa latência, alta segurança

**Transporte Remoto (HTTP/SSE):**

- Comunicação via HTTP com Server-Sent Events
- Permite servidores remotos
- Suporte a múltiplos clientes

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
### Limitações e Considerações de Segurança{cite}`dsacademy_mcp_blog, neo4j_mcp_blog`

#### 1. Limitações do MCP

**Limitações de Performance:**

- Latência de Rede: Servidores remotos podem ter latência alta
- Throughput: Limitado pela capacidade do transporte (HTTP vs STDIO)
- Concorrência: Nem todos os servidores suportam requisições paralelas
- Timeout: Operações longas podem exceder limites de timeout

**Limitações Funcionais:**

- Stateless: Servidores MCP são geralmente stateless entre requisições
- Transações: Não há suporte nativo para transações distribuídas
- Streaming de Dados: Limitado para grandes volumes de dados
- Compatibilidade: Nem todas as ferramentas/APIs têm servidor MCP

**Quando NÃO Usar MCP:**

- Aplicações que precisam de latência ultra-baixa
- Sistemas que requerem transações ACID complexas
- Integrações simples que não justificam a complexidade
- Ambientes com restrições severas de recursos

#### 2. Considerações de Segurança

**Autenticação e Autorização:**

// Exemplo de configuração segura

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
**Validação de Entrada:**

- Sempre validar parâmetros de ferramentas
- Sanitizar dados antes de usar em queries/comandos
- Implementar rate limiting para prevenir abuso
- Usar schemas JSON rigorosos

**Controle de Acesso:**

# Exemplo de verificação de permissões

```python
def verify_permissions(operation, resource):
    if operation == "DELETE" and not user.has_permission("admin"):
        raise PermissionError("Operação DELETE requer permissão de admin")
    if resource.startswith("/system/") and not user.has_permission("system"):
        raise PermissionError("Acesso a recursos do sistema negado")
```

**Isolamento e Sandboxing:**

- Execute servidores MCP em containers ou ambientes isolados
- Use usuários com privilégios limitados
- Implemente timeouts para prevenir operações infinitas
- Monitore recursos (CPU, memória, disco)

**Auditoria e Logging:**

**O que é:** 

Sistema de registro que monitora e documenta todas as operações realizadas através do MCP. É como ter um "diário detalhado" de tudo que acontece entre cliente e servidor. 

**Por que é importante:** 

- **Rastreabilidade**: Saber exatamente quem fez o quê e quando
- **Debugging**: Identificar problemas e entender falhas
- **Segurança**: Detectar uso inadequado ou tentativas de acesso não autorizado
- **Compliance**: Atender requisitos legais de auditoria

**Informações Registradas:**

- ⏰ Timestamp (momento exato da operação) 

- 🔧 Ferramenta/recurso acessado 

- 👤 Usuário que realizou a ação 

- 📋 Parâmetros enviados 

- ✅/❌ Status do resultado (sucesso ou erro) 

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

**Boas Práticas de Segurança:**

1. **Princípio do Menor Privilégio:** Conceda apenas as permissões mínimas necessárias
2. **Defesa em Profundidade:** Múltiplas camadas de segurança
3. **Monitoramento Contínuo:** Logs e alertas para atividades suspeitas
4. **Atualizações Regulares:** Mantenha servidores MCP atualizados
5. **Testes de Segurança:** Auditorias regulares e testes de penetração

### Benefícios do MCP

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

# Sistema MCP para Busca e Análise de Papers Acadêmicos(Aplicação Prática) {cite}`deeplearning_mcp_course`

> Um sistema completo para buscar, analisar e conversar sobre artigos científicos usando o protocolo MCP (Model Context Protocol) com inteligência artificial.

## O que é este projeto?

Este é um sistema que permite:

- 🔍 **Buscar** artigos científicos no ArXiv (maior repositório de artigos acadêmicos)
- 📖 **Ler detalhes** completos de qualquer artigo encontrado
- 🤖 **Analisar** automaticamente com IA (resumos, tendências, comparações)
- 💬 **Conversar** sobre os artigos com um assistente inteligente
- 💾 **Cache inteligente** para respostas mais rápidas

### Como funciona?

O sistema possui duas partes:

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

## Requisitos

### O que você precisa ter instalado:

- **Python 3.8+** ([Baixar aqui](https://www.python.org/downloads/))
- **pip** (gerenciador de pacotes Python - vem com Python)
- **Chave API do Google Gemini** ([Obter gratuitamente aqui](https://makersuite.google.com/app/apikey))

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

✅ Você verá `(.venv)` no início da linha do terminal quando ativado.

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

⏳ Isso pode levar alguns minutos. Aguarde até finalizar.

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

⚠️ **IMPORTANTE**:

- Substitua `sua_chave_api_aqui` pela chave real
- **NUNCA compartilhe** este arquivo publicamente
- Adicione `.env` ao `.gitignore` se usar Git

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

**Dica:** Use termos em inglês para melhores resultados.

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

**Exemplos de perguntas:**
- "Quais são as limitações apontadas?"
- "Que datasets foram usados?"
- "Como os métodos se comparam?"
- "Quais as aplicações práticas?"

### 5. Gerenciamento de Cache

**O que é cache?** Memória temporária que acelera respostas repetidas.

**Comandos:**
- `get_cache_info`: Ver quantos papers estão em cache
- `clear_cache`: Limpar cache (útil para buscas novas)

---

## 📊 Monitoramento e Logs

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

**Níveis:**
- `INFO`: Informações normais
- `WARNING`: Avisos (não crítico)
- `ERROR`: Erros que precisam atenção

---

## Casos de Uso Práticos

### 1. Revisão Bibliográfica Rápida

```
Objetivo: Revisar literatura sobre um tema
Fluxo:
1. Buscar papers (opção 1)
2. Ver detalhes dos mais relevantes (opção 2)
3. Gerar resumo executivo (opção 3)
4. Fazer perguntas específicas (opção 6)
```

### 2. Identificar Tendências de Pesquisa

```
Objetivo: Entender direções da área
Fluxo:
1. Buscar papers recentes (opção 1)
2. Análise de tendências (opção 4)
3. Chat sobre metodologias emergentes (opção 6)
```

### 3. Comparar Abordagens

```
Objetivo: Comparar diferentes métodos
Fluxo:
1. Buscar papers sobre métodos específicos
2. Análise comparativa (opção 5)
3. Perguntar sobre vantagens/desvantagens
```

---

## Segurança e Boas Práticas

### ✅ Faça:

- Mantenha seu `.env` privado
- Use `.gitignore` se versionar o código
- Atualize dependências regularmente: `pip install -U -r requirements.txt`
- Faça backup dos logs importantes
- Monitore uso da API Gemini

### ❌ Não Faça:

- Compartilhar sua API key
- Commitar `.env` no Git
- Fazer milhares de requisições seguidas (rate limit)
- Usar em produção sem autenticação adicional
- Ignorar mensagens de erro nos logs

### Arquivo `.gitignore` Recomendado

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

## Suporte

### Recursos Úteis

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
