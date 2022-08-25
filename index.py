import meilisearch


def index():
    client = meilisearch.Client("http://localhost:7700", "MASTER_KEY")
    index = client.index("catalogs")
    docs = []
    with open("catalog.txt", mode="rt", encoding="utf-8-sig") as stream:
        for i, line in enumerate(stream, start=1):
            items = line.split("|")
            if len(items) != 2:
                continue
            data = {'id': i, 'guid': items[0], 'description': items[1]}
            docs.append(data)
    index.add_documents(docs)
    index.search


if __name__ == '__main__':
    index()