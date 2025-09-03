# Capítulo 2 – Arquiteturas, Tecnologias e Componentes Técnicos

Uma solução de Inteligência Artificial é formada por diferentes **camadas técnicas** que trabalham em conjunto para transformar dados em valor.  
Neste capítulo, você vai entender os principais **componentes de arquitetura, tecnologias e protocolos** utilizados atualmente, de forma clara e prática.

---

## Prompt Engineering e RAG

O **Prompt Engineering** é a arte de **escrever instruções eficazes** para guiar modelos de linguagem, como os LLMs, a gerar respostas úteis e consistentes.  
Trata-se de uma habilidade essencial, pois a qualidade da saída depende diretamente da **clareza e estrutura do prompt** {cite}`liu2023`.

Já o **Retrieval-Augmented Generation (RAG)** combina LLMs com **bases de conhecimento externas**.  
Assim, o modelo não depende apenas do que aprendeu no treinamento, mas pode consultar documentos, bancos de dados ou APIs em tempo real {cite}`lewis2020`.  
Esse paradigma melhora a precisão e reduz alucinações.

---

## API e Integração

Uma **API (Application Programming Interface)** é o meio pelo qual sistemas diferentes **se comunicam**.  
No contexto de IA, as APIs permitem que modelos sejam facilmente conectados a aplicativos, websites ou sistemas corporativos {cite}`fielding2000`.

Exemplo prático:  
- Um e-commerce pode usar a **API de visão computacional** para classificar automaticamente fotos de produtos.  
- Um chatbot pode ser alimentado por uma **API de NLP** para responder perguntas de clientes.

---

## Rodar Localmente vs. Cloud Computing

As soluções de IA podem ser executadas de duas formas principais:

- **Localmente** (*on-premise*): maior controle sobre dados, porém exige infraestrutura robusta.  
- **Na nuvem** (*cloud computing*): escalabilidade, menor custo inicial e acesso a modelos prontos {cite}`armbrust2010`.

A escolha depende de fatores como segurança, custo e velocidade de implantação.

---

## Frontend vs. Backend

Uma aplicação de IA precisa de duas camadas principais:

- **Frontend**: a interface que o usuário final vê e interage (ex.: site, aplicativo).  
- **Backend**: o "motor invisível" que processa dados, executa modelos de IA e retorna resultados.  

Separar essas responsabilidades torna a arquitetura mais **flexível e escalável**.

---

## UX de IA — Interação Humano-Sistema

A **Experiência do Usuário (UX)** em sistemas de IA tem características próprias:  
- Transparência: deixar claro de onde vêm as respostas.  
- Controle: permitir que o usuário refine ou corrija resultados.  
- Confiança: mostrar limitações e incertezas do modelo {cite}`amershi2019`.

Projetar boas interfaces é tão importante quanto a qualidade do modelo em si.

---

## Protocolos como MCP (Model Context Protocol)

O **Model Context Protocol (MCP)** é uma iniciativa recente que propõe **padronizar a comunicação entre aplicações e modelos de IA**.  
Ele busca garantir que diferentes ferramentas possam se conectar de forma segura e consistente, evitando integrações fragmentadas.  

Essa padronização é crucial em um cenário em que múltiplos modelos, serviços e frameworks precisam colaborar.

---

:::{note}
Compreender a **arquitetura e os componentes técnicos** não significa que você precise programar cada parte.  
O mais importante é ter **clareza das opções disponíveis** para tomar decisões estratégicas de implementação.
:::
