def generate_prompt(speech_text):
    """Create a troubleshooting prompt based on the customer's speech input."""
    if not speech_text:
        return "No valid input detected. Please try again."

    return f"""
    You are an AI assistant specializing in WiFi troubleshooting. A customer has described their WiFi issues in the following speech:
    {speech_text}

    Your task is to provide clear, concise, and actionable steps to resolve the customer's problem. Focus entirely on solutions and tailor your recommendations to the specific issue described by the customer. Do not include any analysis or explanations—respond only with practical steps to address the issue.

    Format your response as follows:

    Solutions:
    1. [Step 1]
    2. [Step 2]
    3. [Step 3]

    Recommendations:
    - [Specific advice for the customer based on their issue]

    Provide feedback in a way that is easy for the customer to follow and implement immediately.
    """
