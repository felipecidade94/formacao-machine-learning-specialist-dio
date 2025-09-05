# Classificação de Imagens - Gatos e Cachorros (Transfer Learning)

Este repositório contém a implementação do **primeiro desafio de projeto** da Formação **Machine Learning Specialist** da [DIO](https://www.dio.me/).
O objetivo é aplicar **Transfer Learning** para treinar um modelo capaz de classificar imagens entre **gatos** e **cachorros**, utilizando uma base de dados organizada em treino e validação.

---

## 📂 Estrutura do Projeto

```bash
desafio-1/
│── cats_and_dogs_filtered/      # Dataset organizado
│   ├── train/                   # Conjunto de treino
│   │   ├── cats/                # Imagens de gatos (treino)
│   │   └── dogs/                # Imagens de cachorros (treino)
│   └── validation/              # Conjunto de validação
│       ├── cats/                # Imagens de gatos (validação)
│       └── dogs/                # Imagens de cachorros (validação)
│
│── vectorize.py                 # Script para pré-processamento/vetorização
│── desafio-de-projeto-1.ipynb   # Notebook principal com a solução
│── requirements.txt             # Dependências do projeto
│── README.md                    # Este arquivo
│── LICENSE                      # Licença de uso
│── .gitignore                   # Arquivos ignorados pelo Git
│── venv/                        # Ambiente virtual (não incluso no Git)
│── teste.png / teste2.jpg ...   # Imagens auxiliares
```

---

## 🚀 Como Executar o Projeto

1. **Clone este repositório**:

   ```bash
   git clone https://github.com/felipecidade94/formacao-machine-learning-specialist-dio.git
   cd formacao-machine-learning-specialist-dio/desafio-1
   ```
2. **Crie e ative um ambiente virtual (recomendado)**:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```
3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```
4. **Execute o notebook do projeto**:
   Abra o arquivo `desafio-de-projeto-1.ipynb` no **Jupyter Notebook** ou **VS Code** e siga as etapas para:

   - Carregar o dataset
   - Aplicar Transfer Learning
   - Treinar e avaliar o modelo

---

## 🧠 Técnicas Utilizadas

- **Transfer Learning** com redes neurais pré-treinadas
- **Keras / TensorFlow** para modelagem
- **Data Augmentation** para melhorar a generalização
- Avaliação do modelo em **treino e validação**

---

## 📌 Observações

- O dataset já está organizado em pastas (`train` e `validation`), o que facilita o carregamento via `ImageDataGenerator` do Keras.
- O script `vectorize.py` pode ser usado para auxiliar no pré-processamento ou organização de dados adicionais.
- Os arquivos `teste.png`, `teste2.jpg`, `teste3.jpg` podem ser utilizados para **inferencia manual** após o treinamento do modelo.

---

## 📄 Licença

Este projeto está sob a licença [MIT](./LICENSE).
Sinta-se à vontade para usar, modificar e compartilhar.

---

✍️ Desenvolvido por **Felipe Cidade Soares** durante a Formação *Machine Learning Specialist - DIO*
