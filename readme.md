# 🎵 Hand Tracker YouTube Controller

Projeto em Python que utiliza **visão computacional** para controlar ações do sistema (como volume) através de **gestos da mão em tempo real**, podendo ser usado durante a navegação no YouTube.

---

## 🚀 Tecnologias

- **OpenCV** – captura e processamento de vídeo  
- **MediaPipe** – detecção e rastreamento da mão  
- **PyAutoGUI** – automação de ações no sistema  

---

## 🧠 Como funciona

O sistema utiliza os **landmarks da mão** fornecidos pelo MediaPipe para identificar padrões de posição dos dedos.

Cada gesto é definido com base em:
- Relações entre coordenadas (`x` e `y`)
- Distância entre pontos (ex: indicador e polegar)
- Estados dos dedos (levantado / abaixado)

### 🔒 Robustez da detecção

Para evitar instabilidade (tremores ou ruídos da câmera), o projeto implementa:

- **Margem de tolerância** nas comparações  
  → evita falhas por pequenas variações  

- **Suavização temporal (debounce)**  
  → um gesto só é aceito após aparecer em múltiplos frames consecutivos  

Isso garante uma experiência mais estável e confiável.

---

## ✋ Gestos suportados

| Gesto | Ação |
|------|------|
| ☝️ Apenas indicador | Ação personalizada |
| ✌️ Indicador + médio | Ação personalizada |
| 🤟 Indicador + médio + anelar | Ação personalizada |
| 🖐️ Todos os dedos | Ação personalizada |
| 🤏 Pinça (indicador + polegar próximos) | Diminuir volume |
| ✋ Abertura da mão | Aumentar volume |

---

## ▶️ Como rodar

```bash
python -m venv venv