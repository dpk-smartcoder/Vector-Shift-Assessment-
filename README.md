# 🚀 VectorShift Pipeline Builder

<div align="center">

![Pipeline Builder](https://img.shields.io/badge/Pipeline-Builder-purple?style=for-the-badge)
![React](https://img.shields.io/badge/React-18.2-blue?style=for-the-badge&logo=react)
![FastAPI](https://img.shields.io/badge/FastAPI-0.128-green?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)

**A visual drag-and-drop pipeline builder with DAG (Directed Acyclic Graph) validation**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [API](#-api-documentation) • [Examples](#-examples)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [API Documentation](#-api-documentation)
- [Examples](#-examples)

---

## 🎯 Overview

**VectorShift Pipeline Builder** is an intuitive web application that allows you to build data processing pipelines using a visual drag-and-drop interface. The application validates whether your pipeline forms a valid Directed Acyclic Graph (DAG), ensuring no circular dependencies exist in your workflow.

### Key Highlights

✨ **Visual Pipeline Editor** - Drag and drop nodes to create complex workflows  
🔍 **DAG Validation** - Automatic detection of cycles and graph validation  
🎨 **Modern UI** - Clean, responsive interface built with React Flow  
⚡ **Fast Backend** - High-performance API built with FastAPI  
🔗 **Flexible Connections** - Connect nodes dynamically with visual handles  

---

## ✨ Features

### 🎨 Visual Pipeline Builder
- **Drag-and-Drop Interface** - Intuitive node placement on canvas
- **Dynamic Node Connections** - Visual handles for easy linking
- **Real-time Validation** - Instant feedback on pipeline structure
- **Zoom & Pan Controls** - Navigate large pipelines effortlessly

### 📦 Available Node Types
- **Input** - Text or File input nodes
- **Output** - Text or Image output nodes
- **Text** - Text processing with variable substitution (`[[variables]]`)
- **LLM** - Large Language Model integration
- **Condition** - Conditional logic branching
- **Transform** - Data transformation operations
- **Merge** - Combine multiple data streams
- **Filter** - Filter data based on conditions
- **Calculator** - Mathematical operations

### 🔍 DAG Analysis
- **Cycle Detection** - Identifies circular dependencies
- **Topological Sort** - Uses Kahn's algorithm for validation
- **Graph Statistics** - Node and edge count analysis
- **Visual Feedback** - Clear indication of DAG status

---

## 🛠 Tech Stack

### Frontend
- **React 18.2** - Modern UI framework
- **React Flow 11.8** - Interactive node-based editor
- **Zustand 4.4** - State management
- **React Scripts** - Build tooling

### Backend
- **FastAPI 0.128** - High-performance web framework
- **Python 3.x** - Backend runtime
- **Pydantic 2.10+** - Data validation
- **Uvicorn** - ASGI server

---

## 📦 Installation

### Prerequisites
- **Node.js** (v14 or higher)
- **Python** (v3.8 or higher)
- **npm** or **yarn**

### Step 1: Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/VectorShift.git
cd VectorShift
```

### Step 2: Backend Setup

```bash
# Navigate to backend directory
cd backend-20251230T061211Z-3-001/backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Frontend Setup

```bash
# Navigate to frontend directory (from project root)
cd frontend-20251230T061214Z-3-001/frontend

# Install dependencies
npm install
```

---

## 🚀 Usage

### Starting the Backend Server

```bash
# From backend directory
cd backend-20251230T061211Z-3-001/backend

# Activate virtual environment (if not already activated)
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux

# Start the server
uvicorn main:app --reload
```

The backend will be available at `http://localhost:8000`

### Starting the Frontend Development Server

```bash
# From frontend directory
cd frontend-20251230T061214Z-3-001/frontend

# Start the development server
npm start
```

The frontend will be available at `http://localhost:3000`

### Building a Pipeline

1. **Drag Nodes** - Select nodes from the toolbar and drag them onto the canvas
2. **Configure Nodes** - Click on nodes to configure their properties
3. **Connect Nodes** - Click and drag from output handles to input handles
4. **Submit Pipeline** - Click "Submit Pipeline" to validate your DAG
5. **View Results** - Check the analysis results (nodes, edges, DAG status)

---

## 📁 Project Structure

```
VectorShift/
├── backend-20251230T061211Z-3-001/
│   └── backend/
│       ├── main.py              # FastAPI backend with DAG validation
│       ├── requirements.txt    # Python dependencies
│       └── venv/                # Virtual environment
│
├── frontend-20251230T061214Z-3-001/
│   └── frontend/
│       ├── src/
│       │   ├── App.js           # Main application component
│       │   ├── ui.js            # Pipeline canvas UI
│       │   ├── toolbar.js      # Node toolbar
│       │   ├── submit.js       # Pipeline submission handler
│       │   ├── store.js         # Zustand state management
│       │   └── nodes/           # Node components
│       │       ├── inputNode.js
│       │       ├── outputNode.js
│       │       ├── textNode.js
│       │       ├── llmNode.js
│       │       └── ...
│       ├── package.json         # Frontend dependencies
│       └── public/              # Static assets
│
└── PIPELINE_EXAMPLES.md         # Example pipelines guide
```

---

## 📡 API Documentation

### Endpoints

#### `GET /`
Health check endpoint.

**Response:**
```json
{
  "Ping": "Pong"
}
```

#### `POST /pipelines/parse`
Analyze a pipeline and determine if it's a valid DAG.

**Request Body:**
```json
{
  "nodes": [
    {
      "id": "customInput-1",
      "type": "customInput",
      "position": { "x": 100, "y": 100 },
      "data": { "inputName": "input_1", "inputType": "Text" }
    }
  ],
  "edges": [
    {
      "id": "edge-1",
      "source": "customInput-1",
      "target": "text-1",
      "sourceHandle": "customInput-1-value",
      "targetHandle": "text-1-input"
    }
  ]
}
```

**Response:**
```json
{
  "num_nodes": 4,
  "num_edge": 3,
  "is_dag": true
}
```

**Response Fields:**
- `num_nodes` - Total number of nodes in the pipeline
- `num_edge` - Total number of edges (connections) in the pipeline
- `is_dag` - Boolean indicating if the pipeline is a valid DAG

### DAG Validation Algorithm

The backend uses **Kahn's Algorithm** (topological sort) to detect cycles:
1. Build adjacency list and calculate in-degrees
2. Process nodes with zero in-degree
3. If all nodes are processed → DAG (no cycles)
4. If nodes remain → Cycle detected (not a DAG)

---

## 📚 Examples

### Example 1: Simple Linear Pipeline (DAG: Yes ✅)

```
[Input] ──► [Text] ──► [LLM] ──► [Output]
```

**Result:**
- Nodes: 4
- Edges: 3
- Is DAG: Yes ✓

### Example 2: Pipeline with Cycle (DAG: No ❌)

```
[Text] ──► [LLM]
  ▲          │
  │          │
  └──────────┘
```

**Result:**
- Nodes: 2
- Edges: 2
- Is DAG: No ✗

For detailed examples and step-by-step instructions, see [PIPELINE_EXAMPLES.md](./PIPELINE_EXAMPLES.md)

---

## 🎨 Screenshots

### Pipeline Builder Interface
```
┌─────────────────────────────────────────────────────────┐
│  VectorShift Pipeline Builder                          │
│  Drag nodes from the toolbar to build your pipeline    │
├─────────────────────────────────────────────────────────┤
│  Available Nodes:                                       │
│  [Input] [LLM] [Output] [Text] [Condition] ...        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│     ┌─────┐     ┌─────┐     ┌─────┐     ┌─────┐      │
│     │Input│────►│Text │────►│ LLM │────►│Output│      │
│     └─────┘     └─────┘     └─────┘     └─────┘      │
│                                                         │
│                    [Canvas Area]                        │
│                                                         │
├─────────────────────────────────────────────────────────┤
│              [Submit Pipeline]                          │
└─────────────────────────────────────────────────────────┘
```

---

<div align="center">

**Made with ❤️ using React and FastAPI**

⭐ Star this repo if you find it helpful!

</div>

