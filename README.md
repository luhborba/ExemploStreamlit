# Exemplo de Página de Cadastro com Streamlit e Pandas

## Clonando o Projeto com PIP



### Clone o repositório:
```bash
git clone https://github.com/luhborba/ExemploStreamlit.git
cd ExemploStreamlit
```

### Criando Ambiente Virtual:
```bash
python -m venv .venv
```

### Ativando Ambiente
Windows
```bash
.venv\Scripts\activate
```
Linux
```bash
source .venv/bin/activate
```

### Instalando Dependências

```bash
pip install -r requirements.txt
```

### Executando Streamlit
```bash
streamlit run app.py
```
## Clonando o Projeto com Python

- Caso não tenha `Pyenv e Proetry` instalado é está usando ambiente Linux acesse [Instalando Pyenv e Poetry (WSL/Linux)](https://github.com/luhborba/Wsl-Pyenv-Poetry)
- Caso o ambiente seja Windows, assista este vídeo [Como instalar Python em 2024 + Pyenv, PIP, VENV, PIPX e Poetry](https://www.youtube.com/watch?v=9LYqtLuD7z4&t)

### Clone o repositório:
```bash
git clone https://github.com/luhborba/ExemploStreamlit.git
cd ExemploStreamlit
```

### Configure a versão correta do Python com `pyenv`
```bash
pyenv install 3.12.1
pyenv local 3.12.1
```

### Ativando Poetry
```bash
poetry env use 3.12.1
poetry shell
```

### Insatalando dependências
```bash
poetry install
```

### Rodando Streamlit
```bash
streamlit run app.py
```