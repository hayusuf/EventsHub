"""Python API for react functions."""
import flask
import os
import openai
import json


app = flask.Flask(__name__)


@app.route('/api/question/')
def get_answer():
    """Return answer to question."""
    with open("ai_input.json", 'r') as f:
        data = json.load(f)
    interests = "sports"
    response = openai.ChatCompletion.create(
        engine='gpt-4',
        messages=[
            {"role": "system", "content": "Learn which events are happening by reading my \
             next message so that you can best help the student find events based off of \
             his inputted interests."},
            {"role": "system", "content": "sports"},
            {"role": "user", "content": f"Based off my interests, including {interests}, what event should I attend?"}

        ]
    )

    # print the response
    print(response['choices'][0]['message']['content'])
    answer = response['choices'][0]['message']['content']
    context = {
        "answer": answer
    }

    return flask.jsonify(**context)
