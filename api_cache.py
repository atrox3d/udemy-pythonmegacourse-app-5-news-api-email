from pathlib import Path
import hashlib
import json


class APICache(dict):
    CACHE_PATH = Path('api-cache-files/')

    def __init__(self, url, *args, **kwargs):
        super(APICache, self).__init__(*args, **kwargs)
        self.url = url
        self.load()

    def get_path(self):
        urlhash = hashlib.md5(self.url.encode("utf-8")).hexdigest()
        filename = Path(f'{urlhash}.json')
        filepath = self.CACHE_PATH.joinpath(filename)
        return filepath

    def save(self, **kwargs):
        filepath = self.get_path()
        if not filepath.parent.exists():
            filepath.parent.mkdir()

        with open(filepath, 'w') as jsonfile:
            json.dump(self, jsonfile, indent=4)

    def load(self):
        filepath = self.get_path()
        try:
            with open(filepath, 'r') as jsonfile:
                self.update(json.load(jsonfile))
        except FileNotFoundError:
            self.clear()
        return self

    def update(self, __m=None, **kwargs):
        super().update(__m, **kwargs)
        self.save()


if __name__ == '__main__':
    cache = APICache("URL://")
    print(cache)
    cache.save()
