import os
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

def initialize_model():
    """Initialize IBM Watson AI model with credentials and parameters."""
    credentials = Credentials(
        url=os.getenv('WX_URL'),
        api_key=os.getenv('WX_KEY'),
    )
    parameters = {
        GenParams.DECODING_METHOD: "greedy",
        GenParams.MAX_NEW_TOKENS: 900,
    }
    return ModelInference(
        model_id='mistralai/mistral-large',
        params=parameters,
        credentials=credentials,
        project_id=os.getenv('WX_PID'),
    )

def generate_response(model, prompt):
    """Generate troubleshooting response based on speech input."""
    response = model.generate_text(prompt=prompt, guardrails=False)
    return response
