import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.eth_api import ETHApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ETH: ETHApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ETH: ETHApi,
    }
)
