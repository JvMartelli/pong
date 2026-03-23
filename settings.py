# =============================================================================
# settings.py
# Constantes e configurações globais do jogo Pong.
# Centralizar tudo aqui facilita ajustes sem precisar mexer na lógica.
# =============================================================================

# --- Tela ---
LARGURA = 800
ALTURA = 600
FPS = 60
TITULO = "Pong"

# --- Cores ---
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (100, 100, 100)

# --- Raquetes ---
RAQUETE_LARGURA = 10
RAQUETE_ALTURA = 60
RAQUETE_VELOCIDADE = 5
MARGEM_RAQUETE = 15  # distância da raquete até a borda da tela

# --- Bola ---
BOLA_RAIO = 7
BOLA_VELOCIDADE_INICIAL = 5

# --- Regras ---
PONTOS_PARA_VENCER = 7
