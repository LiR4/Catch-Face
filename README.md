# Catch-Face

Olá, projeto produzido com intuito de facilitar o corte de vídeos em partes que pessoas especificas aparecem nele. 

A ideia foi criada apartir da ideia de guardar momentos, como um vídeo de formatura, uma entrevista, segurança ou encontrar uma pessoal no meio de várias pessoas, em meio a multidão não está preciso do jeito que está sendo utilizado.

## 🛠️ Made with

* [DeepFace](https://github.com/serengil/deepface) - Modelo de reconhecimento e identificação facial.
* [Opencv](https://github.com/opencv/opencv-python) - Modelo utilizado para reconhecimento facial, objetos e manipulação de imagens.
* [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - Biblioteca para criação de interface gráfica.
* [Moviepy](https://github.com/Zulko/moviepy) - Biblioteca de edição de vídeo

## 🚀 Iniciando

Com está sem o executável vamos iniciar da maneira tradicional.  

* Primeiro vamos clonar o repositório.
  
    ```
    git clone https://github.com/LiR4/Catch-Face.git
    ```

* Entrenna pasta do projeto e use o comando.
    ```python
    pip install -r requirements.txt
    ```

*  Agora use esse comando para modular o projeto.
    ```python
    pip install -e
    ```


## 💻 Como usar

Após realizar as etapas acima é bom separar o vídeo que vai utilizar em uma pasta que lembre o caminho e depois uma pasta para imagens da pessoa.

* primeiro passo é clicar em start, quando fizer isso ele vai iniciar pedido para selecionar o arquivo do vídeo.

* Em seguida para selecionar a pasta com as fotos da pessoa.

* Após finalizar o processo o botão mover pode ser utilizado, ele ira mover os clips para a pasta padrão do windows chamada ```Videos```.

