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

