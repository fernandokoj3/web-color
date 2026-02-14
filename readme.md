# 🎨 Web Color Server

Aplicação simples que exibe uma página HTML com **cor de fundo configurável** e algumas informações do servidor.

Ideal para testes de:

* ✔️ Load balancer
* ✔️ Kubernetes / Docker
* ✔️ Health checks visuais
* ✔️ Identificação de instâncias

---

## 🚀 Funcionalidades

A página exibe:

* 🖥️ Nome da máquina (hostname)
* 🌐 Endereço IP do servidor
* 🎨 Cor de fundo configurável (green / blue / yellow / etc.)

---

## 🧱 Tecnologias

* Python
* FastAPI
* HTML/CSS

---

## ▶️ Como executar

### 1️⃣ Criar ambiente virtual

```bash
python -m venv .venv
```

### 2️⃣ Ativar

Linux / Mac:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 3️⃣ Instalar dependências

```bash
pip install fastapi uvicorn
```

### 4️⃣ Executar aplicação

```bash
uvicorn app.main:app --reload
```

---

## 🌐 Acessar no navegador

```
http://localhost:8000
```

Ou rotas específicas:

```
/green
/blue
/yellow
```

---

## 📦 Exemplo de uso

Muito útil quando rodando múltiplas instâncias:

* Docker containers
* Pods no Kubernetes
* Máquinas diferentes atrás de um ingress

Cada instância pode ter uma cor diferente para fácil identificação visual.

---

## 📝 Licença

Uso livre para testes e aprendizado.
