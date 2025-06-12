# gate-python
Python SDK (sync and async) for Gate cryptocurrency exchange with Rest and WS capabilities.

- You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/gate)
- You can check Gate's docs here: [Docs](https://www.google.com/search?q=google+gate+cryptocurrency+exchange+api+docs)
- Github repo: https://github.com/ccxt/gate-python
- Pypi package: https://pypi.org/project/gate-io-api


## Installation

```
pip install gate-io-api
```

## Usage

### Sync

```Python
from gate import GateSync

def main():
    instance = GateSync({})
    ob =  instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = instance.fetch_balance()
    # order = instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

main()
```

### Async

```Python
import sys
import asyncio
from gate import GateAsync

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = GateAsync({})
    ob =  await instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = await instance.fetch_balance()
    # order = await instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```



### Websockets

```Python
import sys
from gate import GateWs

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = GateWs({})
    while True:
        ob = await instance.watch_order_book("BTC/USDC")
        print(ob)
        # orders = await instance.watch_orders("BTC/USDC")

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```





#### Raw call

You can also construct custom requests to available "implicit" endpoints

```Python
        request = {
            'type': 'candleSnapshot',
            'req': {
                'coin': coin,
                'interval': tf,
                'startTime': since,
                'endTime': until,
            },
        }
        response = await instance.public_post_info(request)
```


## Available methods

### REST Unified

- `create_expired_option_market(self, symbol: str)`
- `create_market_buy_order_with_cost(self, symbol: str, cost: float, params={})`
- `create_order_request(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_orders_request(self, orders: List[OrderRequest], params={})`
- `create_orders(self, orders: List[OrderRequest], params={})`
- `fetch_balance(self, params={})`
- `fetch_borrow_interest(self, code: Str = None, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_closed_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_contract_markets(self, params={})`
- `fetch_currencies(self, params={})`
- `fetch_deposit_address(self, code: str, params={})`
- `fetch_deposit_addresses_by_network(self, code: str, params={})`
- `fetch_deposit_withdraw_fees(self, codes: Strings = None, params={})`
- `fetch_deposits(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_rate_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_rate(self, symbol: str, params={})`
- `fetch_funding_rates(self, symbols: Strings = None, params={})`
- `fetch_greeks(self, symbol: str, params={})`
- `fetch_ledger(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_leverage_tiers(self, symbols: Strings = None, params={})`
- `fetch_leverage(self, symbol: str, params={})`
- `fetch_leverages(self, symbols: Strings = None, params={})`
- `fetch_liquidations(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `fetch_market_leverage_tiers(self, symbol: str, params={})`
- `fetch_markets(self, params={})`
- `fetch_my_liquidations(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_my_settlement_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_network_deposit_address(self, code: str, params={})`
- `fetch_ohlcv(self, symbol: str, timeframe='1m', since: Int = None, limit: Int = None, params={})`
- `fetch_open_interest_history(self, symbol: str, timeframe='5m', since: Int = None, limit: Int = None, params={})`
- `fetch_open_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_option_chain(self, code: str, params={})`
- `fetch_option_markets(self, params={})`
- `fetch_option_ohlcv(self, symbol: str, timeframe='1m', since: Int = None, limit: Int = None, params={})`
- `fetch_option_underlyings(self)`
- `fetch_option(self, symbol: str, params={})`
- `fetch_order_book(self, symbol: str, limit: Int = None, params={})`
- `fetch_order_request(self, id: str, symbol: Str = None, params={})`
- `fetch_order_trades(self, id: str, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_order(self, id: str, symbol: Str = None, params={})`
- `fetch_orders_by_status(self, status, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_position(self, symbol: str, params={})`
- `fetch_positions_history(self, symbols: Strings = None, since: Int = None, limit: Int = None, params={})`
- `fetch_positions(self, symbols: Strings = None, params={})`
- `fetch_settlement_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_spot_markets(self, params={})`
- `fetch_ticker(self, symbol: str, params={})`
- `fetch_tickers(self, symbols: Strings = None, params={})`
- `fetch_time(self, params={})`
- `fetch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `fetch_trading_fee(self, symbol: str, params={})`
- `fetch_trading_fees(self, params={})`
- `fetch_transaction_fees(self, codes: Strings = None, params={})`
- `fetch_underlying_assets(self, params={})`
- `fetch_withdrawals(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `add_margin(self, symbol: str, amount: float, params={})`
- `borrow_cross_margin(self, code: str, amount: float, params={})`
- `borrow_isolated_margin(self, symbol: str, code: str, amount: float, params={})`
- `cancel_all_orders(self, symbol: Str = None, params={})`
- `cancel_order(self, id: str, symbol: Str = None, params={})`
- `cancel_orders_for_symbols(self, orders: List[CancellationRequest], params={})`
- `cancel_orders(self, ids: List[str], symbol: Str = None, params={})`
- `close_position(self, symbol: str, side: OrderSide = None, params={})`
- `describe(self)`
- `edit_order_request(self, id: str, symbol: str, type: OrderType, side: OrderSide, amount: Num = None, price: Num = None, params={})`
- `edit_order(self, id: str, symbol: str, type: OrderType, side: OrderSide, amount: Num = None, price: Num = None, params={})`
- `get_margin_mode(self, trigger, params)`
- `get_settlement_currencies(self, type, method)`
- `modify_margin_helper(self, symbol: str, amount, params={})`
- `multi_order_spot_prepare_request(self, market=None, trigger=False, params={})`
- `nonce(self)`
- `prepare_orders_by_status_request(self, status, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `prepare_request(self, market=None, type=None, params={})`
- `reduce_margin(self, symbol: str, amount: float, params={})`
- `repay_cross_margin(self, code: str, amount, params={})`
- `repay_isolated_margin(self, symbol: str, code: str, amount, params={})`
- `safe_market(self, marketId: Str = None, market: Market = None, delimiter: Str = None, marketType: Str = None)`
- `set_leverage(self, leverage: Int, symbol: Str = None, params={})`
- `set_position_mode(self, hedged: bool, symbol: Str = None, params={})`
- `set_sandbox_mode(self, enable: bool)`
- `spot_order_prepare_request(self, market=None, trigger=False, params={})`
- `transfer(self, code: str, amount: float, fromAccount: str, toAccount: str, params={})`
- `upgrade_unified_trade_account(self, params={})`
- `withdraw(self, code: str, amount: float, address: str, tag=None, params={})`

### REST Raw

- `public_wallet_get_currency_chains(request)`
- `public_spot_get_currencies(request)`
- `public_spot_get_currencies_currency(request)`
- `public_spot_get_currency_pairs(request)`
- `public_spot_get_currency_pairs_currency_pair(request)`
- `public_spot_get_tickers(request)`
- `public_spot_get_order_book(request)`
- `public_spot_get_trades(request)`
- `public_spot_get_candlesticks(request)`
- `public_spot_get_time(request)`
- `public_margin_get_currency_pairs(request)`
- `public_margin_get_currency_pairs_currency_pair(request)`
- `public_margin_get_funding_book(request)`
- `public_margin_get_cross_currencies(request)`
- `public_margin_get_cross_currencies_currency(request)`
- `public_margin_get_uni_currency_pairs(request)`
- `public_margin_get_uni_currency_pairs_currency_pair(request)`
- `public_flash_swap_get_currencies(request)`
- `public_futures_get_settle_contracts(request)`
- `public_futures_get_settle_contracts_contract(request)`
- `public_futures_get_settle_order_book(request)`
- `public_futures_get_settle_trades(request)`
- `public_futures_get_settle_candlesticks(request)`
- `public_futures_get_settle_premium_index(request)`
- `public_futures_get_settle_tickers(request)`
- `public_futures_get_settle_funding_rate(request)`
- `public_futures_get_settle_insurance(request)`
- `public_futures_get_settle_contract_stats(request)`
- `public_futures_get_settle_index_constituents_index(request)`
- `public_futures_get_settle_liq_orders(request)`
- `public_futures_get_settle_risk_limit_tiers(request)`
- `public_delivery_get_settle_contracts(request)`
- `public_delivery_get_settle_contracts_contract(request)`
- `public_delivery_get_settle_order_book(request)`
- `public_delivery_get_settle_trades(request)`
- `public_delivery_get_settle_candlesticks(request)`
- `public_delivery_get_settle_tickers(request)`
- `public_delivery_get_settle_insurance(request)`
- `public_options_get_underlyings(request)`
- `public_options_get_expirations(request)`
- `public_options_get_contracts(request)`
- `public_options_get_contracts_contract(request)`
- `public_options_get_settlements(request)`
- `public_options_get_settlements_contract(request)`
- `public_options_get_order_book(request)`
- `public_options_get_tickers(request)`
- `public_options_get_underlying_tickers_underlying(request)`
- `public_options_get_candlesticks(request)`
- `public_options_get_underlying_candlesticks(request)`
- `public_options_get_trades(request)`
- `public_earn_get_uni_currencies(request)`
- `public_earn_get_uni_currencies_currency(request)`
- `private_withdrawals_post_withdrawals(request)`
- `private_withdrawals_post_push(request)`
- `private_withdrawals_delete_withdrawals_withdrawal_id(request)`
- `private_wallet_get_deposit_address(request)`
- `private_wallet_get_withdrawals(request)`
- `private_wallet_get_deposits(request)`
- `private_wallet_get_sub_account_transfers(request)`
- `private_wallet_get_order_status(request)`
- `private_wallet_get_withdraw_status(request)`
- `private_wallet_get_sub_account_balances(request)`
- `private_wallet_get_sub_account_margin_balances(request)`
- `private_wallet_get_sub_account_futures_balances(request)`
- `private_wallet_get_sub_account_cross_margin_balances(request)`
- `private_wallet_get_saved_address(request)`
- `private_wallet_get_fee(request)`
- `private_wallet_get_total_balance(request)`
- `private_wallet_get_small_balance(request)`
- `private_wallet_get_small_balance_history(request)`
- `private_wallet_get_push(request)`
- `private_wallet_post_transfers(request)`
- `private_wallet_post_sub_account_transfers(request)`
- `private_wallet_post_sub_account_to_sub_account(request)`
- `private_wallet_post_small_balance(request)`
- `private_subaccounts_get_sub_accounts(request)`
- `private_subaccounts_get_sub_accounts_user_id(request)`
- `private_subaccounts_get_sub_accounts_user_id_keys(request)`
- `private_subaccounts_get_sub_accounts_user_id_keys_key(request)`
- `private_subaccounts_post_sub_accounts(request)`
- `private_subaccounts_post_sub_accounts_user_id_keys(request)`
- `private_subaccounts_post_sub_accounts_user_id_lock(request)`
- `private_subaccounts_post_sub_accounts_user_id_unlock(request)`
- `private_subaccounts_put_sub_accounts_user_id_keys_key(request)`
- `private_subaccounts_delete_sub_accounts_user_id_keys_key(request)`
- `private_unified_get_accounts(request)`
- `private_unified_get_account_mode(request)`
- `private_unified_get_borrowable(request)`
- `private_unified_get_transferable(request)`
- `private_unified_get_loans(request)`
- `private_unified_get_loan_records(request)`
- `private_unified_get_interest_records(request)`
- `private_unified_get_estimate_rate(request)`
- `private_unified_get_currency_discount_tiers(request)`
- `private_unified_get_risk_units(request)`
- `private_unified_get_unified_mode(request)`
- `private_unified_get_loan_margin_tiers(request)`
- `private_unified_get_leverage_user_currency_config(request)`
- `private_unified_get_leverage_user_currency_setting(request)`
- `private_unified_post_account_mode(request)`
- `private_unified_post_loans(request)`
- `private_unified_post_portfolio_calculator(request)`
- `private_unified_post_leverage_user_currency_setting(request)`
- `private_unified_put_unified_mode(request)`
- `private_spot_get_fee(request)`
- `private_spot_get_batch_fee(request)`
- `private_spot_get_accounts(request)`
- `private_spot_get_account_book(request)`
- `private_spot_get_open_orders(request)`
- `private_spot_get_orders(request)`
- `private_spot_get_orders_order_id(request)`
- `private_spot_get_my_trades(request)`
- `private_spot_get_price_orders(request)`
- `private_spot_get_price_orders_order_id(request)`
- `private_spot_post_batch_orders(request)`
- `private_spot_post_cross_liquidate_orders(request)`
- `private_spot_post_orders(request)`
- `private_spot_post_cancel_batch_orders(request)`
- `private_spot_post_countdown_cancel_all(request)`
- `private_spot_post_amend_batch_orders(request)`
- `private_spot_post_price_orders(request)`
- `private_spot_delete_orders(request)`
- `private_spot_delete_orders_order_id(request)`
- `private_spot_delete_price_orders(request)`
- `private_spot_delete_price_orders_order_id(request)`
- `private_spot_patch_orders_order_id(request)`
- `private_margin_get_accounts(request)`
- `private_margin_get_account_book(request)`
- `private_margin_get_funding_accounts(request)`
- `private_margin_get_auto_repay(request)`
- `private_margin_get_transferable(request)`
- `private_margin_get_loans(request)`
- `private_margin_get_loans_loan_id(request)`
- `private_margin_get_loans_loan_id_repayment(request)`
- `private_margin_get_loan_records(request)`
- `private_margin_get_loan_records_loan_record_id(request)`
- `private_margin_get_borrowable(request)`
- `private_margin_get_cross_accounts(request)`
- `private_margin_get_cross_account_book(request)`
- `private_margin_get_cross_loans(request)`
- `private_margin_get_cross_loans_loan_id(request)`
- `private_margin_get_cross_repayments(request)`
- `private_margin_get_cross_interest_records(request)`
- `private_margin_get_cross_transferable(request)`
- `private_margin_get_cross_estimate_rate(request)`
- `private_margin_get_cross_borrowable(request)`
- `private_margin_get_uni_estimate_rate(request)`
- `private_margin_get_uni_loans(request)`
- `private_margin_get_uni_loan_records(request)`
- `private_margin_get_uni_interest_records(request)`
- `private_margin_get_uni_borrowable(request)`
- `private_margin_post_auto_repay(request)`
- `private_margin_post_loans(request)`
- `private_margin_post_merged_loans(request)`
- `private_margin_post_loans_loan_id_repayment(request)`
- `private_margin_post_cross_loans(request)`
- `private_margin_post_cross_repayments(request)`
- `private_margin_post_uni_loans(request)`
- `private_margin_patch_loans_loan_id(request)`
- `private_margin_patch_loan_records_loan_record_id(request)`
- `private_margin_delete_loans_loan_id(request)`
- `private_flash_swap_get_currencies(request)`
- `private_flash_swap_get_currency_pairs(request)`
- `private_flash_swap_get_orders(request)`
- `private_flash_swap_get_orders_order_id(request)`
- `private_flash_swap_post_orders(request)`
- `private_flash_swap_post_orders_preview(request)`
- `private_futures_get_settle_accounts(request)`
- `private_futures_get_settle_account_book(request)`
- `private_futures_get_settle_positions(request)`
- `private_futures_get_settle_positions_contract(request)`
- `private_futures_get_settle_dual_comp_positions_contract(request)`
- `private_futures_get_settle_orders(request)`
- `private_futures_get_settle_orders_timerange(request)`
- `private_futures_get_settle_orders_order_id(request)`
- `private_futures_get_settle_my_trades(request)`
- `private_futures_get_settle_my_trades_timerange(request)`
- `private_futures_get_settle_position_close(request)`
- `private_futures_get_settle_liquidates(request)`
- `private_futures_get_settle_auto_deleverages(request)`
- `private_futures_get_settle_fee(request)`
- `private_futures_get_settle_risk_limit_tiers(request)`
- `private_futures_get_settle_price_orders(request)`
- `private_futures_get_settle_price_orders_order_id(request)`
- `private_futures_post_settle_positions_contract_margin(request)`
- `private_futures_post_settle_positions_contract_leverage(request)`
- `private_futures_post_settle_positions_contract_risk_limit(request)`
- `private_futures_post_settle_dual_mode(request)`
- `private_futures_post_settle_dual_comp_positions_contract_margin(request)`
- `private_futures_post_settle_dual_comp_positions_contract_leverage(request)`
- `private_futures_post_settle_dual_comp_positions_contract_risk_limit(request)`
- `private_futures_post_settle_orders(request)`
- `private_futures_post_settle_batch_orders(request)`
- `private_futures_post_settle_countdown_cancel_all(request)`
- `private_futures_post_settle_batch_cancel_orders(request)`
- `private_futures_post_settle_price_orders(request)`
- `private_futures_put_settle_orders_order_id(request)`
- `private_futures_delete_settle_orders(request)`
- `private_futures_delete_settle_orders_order_id(request)`
- `private_futures_delete_settle_price_orders(request)`
- `private_futures_delete_settle_price_orders_order_id(request)`
- `private_delivery_get_settle_accounts(request)`
- `private_delivery_get_settle_account_book(request)`
- `private_delivery_get_settle_positions(request)`
- `private_delivery_get_settle_positions_contract(request)`
- `private_delivery_get_settle_orders(request)`
- `private_delivery_get_settle_orders_order_id(request)`
- `private_delivery_get_settle_my_trades(request)`
- `private_delivery_get_settle_position_close(request)`
- `private_delivery_get_settle_liquidates(request)`
- `private_delivery_get_settle_settlements(request)`
- `private_delivery_get_settle_price_orders(request)`
- `private_delivery_get_settle_price_orders_order_id(request)`
- `private_delivery_post_settle_positions_contract_margin(request)`
- `private_delivery_post_settle_positions_contract_leverage(request)`
- `private_delivery_post_settle_positions_contract_risk_limit(request)`
- `private_delivery_post_settle_orders(request)`
- `private_delivery_post_settle_price_orders(request)`
- `private_delivery_delete_settle_orders(request)`
- `private_delivery_delete_settle_orders_order_id(request)`
- `private_delivery_delete_settle_price_orders(request)`
- `private_delivery_delete_settle_price_orders_order_id(request)`
- `private_options_get_my_settlements(request)`
- `private_options_get_accounts(request)`
- `private_options_get_account_book(request)`
- `private_options_get_positions(request)`
- `private_options_get_positions_contract(request)`
- `private_options_get_position_close(request)`
- `private_options_get_orders(request)`
- `private_options_get_orders_order_id(request)`
- `private_options_get_my_trades(request)`
- `private_options_get_mmp(request)`
- `private_options_post_orders(request)`
- `private_options_post_countdown_cancel_all(request)`
- `private_options_post_mmp(request)`
- `private_options_post_mmp_reset(request)`
- `private_options_delete_orders(request)`
- `private_options_delete_orders_order_id(request)`
- `private_earn_get_uni_currencies(request)`
- `private_earn_get_uni_currencies_currency(request)`
- `private_earn_get_uni_lends(request)`
- `private_earn_get_uni_lend_records(request)`
- `private_earn_get_uni_interests_currency(request)`
- `private_earn_get_uni_interest_records(request)`
- `private_earn_get_uni_interest_status_currency(request)`
- `private_earn_post_uni_lends(request)`
- `private_earn_put_uni_interest_reinvest(request)`
- `private_earn_patch_uni_lends(request)`
- `private_loan_get_collateral_orders(request)`
- `private_loan_get_collateral_orders_order_id(request)`
- `private_loan_get_collateral_repay_records(request)`
- `private_loan_get_collateral_collaterals(request)`
- `private_loan_get_collateral_total_amount(request)`
- `private_loan_get_collateral_ltv(request)`
- `private_loan_get_collateral_currencies(request)`
- `private_loan_get_multi_collateral_orders(request)`
- `private_loan_get_multi_collateral_orders_order_id(request)`
- `private_loan_get_multi_collateral_repay(request)`
- `private_loan_get_multi_collateral_mortgage(request)`
- `private_loan_get_multi_collateral_currency_quota(request)`
- `private_loan_get_multi_collateral_currencies(request)`
- `private_loan_get_multi_collateral_ltv(request)`
- `private_loan_get_multi_collateral_fixed_rate(request)`
- `private_loan_get_multi_collateral_current_rate(request)`
- `private_loan_post_collateral_orders(request)`
- `private_loan_post_collateral_repay(request)`
- `private_loan_post_collateral_collaterals(request)`
- `private_loan_post_multi_collateral_orders(request)`
- `private_loan_post_multi_collateral_repay(request)`
- `private_loan_post_multi_collateral_mortgage(request)`
- `private_account_get_detail(request)`
- `private_account_get_rate_limit(request)`
- `private_account_get_stp_groups(request)`
- `private_account_get_stp_groups_stp_id_users(request)`
- `private_account_get_stp_groups_debit_fee(request)`
- `private_account_post_stp_groups(request)`
- `private_account_post_stp_groups_stp_id_users(request)`
- `private_account_delete_stp_groups_stp_id_users(request)`
- `private_rebate_get_agency_transaction_history(request)`
- `private_rebate_get_agency_commission_history(request)`

### WS Unified

- `describe(self)`
- `create_order_ws(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_orders_ws(self, orders: List[OrderRequest], params={})`
- `cancel_all_orders_ws(self, symbol: Str = None, params={})`
- `cancel_order_ws(self, id: str, symbol: Str = None, params={})`
- `edit_order_ws(self, id: str, symbol: str, type: OrderType, side: OrderSide, amount: Num = None, price: Num = None, params={})`
- `fetch_order_ws(self, id: str, symbol: Str = None, params={})`
- `fetch_open_orders_ws(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_closed_orders_ws(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_orders_by_status_ws(self, status: str, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `watch_order_book(self, symbol: str, limit: Int = None, params={})`
- `un_watch_order_book(self, symbol: str, params={})`
- `get_cache_index(self, orderBook, cache)`
- `watch_ticker(self, symbol: str, params={})`
- `watch_tickers(self, symbols: Strings = None, params={})`
- `watch_bids_asks(self, symbols: Strings = None, params={})`
- `subscribe_watch_tickers_and_bids_asks(self, symbols: Strings = None, callerMethodName: Str = None, params={})`
- `watch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `watch_trades_for_symbols(self, symbols: List[str], since: Int = None, limit: Int = None, params={})`
- `un_watch_trades_for_symbols(self, symbols: List[str], params={})`
- `un_watch_trades(self, symbol: str, params={})`
- `watch_ohlcv(self, symbol: str, timeframe='1m', since: Int = None, limit: Int = None, params={})`
- `watch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `watch_balance(self, params={})`
- `watch_positions(self, symbols: Strings = None, since: Int = None, limit: Int = None, params={})`
- `set_positions_cache(self, client: Client, type, symbols: Strings = None)`
- `load_positions_snapshot(self, client, messageHash, type)`
- `watch_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `watch_my_liquidations(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `watch_my_liquidations_for_symbols(self, symbols: List[str] = None, since: Int = None, limit: Int = None, params={})`
- `clean_cache(self, subscription: dict)`
- `get_url_by_market(self, market)`
- `get_type_by_market(self, market: Market)`
- `get_url_by_market_type(self, type: MarketType, isInverse=False)`
- `get_market_type_by_url(self, url: str)`
- `subscribe_public(self, url, messageHash, payload, channel, params={}, subscription=None)`
- `subscribe_public_multiple(self, url, messageHashes, payload, channel, params={})`
- `un_subscribe_public_multiple(self, url, topic, symbols, messageHashes, subMessageHashes, payload, channel, params={})`
- `authenticate(self, url, messageType)`
- `subscribe_private(self, url, messageHash, payload, channel, params, requiresUid=False)`

## Contribution
- Give us a star :star:
- Fork and Clone! Awesome
- Select existing issues or create a new issue.