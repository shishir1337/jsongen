from flask import Flask, request, jsonify
import openai
import json

openai.api_key = "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"
model_engine = "text-davinci-003"

app = Flask(__name__)

@app.route('/generate-json', methods=['POST'])
def generate_json():
    user_input = request.json['user_input']
    properties = user_input.split(',')
    num_objects = request.json.get('num_objects', 3)  # default to 3 if not specified

    # Generate the prompt string with the user-specified properties and number of objects
    property_list = ', '.join(f'"{p.strip()}": ""' for p in properties)
    chatbot_prompt = f"""
    Generate {num_objects} random JSON data for the following properties: {property_list}. 
    Each JSON data should contain an array of objects, where each object has the specified properties with random values. 
    The number of objects in each array should be {num_objects}. The values for each property should be random. 
    The JSON data should be valid.
    """

    # Generate the response from OpenAI
    response = openai.Completion.create(
        engine=model_engine, prompt=chatbot_prompt, max_tokens=2048, n=1, stop=None, temperature=0.5)
    response_text = response["choices"][0]["text"]

    # Extract the JSON data from the response text
    json_data = None
    try:
        json_start = response_text.index('{')
        json_end = response_text.rindex('}') + 1
        json_data = json.loads(response_text[json_start:json_end])
    except ValueError:
        pass

    if json_data is not None:
        return jsonify(json_data)
    else:
        return jsonify(json.loads(response_text.replace('\n', '')))

if __name__ == '__main__':
    app.run(debug=True)
