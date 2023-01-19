# Recomendação de Mapas com o KNN (K-Nearest Neighbors)

Foi implementado o Algoritmo KNN em python, usando o conjunto de bibliotecas do Scikit-Learn para a recomendação de mapas gerados proceduralmente. Este trabalho é feito sobre um jogo já desenvolvido anteriormente cujo sua principal features é a geração procedural de mapas a cada nova rodada do jogador.

Sobre o jogo, ele é um rpg de ação top-down, onde o jogador pode andar, rolar, atacar, atirar facas num cenário totalmente procedural, ao iniciar o jogo, o jogador é direcionado para a hub inicial onde ele pode pegar quests opcionais com npcs para se realizar nesses mapas após a escolha das mesmas, o jogador deve ir ao portal localizado na extrema direta da hub, ao entrar nele o jogador se depara com um menu de parâmetros para a geração, como o tamanho do mapa, a quantidade e densidade de inimigos e itens, o quão labirintico esse mapa é. Após a seleção dos parâmetros, um mapa será gerado baseado pelos parâmetos setados anteriormente.

![Menu com os Parâmetros](https://github.com/NidalMartinsAli/Images/blob/main/menuParametros.png)

Após os jogador completar a sua rodada, ele será redirecionado para o questionário onde este será de grande importancia para este trabalho em específico, este questionário contém dados necessários para o treino do algoritmo KNN. Após o jogador responder todas as perguntas, ele será redirecionado para o hub principal onde o processo todo volta a se repetir.

![Questionário a ser respondido](https://github.com/NidalMartinsAli/Images/blob/main/questionario.png)

Com a inserção do KNN no jogo, o fluxo segue o mesmo, porém algumas respostas coletadas do questionário como também alguns dados da rodada do jogador serão utilizados para a recomendação do próximo disponível para esse jogador, para mais detalhes por favor dê uma olhada no texto final do projeto que estará disponível mais abaixo.

O intuito desse trabalho é melhorar a experiência do jogador, tornando ela mais personalizada e única ao oferencer para ele mapas que se baseiam em seus padrões de gameplay e de como ele respondeu as perguntas do questionário.
O fluxo de todo o processo é descrito da seguinte forma:

![Fluxo do projeto](https://github.com/NidalMartinsAli/Images/blob/main/diagramão.png)

Ele pode ser descrito com seguintes passos:

1. Jogo desenvolvido na Unity.
2. Dataset atualizado em tempo real a cada jogada.
3. KNN (Após a seleção de features, o treinamento é feito e então finalmente um modelo treinado é exportado para a API).
4. API desenvolvida utilizando o flask + python para comunicação entre jogo e IA.

Para a total compreensão deste trabalho, os links abaixo são essenciais.

1. Vídeo com o jogo rodando e como funciona o fluxo da rodada e da recomendação após a mesma: https://www.youtube.com/watch?v=dXJxi9zGEr8
2. Texto final contendo explicações mais detalhadas de todo o projeto: [TCC - Nidal Martins Ali.pdf](https://github.com/NidalMartinsAli/KNN_Model_TCC/blob/main/Monografia_Final%20-%20Nidal%20Martins%20Ali.pdf)
