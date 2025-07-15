# Usa base oficial do Python 3.10, que inclui audioop
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia todos os arquivos do repositório para /app
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Comando para iniciar seu bot
CMD ["python", "main.py"]
