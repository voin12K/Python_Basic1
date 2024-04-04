chess_players = {
    "Carlsen, Magnus": 1865,
    "Firouzja, Alireza": 2804,
    "Ding, Liren": 2799,
    "Caruana, Fabiano": 1792,
    "Nepomniachtchi, Ian": 2773
}

filtered_players = {v: k for k, v in chess_players.items() if v > 2000}

print(filtered_players)
