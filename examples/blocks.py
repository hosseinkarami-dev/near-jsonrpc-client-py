import asyncio
from client import NearClientAsync, ClientError, RpcError, HttpError
from client.errors import RequestTimeoutError
from models import RpcBlockRequest, BlockId, CryptoHash
from models.block_id import BlockIdBlockHeight, BlockIdCryptoHash
from models.rpc_block_request import RpcBlockRequestBlockId


async def main():
    client = NearClientAsync(base_url="https://rpc.mainnet.near.org")

    try:
        params = RpcBlockRequest(
            RpcBlockRequestBlockId(
                block_id=BlockId(BlockIdBlockHeight(178682261))
            )
        )

        block = await client.block(params=params)
        print("Block Result:", block)

    except RpcError as e:
        print(f"{e}: {e.error}")
    except RequestTimeoutError as e:
        print(f"{e}")
    except HttpError as e:
        print(f"{e}: status: {e.status_code}, body: {e.body}")
    except ClientError as e:
        print("Invalid response:", e)

    try:
        params = RpcBlockRequest(
            RpcBlockRequestBlockId(
                block_id=BlockId(BlockIdCryptoHash(CryptoHash("FL6JnFZSZvgRsn9s7qHM3SrC8VXXAfNGRMyMtBfrAiQC").root))
            )
        )

        block = await client.block(params=params)
        print("Block Result:", block)

    except RpcError as e:
        print(f"{e}: {e.error}")
    except RequestTimeoutError as e:
        print(f"{e}")
    except HttpError as e:
        print(f"{e}: status: {e.status_code}, body: {e.body}")
    except ClientError as e:
        print("Invalid response:", e)

    await client.close()


asyncio.run(main())
