import streamlit as st

# --- Title and Description ---
st.title("Breadth First Search (BFS) and Depth First Search (DFS) Visualization")

st.markdown("""
This prototype demonstrates **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** on the defined graph.

**Instructions:**
1. Select the Starting Node (A-H).
2. Choose the search Algorithm (BFS or DFS).
3. Click **'Run Traversal'** to view the path and the step-by-step log.
""")

# --- Display image ---
st.image("LabReport_BSD2513_#1.jpg", caption="Graph Representation", use_container_width=True)

# --- Graph definition ---
graph = {
    'A': ['B', 'D'],
    'B': ['C', 'G', 'E'],
    'C': ['A'],
    'D': ['C'],
    'E': ['H'],
    'F': [],
    'G': ['F'],
    'H': ['G','F']
}

# --- BFS ---
def bfs(graph, start):
    visited, queue = [start], [start]
    order = []

    while queue:
        node = queue.pop(0)
        order.append(node)
        for n in graph[node]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
    return order

# --- DFS ---
def dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited, order = [], []
    visited.append(start)
    order.append(start)
    for n in graph[start]:
        if n not in visited:
            dfs(graph, n, visited, order)
    return order

# --- Streamlit interface ---
start_node = st.selectbox("Select Starting Node:", list(graph.keys()))
algorithm = st.radio("Select Algorithm:", ["BFS", "DFS"])

if st.button("Run Traversal"):
    if algorithm == "BFS":
        st.success("Traversal Order: " + " → ".join(bfs(graph, start_node)))
    else:
        st.info("Traversal Order: " + " → ".join(dfs(graph, start_node)))
