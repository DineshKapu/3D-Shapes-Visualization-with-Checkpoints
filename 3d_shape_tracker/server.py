'''from flask import Flask, render_template
from flask_socketio import SocketIO
import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
socketio = SocketIO(app, async_mode='eventlet', cors_allowed_origins="*", logger=True, engineio_logger=True)

# Store latest positions and checkpoint status
latest_positions = {
    'cube': {
        'x': 0, 
        'y': 0, 
        'z': 0,
        'at_checkpoint': False
    },
    'cone': {
        'x': 2, 
        'y': 0, 
        'z': 0,
        'at_checkpoint': False
    }
}

# Checkpoint positions
checkpoints = {
    'cube': {'x': 5.0, 'y': 0.0, 'z': 0.0},
    'cone': {'x': 10.0, 'y': 0.0, 'z': 0.0}
}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/')
def handle_connect():
    print('Client connected')
    # Send initial positions for both shapes
    for shape in ['cube', 'cone']:
        socketio.emit('position_update', {
            'shape': shape,
            'x': latest_positions[shape]['x'],
            'y': latest_positions[shape]['y'],
            'z': latest_positions[shape]['z'],
            'atCheckpoint': latest_positions[shape]['at_checkpoint']
        }, namespace='/')

@socketio.on('update_position', namespace='/')
def handle_position_update(data):
    global latest_positions
    shape = data['shape']
    
    # Update position
    latest_positions[shape]['x'] = data['x']
    latest_positions[shape]['y'] = data['y']
    latest_positions[shape]['z'] = data['z']
    
    # Check if shape reached checkpoint
    checkpoint = checkpoints[shape]
    threshold = 0.5  # Allowed distance to consider checkpoint reached
    
    distance = ((data['x'] - checkpoint['x'])**2 + 
               (data['y'] - checkpoint['y'])**2 + 
               (data['z'] - checkpoint['z'])**2)**0.5
    
    latest_positions[shape]['at_checkpoint'] = distance <= threshold
    
    # Emit position update
    socketio.emit('position_update', {
        'shape': shape,
        'x': data['x'],
        'y': data['y'],
        'z': data['z'],
        'atCheckpoint': latest_positions[shape]['at_checkpoint']
    }, namespace='/', broadcast=True)

@socketio.on('checkpoint_reached', namespace='/')
def handle_checkpoint_reached(data):
    # Broadcast checkpoint reached notification to all clients
    socketio.emit('checkpoint_reached', data, namespace='/', broadcast=True)

if __name__ == '__main__':
    print("Server running at: http://localhost:5000")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)'''


from flask import Flask, render_template
from flask_socketio import SocketIO
import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
socketio = SocketIO(app, async_mode='eventlet', cors_allowed_origins="*", logger=True, engineio_logger=True)

# Checkpoint positions (matches the image)
checkpoints = {
    'cube': {'x': 100, 'y': 50, 'z': 0, 'label': 'CK1'},
    'cone': {'x': 100, 'y': 0, 'z': 0, 'label': 'CK2'}
}

# Store latest positions
latest_positions = {
    'cube': {'x': 0, 'y': 0, 'z': 0, 'at_checkpoint': False},
    'cone': {'x': 2, 'y': 0, 'z': 0, 'at_checkpoint': False}
}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    # Send initial positions
    for shape in ['cube', 'cone']:
        socketio.emit('position_update', {
            'shape': shape,
            'x': latest_positions[shape]['x'],
            'y': latest_positions[shape]['y'],
            'z': latest_positions[shape]['z'],
            'atCheckpoint': latest_positions[shape]['at_checkpoint']
        })

@socketio.on('update_position')
def handle_position_update(data):
    shape = data['shape']
    
    # Update position
    latest_positions[shape]['x'] = data['x']
    latest_positions[shape]['y'] = data['y']
    latest_positions[shape]['z'] = data['z']
    
    # Check checkpoint status
    checkpoint = checkpoints[shape]
    threshold = 5  # Matching the client-side threshold
    
    distance = ((data['x'] - checkpoint['x'])**2 + 
               (data['y'] - checkpoint['y'])**2 + 
               (data['z'] - checkpoint['z'])**2)**0.5
    
    latest_positions[shape]['at_checkpoint'] = distance <= threshold
    
    # Broadcast update
    socketio.emit('position_update', {
        'shape': shape,
        'x': data['x'],
        'y': data['y'],
        'z': data['z'],
        'atCheckpoint': latest_positions[shape]['at_checkpoint']
    }, broadcast=True)

@socketio.on('checkpoint_reached')
def handle_checkpoint_reached(data):
    # Broadcast notification
    socketio.emit('checkpoint_reached', data, broadcast=True)

if __name__ == '__main__':
    print("Server running at: http://localhost:5000")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)