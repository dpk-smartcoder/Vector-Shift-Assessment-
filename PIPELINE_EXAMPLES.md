# Pipeline Examples for DAG Testing

## Example 1: DAG: Yes (No Cycles) ✅

This is a simple linear pipeline with no cycles - perfect for testing "DAG: Yes" result.

### Visual Pipeline Structure:

```
    [Input]          [Text]          [LLM]         [Output]
    (Text)        "Graph: [[input]]"              (Text)
      │                │              │              │
      │                │              │              │
      └───────────────►└─────────────►└─────────────►
      
      Flow Direction: Left to Right (No cycles = DAG: Yes)
```

**Node Layout on Canvas:**
```
┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐
│ Input   │────►│  Text   │────►│  LLM    │────►│ Output  │
│         │     │         │     │         │     │         │
│ Name:   │     │ Text:   │     │         │     │ Name:   │
│ graph_  │     │ Graph:  │     │         │     │ result  │
│ input   │     │ [[input]]│     │         │     │         │
│         │     │         │     │         │     │ Type:   │
│ Type:   │     │         │     │         │     │ Text    │
│ Text    │     │         │     │         │     │         │
└─────────┘     └─────────┘     └─────────┘     └─────────┘
```

### Step-by-Step Instructions:

1. **Drag an Input node** onto the canvas
   - Set Name: `graph_input`
   - Set Type: `Text` (from dropdown)

2. **Drag a Text node** onto the canvas (to the right of Input)
   - Set Text content to: `Graph: [[input]]`
   - This creates a connection point for the input

3. **Drag an LLM node** onto the canvas (to the right of Text)
   - No configuration needed

4. **Drag an Output node** onto the canvas (to the right of LLM)
   - Set Name: `result`
   - Set Type: `Text` (from dropdown)

5. **Connect the nodes:**
   - Connect: `Input` → `Text` (connect Input's right handle to Text's left handle)
   - Connect: `Text` → `LLM` (connect Text's right handle to LLM's left "prompt" handle)
   - Connect: `LLM` → `Output` (connect LLM's right handle to Output's left handle)

6. **Submit Pipeline** - You should get: **DAG: Yes ✓**

### Expected Output:
```
Pipeline Analysis Results:

Number of Nodes: 4
Number of Edges: 3
Is DAG: Yes ✓
```

**Breakdown:**
- **Nodes (4)**: Input, Text, LLM, Output
- **Edges (3)**: 
  1. Input → Text
  2. Text → LLM
  3. LLM → Output

---

## Example 2: DAG: No (With Cycle) ❌

This pipeline has a cycle, which makes it NOT a DAG - perfect for testing "DAG: No" result.

### 🎯 SIMPLEST WAY TO CREATE A CYCLE (2 Nodes Only):

**Super Simple Example - Just 2 Nodes:**

```
    [Text]          [LLM]
  "[[data]]"        
      │              │
      │              │
      └─────────────►
      ▲              │
      │              │
      └──────────────┘
      
      Cycle: Text → LLM → Text
```

**Step-by-Step (Easiest Method):**

1. **Drag a Text node** onto the canvas
   - Set Text content to: `[[data]]`
   - This creates ONE input handle on the left side (for `data`)

2. **Drag an LLM node** onto the canvas (to the right of Text)
   - No configuration needed
   - LLM has 2 input handles on the left (system at top, prompt at bottom)

3. **Create the forward connection:**
   - Click and drag from Text node's RIGHT handle (output) 
   - Connect it to LLM node's LEFT handle (use the BOTTOM one - "prompt")
   - You should see a line connecting Text → LLM

4. **Create the cycle (backward connection):**
   - Click and drag from LLM node's RIGHT handle (output)
   - Connect it BACK to Text node's LEFT handle (the `[[data]]` handle)
   - You should see a line connecting LLM → Text
   - **This creates the cycle!** 🔄

5. **Submit Pipeline** - You should get: **DAG: No ✗**

**Expected Output:**
```
Pipeline Analysis Results:

Number of Nodes: 2
Number of Edges: 2
Is DAG: No ✗
```