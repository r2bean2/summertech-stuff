from flask import Flask, request  # Make sure to import request

app = Flask(__name__)

# Add methods=['POST'] so it can accept data
@app.route("/", methods=['POST'])
def hello_world():
    # Capture the dictionary sent by the client
    data = request.json
    print(f"Received data: {data}")
    
    # Return a message back to the client
    return "Data received by Hello World!"

if __name__ == '__main__':
    app.run(debug=True)