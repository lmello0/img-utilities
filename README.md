# Image Utilities

Repositório com scritps para encontrar duplicatas e ordenação por data.

## Dependências

- Python 3
- tqdm (pacote de barra de progresso)

## img_equal.py

O script `img_equal.py`, tem a funcionalidade de encontrar imagens duplicadas
e deletá-las. Utiliza `hashing MD5` para identificá-las.

### Utilização

Para procurar por imagens duplicadas em pasta X, execute o script da seguinte forma:

```bash
python img_equal.py /path/to/folder
```

## sort.py

O script `sort.py`, ordena as imagens de uma pasta em subpastas baseadas na data de modificação.

### Utilização

Para ordenar as imagens de uma pasta, execute o script passando a pasta que contém as imagens como parâmetro:

```bash
python sort.py /path/to/folder
```

Os arquivos serão organizados da seguinte forma:

```
arquivo1.jpg | 2024-03-10
arquivo2.jpg | 2023-03-10
...

./images
├── 2023
│   └── Mar
│       └── arquivo2.jpg
└── 2024
    └── Mar
        └── arquivo1.jpg
```