from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional
from collections import defaultdict, deque

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Node(BaseModel):
    id: str
    type: str
    position: Dict
    data: Optional[Dict] = None

class Edge(BaseModel):
    id: Optional[str] = None
    source: str
    target: str
    sourceHandle: Optional[str] = None
    targetHandle: Optional[str] = None

class PipelineRequest(BaseModel):
    nodes: List[Node]
    edges: List[Edge]

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

def is_dag(nodes: List[Node], edges: List[Edge]) -> bool:
    """
    Check if the graph formed by nodes and edges is a Directed Acyclic Graph (DAG).
    Uses topological sort (Kahn's algorithm) to detect cycles.
    """
    if not nodes or not edges:
        return True
    
    # Build adjacency list and in-degree count
    node_ids = {node.id for node in nodes}
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Initialize in-degree for all nodes
    for node in nodes:
        in_degree[node.id] = 0
    
    # Build graph from edges
    for edge in edges:
        source = edge.source
        target = edge.target
        
        # Only consider edges where both nodes exist
        if source in node_ids and target in node_ids:
            graph[source].append(target)
            in_degree[target] += 1
    
    # Kahn's algorithm for topological sort
    queue = deque([node_id for node_id in node_ids if in_degree[node_id] == 0])
    processed = 0
    
    while queue:
        current = queue.popleft()
        processed += 1
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If we processed all nodes, it's a DAG (no cycles)
    # If there are remaining nodes with in-degree > 0, there's a cycle
    return processed == len(node_ids)

@app.post('/pipelines/parse')
def parse_pipeline(pipeline: PipelineRequest):
    nodes = pipeline.nodes
    edges = pipeline.edges
    
    num_nodes = len(nodes)
    num_edges = len(edges)
    is_dag_result = is_dag(nodes, edges)
    
    return {
        'num_nodes': num_nodes,
        'num_edge': num_edges,
        'is_dag': is_dag_result
    }
