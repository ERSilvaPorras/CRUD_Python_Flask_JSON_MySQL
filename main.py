from src.app import app
 
PORT = 5000
HOST = 'localhost'
DEBUG= True
 
if __name__ == "__main__":
    app.run(HOST, PORT, DEBUG)