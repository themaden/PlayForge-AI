import base64

class AssetEncoder:
    """Encodes raster and vector assets into clean data URIs for single-file HTML packaging."""

    @staticmethod
    def svg_to_data_uri(svg_string: str) -> str:
        encoded = base64.b64encode(svg_string.encode('utf-8')).decode('utf-8')
        return f"data:image/svg+xml;base64,{encoded}"
