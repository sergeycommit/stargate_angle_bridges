import json
import random
import asyncio
import time

from web3 import AsyncWeb3
from web3.providers.async_rpc import AsyncHTTPProvider

with open('router_abi.json') as f:
    stargate_abi = json.load(f)
with open('usdc_abi.json') as f:
    usdc_abi = json.load(f)
with open('usdt_abi.json') as f:
    usdt_abi = json.load(f)
with open('stg_abi.json') as f:
    stg_abi = json.load(f)
with open('angle_abi.json') as f:
    angle_abi = json.load(f)
with open('agEUR_abi.json') as f:
    agEUR_abi = json.load(f)
with open('LZ_agEUR_abi.json') as f:
    LZ_agEUR_abi = json.load(f)

class Chain:

    def __init__(self, rpc_url, stargate_address, usdc_address, usdt_address, stg_address, chain_id, explorer_url):
        self.w3 = AsyncWeb3(AsyncHTTPProvider(rpc_url))
        self.stargate_address = self.w3.to_checksum_address(stargate_address)
        self.stargate_contract = self.w3.eth.contract(address=self.stargate_address,
                                                      abi=stargate_abi)
        self.usdc_contract = self.w3.eth.contract(address=self.w3.to_checksum_address(usdc_address),
                                                  abi=usdc_abi) if usdc_address else None
        self.usdt_contract = self.w3.eth.contract(address=self.w3.to_checksum_address(usdt_address),
                                                  abi=usdt_abi) if usdt_address else None
        self.stg_contract = self.w3.eth.contract(address=self.w3.to_checksum_address(stg_address),
                                                  abi=stg_abi) if stg_address else None
        self.chain_id = chain_id
        self.blockExplorerUrl = explorer_url


class Polygon(Chain):
    def __init__(self):
        super().__init__(
            'https://rpc.ankr.com/polygon/e86fe895b18dc4920c2471c81b6984a2636aa25821d1a10863e7652f60597806',
            '0x45A01E4e04F14f7A4a6702c74187c5F6222033cd',
            '0x2791bca1f2de4661ed88a30c99a7a9449aa84174',
            '0xc2132d05d31c914a87c6611c10748aeb04b58e8f',
            '0x2f6f07cdcf3588944bf4c42ac74ff24bf56e7590',
            109,
            'https://polygonscan.com'
        )
        self.angle_address = self.w3.to_checksum_address('0x0c1EBBb61374dA1a8C57cB6681bF27178360d36F')
        self.angle_contract = self.w3.eth.contract(address=self.angle_address,
                                                   abi=angle_abi)
        self.agEUR_contract = self.w3.eth.contract(
            address=self.w3.to_checksum_address('0xE0B52e49357Fd4DAf2c15e02058DCE6BC0057db4'),
            abi=agEUR_abi)


class Fantom(Chain):
    def __init__(self):
        super().__init__(
            'https://rpc.ankr.com/fantom/e86fe895b18dc4920c2471c81b6984a2636aa25821d1a10863e7652f60597806',
            '0xAf5191B0De278C7286d6C7CC6ab6BB8A73bA2Cd6',
            '0x04068da6c83afcfa0e13ba15a6696662335d5b75',
            None,
            '0x2f6f07cdcf3588944bf4c42ac74ff24bf56e7590',
            112,
            'https://ftmscan.com'
        )


class Bsc(Chain):
    def __init__(self):
        super().__init__(
            'https://rpc.ankr.com/bsc/e86fe895b18dc4920c2471c81b6984a2636aa25821d1a10863e7652f60597806',
            '0x4a364f8c717cAAD9A442737Eb7b8A55cc6cf18D8',
            None,
            '0x55d398326f99059fF775485246999027B3197955',
            '0xb0d502e938ed5f4df2e681fe6e419ff29631d62b',
            102,
            'https://bscscan.com'
        )


class Avax(Chain):
    def __init__(self):
        super().__init__(
            'https://rpc.ankr.com/avalanche/e86fe895b18dc4920c2471c81b6984a2636aa25821d1a10863e7652f60597806',
            '0x45A01E4e04F14f7A4a6702c74187c5F6222033cd',
            '0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E',
            '0x9702230A8Ea53601f5cD2dc00fDBc13d4dF4A8c7',
            '0x2F6F07CDcf3588944Bf4C42aC74ff24bF56e7590',
            106,
            'https://snowtrace.io'
        )

class Arbitrum(Chain):
    def __init__(self):
        "rpc_url, stargate_address, usdc_address, usdt_address, chain_id, explorer_url"
        super().__init__(
            'https://rpc.ankr.com/arbitrum/e86fe895b18dc4920c2471c81b6984a2636aa25821d1a10863e7652f60597806',
            '0x53Bf833A5d6c4ddA888F69c22C88C9f356a41614',
            '0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8',
            '0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9',
            '0x6694340fc020c5e6b96567843da2df01b2ce1eb6',
            110,
            'https://arbiscan.io'
        )

class Optimism(Chain):
    def __init__(self):
        "rpc_url, stargate_address, usdc_address, usdt_address, chain_id, explorer_url"
        super().__init__(
            'https://rpc.ankr.com/optimism/e86fe895b18dc4920c2471c81b6984a2636aa25821d1a10863e7652f60597806',
            '0xB0D502E938ed5f4df2E681fE6E419ff29631d62b',
            '0x7F5c764cBc14f9669B88837ca1490cCa17c31607',
            '0x94b008aA00579c1307B0EF2c499aD98a8ce58e58',
            None,
            111,
            'https://optimistic.etherscan.io'
        )

class Gnosis(Chain):
    def __init__(self):
        "rpc_url, stargate_address, usdc_address, usdt_address, chain_id, explorer_url"
        super().__init__(
            'https://rpc.ankr.com/gnosis/e86fe895b18dc4920c2471c81b6984a2636aa25821d1a10863e7652f60597806',
            '0xB0D502E938ed5f4df2E681fE6E419ff29631d62b',
            '0x7F5c764cBc14f9669B88837ca1490cCa17c31607',
            '0x94b008aA00579c1307B0EF2c499aD98a8ce58e58',
            None,
            145,
            'https://gnosisscan.io'
        )
        self.angle_address = self.w3.to_checksum_address('0xfa5ed56a203466cbbc2430a43c66b9d8723528e7')
        self.angle_contract = self.w3.eth.contract(address=self.angle_address,
                                                      abi=angle_abi)
        self.agEUR_contract = self.w3.eth.contract(address=self.w3.to_checksum_address('0x4b1E2c2762667331Bc91648052F646d1b0d35984'),
                                                   abi=agEUR_abi)

class Celo(Chain):
    def __init__(self):
        "rpc_url, stargate_address, usdc_address, usdt_address, chain_id, explorer_url"
        super().__init__(
            'https://rpc.ankr.com/celo/e86fe895b18dc4920c2471c81b6984a2636aa25821d1a10863e7652f60597806',
            '0xB0D502E938ed5f4df2E681fE6E419ff29631d62b',
            '0x7F5c764cBc14f9669B88837ca1490cCa17c31607',
            '0x94b008aA00579c1307B0EF2c499aD98a8ce58e58',
            None,
            125,
            'https://celoscan.io'
        )
        self.angle_address = self.w3.to_checksum_address('0xf1ddcaca7d17f8030ab2eb54f2d9811365efe123')
        self.angle_contract = self.w3.eth.contract(address=self.angle_address,
                                                      abi=angle_abi)
        self.agEUR_contract = self.w3.eth.contract(address=self.w3.to_checksum_address('0xC16B81Af351BA9e64C1a069E3Ab18c244A1E3049'),
                                                   abi=agEUR_abi)
        self.lz_agEUR_contract = self.w3.eth.contract(address=self.w3.to_checksum_address('0xf1dDcACA7D17f8030Ab2eb54f2D9811365EFe123'),
                                                      abi=LZ_agEUR_abi)

polygon = Polygon()
fantom = Fantom()
bsc = Bsc()
avax = Avax()
arbitrum = Arbitrum()
optimism = Optimism()
celo = Celo()
gnosis = Gnosis()


async def swap_usdc(chain_from: Chain, chain_to: Chain, wallet, AMOUNT_TO_SWAP, MIN_AMOUNT):
    try:
        account = chain_from.w3.eth.account.from_key(wallet)
        address = account.address
        gas_price = await chain_from.w3.eth.gas_price

        fees = await chain_from.stargate_contract.functions.quoteLayerZeroFee(chain_to.chain_id,
                                                                            1,
                                                                            "0x0000000000000000000000000000000000001010",
                                                                            "0x",
                                                                            [0, 0,
                                                                             "0x0000000000000000000000000000000000000001"]
                                                                            ).call()
        fee = fees[0]

        allowance = await chain_from.usdc_contract.functions.allowance(address, chain_from.stargate_address).call()

        if allowance < AMOUNT_TO_SWAP:
            max_amount = AsyncWeb3.to_wei(2 ** 64 - 1, 'ether')

            approve_txn = await chain_from.usdc_contract.functions.approve(chain_from.stargate_address,
                                                                           max_amount).build_transaction({
                'from': address,
                'gas': 150000,
                'gasPrice': gas_price,
                'nonce': await chain_from.w3.eth.get_transaction_count(address),
            })
            signed_approve_txn = chain_from.w3.eth.account.sign_transaction(approve_txn, wallet)
            approve_txn_hash = await chain_from.w3.eth.send_raw_transaction(signed_approve_txn.rawTransaction)

            print(
                f"{chain_from.__class__.__name__} | USDT APPROVED {chain_from.blockExplorerUrl}/tx/{approve_txn_hash.hex()}")

            await asyncio.sleep(30)

        usdc_balance = await chain_from.usdc_contract.functions.balanceOf(address).call()

        if usdc_balance >= AMOUNT_TO_SWAP:

            chainId = chain_to.chain_id
            source_pool_id = 1
            dest_pool_id = 1
            refund_address = address
            amountIn = AMOUNT_TO_SWAP
            amountOutMin = MIN_AMOUNT
            lzTxObj = [0, 0, '0x0000000000000000000000000000000000000001']
            to = address
            data = '0x'

            swap_txn = await chain_from.stargate_contract.functions.swap(
                chainId, source_pool_id, dest_pool_id, refund_address, amountIn, amountOutMin, lzTxObj, to, data
            ).build_transaction({
                'from': address,
                'value': fee,
                'gasPrice': await chain_from.w3.eth.gas_price,
                'nonce': await chain_from.w3.eth.get_transaction_count(address)
            })

            signed_swap_txn = chain_from.w3.eth.account.sign_transaction(swap_txn, wallet)
            swap_txn_hash = await chain_from.w3.eth.send_raw_transaction(signed_swap_txn.rawTransaction)
            return swap_txn_hash

        elif usdc_balance < AMOUNT_TO_SWAP:

            min_amount = usdc_balance - (usdc_balance * 5) // 1000

            chainId = chain_to.chain_id
            source_pool_id = 1
            dest_pool_id = 1
            refund_address = address
            amountIn = usdc_balance
            amountOutMin = min_amount
            lzTxObj = [0, 0, '0x0000000000000000000000000000000000000001']
            to = address
            data = '0x'

            swap_txn = await chain_from.stargate_contract.functions.swap(
                chainId, source_pool_id, dest_pool_id, refund_address, amountIn, amountOutMin, lzTxObj, to, data
            ).build_transaction({
                'from': address,
                'value': fee,
                'gasPrice': await chain_from.w3.eth.gas_price,
                'nonce': await chain_from.w3.eth.get_transaction_count(address)
            })

            signed_swap_txn = chain_from.w3.eth.account.sign_transaction(swap_txn, wallet)
            swap_txn_hash = await chain_from.w3.eth.send_raw_transaction(signed_swap_txn.rawTransaction)
            return swap_txn_hash
    except Exception as e:
        print(f"Exception occurred in swap_usdc: {e}")

async def swap_usdt(chain_from, chain_to, wallet, AMOUNT_TO_SWAP, MIN_AMOUNT):
    try:
        account = chain_from.w3.eth.account.from_key(wallet)
        address = account.address
        nonce = await chain_from.w3.eth.get_transaction_count(address)
        gas_price = await chain_from.w3.eth.gas_price
        fees = await chain_from.stargate_contract.functions.quoteLayerZeroFee(chain_to.chain_id,
                                                                              1,
                                                                              "0x0000000000000000000000000000000000001010",
                                                                              "0x",
                                                                              [0, 0,
                                                                               "0x0000000000000000000000000000000000000001"]
                                                                              ).call()
        fee = fees[0]

        allowance = await chain_from.usdt_contract.functions.allowance(address, chain_from.stargate_address).call()

        if allowance < AMOUNT_TO_SWAP:
            max_amount = chain_from.w3.to_wei(2 ** 64 - 1, 'ether')
            approve_txn = await chain_from.usdt_contract.functions.approve(chain_from.stargate_address,
                                                                           max_amount).build_transaction({
                'from': address,
                'gas': 150000,
                'gasPrice': gas_price,
                'nonce': nonce,
            })
            signed_approve_txn = chain_from.w3.eth.account.sign_transaction(approve_txn, wallet)
            approve_txn_hash = await chain_from.w3.eth.send_raw_transaction(signed_approve_txn.rawTransaction)
            print(
                f"{chain_from.__class__.__name__} | USDT APPROVED {chain_from.blockExplorerUrl}/tx/{approve_txn_hash.hex()}")
            nonce += 1

            await asyncio.sleep(30)

        usdt_balance = await chain_from.usdt_contract.functions.balanceOf(address).call()

        if usdt_balance >= AMOUNT_TO_SWAP:

            chainId = chain_to.chain_id
            source_pool_id = 2
            dest_pool_id = 2
            refund_address = account.address
            amountIn = AMOUNT_TO_SWAP
            amountOutMin = MIN_AMOUNT
            lzTxObj = [0, 0, '0x0000000000000000000000000000000000000001']
            to = account.address
            data = '0x'

            swap_txn = await chain_from.stargate_contract.functions.swap(
                chainId, source_pool_id, dest_pool_id, refund_address, amountIn, amountOutMin, lzTxObj, to, data
            )\
            .build_transaction({
                'from': address,
                'value': fee,
                'gasPrice': await chain_from.w3.eth.gas_price,
                'nonce': await chain_from.w3.eth.get_transaction_count(address),
            })

            signed_swap_txn = chain_from.w3.eth.account.sign_transaction(swap_txn, wallet)
            swap_txn_hash = await chain_from.w3.eth.send_raw_transaction(signed_swap_txn.rawTransaction)
            return swap_txn_hash

        elif usdt_balance < AMOUNT_TO_SWAP:

            min_amount = usdt_balance - (usdt_balance * 5) // 1000

            chainId = chain_to.chain_id
            source_pool_id = 2
            dest_pool_id = 2
            refund_address = account.address
            amountIn = usdt_balance
            amountOutMin = min_amount
            lzTxObj = [0, 0, '0x0000000000000000000000000000000000000001']
            to = account.address
            data = '0x'

            swap_txn = await chain_from.stargate_contract.functions.swap(
                chainId, source_pool_id, dest_pool_id, refund_address, amountIn, amountOutMin, lzTxObj, to, data
            ).build_transaction({
                'from': address,
                'value': fee,
                'gasPrice': await chain_from.w3.eth.gas_price,
                'nonce': await chain_from.w3.eth.get_transaction_count(address),
            })

            signed_swap_txn = chain_from.w3.eth.account.sign_transaction(swap_txn, wallet)
            swap_txn_hash = await chain_from.w3.eth.send_raw_transaction(signed_swap_txn.rawTransaction)
            return swap_txn_hash
    except Exception as e:
        print(f"Exception occurred in swap_usdt: {e}")


async def swap_usdt_to_usdc(chain_from, chain_to, wallet, AMOUNT_TO_SWAP, MIN_AMOUNT):
    try:
        account = chain_from.w3.eth.account.from_key(wallet)
        address = account.address
        nonce = await chain_from.w3.eth.get_transaction_count(address)
        gas_price = await chain_from.w3.eth.gas_price
        fees = await chain_from.stargate_contract.functions.quoteLayerZeroFee(chain_to.chain_id,
                                                                              1,
                                                                              "0x0000000000000000000000000000000000001010",
                                                                              "0x",
                                                                              [0, 0,
                                                                               "0x0000000000000000000000000000000000000001"]
                                                                              ).call()
        fee = fees[0]

        allowance = await chain_from.usdt_contract.functions.allowance(address, chain_from.stargate_address).call()

        if allowance < AMOUNT_TO_SWAP:
            max_amount = chain_from.w3.to_wei(2 ** 64 - 1, 'ether')

            approve_txn = await chain_from.usdt_contract.functions.approve(chain_from.stargate_address,
                                                                           max_amount).build_transaction({
                'from': address,
                'gas': 150000,
                'gasPrice': gas_price,
                'nonce': nonce,
            })
            signed_approve_txn = chain_from.w3.eth.account.sign_transaction(approve_txn, wallet)
            approve_txn_hash = await chain_from.w3.eth.send_raw_transaction(signed_approve_txn.rawTransaction)

            print(
                f"{chain_from.__class__.__name__} | USDT APPROVED {chain_from.blockExplorerUrl}/tx/{approve_txn_hash.hex()}")
            nonce += 1

            await asyncio.sleep(30)

        usdt_balance = await chain_from.usdt_contract.functions.balanceOf(address).call()

        if usdt_balance >= AMOUNT_TO_SWAP:

            chainId = chain_to.chain_id
            source_pool_id = 2
            dest_pool_id = 1
            refund_address = account.address
            amountIn = AMOUNT_TO_SWAP
            amountOutMin = MIN_AMOUNT
            lzTxObj = [0, 0, '0x0000000000000000000000000000000000000001']
            to = account.address
            data = '0x'

            swap_txn = await chain_from.stargate_contract.functions.swap(
                chainId, source_pool_id, dest_pool_id, refund_address, amountIn, amountOutMin, lzTxObj, to, data
            ).build_transaction({
                'from': address,
                'value': fee,
                'gasPrice': await chain_from.w3.eth.gas_price,
                'nonce': await chain_from.w3.eth.get_transaction_count(address),
            })

            signed_swap_txn = chain_from.w3.eth.account.sign_transaction(swap_txn, wallet)
            swap_txn_hash = await chain_from.w3.eth.send_raw_transaction(signed_swap_txn.rawTransaction)
            return swap_txn_hash

        elif usdt_balance < AMOUNT_TO_SWAP:

            min_amount = usdt_balance - (usdt_balance * 5) // 1000

            chainId = chain_to.chain_id
            source_pool_id = 2
            dest_pool_id = 1
            refund_address = account.address
            amountIn = usdt_balance
            amountOutMin = min_amount
            lzTxObj = [0, 0, '0x0000000000000000000000000000000000000001']
            to = account.address
            data = '0x'

            swap_txn = await chain_from.stargate_contract.functions.swap(
                chainId, source_pool_id, dest_pool_id, refund_address, amountIn, amountOutMin, lzTxObj, to, data
            ).build_transaction({
                'from': address,
                'value': fee,
                'gasPrice': await chain_from.w3.eth.gas_price,
                'nonce': await chain_from.w3.eth.get_transaction_count(address),
            })

            signed_swap_txn = chain_from.w3.eth.account.sign_transaction(swap_txn, wallet)
            swap_txn_hash = await chain_from.w3.eth.send_raw_transaction(signed_swap_txn.rawTransaction)
            return swap_txn_hash
    except Exception as e:
        print(f"Exception occurred in swap_usdt: {e}")


async def swap_stg(chain_from, chain_to, wallet, AMOUNT_TO_SWAP, MIN_AMOUNT):
    try:
        account = chain_from.w3.eth.account.from_key(wallet)
        address = account.address
        nonce = await chain_from.w3.eth.get_transaction_count(address)
        gas_price = await chain_from.w3.eth.gas_price

        # allowance = await chain_from.usdt_contract.functions.allowance(address, chain_from.stargate_address).call()
        #
        # if allowance < AMOUNT_TO_SWAP:
        #     max_amount = chain_from.w3.to_wei(2 ** 64 - 1, 'ether')
        #     approve_txn = await chain_from.usdt_contract.functions.approve(chain_from.stargate_address,
        #                                                                    max_amount).build_transaction({
        #         'from': address,
        #         'gas': 150000,
        #         'gasPrice': gas_price,
        #         'nonce': nonce,
        #     })
        #     signed_approve_txn = chain_from.w3.eth.account.sign_transaction(approve_txn, wallet)
        #     approve_txn_hash = await chain_from.w3.eth.send_raw_transaction(signed_approve_txn.rawTransaction)
        #     print(
        #         f"{chain_from.__class__.__name__} | USDT APPROVED {chain_from.blockExplorerUrl}/tx/{approve_txn_hash.hex()}")
        #     nonce += 1
        #
        #     await asyncio.sleep(30)
        #
        balance = await chain_from.stg_contract.functions.balanceOf(address).call()
        print(balance, balance - AMOUNT_TO_SWAP)

        if AMOUNT_TO_SWAP > balance:
            AMOUNT_TO_SWAP = balance - (balance * 5) // 1000

        if balance >= AMOUNT_TO_SWAP:

            chainId = chain_to.chain_id
            refund_address = account.address
            amountIn = AMOUNT_TO_SWAP
            zroPaymentAddress = '0x0000000000000000000000000000000000000000'
            adapterParam = '0x00010000000000000000000000000000000000000000000000000000000000014c08'

            fees = await chain_from.stg_contract.functions.estimateSendTokensFee(chain_to.chain_id, False, '0x'
                                                                                 ).call()
            fee = int(fees[0]*1.03)

            swap_txn = await chain_from.stg_contract.functions.sendTokens(
                chainId, refund_address, amountIn, zroPaymentAddress, adapterParam).build_transaction({
                'from': address,
                'value': fee,
                'gasPrice': await chain_from.w3.eth.gas_price,
                'nonce': await chain_from.w3.eth.get_transaction_count(address),
            })

            signed_swap_txn = chain_from.w3.eth.account.sign_transaction(swap_txn, wallet)
            swap_txn_hash = await chain_from.w3.eth.send_raw_transaction(signed_swap_txn.rawTransaction)

            return swap_txn_hash
        else:
            print(f"Транза не прошла {wallet} с балансом {balance} и amount{AMOUNT_TO_SWAP}")
    except Exception as e:
        print(f"Exception occurred in swap_stg: {e}")


async def swap_agEUR(chain_from, chain_to, wallet, AMOUNT_TO_SWAP, MIN_AMOUNT):
    try:
        account = chain_from.w3.eth.account.from_key(wallet)
        address = account.address
        nonce = await chain_from.w3.eth.get_transaction_count(address)
        gas_price = await chain_from.w3.eth.gas_price

        allowance = await chain_from.agEUR_contract.functions.allowance(address, chain_from.angle_address).call()

        if allowance < AMOUNT_TO_SWAP:
            max_amount = chain_from.w3.to_wei(2 ** 64 - 1, 'ether')
            approve_txn = await chain_from.agEUR_contract.functions.approve(chain_from.angle_address,
                                                                           max_amount).build_transaction({
                'from': address,
                'gas': 150000,
                'gasPrice': gas_price,
                'nonce': nonce,
            })
            signed_approve_txn = chain_from.w3.eth.account.sign_transaction(approve_txn, wallet)
            approve_txn_hash = await chain_from.w3.eth.send_raw_transaction(signed_approve_txn.rawTransaction)
            print(
                f"{chain_from.__class__.__name__} | agEUR APPROVED {chain_from.blockExplorerUrl}/tx/{approve_txn_hash.hex()}")
            nonce += 1

            await asyncio.sleep(30)

        balance = await chain_from.agEUR_contract.functions.balanceOf(address).call()

        if AMOUNT_TO_SWAP > balance:
            AMOUNT_TO_SWAP = balance - (balance * 5) // 1000

        if balance >= AMOUNT_TO_SWAP:

            chainId = chain_to.chain_id
            refund_address = account.address
            amountIn = AMOUNT_TO_SWAP
            zroPaymentAddress = '0x0000000000000000000000000000000000000000'
            adapterParam = '0x00010000000000000000000000000000000000000000000000000000000000030d40'

            fees = await chain_from.angle_contract.functions.estimateSendFee(chain_to.chain_id, refund_address,
                                                                             AMOUNT_TO_SWAP, False, '0x'
                                                                                 ).call()
            fee = int(fees[0]*1.02)

            swap_txn = await chain_from.angle_contract.functions.send(
                chainId, refund_address, amountIn, refund_address, zroPaymentAddress, adapterParam).build_transaction({
                'from': address,
                'value': fee,
                'gasPrice': await chain_from.w3.eth.gas_price,
                'nonce': await chain_from.w3.eth.get_transaction_count(address),
            })

            signed_swap_txn = chain_from.w3.eth.account.sign_transaction(swap_txn, wallet)
            swap_txn_hash = await chain_from.w3.eth.send_raw_transaction(signed_swap_txn.rawTransaction)

            return swap_txn_hash
        else:
            print(f"Транза не прошла {wallet} с балансом {balance} и amount{AMOUNT_TO_SWAP}")
    except Exception as e:
        print(f"Exception occurred in swap_agEUR: {wallet} | {e}")


async def withdraw_LZ_agEUR(chain_from, chain_to, wallet, AMOUNT_TO_SWAP, MIN_AMOUNT):
    try:
        account = chain_from.w3.eth.account.from_key(wallet)
        address = account.address

        balance = await chain_from.lz_agEUR_contract.functions.balanceOf(address).call()

        if balance:
            refund_address = account.address
            amountIn = balance

            fees = await chain_from.angle_contract.functions.estimateSendFee(chain_to.chain_id, refund_address,
                                                                             AMOUNT_TO_SWAP, False, '0x'
                                                                                 ).call()
            fee = int(fees[0]*1.02)

            swap_txn = await chain_from.angle_contract.functions.withdraw(amountIn, refund_address)\
                .build_transaction({
                'from': address,
                'value': 0,
                'gasPrice': await chain_from.w3.eth.gas_price,
                'nonce': await chain_from.w3.eth.get_transaction_count(address),
            })

            signed_swap_txn = chain_from.w3.eth.account.sign_transaction(swap_txn, wallet)
            swap_txn_hash = await chain_from.w3.eth.send_raw_transaction(signed_swap_txn.rawTransaction)

            return swap_txn_hash
        else:
            print(f"Fail Транза withdraw не прошла {wallet} с балансом {balance}")
    except Exception as e:
        print(f" Fail Exception occurred in withdraw LZ_agEUR: {wallet} | {e}")

async def check_balance(address, contract):
    balance = await contract.functions.balanceOf(address).call()
    return balance


async def get_token_decimals(token_contract):
    decimals = await token_contract.functions.decimals().call()
    return decimals


async def work(wallet):
    account = polygon.w3.eth.account.from_key(wallet)
    address = account.address

    chains = [
       #  Create your own personal functions.
       #  Example below:

       #  (from.chain, to.chain, from.chain.token_contract, swap function, 'token', 'From chain', 'To chain'), 
       #  swap_usdc for swapping usdc, swap_usdt for swapping usdt, swap_usdt_to_usdc for swapping usdt to usdc when bridging.

        # (celo, celo, celo.lz_agEUR_contract, withdraw_LZ_agEUR, "LZ_agEUR", "celo", "celo"),
        (celo, gnosis, celo.agEUR_contract, swap_agEUR, "agEUR", "celo", "gnosis"),
        (gnosis, celo, gnosis.agEUR_contract, swap_agEUR, "agEUR", "gnosis", "celo"),
        (celo, gnosis, celo.agEUR_contract, swap_agEUR, "agEUR", "celo", "gnosis"),
        (gnosis, celo, gnosis.agEUR_contract, swap_agEUR, "agEUR", "gnosis", "celo"),
        (celo, gnosis, celo.agEUR_contract, swap_agEUR, "agEUR", "celo", "gnosis"),
        (gnosis, celo, gnosis.agEUR_contract, swap_agEUR, "agEUR", "gnosis", "celo"),
        (celo, gnosis, celo.agEUR_contract, swap_agEUR, "agEUR", "celo", "gnosis"),
        (gnosis, celo, gnosis.agEUR_contract, swap_agEUR, "agEUR", "gnosis", "celo"),
        (gnosis, celo, gnosis.agEUR_contract, swap_agEUR, "agEUR", "gnosis", "celo"),
        (celo, gnosis, celo.agEUR_contract, swap_agEUR, "agEUR", "celo", "gnosis"),
        (gnosis, celo, gnosis.agEUR_contract, swap_agEUR, "agEUR", "gnosis", "celo"),
        (celo, gnosis, celo.agEUR_contract, swap_agEUR, "agEUR", "celo", "gnosis"),
        (gnosis, celo, gnosis.agEUR_contract, swap_agEUR, "agEUR", "gnosis", "celo"),
        (celo, gnosis, celo.agEUR_contract, swap_agEUR, "agEUR", "celo", "gnosis"),
        (gnosis, celo, gnosis.agEUR_contract, swap_agEUR, "agEUR", "gnosis", "celo"),
        (celo, gnosis, celo.agEUR_contract, swap_agEUR, "agEUR", "celo", "gnosis"),
        (gnosis, celo, gnosis.agEUR_contract, swap_agEUR, "agEUR", "gnosis", "celo"),
        #(polygon, bsc, polygon.stg_contract, swap_stg, "STG", "Polygon", "Bsc"),
        # (polygon, celo, polygon.agEUR_contract, swap_agEUR, "agEUR", "polygon", "celo"),
        # (polygon, bsc, polygon.usdt_contract, swap_usdt, "USDT", "Polygon", "BSC"),
        # (arbitrum, bsc, arbitrum.stg_contract, swap_stg, "STG", "Arb", "BSC"),
        # (avax, bsc, avax.usdt_contract, swap_usdt, "USDT", "Avax", "BSC"),
        # (avax, polygon, avax.usdc_contract, swap_usdc, "USDC", "Avax", "Polygon"),
        # (optimism, bsc, optimism.usdt_contract, swap_usdt, "USDT", "Opt", "BSC"),
        # (optimism, polygon, optimism.usdc_contract, swap_usdc, "USDC", "Opt", "Polygon")
        # (polygon, fantom, polygon.usdc_contract, swap_usdc, "USDC", "Polygon", "Fantom"),
        # (fantom, polygon, fantom.usdc_contract, swap_usdc, "USDC", "Fantom", "Polygon"),
        # (fantom, avax, fantom.usdc_contract, swap_usdc, "USDC", "Fantom", "Avax")
    ]
    randomize, quantity = False, len(chains)    # рандомизация
    if randomize:
        random.shuffle(chains)
        quantity = random.randint(1, quantity)

    for (from_chain, to_chain, contract, swap_fn, token, from_name, to_name) in chains[:quantity]:

        amount_min = 0.05  # Min amount to bridge
        amount_max = 0.15 # Max amount to bridge

        amount_random = random.uniform(amount_min, amount_max)
        try:
            decimals = await get_token_decimals(contract)
        except:
            decimals = 18
        amount_to_swap = int(amount_random * (10 ** decimals))

        slippage = 5
        min_amount = int(amount_to_swap - (amount_to_swap * slippage) // 1000)

        start_delay = random.randint(10, 60)
        await asyncio.sleep(start_delay)

        balance = await check_balance(address, contract)
        if balance < 4 * (10 ** 6):
            print(address, from_name, balance)
            continue
            # await asyncio.sleep(60)
            # balance = await check_balance(address, contract)
        try:
            txn_hash = await swap_fn(from_chain, to_chain, wallet, amount_to_swap, min_amount)
            print(
                f"{from_name} -> {to_name} | {token} | {address} | Transaction: {from_chain.blockExplorerUrl}/tx/{txn_hash.hex()}")
        except Exception as e:
            fails.append(address)
            print('Fail', address, e)

    print(f'Wallet: {address} | DONE')


async def main():
    with open('private_keys.txt', 'r') as f:
        WALLETS = [row.strip() for row in f]

    tasks = []
    fails = []
    for wallet in WALLETS:
        tasks.append(asyncio.create_task(work(wallet)))

    for task in tasks:
        await task

    print(f'*** ALL JOB IS DONE ***')


if __name__ == '__main__':
    asyncio.run(main())

