% PERGUNTA 1:
% Qual é o ranking das moedas que mais valorizaram nas últimas 24h?

% Sentença auxiliar
moeda_variacao(Id, Change) :-
    crypto(Id, _, _, _, Change, _, _).

% Agrupa, ordena e inverte para o maior ficar no topo
ranking_valorizacao(Top10) :-
    findall(Change-Id, moeda_variacao(Id, Change), Lista),
    sort(Lista, ListaOrd),
    reverse(ListaOrd, Tabela),
    % Pega apenas os 10 primeiros para não travar a tela
    length(Top10, 10),
    append(Top10, _, Tabela).


% PERGUNTA 2:
% Quais moedas estão valendo menos de 20% do seu valor máximo histórico (ATH)?

desconto_historico(Id, Preco, ATH, Razao) :-
    crypto(Id, _, Preco, _, _, ATH, _),
    ATH > 0,              % Evita divisão por zero
    Razao is Preco / ATH,
    Razao < 0.2.          % Filtra por moedas abaixo de 20% do ATH


% PERGUNTA 3:
% Qual é a média de volume financeiro de negociação das moedas no Top N (ex: Top 20)?

% Pega o volume das moedas até o rank limite
volume_top_n(RankLimite, Vol) :-
    crypto(_, _, _, Rank, _, _, Vol),
    Rank =< RankLimite.

% Calcula a média de volume
media_volume_top(RankLimite, Media) :-
    findall(V, volume_top_n(RankLimite, V), ListaVolumes),
    sum_list(ListaVolumes, TotalVolume),
    length(ListaVolumes, QtdMoedas),
    QtdMoedas > 0,
    Media is TotalVolume / QtdMoedas.
