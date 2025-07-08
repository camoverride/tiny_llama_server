import requests
import yaml



# Load config file
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Prompt provided by the user.
user_prompt = "my childhood in new jersey was happy. I loved the snow."

# Prompt provided by the system, with user prompt inserted.
full_prompt = f"### Human: Write a short 5-7-5 haiku about the following: {user_prompt}. ### Respond with just the poem and nothing else. Remember a haiku is just 3 lines. Assistant:"

# Hit the API endpoint.
response = requests.post(url=config["api_url"],
                         json={"prompt": full_prompt},
                         headers={"Content-Type": "application/json"})

# Check the server's response.
if response.ok:
    print("LLM Reply: ", response.json()["reply"])

else:
    print("Error:", response.status_code, response.text)
