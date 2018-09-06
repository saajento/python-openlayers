from .view import View
from .layer import Layer

class Map:
    """
    A map has:
    - view: a view object
    - layers: a list of layers
    - https://openlayers.org/en/latest/apidoc/module-ol_Map-Map.html
    """
    WHITELIST = []

    def __init__(self, **kwargs):

        pass

    def _if_in(self, whitelist=None, kwargs):
        whitelist = whitelist or self.WHITELIST
        for x in kwargs:
            if x in whitelist:
                setattr(self, x, kwargs[x])
