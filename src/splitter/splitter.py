from quart import Response, Quart

from common.storage import FragmentStorage

EMBEDDER_URLS = os.environ.get('EMBEDDER_URLS', 'http://127.0.0.1:40004').split()
EMBEDDER_CHUNK_SIZE = int(os.environ.get('EMBEDDER_CHUNK_SIZE', '1'))

EMBEDDER_CLIENT = EmbedderClient(EMBEDDER_URLS)

QDRANT_LOCATION = os.environ.get('QDRANT_LOCATION', 'localhost')
QDRANT_HTTP_PORT = int(os.environ.get('QDRANT_HTTP_PORT', '6333'))
QDRANT_GRPC_PORT = int(os.environ.get('QDRANT_GRPC_PORT', '6334'))


class Splitter:


    def __init__(self) -> None:
        self.fragment_storage: FragmentStorage = FragmentStorage(project_id)

    def __split(self):
        with timer(f'Extracted archive for project {self.project_id!r}'):
            self.fragment_storage.save(self.__split(files))

    def __split(self, documents: List[Document]) -> Iterator[Fragment]:
        path = ''
        fragment_count = 0
        try:
            for path, data in documents:

                doc_type_cls = doc_types.detect_by_extension(path)
                if doc_type_cls is None:
                    print(f'Skipping unsupported document {path!r} in project {self.project_id!r}')
                    continue

                for fragment in doc_type_cls().load(path, data):
                    fragment_count += 1
                    yield fragment

                asyncio.sleep(0)

        except KeyboardInterrupt:
            raise
        except Exception:
            print(f'Failed to load file {path!r} in project {self.project_id!r}')
            print_exc()
            raise LoaderException(f'Failed to load file: {path!r}')
        print(f'Loaded {len(documents)} files into {fragment_count} fragments')


class Embedder:

    def __init__(self, project_id: str) -> None:
        self.project_id: str = project_id
        self.fragment_storage: FragmentStorage = FragmentStorage(project_id)
        self.state_storage: EmbeddingProgressStorage = EmbeddingProgressStorage(project_id)

    def embed_all_fragments(self):
        if self.state_storage.exists:
            state: bytes = self.state_storage.load()
        else:
            self.state_storage.touch()
            state: bytes = b''

        batch = []
        for fragment in self.fragment_storage.load():
            if len(batch) < EMBEDDER_CHUNK_SIZE:
                batch.append(fragment)
            else:
                self.embed_batch(batch)

        if batch:
            self.embed_batch(batch)

    def embed_batch(self, batch):
        fragments: List[Fragment] = [Fragment(**fields) for fields in body['fragments']]
        embeddings = await EMBEDDER_MODEL.embed_fragments(fragments)
        response = dict(embeddings=embeddings.tolist())


app = Quart(__name__)


@app.get('/')
async def canary():
    return Response(response='OK', status=200)


@app.post("/download/<string:project_id>")
async def trigger(project_id: str):
    project_id = project_id.lower()
    if not C.RX_GUID.match(project_id):
        return Response(response='Invalid project_id, it must be a GUID', status=400)



@app.post("/embed/query")
async def process_project():
    embedder = Embedder(project_id)
    embedder.embed_all_fragments()

    body: Dict[str, any] = await request.get_json(force=True)
    query = body.get('query', '')

    if not query.strip():
        return Response(response='Empty or missing query', status=400)

    # FIXME: Move this up the call chain to the Project level,
    # this level must receive a ready to use instruction text
    doc_type_cls: Type = None
    if query.startswith('.') and ' ' in query:
        ext, query = query.split(' ', 1)
        doc_type_cls = doc_types.detect_by_extension(ext.lower())

    embeddings = await EMBEDDER_MODEL.embed_query(query, doc_type_cls)
    response = dict(embedding=embeddings[0].tolist())

    return Response(response=json.dumps(response), status=200)


def run():
    app.run(debug=True, host="localhost", port=PORT)


async def run_task():
    await app.run_task(debug=True, host="localhost", port=PORT)


if __name__ == "__main__":
    run()
