Imagens Personalizadas com Docker

Instruções de Build e Execução

Pré-requisitos
* Ter o Docker instalado e rodando na máquina.

1. Construir a Imagem (Build)
Execute o comando abaixo no terminal (na raiz do projeto, onde o `Dockerfile` está localizado) para criar a imagem customizada:
```bash
docker build -t minha-app-python:1.0 .
```

2. Executar o Contêiner (Run)
Para iniciar a aplicação dentro do ambiente isolado do Docker e visualizar o resultado, utilize o comando:
```bash
docker run --rm minha-app-python:1.0
```

Evidências de Funcionamento

1. Registro da Construção da Imagem (Build)

PS imagens_personalizadas> docker build -t minha-app-python:1.0 .
[+] Building 9.6s (10/10) FINISHED                                                                                                                         docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                                       0.0s
 => => transferring dockerfile: 202B                                                                                                                                       0.0s
 => [internal] load metadata for docker.io/library/python:3.12-slim                                                                                                        2.0s
 => [internal] load .dockerignore                                                                                                                                          0.0s
 => => transferring context: 107B                                                                                                                                          0.0s
 => [1/5] FROM docker.io/library/python:3.12-slim@sha256:423ed6ab25b1921a477529254bfeeabf5855151dc2c3141699a1bfc852199fbf                                                  4.8s
 => => resolve docker.io/library/python:3.12-slim@sha256:423ed6ab25b1921a477529254bfeeabf5855151dc2c3141699a1bfc852199fbf                                                  0.0s
 => => sha256:b32430367bf08f32c23778909985ac645d1794f0aeef670aa796a50c8751527d 248B / 248B                                                                                 0.2s
 => => sha256:df79d931cd67092e2b8e48d8f6369922571efe4ee0f9af71636ce36600481492 12.11MB / 12.11MB                                                                           1.3s
 => => sha256:aff2d9f8dc87f4c10bbb7f438f3a325169379776bdfad5c49e4be5acc3c2f192 1.29MB / 1.29MB                                                                             0.8s
 => => sha256:e95a6c7ea7d49b37920899b023ecd0e32796c976c1748491f76cae53ba86d13a 29.79MB / 29.79MB                                                                           3.3s
 => => extracting sha256:e95a6c7ea7d49b37920899b023ecd0e32796c976c1748491f76cae53ba86d13a                                                                                  0.8s
 => => extracting sha256:aff2d9f8dc87f4c10bbb7f438f3a325169379776bdfad5c49e4be5acc3c2f192                                                                                  0.1s
 => => extracting sha256:df79d931cd67092e2b8e48d8f6369922571efe4ee0f9af71636ce36600481492                                                                                  0.4s
 => => extracting sha256:b32430367bf08f32c23778909985ac645d1794f0aeef670aa796a50c8751527d                                                                                  0.0s
 => [internal] load build context                                                                                                                                          0.0s
 => => transferring context: 982B                                                                                                                                          0.0s
 => [2/5] WORKDIR /app                                                                                                                                                     0.2s
 => [3/5] COPY requirements.txt .                                                                                                                                          0.0s
 => [4/5] RUN pip install --no-cache-dir -r requirements.txt                                                                                                               1.7s
 => [5/5] COPY . .                                                                                                                                                         0.1s
 => exporting to image                                                                                                                                                     0.7s
 => => exporting layers                                                                                                                                                    0.4s
 => => exporting config sha256:55e3a02956eba3f5d4659d87f96379adfe2297b54c018f97da666c26dcaf5234                                                                            0.0s
 => => exporting attestation manifest sha256:42b41fc4cffda44208e8a265b5c7ff34b842f900d9ad6ca9fb418ec257f01650                                                              0.0s
 => => exporting manifest list sha256:9e6165f512f0c3753783ff4d72628efdc871c1398070b73fc4584b75400468ce                                                                     0.0s
 => => naming to docker.io/library/minha-app-python:1.0                                                                                                                    0.0s
 => => unpacking to docker.io/library/minha-app-python:1.0                                                                                                                 0.2s

2. Registro da Execução da Aplicação (Run)

PS imagens_personalizadas> docker run --rm minha-app-python:1.0
EXECUTANDO APLICAÇÃO DENTRO DO CONTÊINER DOCKER
 - Resultado da soma (10 + 5): 15
 - Resultado da multiplicação (4 * 3): 12
 - Resultado da divisão (20 / 4): 5.0
Aplicação executada com SUCESSO