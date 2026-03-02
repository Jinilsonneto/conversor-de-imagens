CONVERSOR DE IMAGENS EM LOTE - TUTORIAL COMPLETO
================================================

Converte uma pasta inteira de imagens de um formato para outro.
Suporta: .gif, .png, .jpg, .jpeg, .bmp, .webp, .tiff, .ico


REQUISITOS
----------

  - Python 3.7 ou superior
  - Biblioteca Pillow

  Para verificar se o Python esta instalado:
    python3 --version


INSTALACAO
----------

  1. Baixe o arquivo conversor_imagens.py

  2. Instale a biblioteca Pillow:

     Windows:
       pip install Pillow

     Linux / Ubuntu / Debian:
       pip install Pillow --break-system-packages

     macOS:
       pip3 install Pillow

  3. Pronto! Nao precisa instalar mais nada.


COMO USAR
---------

  Abra o terminal na pasta onde esta o arquivo e rode:

     Windows:
       python conversor_imagens.py

     Linux / macOS:
       python3 conversor_imagens.py


  O programa vai te fazer 4 perguntas:

    1. Qual e a pasta com as imagens originais?
       Exemplo Windows : C:\Users\Joao\Downloads\gifs
       Exemplo Linux   : /home/joao/Downloads/gifs

    2. Qual e o formato de entrada?
       Exemplo: gif

    3. Qual e o formato de saida?
       Exemplo: png  ou  jpg

    4. Onde salvar as imagens convertidas?
       (Aperte Enter para criar uma pasta automatica no mesmo lugar)


  Depois disso ele converte tudo sozinho e mostra o progresso:
    [   1/600] imagem1.gif -> imagem1.png OK
    [   2/600] imagem2.gif -> imagem2.png OK


MODO RAPIDO (sem perguntas)
---------------------------

  Se voce sempre usa as mesmas pastas e formatos, edite as
  variaveis no topo do arquivo conversor_imagens.py:

    PASTA_ENTRADA   = "C:/fotos/gifs"
    PASTA_SAIDA     = "C:/fotos/convertidas"
    FORMATO_ENTRADA = "gif"
    FORMATO_SAIDA   = "png"

  Assim ele roda direto sem perguntar nada.


ONDE FICAM OS ARQUIVOS CONVERTIDOS?
------------------------------------

  Por padrao, uma nova pasta e criada automaticamente
  do lado da pasta original com o sufixo do novo formato.

  Exemplo:
    Pasta original   ->  /Downloads/gifs
    Pasta convertida ->  /Downloads/gifs_png

  Os arquivos originais NAO sao apagados.


FORMATOS SUPORTADOS
-------------------

  .gif  .png  .jpg  .jpeg  .bmp  .webp  .tiff  .ico

  Qualquer combinacao funciona. Exemplos:
    gif  -> png
    gif  -> jpg
    bmp  -> webp
    tiff -> jpg


OBSERVACOES IMPORTANTES
-----------------------

  - GIFs animados: apenas o primeiro frame e salvo.

  - Convertendo para JPG: imagens com fundo transparente
    recebem fundo branco automaticamente.

  - Convertendo para PNG: transparencia e preservada.

  - A qualidade do JPG padrao e 90 (de 0 a 100).
    Para mudar, edite a variavel QUALIDADE_JPG no arquivo.


PROBLEMAS COMUNS
----------------

  Erro: ModuleNotFoundError: No module named 'PIL'
  -> Pillow nao esta instalado. Rode o comando de instalacao
     descrito na secao INSTALACAO acima.

  Erro: externally-managed-environment (Linux)
  -> Use: pip install Pillow --break-system-packages

  Nenhum arquivo encontrado na pasta
  -> Verifique se o formato de entrada esta correto.

  O terminal nao reconhece "python"
  -> Tente "python3" no lugar de "python".


LICENCA
-------

  Livre para usar, modificar e distribuir.
