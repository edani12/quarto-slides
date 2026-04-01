import requests
import os

def query_stepfun_flash(prompt, api_key=None, model="stepfun/step-3.5-flash"):
    """
    Send a prompt to StepFun3.5 Flash via OpenRouter API.
    
    Args:
        prompt (str): The user's prompt/text to send to the model
        api_key (str, optional): OpenRouter API key. If None, will try to get from OPENROUTER_API_KEY env var
        model (str): The model identifier. Default is "stepfun/step-3.5-flash"
    
    Returns:
        dict: The API response as a dictionary, or None if request failed
    """
    if api_key is None:
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("API key must be provided or set in OPENROUTER_API_KEY environment variable")
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/your-username/your-repo",  # Optional but recommended
        "X-Title": "DATASCI 350 Lecture Practice"  # Optional app name
    }
    
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 1000
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling OpenRouter API: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("Please set OPENROUTER_API_KEY environment variable or pass api_key directly")
    else:
        result = query_stepfun_flash("Hello, how are you?", api_key=api_key)
        if result:
            print("Response:", result.get("choices", [{}])[0].get("message", {}).get("content", "No content"))
