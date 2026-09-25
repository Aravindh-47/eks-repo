from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>CICD Demo Application</h1>
    <h2>Jenkins → Docker → ECR → EKS</h2>
    <p>Deployment Successful!</p>
    """

@app.route("/health")
def health():
    return {"status": "UP"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
