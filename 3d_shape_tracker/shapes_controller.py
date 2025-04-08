'''
import numpy as np
import open3d as o3d

class ShapesController:
    def __init__(self):
        # Initialize cube
        self.cube = {
            'mesh': o3d.geometry.TriangleMesh.create_box(width=1.0, height=1.0, depth=1.0),
            'position': np.array([0.0, 0.0, 0.0]),
            'move_step': 0.5,
            'color': [0.5, 0.5, 0.8]  # Light blue
        }
        self.cube['mesh'].compute_vertex_normals()
        self.cube['mesh'].paint_uniform_color(self.cube['color'])
        
        # Initialize cone
        self.cone = {
            'mesh': o3d.geometry.TriangleMesh.create_cone(radius=0.5, height=1.0),
            'position': np.array([2.0, 0.0, 0.0]),  # Start 2 units to the right of cube
            'move_step': 0.5,
            'color': [0.8, 0.5, 0.5]  # Light red
        }
        self.cone['mesh'].compute_vertex_normals()
        self.cone['mesh'].paint_uniform_color(self.cone['color'])
        
    def move_shape(self, shape, direction):
        if shape == 'cube':
            target = self.cube
        else:
            target = self.cone
            
        if direction == 'left':
            target['position'][0] -= target['move_step']
            target['mesh'].translate(np.array([-target['move_step'], 0, 0]))
        elif direction == 'right':
            target['position'][0] += target['move_step']
            target['mesh'].translate(np.array([target['move_step'], 0, 0]))
        elif direction == 'up':
            target['position'][1] += target['move_step']
            target['mesh'].translate(np.array([0, target['move_step'], 0]))
        elif direction == 'down':
            target['position'][1] -= target['move_step']
            target['mesh'].translate(np.array([0, -target['move_step'], 0]))
        elif direction == 'forward':
            target['position'][2] += target['move_step']
            target['mesh'].translate(np.array([0, 0, target['move_step']]))
        elif direction == 'backward':
            target['position'][2] -= target['move_step']
            target['mesh'].translate(np.array([0, 0, -target['move_step']]))
            
        return {
            'x': float(target['position'][0]),
            'y': float(target['position'][1]),
            'z': float(target['position'][2])
        } '''


import numpy as np
import open3d as o3d

class ShapesController:
    def __init__(self):
        # Initialize cube
        self.cube = {
            'mesh': o3d.geometry.TriangleMesh.create_box(width=1.0, height=1.0, depth=1.0),
            'position': np.array([0.0, 0.0, 0.0]),
            'move_step': 5.0,  # Larger step to reach checkpoints faster
            'color': [0.5, 0.5, 0.8]  # Light blue
        }
        self.cube['mesh'].compute_vertex_normals()
        self.cube['mesh'].paint_uniform_color(self.cube['color'])
        
        # Initialize cone
        self.cone = {
            'mesh': o3d.geometry.TriangleMesh.create_cone(radius=0.5, height=1.0),
            'position': np.array([2.0, 0.0, 0.0]),
            'move_step': 5.0,  # Larger step to reach checkpoints faster
            'color': [0.8, 0.5, 0.5]  # Light red
        }
        self.cone['mesh'].compute_vertex_normals()
        self.cone['mesh'].paint_uniform_color(self.cone['color'])
        
    def move_shape(self, shape, direction):
        target = self.cube if shape == 'cube' else self.cone
            
        if direction == 'left':
            target['position'][0] -= target['move_step']
            target['mesh'].translate(np.array([-target['move_step'], 0, 0]))
        elif direction == 'right':
            target['position'][0] += target['move_step']
            target['mesh'].translate(np.array([target['move_step'], 0, 0]))
        elif direction == 'up':
            target['position'][1] += target['move_step']
            target['mesh'].translate(np.array([0, target['move_step'], 0]))
        elif direction == 'down':
            target['position'][1] -= target['move_step']
            target['mesh'].translate(np.array([0, -target['move_step'], 0]))
        elif direction == 'forward':
            target['position'][2] += target['move_step']
            target['mesh'].translate(np.array([0, 0, target['move_step']]))
        elif direction == 'backward':
            target['position'][2] -= target['move_step']
            target['mesh'].translate(np.array([0, 0, -target['move_step']]))
            
        return {
            'x': float(target['position'][0]),
            'y': float(target['position'][1]),
            'z': float(target['position'][2])
        }