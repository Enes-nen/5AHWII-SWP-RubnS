import random

# ================================
# Poker Simulator
# ================================


# --- Deck aufbauen ---
suits = ['♠', '♥', '♦', '♣']
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

deck = [rank + suit for suit in suits for rank in ranks]


# --- Kombinationen als Dictionary ---
hand_names = {
    0: "High Card",
    1: "One Pair",
    2: "Two Pair",
    3: "Three of a Kind",
    4: "Straight",
    5: "Flush",
    6: "Full House",
    7: "Four of a Kind",
    8: "Straight Flush"
}

# --- Theoretische Wahrscheinlichkeiten ---
theoretical_probs = {
    "High Card": 50.1177,
    "One Pair": 42.2569,
    "Two Pair": 4.7539,
    "Three of a Kind": 2.1128,
    "Straight": 0.3925,
    "Flush": 0.1965,
    "Full House": 0.1441,
    "Four of a Kind": 0.0240,
    "Straight Flush": 0.00139
}


# --- Eine Hand ziehen ---
def draw_hand():
    return random.sample(deck, 5)


# --- Zähle wie oft jeder Wert vorkommt ---
def count_ranks(hand):
    counts = {}
    for card in hand:
        rank = card[:-1]
        counts[rank] = counts[rank] + 1 if rank in counts else 1
    return counts


# --- Kombination erkennen ---
def evaluate_hand(hand):
    rank_counts = count_ranks(hand)
    values = list(rank_counts.values())

    suits_in_hand = []
    for card in hand:
        suits_in_hand.append(card[-1])
    is_flush = len(set(suits_in_hand)) == 1

    rank_values = []
    for card in hand:
        rank = card[:-1]
        rank_values.append(ranks.index(rank))
    rank_values.sort()

    is_straight = True
    for i in range(1, len(rank_values)):
        if rank_values[i] - rank_values[i-1] != 1:
            is_straight = False
            break

    if is_straight and is_flush:
        return hand_names[8]
    elif 4 in values:
        return hand_names[7]
    elif 3 in values and 2 in values:
        return hand_names[6]
    elif is_flush:
        return hand_names[5]
    elif is_straight:
        return hand_names[4]
    elif 3 in values:
        return hand_names[3]
    elif values.count(2) == 2:
        return hand_names[2]
    elif 2 in values:
        return hand_names[1]
    else:
        return hand_names[0]


# --- Simulation ---
def simulate(games):
    results = {}
    for i in range(games):
        hand = draw_hand()
        combo = evaluate_hand(hand)
        results[combo] = results[combo] + 1 if combo in results else 1
    return results


# --- Ausgabe mit Vergleich ---
def print_results(results, total):
    print("Poker Simulation über", total, "Spiele")
    print("------------------------------------------------------------")
    print("Kombination | Sim (%) | Theorie (%) | Differenz (%)")
    print("------------------------------------------------------------")

    for combo in results:
        simulated = (results[combo] / total) * 100
        theoretical = theoretical_probs[combo]
        difference = simulated - theoretical

        print(combo, "|",
              round(simulated, 4), "% |",
              theoretical, "% |",
              round(difference, 4), "%")

    print("------------------------------------------------------------")


def main():
    games = 100000
    results = simulate(games)
    print_results(results, games)


main()
