import json
import os

from testskit.conf.settings.source import source, sourced


def test_source_from_json():
    souce = source.from_json('example.json')

    assert souce('MY_KEY') == 'my_value'

    assert souce('MY_OTHER_KEY') == 123


def test_source_from_class():
    class Settings(sourced.Settings):
        @sourced.default(6.0)
        def timeout(self): pass

    config = Settings(lambda key, _: json.load(open('example.json')).get(key), os.getenv)

    assert config.timeout == 6.0
