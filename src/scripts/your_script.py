"""Main script for your project.

Usage:
    python src/scripts/your_script.py <config_key>=<config_value> ...
"""

#import hydra
import requests
#from omegaconf import DictConfig

from greynir_client.client import example_function
from greynir_client.datamodel import TranslationRequestData, LANGS, TranslationResponseData


#@hydra.main(config_path="../../config", config_name="config", version_base=None)
def main() -> None:
    """Main function for your project.

    Args:
        config: The Hydra config for your project.
    """
    with open("apikey.txt", "r") as f:
        apikey = f.read().strip()

    header = {
        "X-API-Key": apikey,
        "Content-Type": "application/json",
        "accept": "application/json",
    }
    contents = [
            'Where is the museum? I want to buy bread and milk. I should buy a boat.',
            'This fundamental plant growth research is also a key example of how Nasa is working to unlock agricultural innovations that could help us understand how plants might overcome stressful conditions in food-scarce areas here on Earth.',
    ]
    translation_request = TranslationRequestData(
        contents=contents,
        sourceLanguageCode=LANGS.en,
        targetLanguageCode=LANGS.is_,
        model="mbart-multi-doc",
        domain=None,
    )

    response = requests.post(
        url="https://api.greynir.is/translate/",
        data=translation_request.model_dump_json(),
        headers=header,
    )
    if response.status_code == 200:
        translation_response = TranslationResponseData.model_validate_json(response.content)
        print(translation_response)
    else:
        raise RuntimeError("Request returned status code %d, content: %s" % (response.status_code, response.text))





if __name__ == "__main__":
    main()
