from flask import Flask, jsonify, render_template, Response
import json
import os

# Get the base directory (parent of src/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Set template_folder to the correct path
app = Flask(__name__, template_folder=os.path.join(BASE_DIR, 'templates'))

@app.route('/')
def index():
    try:
        # Read servers.json from v0 directory
        file_path = os.path.join(BASE_DIR, 'v0', 'servers.json')
        
        with open(file_path) as f:
            data = json.load(f)

        # Extract the servers array and flatten the structure
        if isinstance(data, dict) and 'servers' in data:
            servers_raw = data['servers']
            servers = []
            for server_entry in servers_raw:
                # Each entry has a 'server' field with the actual server info
                if isinstance(server_entry, dict) and 'server' in server_entry:
                    servers.append(server_entry['server'])
                else:
                    servers.append(server_entry)
        elif isinstance(data, list):
            servers = data
        else:
            servers = [data]

        return render_template('index.html', servers=servers)
    except FileNotFoundError:
        return render_template('index.html', servers=[])
    except json.JSONDecodeError:
        return "Error: Invalid JSON in server configuration file", 500

@app.route('/server/<int:server_id>')
def server_detail(server_id):
    try:
        # Read servers.json from v0 directory
        file_path = os.path.join(BASE_DIR, 'v0', 'servers.json')
        
        with open(file_path) as f:
            data = json.load(f)

        # Extract the servers array and flatten the structure
        if isinstance(data, dict) and 'servers' in data:
            servers_raw = data['servers']
            servers = []
            for server_entry in servers_raw:
                # Each entry has a 'server' field with the actual server info
                if isinstance(server_entry, dict) and 'server' in server_entry:
                    servers.append(server_entry['server'])
                else:
                    servers.append(server_entry)
        elif isinstance(data, list):
            servers = data
        else:
            servers = [data]

        if server_id >= len(servers):
            return "Server not found", 404

        server = servers[server_id]
        server_json = json.dumps(server, indent=2)

        return render_template('detail.html', server=server, server_json=server_json)
    except FileNotFoundError:
        return "Server configuration file not found", 404
    except json.JSONDecodeError:
        return "Error: Invalid JSON in server configuration file", 500

@app.route('/v0/servers')
@app.route('/v0.1/servers')
@app.route('/registry')
def get_registry():
    try:
        # Read servers.json from v0 directory
        file_path = os.path.join(BASE_DIR, 'v0', 'servers.json')
        
        with open(file_path) as f:
            data = json.load(f)
        return Response(json.dumps(data), mimetype='application/json')
    except FileNotFoundError:
        return Response(json.dumps({"error": "Server configuration file not found"}), mimetype='application/json', status=404)

@app.route('/health')
def health_check():
    return "service is running", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)