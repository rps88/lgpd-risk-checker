import pandas as pd

# Lista de colunas consideradas dados pessoais/sensíveis
colunas_criticas = ['nome', 'cpf', 'email', 'telefone', 'endereco', 'data_nascimento']

# Carregar a planilha
arquivo = 'exemplo_dados.csv'
df = pd.read_csv(arquivo)

print(f"\n📊 Analisando o arquivo: {arquivo}\n")

# Verifica se há dados críticos
colunas_encontradas = [col for col in colunas_criticas if col in df.columns]

if colunas_encontradas:
    print("⚠️  Dados pessoais/sensíveis encontrados:")
    for col in colunas_encontradas:
        print(f" - {col}")
else:
    print("✅ Nenhum dado pessoal crítico encontrado.")

print("\n✅ Análise concluída.")
