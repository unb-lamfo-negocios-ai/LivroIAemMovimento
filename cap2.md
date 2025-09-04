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
