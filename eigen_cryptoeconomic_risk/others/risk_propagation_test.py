
import networkx as nx
import matplotlib.pyplot as plt
import random

# Create a network
G = nx.Graph()
nodes = ["Node1", "Node2", "Node3", "Node4"]
G.add_node("Node5")
edges = [("Node1", "Node2"), ("Node2", "Node3"), ("Node3", "Node4")]
G.add_edges_from([("Node2", "Node5"), ("Node5", "Node4")])

# Define a risk scenario
def risk_impact(node):
    # Here, there's a 30% chance that the node will be impacted
    return random.random() < 0.3  # 0.3 is the probability of being impacted


# Simulate risk propagation
def simulate_risk(G, start_node):
    impacted_nodes = set()
    nodes_to_check = [start_node]

    while nodes_to_check:
        current_node = nodes_to_check.pop()
        if risk_impact(current_node):
            impacted_nodes.add(current_node)
            nodes_to_check.extend([n for n in G.neighbors(current_node) if n not in impacted_nodes])

    return impacted_nodes

# Run the simulation
start_node = "Node1"
result = simulate_risk(G, start_node)
print("Impacted Nodes:", result)

# Plot the network
plt.figure(figsize=(8, 5))
pos = nx.spring_layout(G)  # positions for all nodes

# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

# labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

# Highlight impacted nodes
nx.draw_networkx_nodes(G, pos, nodelist=result, node_color="r", node_size=700)

plt.axis("off")
plt.show()
