import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse

def radar_chart(player1_data, player2_data, attributes, player1_name, player2_name):
    num_vars = len(attributes)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist() + [0]

    player1_data = np.append(player1_data, player1_data[0])
    player2_data = np.append(player2_data, player2_data[0])

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, player1_data, color='red', alpha=0.25, label=player1_name)
    ax.fill(angles, player2_data, color='blue', alpha=0.25, label=player2_name)
    
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(attributes)

    plt.legend(loc='upper right')
    plt.title(f'Radar Chart Comparison: {player1_name} vs {player2_name}')
    plt.show()

def main():
    df = pd.read_csv('results.csv')

    parser = argparse.ArgumentParser(description='Radar Chart Comparison between Players')
    parser.add_argument('--p1', required=True, help='Player 1 Name')
    parser.add_argument('--p2', required=True, help='Player 2 Name')
    parser.add_argument('--attributes', required=True, help='Comma-separated list of attributes')
    
    args = parser.parse_args()
    attributes = args.attributes.split(',')

    for attr in attributes:
        if attr not in df.columns:
            raise ValueError(f"Attribute not found: {attr}")

    player1_data = df.loc[df['Name'] == args.p1, attributes].values.flatten()
    player2_data = df.loc[df['Name'] == args.p2, attributes].values.flatten()

    if player1_data.size == 0:
        raise ValueError(f"Player '{args.p1}' not found.")
    if player2_data.size == 0:
        raise ValueError(f"Player '{args.p2}' not found.")

    radar_chart(player1_data, player2_data, attributes, args.p1, args.p2)

if __name__ == "__main__":
    main()
