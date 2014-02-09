from app import app

myIp = "0.0.0.0"
#myIp = "10.0.0.122"

if __name__ == "__main__":
  app.run(host=myIp,debug=True)
