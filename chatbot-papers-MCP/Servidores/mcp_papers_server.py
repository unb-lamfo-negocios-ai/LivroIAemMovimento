#!/usr/bin/env python3
"""
Servidor MCP para busca e análise de papers acadêmicos.
Baseado no chatbot_gemini.py original.
"""

import os
import sys
import json
import asyncio
import logging
from typing import List, Dict, Any, Optional
from datetime import datetime

# Importações do FastMCP
from fastmcp import FastMCP, Context


# Importações do projeto original
import arxiv
import google.generativeai as genai
from dotenv import load_dotenv
import re

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Carregar variáveis de ambiente
load_dotenv()

# Inicializar o servidor MCP
mcp = FastMCP(
    name="papers-academic-server",
    version="1.0.0",
    instructions="Servidor MCP para busca e análise de papers acadêmicos usando ArXiv e Google Gemini"
)

class PapersService:
    """Serviço centralizado para gerenciar busca de papers e interação com Gemini."""
    
    def __init__(self):
        """Inicializa o serviço com configurações do Gemini."""
        api_key = os.getenv('GOOGLE_API_KEY')
        genai.configure(api_key=api_key) #type: ignore
        if not api_key:
            logger.error("GOOGLE_API_KEY não encontrada no ambiente")
            raise ValueError("GOOGLE_API_KEY não encontrada no arquivo .env")
        
        
        self.model = genai.GenerativeModel('gemini-2.5-pro') #type: ignore
        self.papers_cache: List[Dict[str, Any]] = []
        logger.info("PapersService inicializado com sucesso")

    async def search_papers_async(self, query: str, max_results: int = 5) -> List[Dict[str, Any]]:
        """Busca papers no ArXiv de forma assíncrona."""
        try:
            # Validação de parâmetros
            if not query or not isinstance(query, str):
                return []
            
            max_results = min(max(1, max_results), 10)
            
            logger.info(f"Buscando papers sobre: '{query}'")
            
            # Executar busca em thread separada para não bloquear
            loop = asyncio.get_event_loop()
            papers = await loop.run_in_executor(
                None, 
                self._search_papers_sync, 
                query, 
                max_results
            )
            
            self.papers_cache = papers
            logger.info(f"Encontrados {len(papers)} papers relevantes")
            return papers
            
        except Exception as e:
            logger.error(f"Erro ao buscar papers: {str(e)}")
            return []

    def _search_papers_sync(self, query: str, max_results: int) -> List[Dict[str, Any]]:
        """Executa busca síncrona no ArXiv."""
        client = arxiv.Client()
        search = arxiv.Search(
            query=query.strip(),
            max_results=max_results,
            sort_by=arxiv.SortCriterion.Relevance
        )
        
        papers = []
        for result in client.results(search):
            if len(papers) >= max_results:
                break
                
            try:
                paper = {
                    "title": result.title.strip(),
                    "summary": result.summary.strip()[:1000],  # Limitar resumo
                    "authors": [author.name for author in result.authors][:5],
                    "published": result.published.strftime("%Y-%m-%d") if result.published else "N/A",
                    "url": result.entry_id,
                    "pdf_url": result.pdf_url,
                    "categories": result.categories[:3] if hasattr(result, 'categories') else []
                }
                papers.append(paper)
            except Exception as e:
                logger.warning(f"Erro ao processar paper: {e}")
                continue
        
        return papers

    async def analyze_papers_async(self, papers: List[Dict[str, Any]], analysis_type: str = "summary") -> str:
        """Analisa papers usando Gemini de forma assíncrona."""
        if not papers:
            return "Nenhum paper disponível para análise."
        
        try:
            loop = asyncio.get_event_loop()
            analysis = await loop.run_in_executor(
                None,
                self._analyze_papers_sync,
                papers,
                analysis_type
            )
            return analysis
        except Exception as e:
            logger.error(f"Erro ao analisar papers: {str(e)}")
            return f"Erro na análise: {str(e)}"

    def _analyze_papers_sync(self, papers: List[Dict[str, Any]], analysis_type: str) -> str:
        """Executa análise síncrona com Gemini."""
        papers_context = self._format_papers_context(papers)
        
        prompts = {
            "summary": f"""
                Analise os seguintes papers acadêmicos e forneça um resumo executivo destacando:
                1. Principais temas e tendências
                2. Metodologias mais utilizadas
                3. Descobertas significativas
                4. Lacunas de pesquisa identificadas
                
                Papers:
                {papers_context}
            """,
            "trends": f"""
                Identifique as principais tendências de pesquisa nos papers abaixo:
                - Tecnologias emergentes
                - Mudanças de paradigma
                - Áreas de crescimento
                
                Papers:
                {papers_context}
            """,
            "comparison": f"""
                Compare e contraste os papers abaixo considerando:
                - Abordagens metodológicas
                - Resultados obtidos
                - Contribuições únicas
                
                Papers:
                {papers_context}
            """
        }
        
        prompt = prompts.get(analysis_type, prompts["summary"])
        response = self.model.generate_content(prompt)
        
        return response.text.strip() if response and response.text else "Análise não disponível."

    def _format_papers_context(self, papers: List[Dict[str, Any]]) -> str:
        """Formata papers para contexto do prompt."""
        context = ""
        for i, paper in enumerate(papers[:5], 1):  # Limitar a 5 papers
            authors = ", ".join(paper["authors"][:2]) + (" et al." if len(paper["authors"]) > 2 else "")
            context += f"""
Paper {i}:
Título: {paper["title"]}
Autores: {authors}
Data: {paper["published"]}
Resumo: {paper["summary"][:500]}...
URL: {paper["url"]}

"""
        return context

# Instância global do serviço
papers_service = PapersService()

# ========== FERRAMENTAS MCP ==========

@mcp.tool()
async def search_papers(
    ctx: Context,
    query: str,
    max_results: int = 5
) -> Dict[str, Any]:
    """
    Busca papers acadêmicos no ArXiv.
    
    Args:
        query: Termos de busca para encontrar papers
        max_results: Número máximo de resultados (1-10)
    
    Returns:
        Lista de papers encontrados com título, autores, resumo e links
    """
    logger.info(f"Tool 'search_papers' chamada com query='{query}', max_results={max_results}")
    
    papers = await papers_service.search_papers_async(query, max_results)
    
    return {
        "success": len(papers) > 0,
        "count": len(papers),
        "papers": papers,
        "message": f"Encontrados {len(papers)} papers sobre '{query}'"
    }

@mcp.tool()
async def get_paper_details(
    ctx: Context,
    paper_index: int = 0
) -> Dict[str, Any]:
    """
    Obtém detalhes completos de um paper do cache.
    
    Args:
        paper_index: Índice do paper no cache (começa em 0)
    
    Returns:
        Detalhes completos do paper incluindo resumo completo
    """
    if not papers_service.papers_cache:
        return {
            "success": False,
            "message": "Nenhum paper no cache. Execute uma busca primeiro."
        }
    
    if paper_index < 0 or paper_index >= len(papers_service.papers_cache):
        return {
            "success": False,
            "message": f"Índice inválido. Cache contém {len(papers_service.papers_cache)} papers."
        }
    
    paper = papers_service.papers_cache[paper_index]
    return {
        "success": True,
        "paper": paper,
        "index": paper_index,
        "total_cached": len(papers_service.papers_cache)
    }

@mcp.tool()
async def analyze_papers(
    ctx: Context,
    analysis_type: str = "summary"
) -> Dict[str, Any]:
    """
    Analisa papers no cache usando IA.
    
    Args:
        analysis_type: Tipo de análise ('summary', 'trends', 'comparison')
    
    Returns:
        Análise detalhada dos papers
    """
    if not papers_service.papers_cache:
        return {
            "success": False,
            "message": "Nenhum paper no cache. Execute uma busca primeiro."
        }
    
    valid_types = ["summary", "trends", "comparison"]
    if analysis_type not in valid_types:
        return {
            "success": False,
            "message": f"Tipo de análise inválido. Use: {', '.join(valid_types)}"
        }
    
    logger.info(f"Analisando {len(papers_service.papers_cache)} papers - tipo: {analysis_type}")
    
    analysis = await papers_service.analyze_papers_async(
        papers_service.papers_cache, 
        analysis_type
    )
    
    return {
        "success": True,
        "analysis_type": analysis_type,
        "papers_analyzed": len(papers_service.papers_cache),
        "analysis": analysis
    }

@mcp.tool()
async def clear_cache(ctx: Context) -> Dict[str, Any]:
    """
    Limpa o cache de papers.
    
    Returns:
        Status da operação
    """
    previous_count = len(papers_service.papers_cache)
    papers_service.papers_cache = []
    
    return {
        "success": True,
        "message": f"Cache limpo. {previous_count} papers removidos."
    }

@mcp.tool()
async def get_cache_info(ctx: Context) -> Dict[str, Any]:
    """
    Retorna informações sobre o cache atual.
    
    Returns:
        Informações sobre papers no cache
    """
    cache = papers_service.papers_cache
    
    if not cache:
        return {
            "success": True,
            "cached_papers": 0,
            "message": "Cache vazio"
        }
    
    # Estatísticas do cache
    categories = []
    for paper in cache:
        if "categories" in paper:
            categories.extend(paper.get("categories", []))
    
    unique_categories = list(set(categories))
    
    # Anos de publicação
    years = []
    for paper in cache:
        if paper.get("published") and paper["published"] != "N/A":
            try:
                year = paper["published"].split("-")[0]
                years.append(year)
            except:
                pass
    
    return {
        "success": True,
        "cached_papers": len(cache),
        "paper_titles": [p["title"][:100] for p in cache],
        "categories": unique_categories[:10],
        "publication_years": list(set(years)),
        "total_authors": sum(len(p.get("authors", [])) for p in cache),
        "message": f"Cache contém {len(cache)} papers"
    }

@mcp.tool()
async def chat_about_papers(
    ctx: Context,
    message: str
) -> Dict[str, Any]:
    """
    Chat interativo sobre papers usando IA.
    
    Args:
        message: Pergunta ou comando sobre papers
    
    Returns:
        Resposta contextualizada do assistente
    """
    try:
        # Verificar se precisa fazer busca
        search_keywords = ['busque', 'procure', 'encontre', 'pesquise']
        needs_search = any(keyword in message.lower() for keyword in search_keywords)
        
        if needs_search:
            # Extrair query de busca
            query = message.lower()
            for keyword in search_keywords:
                query = query.replace(keyword, "").strip()
            
            # Buscar papers
            papers = await papers_service.search_papers_async(query, 5)
            
            if papers:
                # Gerar resposta com contexto
                context = papers_service._format_papers_context(papers)
                prompt = f"""
                Pergunta do usuário: {message}
                
                Papers encontrados:
                {context}
                
                Responda de forma clara e informativa sobre os papers encontrados.
                """
            else:
                prompt = f"""
                Pergunta do usuário: {message}
                
                Não foram encontrados papers sobre este tema.
                Sugira alternativas ou forneça informações gerais sobre o tópico.
                """
        else:
            # Usar cache se disponível
            if papers_service.papers_cache:
                context = papers_service._format_papers_context(papers_service.papers_cache)
                prompt = f"""
                Pergunta do usuário: {message}
                
                Papers disponíveis no contexto:
                {context}
                
                Responda baseando-se nos papers disponíveis.
                """
            else:
                prompt = f"""
                Pergunta do usuário: {message}
                
                Responda como um assistente especializado em papers acadêmicos.
                Sugira fazer buscas se necessário.
                """
        
        # Gerar resposta
        response = papers_service.model.generate_content(prompt)
        answer = response.text.strip() if response and response.text else "Não foi possível gerar uma resposta."
        
        return {
            "success": True,
            "message": message,
            "response": answer,
            "papers_in_context": len(papers_service.papers_cache)
        }
        
    except Exception as e:
        logger.error(f"Erro no chat: {str(e)}")
        return {
            "success": False,
            "message": f"Erro ao processar mensagem: {str(e)}"
        }

# MAIN 

def main():
    """Função principal para executar o servidor."""
    try:
        # Verificar configuração
        if not os.getenv('GOOGLE_API_KEY'):
            logger.error("GOOGLE_API_KEY não configurada!")
            sys.exit(1)
        
        logger.info("Iniciando servidor MCP de Papers Acadêmicos...")
        
        # Executar servidor
        mcp.run()
        
    except KeyboardInterrupt:
        logger.info("Servidor interrompido pelo usuário")
    except Exception as e:
        logger.error(f"Erro fatal: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()