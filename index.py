from flask import Flask

app         = Flask(__name__, template_folder='.')
myIp        = "10.0.0.122"

if __name__ == "__main__":
  app.run(host=myIp, debug=True)
