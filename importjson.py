import json
import pandas as pd
import os
from informativo import gerar_informativo, gerar_informativo_ura
from typing import Dict, Any, List

COLUNAS_SMS = [
    'empresa', 'campanha_id', 'entregue', 'total_disparos', 
    'cliques', 'total_respostas', 'status', 'invalidas'
]
COLUNAS_URA = [
    'id', 'nome_campanha', 'usuario', 'status', 'quantidade_leads', 
    'total_convertido', 'total_falta_ligar', 'total_atendidos', 
    'total_nao_atendidos', 'empresa', 'total_convertido_dia'
]

# --- Função de Validação ---
def _validar_colunas(data_list: List[Dict], chaves_necessarias: List[str], tipo_json: str):
    """Verifica se o primeiro item da lista de dados contém todas as chaves necessárias."""
    if not data_list:
        raise ValueError(f"JSON do tipo {tipo_json} está vazio ou mal formatado.")
        
    primeiro_item = data_list[0]
    colunas_ausentes = [chave for chave in chaves_necessarias if chave not in primeiro_item]
    
    if colunas_ausentes:
        # Se uma chave estiver faltando, levanta um erro claro
        raise ValueError(f"JSON de {tipo_json} inválido. Colunas ausentes: {', '.join(colunas_ausentes)}")

def processar_json_arquivo(json_path: str, output_folder: str) -> Dict[str, str]:
    """
    Detecta automaticamente o tipo de JSON (SMS ou URA) e o processa,
    lendo o arquivo apenas uma vez.
    """
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # Verificar a estrutura básica
        if "data" not in data or not isinstance(data["data"], list) or not data["data"]:
            raise ValueError("JSON não contém a chave 'data' ou a lista 'data' está vazia.")
            
        primeiro_item = data["data"][0]
        
        # Detecção baseada em campos únicos
        if "total_disparos" in primeiro_item and "entregue" in primeiro_item:
            print("""Processando como JSON de SMS no Importjson.py... \nAguarde o prcessamento ser concluído...\n""")
            return _processar_disparos_sms(data, output_folder)
            
        elif "quantidade_leads" in primeiro_item and "total_convertido" in primeiro_item:
            print("""Processando como JSON de URA no Importjson.py... \nAguarde o prcessamento ser concluído...\n""")
            return _processar_disparos_ura(data, output_folder)
            
        else:
            # Tenta inferir pelas colunas obrigatórias
            try:
                _validar_colunas(data["data"], COLUNAS_SMS, "SMS")
                print("Processando como JSON de SMS (inferido)...")
                return _processar_disparos_sms(data, output_folder)
            except ValueError:
                try:
                    _validar_colunas(data["data"], COLUNAS_URA, "URA")
                    print("Processando como JSON de URA (inferido)...")
                    return _processar_disparos_ura(data, output_folder)
                except ValueError:
                    raise ValueError("Estrutura do JSON não reconhecida. Não é SMS nem URA.")
                    
    except json.JSONDecodeError:
        raise ValueError("Erro ao ler o arquivo. O JSON parece estar mal formatado.")
    except Exception as e:
        print(f"Erro inesperado ao detectar tipo de JSON: {e}")
        raise # Re-levanta a exceção para ser tratada pelo Flask

def _processar_disparos_sms(front: Dict, output_folder: str) -> Dict[str, str]:
    """Processa dados de campanhas SMS. Recebe o objeto JSON já carregado."""
    try:
        dados = front["data"]
        _validar_colunas(dados, COLUNAS_SMS, "SMS") # Valida colunas
        df = pd.DataFrame(dados)

        # Cálculos para SMS
        df["taxa_entrega"] = (df["entregue"] / df["total_disparos"].replace(0, 1) * 100).round(2)
        df["taxa_cliques"] = (df["cliques"] / df["entregue"].replace(0, 1) * 100).round(2)
        df["taxa_respostas"] = (df["total_respostas"] / df["entregue"].replace(0, 1) * 100).round(2)

        # Gera informativos automáticos
        informativos = []
        for _, row in df.iterrows():
            texto = gerar_informativo(
                empresa=row["empresa"],
                campanha_id=row["campanha_id"],
                entregue=row["entregue"],
                invalidas=row["invalidas"],
                total_disparos=row["total_disparos"],
                cliques=row["cliques"],
                total_respostas=row["total_respostas"],
                status=row["status"]
            
            )
            informativos.append({
                "empresa": row["empresa"],
                "campanha_id": row["campanha_id"],
                "informativo": texto,
            })
            
        df_informativo = pd.DataFrame(informativos)

        # Define caminhos de saída
        excel_path = os.path.join(output_folder, "analise_disparos_sms.xlsx")
        txt_dir = os.path.join(output_folder, "informativos_sms_txt")
        resumo_dir = os.path.join(output_folder, "resumos_empresas_sms")
        os.makedirs(txt_dir, exist_ok=True)
        os.makedirs(resumo_dir, exist_ok=True)

        # Escreve Excel
        with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
            df.to_excel(writer, sheet_name="Análise Detalhada", index=False)
            df_informativo.to_excel(writer, sheet_name="Informativos", index=False)

        # Escreve TXTs individuais
        for empresa, grupo in df_informativo.groupby("empresa"):
            file_name = os.path.join(txt_dir, f"{empresa.replace(' ', '_')}_sms.txt")
            with open(file_name, "w", encoding="utf-8") as f:
                for _, linha in grupo.iterrows():
                    f.write(linha["informativo"])
                    f.write("\n" + "-" * 60 + "\n\n")

        # Gera Resumos Consolidados (se houver múltiplas campanhas)
        for empresa, grupo_empresa in df.groupby("empresa"):
            if len(grupo_empresa) > 1:
                resumo = _gerar_resumo_empresa_sms(grupo_empresa, empresa)
                
                # Salva resumo em arquivo separado
                resumo_file = os.path.join(resumo_dir, f"RESUMO_{empresa.replace(' ', '_')}_sms.txt")
                with open(resumo_file, "w", encoding="utf-8") as f:
                    f.write(resumo)
                
                # Adiciona resumo no topo do arquivo principal da empresa
                file_name = os.path.join(txt_dir, f"{empresa.replace(' ', '_')}_sms.txt")
                with open(file_name, "r", encoding="utf-8") as f:
                    conteudo_existente = f.read()
                
                with open(file_name, "w", encoding="utf-8") as f:
                    f.write("=" * 80 + "\n")
                    f.write("RESUMO CONSOLIDADO DA EMPRESA\n")
                    f.write("-" * 80 + "\n\n")
                    f.write(resumo)
                    f.write("\n" + "-" * 80 + "\n")
                    f.write("DETALHAMENTO POR CAMPANHA\n")
                    f.write("=" * 80 + "\n\n")
                    f.write(conteudo_existente)
        print("Relatório de SMS")

        # Retorna um dicionário com todos os caminhos relevantes
        return {
            "excel_path": excel_path,
            "txt_dir": txt_dir,
            "resumo_dir": resumo_dir,
            "tipo": "sms"
        }

    except (KeyError, ValueError) as e:
        # Captura erros de coluna/chave específicos
        raise ValueError(f"Erro ao processar dados de SMS: {e}")
    except Exception as e:
        print(f"Erro inesperado no processamento de SMS: {e}")
        raise

def _gerar_resumo_empresa_sms(df_empresa, nome_empresa):
    """Gera resumo consolidado para empresas com múltiplas campanhas SMS"""
    
    # Ordenar por taxa de cliques (melhores primeiro)
    df_sorted = df_empresa.sort_values("taxa_cliques", ascending=False)
    
    # Identificar campanhas com baixo engajamento
    campanhas_baixo_engajamento = df_sorted[df_sorted["taxa_cliques"] < 1.0]
    
    # Construir o resumo
    resumo = f"Resumo de Desempenho - {nome_empresa}\n\n"
    
    # Melhores em cliques
    resumo += "Melhor engajamento em cliques:\n"
    top_campanhas = df_sorted.head(3)  # Top 3 campanhas
    for _, campanha in top_campanhas.iterrows():
        resumo += f"Campanha {campanha['campanha_id']} - {campanha['taxa_cliques']}%\n"
    
    # Campanhas com baixo engajamento
    if not campanhas_baixo_engajamento.empty:
        resumo += f"\n▲ Campanhas com baixo engajamento (<1%): "
        ids_baixo_engajamento = [str(int(campanha['campanha_id'])) for _, campanha in campanhas_baixo_engajamento.iterrows()]
        resumo += ", ".join(ids_baixo_engajamento)
        resumo += "\n"
    
    # Sugestões rápidas
    resumo += "\nSugestões rápidas:\n"
    resumo += "• Reforçar CTA e valor do clique\n"
    resumo += "• Testar horários diferentes\n"
    resumo += "• Destacar melhor o link no texto\n"
    resumo += "• Personalizar mensagem por segmento\n"
    resumo += "• Revisar lista de contatos\n\n"
    resumo += "Obrigado pela parceria e bons disparos!\n"
    
    return resumo


def _processar_disparos_ura(data: Dict, output_folder: str) -> Dict[str, str]:

    """Processa dados de campanhas URA. Recebe o objeto JSON já carregado."""
    try:
        dados = data["data"]
        _validar_colunas(dados, COLUNAS_URA, "URA") # Valida colunas
        df = pd.DataFrame(dados)

        # Cálculos específicos para URA
        df["taxa_conversao"] = (df["total_convertido"] / df["total_atendidos"].replace(0, 1) * 100).round(2)
        
        df["tentativas_totais"] = (df["total_atendidos"].fillna(0) + df["total_nao_atendidos"].fillna(0))
        df["porcentagem_andamento"] = (df["tentativas_totais"] / df["quantidade_leads"].replace(0, 1) * 100).round(2)
        
        df["status_campanha"] = df["status"].map({
            1: "Não iniciado",
            2: "Em andamento", 
            3: "Pausado",
            4: "Finalizado"
        }).fillna("Desconhecido") # Adiciona fallback

        # Gera informativos para URA
        informativos = []
        for _, row in df.iterrows():
            # Tratamento para dados aninhados (empresa, usuario)
            empresa_nome = row.get("empresa", {}).get("nome_empresa", "Empresa Padrão")
            usuario_email = row.get("usuario", {}).get("email", "email@padrao.com")

            texto = gerar_informativo_ura(
                campanha_id=row["id"],
                nome_campanha=row["nome_campanha"],
                usuario_email=usuario_email,
                status_campanha=row["status_campanha"],
                taxa_conversao=row["taxa_conversao"],
                porcentagem_andamento=row["porcentagem_andamento"],
                quantidade_leads=row["quantidade_leads"],
                total_falta_ligar=row["total_falta_ligar"],
                total_convertido=row["total_convertido"],
                total_convertido_dia=row["total_convertido_dia"],
                total_atendidos=row["total_atendidos"],
                total_nao_atendidos=row["total_nao_atendidos"]
            )
            informativos.append({
                "empresa": empresa_nome,
                "campanha_id": row["id"],
                "nome_campanha": row["nome_campanha"],
                "informativo": texto
            })
        df_informativo = pd.DataFrame(informativos)

        # Define caminhos de saída
        excel_path = os.path.join(output_folder, "analise_campanhas_ura.xlsx")
        txt_dir = os.path.join(output_folder, "informativos_ura_txt")
        os.makedirs(txt_dir, exist_ok=True)

        # Escreve Excel
        with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
            df.to_excel(writer, sheet_name="Análise Detalhada", index=False)
            df_informativo.to_excel(writer, sheet_name="Informativos", index=False)

        # Escreve TXTs por empresa
        for empresa, grupo in df_informativo.groupby("empresa"):
            file_name = os.path.join(txt_dir, f"{empresa.replace(' ', '_')}_ura.txt")
            with open(file_name, "w", encoding="utf-8") as f:
                f.write("Bom dia, pessoal! \n")
                f.write("Segue relação da performance das campanhas em andamento:\n\n")
                for _, linha in grupo.iterrows():
                    f.write(linha["informativo"])
                    f.write("\n\n" + "-" * 40 + "\n")
        
        # Retorna um dicionário com todos os caminhos relevantes
        return {
            "excel_path": excel_path,
            "txt_dir": txt_dir,
            "tipo": "ura"
        }
        
    except (KeyError, ValueError) as e:
        # Captura erros de coluna/chave específicos
        raise ValueError(f"Erro ao processar dados de URA: {e}")
    except Exception as e:
        print(f"Erro inesperado no processamento de URA: {e}")
        raise
