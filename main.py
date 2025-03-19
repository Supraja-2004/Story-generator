from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel('gemini-pro')

def generate(prompt):
    response = model.generate_content(prompt)
    return response.text

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    if request.method == "POST":
        option = request.form.get("option")
        topic = request.form.get("topic")
        additional = request.form.get("additional")
        essay_length = request.form.get("essay_length")
        essay_type = request.form.get("essay_type")

        if option == "Essay Generation":
            prompt = f"""Write an essay on topic '{topic}' with a {essay_length} tone. 
            Here are some additional points regarding this: {additional}. 
            Structure the essay with an introduction, body paragraphs, and a strong conclusion. 
            Ensure clarity, engagement, grammar, and punctuation. 
            Most importantly, provide an essay that is {essay_type} in style."""
            response = generate(prompt)

        elif option == "Text Generation":
            response = generate(topic)

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)

