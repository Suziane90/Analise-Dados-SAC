import PyPDF2

caminho_arquivo = r'C:\Users\LIVRE\Desktop\SAC-material\Relatório_GRSAC_2023_ITAU.pdf'

# Abrir o PDF
with open(caminho_arquivo, 'rb') as arquivo_pdf:
    leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)
    
    # Extraindo informações do PDF
    numero_de_paginas = len(leitor_pdf.pages)
    print(f"O PDF tem {numero_de_paginas} páginas.")
    
    # Ler conteúdo de uma página específica (tentando a segunda página)
    pagina = leitor_pdf.pages[1]
    conteudo = pagina.extract_text()
    print(conteudo)
