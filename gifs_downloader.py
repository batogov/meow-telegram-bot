import json
import uuid
from urllib import request

from tokens import GIPHY_TOKEN


def generate_name():
    return str(uuid.uuid1().hex)[:10]


query_base = 'http://api.giphy.com/v1/gifs/search?'


tag = 'cat'
limit = 25
offset = 0

folder = 'gifs'


for i in range(20):
    query = query_base + '&'.join(['q=' + tag,
                                   'limit=' + str(limit),
                                   'offset=' + str(offset),
                                   'api_key=' + GIPHY_TOKEN])

    r = request.urlopen(query)
    data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))

    links = []
    for each_gif_data in data['data']:
        links.append(each_gif_data['images']['downsized_large']['url'])

    for link in links:
        gif_file = open(folder + '/' + generate_name() + '.gif', 'wb')
        gif_file.write(request.urlopen(link).read())
        gif_file.close()

    offset += limit

    print('{} GIFs were downloaded with tag "{}".'.format(str(limit), tag), end=' ')
    print('Next offset will be {}.'.format(str(offset)))
