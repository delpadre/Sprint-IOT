# Grupo:
Lucas bertolassi iori - RM553183  
Giovanna Franco - RM553701
Rafael Almeida - RM554019
Rafael Jorge Del Padre - Rm552765

# 👁️ Sistema de Detecção Facial com OpenCV (Haar Cascade)

## 📌 Objetivo do Projeto
Este projeto implementa uma aplicação local de **detecção facial** utilizando **OpenCV** e o classificador Haar Cascade.  
A aplicação abre a webcam do computador e identifica rostos em tempo real, exibindo retângulos verdes ao redor das faces detectadas.

---

## 🧠 Tecnologias Utilizadas
- Python 3.x  
- OpenCV (cv2)  
- Haar Cascade Frontal Face Classifier  
- Execução totalmente local (nenhum dado é enviado para servidores)

---

## 🖥️ Funcionamento
O sistema utiliza o arquivo `haarcascade_frontalface_default.xml`, um classificador pré-treinado baseado em Haar Cascade que identifica padrões faciais analisando contraste, regiões e bordas do rosto.

O processo funciona assim:

1. A webcam captura a imagem.
2. A imagem é convertida para tons de cinza.
3. O Haar Cascade analisa o frame.
4. Quando um rosto é detectado, um retângulo verde é desenhado.

---

## ⚙️ Parâmetros Ajustáveis

### 🔹 **scaleFactor**
Controla o quanto a imagem diminui a cada análise.  
- **1.05** → Sensível (detecta mais, mas também erra mais)
- **1.3** → Detecta menos, porém menos erros

### 🔹 **minNeighbors**
Número de “confirmações” necessárias para validar um rosto.  
- **2–3** → detecta mais, mas erra mais  
- **5–6** → mais confiável, porém detecta menos

### 🔹 **minSize**
Tamanho mínimo de um rosto para ser considerado.  
- Exemplo: `(30, 30)` → detecta rostos pequenos  

Esses parâmetros podem ser alterados e mostrados no vídeo para demonstrar o impacto — **exigência da professora**.

---

## ▶️ Como Executar

### 1️⃣ Instale as dependências
```bash
pip install opencv-python
