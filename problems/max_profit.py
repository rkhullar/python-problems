"""
Given the history of prices for a stock, find the optimal time to buy and sell one share.

scratch pads
https://repl.it/repls/MiniatureRosybrownCommands
https://repl.it/repls/FunnyAromaticParticle
"""

from typing import List, Dict


def solution(data: List) -> Dict:
    min_idx, max_idx, buy_idx, sell_idx = 0, 0, 0, 0
    max_profit = 0

    for index, value in enumerate(data):

        if value < data[min_idx]:
            min_idx = index
        if value > data[max_idx]:
            max_idx = index

        if data[min_idx] < data[buy_idx]:
            buy_idx = min_idx

        new_profit = value - data[buy_idx]

        if new_profit > max_profit:
            sell_idx = index
            max_profit = new_profit

    return dict(buy_idx=buy_idx, sell_idx=sell_idx, max_profit=max_profit)
