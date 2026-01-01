from near_jsonrpc_client.api_methods_async import APIMixinAsync
from near_jsonrpc_client.api_methods_sync import APIMixinSync
from .base_client import NearBaseClientAsync, NearBaseClientSync


class NearClientAsync(NearBaseClientAsync, APIMixinAsync):
    """NearClientAsync with generated API methods mixed in."""
    pass


class NearClientSync(NearBaseClientSync, APIMixinSync):
    """NearClientSync with generated API methods mixed in."""
    pass
