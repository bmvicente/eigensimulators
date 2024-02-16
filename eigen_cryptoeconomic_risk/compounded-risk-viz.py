import streamlit as st
import numpy as np
import plotly.graph_objects as go
import random
import networkx as nx  # Added import statement for networkx

st.set_page_config(layout="wide")

st.title("AVS Compounding Risk with Operator Network")

st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")

def adjust_positions(pos, operators, adjustment_step=0.1):
    adjusted_pos = pos.copy()
    for i, op1 in enumerate(operators):
        for op2 in operators[i+1:]:
            while np.linalg.norm(np.array(adjusted_pos[op1]) - np.array(adjusted_pos[op2])) < adjustment_step:
                adjusted_pos[op2] = (adjusted_pos[op2][0] + adjustment_step, adjusted_pos[op2][1] + adjustment_step)
    return adjusted_pos


col1, col2, col3, col4 = st.columns(4, gap="large")

with col1:
    num_operators = st.slider('**Number of Operators**', 1, 5, 5)

with col2:
    num_avss = st.slider('**Number of AVSs**', num_operators, 15, max(num_operators, 15))

with col3:
    avg_risk_score = st.slider('**AVS Average Risk Score**', 0, 100, 0)

with col4:
    category_dominance = st.slider('**AVS Category Dominance**', 0, 100, 0)

st.write("\n")

col5, col6, col7 = st.columns(3, gap="large")

with col5:
    entrenchment_level = st.slider('**Operator Entrenchment Level (%)**', 0, 100, 0, key='entrenchment_slider')

with col6:
    centralization_level = st.slider('**Centralization Level of Node Operators**', 0, 100, 0, key='centralization_slider')

with col7:
    reputation_level = st.slider('**Operator Reputation Level**', 0, 100, 0, key='reputation_slider')


if st.button("Update State"):
    st.write("")

np.random.seed(0)

operators = [f"Operator {i+1}" for i in range(num_operators)]
avss = []




# Creating operators and AVSs with attributes
for i in range(num_avss):
    operator = operators[i % len(operators)]  # Ensures at least one AVS per operator, then cycles through operators

    # Determine category based on dominance or random selection
    if np.random.rand() < category_dominance / 100.0:
        category = 0  # Dominant category
    else:
        category = np.random.randint(0, 3)
    
    risk_score = np.random.normal(loc=avg_risk_score, scale=10)
    risk_score = np.clip(risk_score, 1, 100)

    # Add 'category' key to each AVS dictionary
    avss.append({'name': f"AVS {i+1}", 'category': category, 'risk_score': int(risk_score), 'operator': operator})




# Assigning at least one AVS to each Operator and filling the rest
for i in range(num_operators):
    risk_score = np.random.normal(loc=avg_risk_score, scale=10)  # Normal distribution around the average risk score
    risk_score = np.clip(risk_score, 1, 100)  # Ensure risk score is within bounds
    avss.append({'name': f"AVS {i+1}",
                'risk_score': int(risk_score), 'operator': operators[i], 'category': np.random.randint(0, 3)})




# Adjusting operator entrenchment level
if entrenchment_level > 0:
    # Identify which operators are over-entrenched
    operator_entrenchment = {op: entrenchment_level/100.0 for op in operators}

    # Normalize probabilities
    total = sum(operator_entrenchment.values())
    normalized_entrenchment = [operator_entrenchment[op]/total for op in operators]

    for avs in avss:
        avs['operator'] = np.random.choice(operators, p=normalized_entrenchment)





# Create the graph
G = nx.DiGraph()
G.add_nodes_from(operators, bipartite=0, node_color='blue', node_type='operator')

for avs in avss:
    G.add_node(avs['name'], bipartite=1, node_color='red', node_type='avs', category=avs['category'])
    G.add_edge(avs['operator'], avs['name'], weight=avs['risk_score'])

# Calculate positions for visualization
pos = nx.spring_layout(G, seed=42)
pos = adjust_positions(pos, operators, adjustment_step=0.1)

fig = go.Figure()

# Add operators
operator_legend_added = set()
for avs in avss:
    if avs['operator'] not in operator_legend_added:
        fig.add_trace(go.Scatter(x=[pos[avs['operator']][0]], y=[pos[avs['operator']][1]], mode='markers', 
                                 marker=dict(size=20, color='blue', symbol='square'), text=avs['operator'], name='Operators'))
        operator_legend_added.add(avs['operator'])



# Add AVSs
initial_avs_size = 20
avs_sizes = [initial_avs_size] * len(avss)  # Start with size 20 for all AVSs
for avs in avss:
    category = avs['category']
    color = ['green', 'pink', 'red'][category]
    size_factor = avs['risk_score'] * 0.20
    max_entrenchment_level = 100  # Assuming maximum entrenchment level is 100%
    entrenchment_size_factor = (avs['entrenchment_level'] / max_entrenchment_level) * 10  # Adjust the scaling factor as needed
    category_dominance_size_factor = category_dominance * 0.15  # Assuming category_dominance is a percentage
    avs_sizes.append(initial_avs_size + size_factor + entrenchment_size_factor + category_dominance_size_factor)
    fig.add_trace(go.Scatter(x=[pos[avs['name']][0]], 
                             y=[pos[avs['name']][1]], 
                             mode='markers', 
                             marker=dict(size=initial_avs_size + size_factor + category_dominance_size_factor, color=color), 
                             text=avs['name'], 
                             name=['Decentralized Sequencer AVS', 'Oracle AVS', 'Data Availability AVS'][category]))



# Add edges
edge_trace = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_trace.append(go.Scatter(x=[x0, x1], y=[y0, y1], mode='lines', line=dict(color='gray', width=1), 
                             hoverinfo='none', showlegend=False))

# Ensure lines do not overlap
line_positions = {}
for i, trace in enumerate(edge_trace):
    x0, y0 = trace['x'][0], trace['y'][0]
    x1, y1 = trace['x'][1], trace['y'][1]
    if (x0, y0) not in line_positions or (x1, y1) not in line_positions:
        line_positions[(x0, y0)] = i
        line_positions[(x1, y1)] = i
        fig.add_trace(trace)

# Add arrow pointers
for edge, trace in zip(G.edges(), edge_trace):
    x0, y0 = trace['x'][0], trace['y'][0]
    x1, y1 = trace['x'][1], trace['y'][1]
    fig.add_annotation(x=x1, y=y1,
                       ax=x0, ay=y0,
                       xref='x', yref='y',
                       axref='x', ayref='y',
                       showarrow=True,
                       arrowhead=3,
                       arrowsize=2,
                       arrowwidth=1,
                       arrowcolor='gray')

# Update layout
fig.update_layout(showlegend=True, 
                  legend=dict(x=1, y=1, font=dict(size=12), itemsizing='constant'), 
                  width=1200, height=800)

# Display the plot using Streamlit
st.plotly_chart(fig, use_container_width=True)

st.write("\n")
