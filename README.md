# hera-chat-bot

``` Shell
pip install nltk
pip install numpy
pip install keras
pip install tensorflow
```

- NLTK — É uma das ferramentas mais utilizadas para processamento de linguagem natural, foi desenvolvida em Python e tem uma gama muito grande de recursos, como: classificação, tokenização, stemming, tagging, parsing e raciocínio semântico. Todas essas funções são utilizadas para análise de texto;
- Numpy — É uma biblioteca para a linguagem Python com funções para se trabalhar com computação numérica, e que pode realizar operações de álgebra linear de maneira muito eficiente;
Tensorflow — É uma biblioteca de código aberto criada para aprendizado de máquina, computação numérica e muitas outras tarefas;
- Keras — Por último, e de extrema importância, usamos o Keras para a estrutura de aprendizado profundo, essa lib poderosíssima é uma das principais APIs de redes neurais de alto nível.
Será interessante vocês lerem como essas bibliotecas funcionam para entender melhor o nosso código.


Extraindo os dados e criando nossa interface (GUI)
- clear_writing que é a responsável por limpar as palavras inseridas, ou seja, fazer a higienização da mensagem enviada pelo usuário
- bag_of_words é a função responsável por criar um pacote de palavras que será usado para as previsões.
- class_prediction faz a previsão do pacote de palavras, usamos como limite de erro 0.25 para evitarmos overfitting e classificamos esses resultados por força da probabilidade;
- get_response é a função que vamos usar depois que fizermos todo o processo acima, com nosso retorno de intenção, verificamos qual as mensagens de retorno do json, usamos o random para pegarmos apenas uma resposta da lista.


