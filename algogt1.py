import networkx as nx
import matplotlib.pyplot as plt

# Define the Gale-Shapley algorithm to find stable matches.
def gale_shapley(men_preferences, women_preferences):
    """
    Implements the Gale-Shapley algorithm to solve the stable marriage problem.
    
    Args:
    men_preferences (dict): Maps men's names to lists of women in order of preference.
    women_preferences (dict): Maps women's names to lists of men in order of preference.

    Returns:
    dict: Stable matches where keys are men's names and values are their matched women's names.
    """
    # Initialize all men as free and have not yet proposed to any woman.
    free_men = list(men_preferences.keys())
    # Dictionary to store current engagements where keys are men's names and values are women's names.
    engagements = {}

    # Continue the algorithm while there are still free men who haven't proposed to every woman.
    while free_men:
        # Select the first man from the list of free men.
        man = free_men[0]
        # Get his list of preferences.
        woman_list = men_preferences[man]
        # Iterate over his list of preferred women.
        for woman in woman_list:
            # Check if the current woman is not yet engaged.
            if woman not in engagements.values():
                # Engage the man and the woman.
                engagements[man] = woman
                # Remove the man from the list of free men.
                free_men.remove(man)
                # Exit the loop once engagement is done.
                break
            else:
                # Find the current partner of the woman.
                current_man = [k for k, v in engagements.items() if v == woman][0]
                # Check if the woman prefers the new man over her current partner.
                if women_preferences[woman].index(man) < women_preferences[woman].index(current_man):
                    # The woman prefers the new man. Break the current engagement.
                    engagements[man] = woman
                    # Engage the woman with the new man.
                    engagements.pop(current_man)
                    # Remove the new man from the list of free men.
                    free_men.remove(man)
                    # Add the previous partner back to the list of free men.
                    free_men.append(current_man)
                    # Exit the loop once the new engagement is done.
                    break

    return engagements

# Preferences for each man and woman.
men_preferences = {
    'A': ['X', 'Y', 'Z'],
    'B': ['Y', 'X', 'Z'],
    'C': ['Y', 'Z', 'X']
}
women_preferences = {
    'V': ['B', 'A', 'C'],
    'U': ['A', 'B', 'C'],
    'X': ['C', 'B', 'B'],
    'Y': ['B', 'A', 'C'],
    'Z': ['C', 'A', 'B']
}

# Compute the stable matches using the Gale-Shapley algorithm.
matches = gale_shapley(men_preferences, women_preferences)
print("Stable matches:", matches)

# Visualization of the stable matches using a bipartite graph.
G = nx.Graph()
# Add nodes for men.
G.add_nodes_from(men_preferences.keys(), bipartite=0, label='man')
# Add nodes for women.
G.add_nodes_from(women_preferences.keys(), bipartite=1, label='woman')
# Add edges for each stable match.
for man, woman in matches.items():
    G.add_edge(man, woman, color='red')  # Red edges signify stable matches.

# Set node positions for a bipartite layout.
pos = {node: [0, i] for i, node in enumerate(men_preferences)}  # Position men on one side.
pos.update({node: [1, i] for i, node in enumerate(women_preferences)})  # Position women on the opposite side.

# Draw the bipartite graph with labeled nodes and colored edges.
colors = [G[u][v]['color'] for u, v in G.edges]  # Get the color for each edge.
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color=colors, width=2)  # Draw the graph with labels and colored edges.
plt.show()  # Display the graph.
