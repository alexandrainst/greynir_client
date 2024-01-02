"""Main script for your project.

Usage:
    python src/scripts/your_script.py <config_key>=<config_value> ...
"""

#import hydra
import requests
#from omegaconf import DictConfig

from greynir_client.client import translate_en_to_is
from greynir_client.datamodel import TranslationRequestData, LANGS, TranslationResponseData


#@hydra.main(config_path="../../config", config_name="config", version_base=None)
def main() -> None:
    """Main function for your project.

    Args:
        config: The Hydra config for your project.
    """
    with open("apikey.txt", "r") as f:
        apikey = f.read().strip()

    contents = [
            'Where is the museum? I want to buy bread and milk. I should buy a boat.',
            'This fundamental plant growth research is also a key example of how Nasa is working to unlock agricultural innovations that could help us understand how plants might overcome stressful conditions in food-scarce areas here on Earth.',
    ]

    translation_response = translate_en_to_is(apikey, contents)
    print(translation_response)





if __name__ == "__main__":
    main()
