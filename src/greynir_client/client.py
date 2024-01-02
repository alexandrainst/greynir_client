"""An example module for your project."""

import logging
import requests

from .datamodel import TranslationRequestData, LANGS, TranslationResponseData

logger = logging.getLogger(__name__)


def translate_en_to_is(apikey: str, contents: list[str]) -> TranslationResponseData:
    """Translate a list of strings from English to Icelandic.
    """

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
        return translation_response
    else:
        raise RuntimeError("Request returned status code %d, content: %s" % (response.status_code, response.text))

