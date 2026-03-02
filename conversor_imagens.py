"""
🖼️ Conversor de Imagens em Lote
================================
Converte todas as imagens de uma pasta de um formato para outro.
Suporta: .gif, .png, .jpg, .jpeg, .bmp, .webp, .tiff, .ico

Como usar:
  python conversor_imagens.py

Dependências:
  pip install Pillow
"""

import os
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("❌ Pillow não está instalado. Rode: pip install Pillow")
    sys.exit(1)

# ──────────────────────────────────────────────
# CONFIGURAÇÕES — edite aqui se quiser
# ──────────────────────────────────────────────
PASTA_ENTRADA   = ""          # Ex: "C:/fotos/gifs" — deixe vazio para perguntar
PASTA_SAIDA     = ""          # Ex: "C:/fotos/png"  — deixe vazio para criar automaticamente
FORMATO_ENTRADA = ""          # Ex: "gif"           — deixe vazio para perguntar
FORMATO_SAIDA   = ""          # Ex: "png"           — deixe vazio para perguntar
QUALIDADE_JPG   = 90          # Qualidade do JPEG (1–100)
MANTER_ORIGINAL = True        # Não apaga os arquivos originais
# ──────────────────────────────────────────────


FORMATOS_SUPORTADOS = ["gif", "png", "jpg", "jpeg", "bmp", "webp", "tiff", "ico"]

def perguntar(prompt, opcoes=None):
    while True:
        resposta = input(prompt).strip()
        if not opcoes or resposta.lower() in opcoes:
            return resposta.lower()
        print(f"  ⚠️  Opção inválida. Escolha entre: {', '.join(opcoes)}")

def converter_imagem(caminho_entrada: Path, caminho_saida: Path, formato_saida: str):
    """Converte uma única imagem e retorna True se deu certo."""
    try:
        with Image.open(caminho_entrada) as img:
            # GIFs animados: pega apenas o primeiro frame
            if hasattr(img, "n_frames") and img.n_frames > 1:
                img.seek(0)

            # PNG e JPG não suportam modo 'P' ou transparência RGBA da mesma forma
            if formato_saida in ("jpg", "jpeg"):
                if img.mode in ("RGBA", "P", "LA"):
                    fundo = Image.new("RGB", img.size, (255, 255, 255))
                    if img.mode == "P":
                        img = img.convert("RGBA")
                    fundo.paste(img, mask=img.split()[-1] if img.mode == "RGBA" else None)
                    img = fundo
                elif img.mode != "RGB":
                    img = img.convert("RGB")
                img.save(caminho_saida, quality=QUALIDADE_JPG, optimize=True)
            else:
                if formato_saida == "png" and img.mode == "P":
                    img = img.convert("RGBA")
                img.save(caminho_saida)

        return True
    except Exception as e:
        print(f"    ❌ Erro: {e}")
        return False


def main():
    print("\n" + "═" * 50)
    print("  🖼️  Conversor de Imagens em Lote")
    print("═" * 50 + "\n")

    # ── Pasta de entrada
    pasta_entrada = PASTA_ENTRADA or input("📂 Pasta com as imagens originais: ").strip().strip('"')
    pasta_entrada = Path(pasta_entrada)
    if not pasta_entrada.is_dir():
        print(f"❌ Pasta não encontrada: {pasta_entrada}")
        sys.exit(1)

    # ── Formato de entrada
    fmt_entrada = FORMATO_ENTRADA or perguntar(
        f"🔄 Formato de entrada {FORMATOS_SUPORTADOS}: ",
        FORMATOS_SUPORTADOS
    )
    fmt_entrada = fmt_entrada.lstrip(".")

    # ── Formato de saída
    fmt_saida = FORMATO_SAIDA or perguntar(
        f"💾 Formato de saída {FORMATOS_SUPORTADOS}: ",
        FORMATOS_SUPORTADOS
    )
    fmt_saida = fmt_saida.lstrip(".")

    # ── Pasta de saída
    pasta_saida_padrao = pasta_entrada.parent / f"{pasta_entrada.name}_{fmt_saida}"
    if PASTA_SAIDA:
        pasta_saida = Path(PASTA_SAIDA)
    else:
        resposta = input(f"📁 Pasta de saída [{pasta_saida_padrao}]: ").strip().strip('"')
        pasta_saida = Path(resposta) if resposta else pasta_saida_padrao

    pasta_saida.mkdir(parents=True, exist_ok=True)

    # ── Listar arquivos
    arquivos = sorted(pasta_entrada.glob(f"*.{fmt_entrada}"))
    if not arquivos:
        arquivos = sorted(pasta_entrada.glob(f"*.{fmt_entrada.upper()}"))

    if not arquivos:
        print(f"\n⚠️  Nenhum arquivo .{fmt_entrada} encontrado em {pasta_entrada}")
        sys.exit(0)

    print(f"\n✅ {len(arquivos)} arquivo(s) .{fmt_entrada} encontrado(s).")
    print(f"📤 Salvando .{fmt_saida} em: {pasta_saida}\n")

    # ── Converter
    ok = 0
    erros = 0
    for i, arq in enumerate(arquivos, 1):
        destino = pasta_saida / (arq.stem + f".{fmt_saida}")
        print(f"  [{i:>4}/{len(arquivos)}] {arq.name} → {destino.name}", end=" ")
        if converter_imagem(arq, destino, fmt_saida):
            print("✔")
            ok += 1
        else:
            erros += 1

    # ── Resultado
    print("\n" + "─" * 50)
    print(f"  ✅ Convertidos com sucesso : {ok}")
    if erros:
        print(f"  ❌ Erros                  : {erros}")
    print(f"  📁 Imagens salvas em      : {pasta_saida}")
    print("─" * 50 + "\n")


if __name__ == "__main__":
    main()
