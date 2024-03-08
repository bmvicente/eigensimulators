# MAKE ARROWS ALL THE SAME SIZE & MAKE SURE THEY DON'T OVERLAP
# MAKE THE DISPLAY REALLY ORGANIZED, LIKE IN A FLOWER FORMAT
# ONE FLOWER IN THE TOP LEFT, ANOTHER IN THE TOP RIGHT, ETC



# Import necessary libraries
import streamlit as st  # For creating web applications
import numpy as np  # For numerical operations
import plotly.graph_objects as go  # For creating figures and visualizations
import random  # For generating random numbers
import networkx as nx  # For creating and visualizing complex networks

# Set Streamlit page layout to wide mode for better visualization
st.set_page_config(layout="wide")

st.title("AVS Ecosystem Compounded Risk Simulator")

st.write("\n" * 4)

# Function to adjust node positions to prevent overlap
def adjust_positions(pos, operators, adjustment_step=0.1):
    adjusted_pos = pos.copy()
    # Iterate through pairs of operators to ensure their positions are not too close to each other
    for i, op1 in enumerate(operators):
        for op2 in operators[i+1:]:
            # Adjust position if operators are closer than the adjustment step
            while np.linalg.norm(np.array(adjusted_pos[op1]) - np.array(adjusted_pos[op2])) < adjustment_step:
                adjusted_pos[op2] = (adjusted_pos[op2][0] + adjustment_step, adjusted_pos[op2][1] + adjustment_step)
    return adjusted_pos

# Initialize session state for number of operators if not already set
if 'num_operators' not in st.session_state:
    st.session_state.num_operators = 0





st.write("**AVS METRICS**")

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    num_avss = st.slider('**Number of AVSs**', st.session_state.num_operators, 15, max(st.session_state.num_operators, 15))

with col2:
    avg_risk_score = st.slider('**AVS Average Risk Score**', 0, 100, 0)

with col3:
    category_dominance = st.slider('**AVS Category Dominance**', 0, 100, 0, format='%d%%')

st.write("\n" * 2)





st.write("**OPERATOR METRICS**")

col4, col5, col6, col7 = st.columns(4, gap="large")

with col4:
    st.session_state.num_operators = st.slider('**Number of Operators**', 1, 5, 5)

with col5:
    entrenchment_level = st.slider('**Operator Entrenchment Level**', 0, 100, 0, key='entrenchment_slider', format='%d%%')

with col6:
    centralization_level = st.slider('**Centralization Level of Node Operators**', 0, 100, 0, key='centralization_slider', format='%d%%')

with col7:
    reputation_level = st.slider('**Operator Reputation Level**', 0, 100, 0, key='reputation_slider', format='%d%%')

st.write("\n")






if st.button("Update State"):
    st.write("")

# Set random seed for reproducibility
np.random.seed(0)






# Create a list of operator names based on the number of operators
operators = [f"Operator {i+1}" for i in range(st.session_state.num_operators)]

# Initialize an empty list for AVSs
avss = []

# Loop to create AVSs with attributes based on input metrics
for i in range(num_avss):

    # Assign an operator to each AVS, cycling through the list of operators
    operator = operators[i % len(operators)]

    # Determine category based on dominance slider or randomly
    category = 0 if np.random.rand() < category_dominance / 100.0 else np.random.randint(0, 3)

    # Generate a risk score for the AVS based on the average risk score with some variability
    risk_score = np.clip(np.random.normal(loc=avg_risk_score, scale=10), 1, 100)

    # Generate a random entrenchment level for the AVS
    entrenchment = np.random.randint(0, 100)

    # Append a dictionary with AVS details to the avss list
    avss.append({
        'name': f"AVS {i+1}",
        'category': category,
        'risk_score': int(risk_score),
        'operator': operator,
        'entrenchment_level': entrenchment
    })


# Loop to ensure each operator has at least one AVS and fill the rest
for i in range(st.session_state.num_operators):

    # Generate a risk score for the AVS
    risk_score = np.clip(np.random.normal(loc=avg_risk_score, scale=10), 1, 100)

    # Append an AVS for each operator to the avss list
    avss.append({
        'name': f"AVS {i+1}",
        'risk_score': int(risk_score),
        'operator': operators[i],
        'category': np.random.randint(0, 3)
    })



### WTF is this

# Adjust operator entrenchment level if it's greater than 0
if entrenchment_level > 0:

    # Create a dictionary mapping operators to their entrenchment level
    operator_entrenchment = {op: entrenchment_level / 100.0 for op in operators}

    # Normalize entrenchment levels to sum to 1
    total_entrenchment = sum(operator_entrenchment.values())
    normalized_entrenchment = {op: level / total_entrenchment for op, level in operator_entrenchment.items()}

    # Assign normalized entrenchment levels to AVSs
    for avs in avss:
        avs['operator_entrenchment'] = normalized_entrenchment[avs['operator']]




# Create a directed graph using NetworkX
G = nx.DiGraph()

# Add operator nodes to the graph with certain attributes
# 'bipartite=0' indicates these are one type of node in a bipartite graph,
# 'node_color' and 'node_type' are custom attributes that may be used for visualization or analysis
G.add_nodes_from(operators, bipartite=0, node_color='blue', node_type='operator')

# Loop through the list of AVS entities to add them to the graph with associated attributes
for avs in avss:
    # Add each AVS as a node with attributes like 'category' and 'node_type'
    # 'bipartite=1' indicates these nodes are the second type in the bipartite graph
    G.add_node(avs['name'], bipartite=1, node_color='red', node_type='avs', category=avs['category'])
    # Create an edge between the operator and the AVS node, with the 'weight' being the risk score
    G.add_edge(avs['operator'], avs['name'], weight=avs['risk_score'])

# Calculate positions for nodes in the graph for visualization purposes
# 'nx.spring_layout' is a force-directed layout algorithm that positions nodes in a way that
# nodes with connections (edges) are pulled closer together, while nodes without connections push apart
pos = nx.spring_layout(G, seed=42)
# Adjust positions to prevent overlap and ensure that nodes are not too close to each other
pos = adjust_positions(pos, operators, adjustment_step=0.1)

# Initialize a Plotly figure for graph visualization
fig = go.Figure()

# Add operators to the visualization
# This block ensures that each operator is represented only once in the legend
operator_legend_added = set()
for avs in avss:
    if avs['operator'] not in operator_legend_added:
        # Add a scatter plot for operators with a blue square marker
        fig.add_trace(go.Scatter(
            x=[pos[avs['operator']][0]],  # x position from the layout
            y=[pos[avs['operator']][1]],  # y position from the layout
            mode='markers',  # Only markers, no lines
            marker=dict(size=20, color='blue', symbol='square'),  # Square marker for operators
            text=avs['operator'],  # Operator name as hover text
            name='Operators'  # Name for legend entry
        ))
        operator_legend_added.add(avs['operator'])

# Add AVSs to the visualization
# 'initial_avs_size' is the base size of the AVS markers
initial_avs_size = 20
# Loop through the AVS entities to add them as scatter plot markers
for avs in avss:
    category = avs['category']
    color = ['green', 'pink', 'red'][category]  # Color coding for categories
    # Calculate size factors based on risk score, entrenchment level, and category dominance
    size_factor = avs['risk_score'] * 0.40  # Size increase based on risk score
    max_entrenchment_level = 100  # Assuming maximum entrenchment level is 100%
    entrenchment_size_factor = (avs['operator_entrenchment'] / max_entrenchment_level) * 10  # Size increase based on entrenchment
    category_dominance_size_factor = category_dominance * 0.40  # Size increase based on category dominance
    # The final size is the sum of the base size and the calculated factors
    final_size = initial_avs_size + size_factor + entrenchment_size_factor + category_dominance_size_factor
    # Add a scatter plot for AVSs with a circular marker
    fig.add_trace(go.Scatter(
        x=[pos[avs['name']][0]],  # x position from the layout
        y=[pos[avs['name']][1]],  # y position from the layout
        mode='markers',  # Only markers, no lines
        marker=dict(size=final_size, color=color),  # Marker size and color
        text=avs['name'],  # AVS name as hover text
        name=['Decentralized Sequencer AVS', 'Oracle AVS', 'Data Availability AVS'][category]  # Name for legend entry based on category
    ))

# Add edges (lines) to the visualization to show connections between operators and AVSs
# 'edge_trace' is a list to store the line objects for the graph
edge_trace = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]  # Position of the starting node (operator)
    x1, y1 = pos[edge[1]]  # Position of the ending node (AVS)
    # Add a line object representing the edge
    edge_trace.append(go.Scatter(
        x=[x0, x1], y=[y0, y1],
        mode='lines',  # Only lines, no markers
        line=dict(color='gray', width=1),  # Line styling
        hoverinfo='none',  # No hover information
        showlegend=False  # Do not show in legend
    ))

# Add the edge traces to the figure
for trace in edge_trace:
    fig.add_trace(trace)

# Add arrow annotations to indicate the direction of the edges
for edge, trace in zip(G.edges(), edge_trace):
    x0, y0 = trace['x'][0], trace['y'][0]  # Start of the line
    x1, y1 = trace['x'][1], trace['y'][1]  # End of the line
    # Add an annotation with an arrow at the end of the line
    fig.add_annotation(
        x=x1, y=y1,
        ax=x0, ay=y0,
        xref='x', yref='y',
        axref='x', ayref='y',
        showarrow=True,
        arrowhead=3,
        arrowsize=2,
        arrowwidth=1,
        arrowcolor='gray'
    )

# Update the layout of the figure
fig.update_layout(
    showlegend=True,
    legend=dict(x=1, y=1, font=dict(size=12), itemsizing='constant'),
    width=1200, height=800  # Set the size of the figure
)

# Display the plot using Streamlit
st.plotly_chart(fig, use_container_width=True)

# Insert blank line for formatting purposes
st.write("\n")