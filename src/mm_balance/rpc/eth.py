from decimal import Decimal

from mm_eth import erc20, rpc
from mm_std import Ok, Result

from mm_balance.constants import RETRIES_BALANCE, RETRIES_DECIMALS, TIMEOUT_BALANCE, TIMEOUT_DECIMALS


def get_native_balance(nodes: list[str], address: str, proxies: list[str], round_ndigits: int) -> Result[Decimal]:
    return rpc.eth_get_balance(nodes, address, proxies=proxies, attempts=RETRIES_BALANCE, timeout=TIMEOUT_BALANCE).and_then(
        lambda b: Ok(round(Decimal(b / 10**18), round_ndigits)),
    )


def get_token_balance(
    nodes: list[str], wallet_address: str, token_address: str, decimals: int, proxies: list[str], round_ndigits: int
) -> Result[Decimal]:
    return erc20.get_balance(
        nodes,
        token_address,
        wallet_address,
        proxies=proxies,
        attempts=RETRIES_BALANCE,
        timeout=TIMEOUT_BALANCE,
    ).and_then(
        lambda b: Ok(round(Decimal(b / 10**decimals), round_ndigits)),
    )


def get_token_decimals(nodes: list[str], token_address: str, proxies: list[str]) -> Result[int]:
    return erc20.get_decimals(nodes, token_address, timeout=TIMEOUT_DECIMALS, proxies=proxies, attempts=RETRIES_DECIMALS)
