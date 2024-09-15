import json
import argparse
from chatgpt import ChatGPTBot
from gemini import GeminiBot
from huggingface import HuggingFaceBot

# Function to load the appropriate bot based on API type
def load_bot(api_type, token, model_name):
    if api_type.lower() == "chatgpt":
        return ChatGPTBot(token, model_name)
    elif api_type.lower() == "gemini":
        return GeminiBot(token, model_name)
    elif api_type.lower() == "hf":
        return HuggingFaceBot(token, model_name)
    else:
        raise ValueError("Unsupported API type! Use one of: 'chatgpt', 'gemini', 'hf'.")

# Main program
def main():
    # Argument parser to handle input
    parser = argparse.ArgumentParser(description="Run AI bot based on API type")
    parser.add_argument("--token", required=True, help="API token")
    parser.add_argument("--model", required=True, help="Model name")
    parser.add_argument("--api_type", required=True, choices=["chatgpt", "gemini", "hf"], help="API type (chatgpt, gemini, hf)")
    parser.add_argument("--file", required=True, help="Output JSON file name", default=None)
    parser.add_argument("--text", required=True, help="Text input for the model", default=None)
    parser.add_argument("--output_file", required=True, help="Text input for the model", default='./bot_output.json')
    
    args = parser.parse_args()

    # Load the bot based on API type
    bot = load_bot(args.api_type, args.token, args.model)

    if args.text is not None:
        print(bot.generate(args.text))
    elif args.file is not None:
        with open(args.file, 'r') as json_file:
            data = json.load(json_file)

        output_data = {
            "query": data['query'],
            "response": bot.generate(data['query'])
        }

        if args.output_file is not None:
            with open(args.output_file, 'w') as json_file:
                json.dump(output_data, json_file, indent=4)

            print(f"Response saved to {args.file}")

if __name__ == "__main__":
    main()
