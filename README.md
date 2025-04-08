# 3D Shapes Visualization with Checkpoints
A real-time 3D visualization system that tracks the positions of a cube and cone as they move from the origin to their respective checkpoints (CK1 and CK2). Includes a web-based dashboard with interactive 2D graph visualization.

## Features
- **Dual Shape Visualization**: Track both cube and cone simultaneously
- **Checkpoint System**: 
  - Cube target: CK1 at (100, 50, 0)
  - Cone target: CK2 at (100, 0, 0)
- **Real-time Tracking**: Web dashboard updates positions instantly
- **Interactive Controls**:
  - Cube: WASD-QE keys
  - Cone: Arrow keys + TAB/SHIFT
- **Visual Feedback**:
  - Color-coded shapes and checkpoints
  - Dashed guideline to checkpoints
  - Position coordinates display
- **Notification System**: Alerts when shapes reach checkpoints

## System Architecture
3d_shapes_project/
├── static/ # Static files
├── templates/
│ └── index.html # Web dashboard
├── cube_app.py # 3D visualizer application
├── shapes_controller.py # Shapes movement logic
├── server.py # Flask/SocketIO server
├── requirements.txt # Python dependencies
└── README.md # This file
