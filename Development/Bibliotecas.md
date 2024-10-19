## Resumo
- OS
- Shutil
- Random
- Stat

### Biblioteca `os`
A biblioteca `os` permite a interação com o sistema operacional, oferecendo funcionalidades para manipular arquivos, diretórios, processos e muito mais.
Embora seja a primeira usada para lidar com controle do sistema operacional, ela não oferece uma funcionalidade abrangete para deletar ou remover permissões

**Principais Funcionalidades:**
1. **Manipulação de Arquivos e Diretórios:**
   - `os.getcwd()`: Retorna o diretório de trabalho atual.
   - `os.chdir(path)`: Altera o diretório de trabalho.
   - `os.listdir(path)`: Lista arquivos e diretórios em um caminho.
   - `os.mkdir(path)`: Cria um novo diretório.
   - `os.makedirs(path)`: Cria diretórios intermediários.
   - `os.remove(path)`: Remove um arquivo.
   - `os.rmdir(path)`: Remove um diretório vazio.
   - `os.removedirs(path)`: Remove diretórios recursivamente até encontrar um não vazio.

________________________________________________________________

### Biblioteca `shutil`
A biblioteca `shutil` complementa `os` para operações de manipulação de arquivos e diretórios, fornecendo uma interface mais simples.
Foi a que mais usei durante todos os testes, me pareceu a mais poderosa em manipulação de arquivos

**Principais Funcionalidades:**
1. **Copiar Arquivos e Diretórios:**
   - `shutil.copy(src, dst)`: Copia o arquivo `src` para `dst`.
   - `shutil.copy2(src, dst)`: Copia arquivo preservando metadados.
   - `shutil.copytree(src, dst)`: Copia diretórios recursivamente.
2. **Mover/Renomear Arquivos:**
   - `shutil.move(src, dst)`: Move ou renomeia arquivos/diretórios.
3. **Remover Diretórios Recursivamente:**
   - `shutil.rmtree(path)`: Remove um diretório e seu conteúdo.
4. **Compactação de Arquivos:**
   - `shutil.make_archive(base_name, format, root_dir)`: Cria um arquivo compactado.
5. **Verificação de Espaço em Disco:**
   - `shutil.disk_usage(path)`: Retorna o uso do disco em um caminho.

________________________________________________________________

### Biblioteca `random`  
A biblioteca `random` gera números pseudoaleatórios e realiza operações baseadas em probabilidade.

**Principais Funcionalidades:**
- `random.random()`: Retorna um número aleatório entre 0 e 1.
- `random.randint(a, b)`: Retorna um número inteiro aleatório entre `a` e `b`.
- `random.choice(seq)`: Retorna um item aleatório de uma sequência.
- `random.shuffle(seq)`: Embaralha uma lista.
- `random.sample(population, k)`: Retorna uma lista com `k` elementos aleatórios de uma população.

_______________________________________________________________________________________________________________________________

### Biblioteca `stat`
A biblioteca `stat` é usada para interpretar resultados de chamadas do sistema relacionadas a arquivos (como permissões e tipos de arquivos).

**Principais Funcionalidades:**
- `stat.S_ISDIR(mode)`: Verifica se o modo corresponde a um diretório.
- `stat.S_ISREG(mode)`: Verifica se o modo corresponde a um arquivo regular.
- Constantes como `stat.S_IRWXU`, `stat.S_IRWXG`, `stat.S_IRWXO` são usadas para verificar permissões de leitura, escrita e execução para o dono, grupo e outros usuários.

Essas bibliotecas são fundamentais para manipular arquivos, diretórios, gerar números aleatórios e trabalhar com permissões e atributos de arquivos no sistema operacional.
