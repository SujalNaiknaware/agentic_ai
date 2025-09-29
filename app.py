from flask import Flask, request, render_template
from customer_ai import run_customer_support

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    error = None
    if request.method == "POST":
        query = request.form.get("query")
        try:
            result = run_customer_support(query)
            response = result["response"]   # ✅ only return response
        except Exception as e:
            error = f"Error: {str(e)}"
    return render_template("index.html", response=response, error=error)

if __name__ == "__main__":
    app.run(debug=True)
