# Catch-Face

Olá, projeto produzido com intuito de facilitar o corte de vídeos em partes que pessoas especificas aparecem nele.

A ideia foi criada apartir da ideia de guardar momentos, como um vídeo de formatura, uma entrevista, segurança ou encontrar uma pessoal no meio de várias pessoas, em meio a multidão não está preciso do jeito que está sendo utilizado.

## 🛠️ Made with

- [DeepFace](https://github.com/serengil/deepface) - Modelo de reconhecimento e identificação facial.
- [Opencv](https://github.com/opencv/opencv-python) - Modelo utilizado para reconhecimento facial, objetos e manipulação de imagens.
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - Biblioteca para criação de interface gráfica.
- [Moviepy](https://github.com/Zulko/moviepy) - Biblioteca de edição de vídeo

## 🚀 Iniciando

Com está sem o executável vamos iniciar da maneira tradicional.

- Primeiro vamos clonar o repositório.

  ```Shell
  git clone https://github.com/LiR4/Catch-Face.git
  ```

- Entre na pasta do projeto e use o comando.

  ```Shell
  pip install -r requirements.txt
  ```

- Agora use esse comando para modular o projeto.
  ```Shell
  pip install -e
  ```

## 💻 Como usar

Após realizar as etapas acima é bom separar o vídeo que vai utilizar em uma pasta que lembre o caminho e depois uma pasta para imagens da pessoa.

- primeiro passo é clicar em start, quando fizer isso ele vai iniciar pedido para selecionar o arquivo do vídeo.

- Em seguida para selecionar a pasta com as fotos da pessoa.

- Após finalizar o processo o botão mover pode ser utilizado, ele ira mover os clips para a pasta padrão do windows chamada `Videos`.

## 📝 Code

### Config Handler

A classe ConfigHandler auxilia na buscar dos diretorios, pois utiliza de um config.ini para informar os caminhos das pastas.

Sendo direto ele retorna os caminhos para os comandos.

```Python
class ConfigHandler:
    config = configparser.ConfigParser()
    config.read(r"shared\config.ini", encoding="utf-8-sig")

    def get_path_data(self) -> str:
        return self.config.get("path", "data")

    def get_path_cut(self) -> str:
        return self.config.get("path", "cut")

    def get_path_test(self) -> str:
        return self.config.get("path", "test")

    def get_path_comp(self) -> str:
        return self.config.get("path", "compare")
```

### dir command

A classe DirCommand é utilizada para a criação de pastas que não existe, assim servindo como inicializador destas.

- Ele depende exclusivamente do **_ConfigHandler_**, pois precisa dos caminhos do diretório.

```Python
class DirCommand:
    def __init__(self, config: ConfigHandler):
        self.config = config

    #this function create path doesn't exist
    def create_path(self):
        path_data = self.config.get_path_data()
        path_cut = self.config.get_path_cut()
        path_test =  self.config.get_path_test()
        path_compare = self.config.get_path_comp()

        if(os.path.isdir(path_data) == False):
            clip = os.path.join('shared', 'data')
            os.makedirs(clip)

        if(os.path.isdir(path_cut) == False):
            clip = os.path.join(path_data, 'clip')
            os.makedirs(clip)

        if(os.path.isdir(path_test) == False):
            clip = os.path.join(path_data, 'test')
            os.makedirs(clip)

        if(os.path.isdir(path_compare) == False):
            clip = os.path.join(path_test, 'compare')
            os.makedirs(clip)
```

### video command

A classe Video Command é a principal do projeto, pois executa as pricipais funções que formam o projeto.

- Ele é dependente da classe **_ConfigHandler_** e **_AppCommand_**, config para passar os diretorios e app para ter os arquivos como vídeo e pasta de comparação.

Por se tratar da parte principal será dividida em blocos.

```Python
class VideoCommand:
    def __init__(self, config:ConfigHandler, app:AppCommand):

        self.config = config
        self.app = app
        self.results = []
        self.last_time = []
        self.time_start = 0.0
        self.time_end = 0.0
        self.count = 0
        self.path_cut = config.get_path_cut()
        self.exe = []
```

### get_faces_on_video

Tem como função principal encontrar a parte em que rostos são encontrados no vídeo, eliminando partes sujas que tornam a execução mais lenta.

- Depende somente do parametro seconds que exerce a função de aquanto tempo de video vai ser capturado.

Infelizmenete não esta capturando automaticamente enquanto a pessoa está em cena.

```Python
def get_faces_on_video(self, seconds=3):

    video_path = self.app.video_file()

    video = cv2.VideoCapture(video_path)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    while True:
        sucess, img = video.read()
        faces = face_cascade.detectMultiScale(img, 1.3, 4)

        if(type(faces).__module__ == np.__name__):
            self.time_start = (video.get(cv2.CAP_PROP_POS_MSEC))/1000
            self.last_time.append(self.time_start)

        if(type(faces).__module__ != np.__name__):
            self.time_end = (video.get(cv2.CAP_PROP_POS_MSEC))/1000

        if(self.time_start != 0.0 and self.time_end != 0.0): # cut section
            if(self.last_time[self.count]+1 < self.time_start):
                self.cut(video_path, self.time_start, self.time_end, self.count, seconds)
                print(f"time start: {self.time_start}, time end: {self.time_end+seconds}")
                self.count += 1

            self.time_start = 0.0
            self.time_end = 0.0


        # cv2.imshow("teste",img)
        if sucess != True:
            break

    self.clips_have_face()
```

### cut

Tem como objetivo realizar o corte do vídeo em clips, mas colocada em uma função sem necesidade a principio, mas quando colocada diretamente ocorre erro e não corta.

```Python
def cut(self,video_file, time_start, time_end, count, second):
    ffmpeg_extract_subclip(video_file, time_start, time_end+second, targetname=self.config.get_path_cut()+f'\cut{count}.mp4')
```
### clips_have_face
Utiliza de um looping juntamente com a função que compara se no clips tem o rosto da pessoa.

```Python
def clips_have_face(self):
    compare_dir = self.app.compare_dir()
    for file in os.listdir(self.path_cut):
        print("--------\n",self.path_cut+'\\'+file,"\n--------")
        self.catch_face(self.path_cut+'\\'+file, compare_dir)      
```

### catch_face 
Tem como objetivo principal identificar se o rosto é correspondente se baseando na pasta selecionada ou passada como parâmetro para a função.

* Ele necessita do video selecionado e a pasta para iniciar.

Ao iniciar utiliza da comparação de frame a frame com as imagens presentes na pasta.

```Python
def catch_face(self, file, compare):
    video = cv2.VideoCapture(file)
    if(video.isOpened):
        while True:
            state, frames = video.read()
            if(state):
                cv2.imwrite('./shared/data/test/teste.jpg', frames)
                dfs = DeepFace.find(img_path = './shared/data/test/teste.jpg', db_path = compare, enforce_detection=False)
                if(len(dfs[0])!=0):
                    self.results.append(file)
                    break
            else:
                break
```
### move_clips

Sua função é mover clips que foi encontrado a pessoa no vídeo para a pasta padrão ***Videos*** do Windows.

```Python
def move_clips(self):
    for files in os.listdir(self.path_cut):
        for videos in self.results:
            if(files == str(videos.replace(f'{self.path_cut}'+'\\', ''))):
                shutil.move(videos, f'C:/Users/{os.getlogin()}/Videos')
```