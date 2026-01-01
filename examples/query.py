import asyncio
from near_jsonrpc_client import NearClientAsync, ClientError, RpcError, HttpError, RequestTimeoutError
from near_jsonrpc_models import RpcQueryRequest, AccountId, FunctionArgs, RpcQueryRequestCallFunctionByFinality


async def main():
    client = NearClientAsync(base_url="https://rpc.mainnet.near.org")

    try:
        params = RpcQueryRequest(
            RpcQueryRequestCallFunctionByFinality(
                finality='final',
                account_id=AccountId(root='wrap.testnet'),
                args_base64=FunctionArgs('e30='),
                method_name='ft_balance_of2',
                request_type='call_function',
            )
        )

        tx = await client.query(params=params)
        print("Tx:", tx)

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
