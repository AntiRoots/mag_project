import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Lae sisse kohtulahendite andmed
df = pd.read_csv("data/raw_lahendid.csv", encoding="utf-8")

# Loome graafi
G = nx.Graph()

# Lisame graafi sõlmed (kohtulahendite numbrid)
for case in df["Kohtuasja nr"]:
    G.add_node(case)

# Lisame graafi servad, kui lahendid jagavad samu seaduse sätteid
for _, row in df.iterrows():
    case = row["Kohtuasja nr"]
    related_cases = df[df["Kohtu sätted"] == row["Kohtu sätted"]]["Kohtuasja nr"].tolist()
    
    for related in related_cases:
        if case != related:
            G.add_edge(case, related)

# Joonista graaf
plt.figure(figsize=(12, 8))
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray", node_size=1000, font_size=8)
plt.title("Kohtulahendite vahelised seosed seaduse sätete põhjal")
plt.show()
