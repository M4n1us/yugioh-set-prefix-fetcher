import httpx
import asyncio

from config.config_handler import config


async def handle_language(language, type):
    running = True
    request = config.api() + (config.request().replace("___LANG___", language))
    offset = 0
    entries = {}
    while running:
        print("Processing: language=%s, offset=%i" % (language, offset))
        response = await httpx.AsyncClient().get(request.replace("___OFFSET___", str(offset)), timeout=100)
        response = response.json()
        if 'query-continue-offset' not in response.keys():
            running = False
        else:
            offset = response['query-continue-offset']
        entries.update(handle_results(response["query"]["results"], language, type))
    return entries


def handle_results(results, language, type):
    ret = {}
    for element in results:
        set_data = element.popitem()[1]
        data = set_data["printouts"]["Prefix"][0]
        if isinstance(data, str):
            ret[data] = {"lang": language, "type": type}
    return ret


async def main():
    requests = []

    for element in config.languages():
        requests.append(handle_language(element["lang"], element["type"]))

    test = await asyncio.gather(*requests)
    return test

if __name__ == '__main__':
    test = asyncio.run(main())
    print(len(test))
    print(test)
    concat = {}
    for el in test:
        concat.update(el)

    print(len(concat))
    print(concat)
