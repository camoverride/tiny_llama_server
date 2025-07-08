from flask import Flask, request
from flask_restful import Resource, Api
from transformers import AutoTokenizer, pipeline
import torch
import yaml



# Load config file
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)


# Load model and tokenizer
model_path = config["model_path"]
tokenizer = AutoTokenizer.from_pretrained(model_path)
generator = pipeline(
    "text-generation",
    model=model_path,
    torch_dtype=torch.float16,
    device_map="auto",
)

# Create Flask app and API
app = Flask(__name__)
api = Api(app)

class Reply(Resource):
    def post(self):
        # Extract the prompt.
        prompt = request.json.get("prompt", "")

        # 404 if no prompt.
        if not prompt:
            return {"error": "Missing prompt"}, 400

        # LLM arguments
        result = generator(
            prompt,
            do_sample=True,
            top_k=50,
            top_p=0.7,
            eos_token_id=tokenizer.eos_token_id,
            num_return_sequences=1,
            repetition_penalty=1.1,
            max_new_tokens=25,
        )

        # Return the response
        reply = result[0]["generated_text"].split("Assistant:")[-1].strip()
        return {"reply": reply}


# Register endpoint
api.add_resource(Reply, "/generate")



if __name__ == "__main__":

    app.run(debug=True)
