from app import app

myIp    = "0.0.0.0"
myPort  = 5050

if __name__ == "__main__":
  app.run(host=myIp, port=myPort, debug=True)
