from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
from openai import OpenAI

# openai.api_key = "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"


# client = OpenAI(
#   api_key=""  # this is also the default, it can be omitted
# )



app = Flask(__name__)
app.config["MONGO_URI"] = process.env.MONGO_URI
mongo = PyMongo(app)

@app.route("/")
def home():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template("index.html", myChats = myChats)

@app.route("/api", methods=["GET", "POST"])
def qa():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question": question})
        print(chat)
        if chat:
            data = {"question": question, "answer": f"{chat['answer']}"}
            return jsonify(data)
        else:
            client = OpenAI(api_key = process.env.OPEN_API_KEY)
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Answer the questions"},
                    {"role": "user", "content": question}
                ]
            )

            response = completion.choices[0].message.content

            print(response)
            data = {"question": question, "answer": response}
            mongo.db.chats.insert_one({"question": question, "answer": response})
            return jsonify(data)
    data = {"result": "Thank you! I'm just a machine learning model designed to respond to questions and generate text based on my training data. Is there anything specific you'd like to ask or discuss? "}
    return jsonify(data)

app.run(debug=True)
