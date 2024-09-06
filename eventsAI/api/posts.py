"""REST API for posts."""
import flask
import eventsAI
import os
import openai
import json
from eventsAI.api.helper import check_login

@eventsAI.app.route('/api/question/')
def get_answer():
    prompt = flask.request.args.get("prompt", type=str)


    openai.api_type = "azure"
    openai.api_base = 'https://api.umgpt.umich.edu/azure-openai-api/ptu'
    openai.api_key= "b5dd31fb62e843569434325e2664cd3d"
    openai.api_version="2023-07-01-preview"
    
    # Load previous context
    with open("ai_context.json", 'r') as file:
       context = json.load(file)

    # Use the stored answer as system context
    system_content = f"Use the following data to help the user! {context['answer']}"


    with open("ai_input.json", 'r') as file:
        json_data = json.load(file) 
        pretty_json = json.dumps(json_data[:20], indent=2)
        print(pretty_json)

    # Call OpenAI API
    response = openai.ChatCompletion.create(
        engine="gpt-4",
        messages=[
            {"role": "system", "content": system_content+"Use the following data to help the user!"+pretty_json},
            #{"role": "system", "content": system_content},
            {"role": "user", "content": f"{prompt}"}
        ]
    )

    # Extract answer and update context
    answer = response['choices'][0]['message']['content']
    context = {}
    context["answer"] = answer
    # Save updated context
    with open("ai_context.json", 'w') as file:
        json.dump(context, file)

    # Return the answer
    return flask.jsonify({"answer": answer})