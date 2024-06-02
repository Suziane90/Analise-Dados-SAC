import sqlite3
import PyPDF2

# Extrair texto do PDF
with open('C:/Users/LIVRE/Desktop/SAC-material/Relatório_GRSAC_2023_ITAU.pdf', 'rb') as arquivo_pdf:
    leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)
    texto_pdf = ""
    for pagina in leitor_pdf.pages:
        texto_pdf += pagina.extract_text()

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('ExemploGRSAC.db')
c = conn.cursor()

# Criar a tabela se ela não existir
c.execute('''
CREATE TABLE IF NOT EXISTS relatorio_grsac (
    id INTEGER PRIMARY KEY,
    conteudo TEXT
)
''')

# Inserir o texto extraído no banco de dados
c.execute('''
INSERT INTO relatorio_grsac (conteudo)
VALUES (?)
''', (texto_pdf,))

# Salvar (confirmar) as alterações
conn.commit()

# Fechar a conexão
conn.close()

print("Texto do PDF armazenado com sucesso no banco de dados!")
