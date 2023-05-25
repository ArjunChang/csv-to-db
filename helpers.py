from difflib import SequenceMatcher

DATABASE_TABLES = [
    "ae_aggregated_liquidity_trades",
    "ae_market_making_contracts",
    "ae_market_making_realized_gain_loss",
    "ae_staking_assets",
    "ae_staking_liabilities",
    "ae_structured_product_credit"
]

DATABASE_TABLE_ATRRIBUTE_MAPPING = {
    "ae_aggregated_liquidity_trades": (
        "customer_id", "coverage", "internal", "customer_revenue", "customer_cost", "customer_cost_wo_discount", "customer_PNL", "total_revenue", 
        "total_cost", "total_cost_wo_discount", "total_PNL", "exchange", "customer_proxy_id", "company_name", "persona_type", "trade_date", "side", 
        "token_type", "base_token", "quote_token", "fees_token", "is_maker", "rebate_token", "subaccount_id", "product_type_int", "product_type", 
        "margin_mode", "platform", "product", "total_trades", "total_orders", "quantity", "volume", "trade_size_usd", "fees_owed_usd", 
        "affiliate_rebate_usd", "fees_rebate_usd", "fee_total_usd", "net_customer_fees_usd", "net_savings_usd", "customer_fees_without_discount", 
        "default_fees_in_usd", "pdate", "v_plus", "v_minus", "e_plus", "e_minus", "v_minus_n", "internal_agg_edge_metrics", "customer_revenue_agg_edge_metrics", 
        "customer_cost_agg_edge_metrics", "customer_cost_wo_discount_agg_edge_metrics", "customer_pnl_agg_edge_metrics", "total_revenue_agg_edge_metrics", 
        "total_cost_gg_edge_metrics", "total_cost_wo_discount_agg_edge_metrics", "total_pnl_agg_edge_metrics", "token_type_agg_edge_metrics", 
        "t_create", "t_update", "t_delete"
    ),
    "ae_market_making_contracts": (
        "particulars", "mm_contract", "counterparty_name", "counterparty_code", "mm_token_name", "nature_of_mm_contract", "period_of_contract", "contract_start_date", 
        "contract_end_date", "token_quantity", "strike_price_of_contract", "quantity_sold_cumulative", "price_of_quantity_sold_average", "gain_loss_on_sale_of_tokens", 
        "remaining_mm_tokens", "24_hrs_liquidity_of_mm_token", "has_contract_terms_revised", "gain_loss_on_revision_of_contract", "eop_price", 
        "notional_gain_loss_based_on_eop_price", "token_received_date", "transaction_hash_token_received", "token_return_date", "transaction_hash_token_sent", 
        "t_create", "t_update", "t_delete"
    ),
    "ae_market_making_realized_gain_loss": (
        'particulars', 'mm_contract', 'counterparty_name', 'counterparty_code', 'mm_token_name', 'nature_of_mm_contract', 'period_of_contract', 'contract_start_date', 
        'contract_end_date', 'token_quantity', 'strike_price_of_contract', 'quantity_sold', 'price_of_quantity_sold', 'gain_loss_on_sale_of_tokens', 
        't_create', 't_update', 't_delete'
    ),
    "ae_staking_assets": (
        'asset_staked', 'validator_name', 'validator_code', 'blockchain_id', 'token', 'token_status', 'start_date', 'end_date', 'duration_staked_loan', 'trading_entity', 
        'rewards_earned_till_date', 'rebate_earned_till_date', 'apy', 'loan_id', 'rewards', 'rewards_validator', 'net_rewards_falconx', 'transaction_hash', 't_create', 
        't_delete', 't_update'
    ),
    "ae_staking_liabilities": (
        'loan_id', 'counterparty_name', 'counterparty_code', 'token', 'start_date', 'end_time', 'duration_of_loan', 'entity', 'rewards_dist_ratio', 'gross_rewards', 
        'net_rewards', 'attachment', 'transaction_hash', 'input_by', 't_create', 't_update', 't_delete'
    ),
    "ae_structured_product_credit": (
        'sp', 'counterparty_name', 'counterparty_code', 'token', 'token_quantity', 'notional_value', 'fixed_interest_rate', 'interest_token', 'start_date', 'end_date', 
        'duration_of_loan', 'funding_rate_source', 'eod_price_of_token', 'notional_based_on_eop', 'funding_rate', 'entity', 'funding_fee_amount_per_day', 
        'funding_fee_cumulative', 'funding_fee_outstanding', 'collateral', 'attachment', 'transaction_hash_loan', 'transaction_hash_interest_payments', 'entry_details', 
        'transaction_entry_input_time', 'source', 'modification_time', 'record_modified_by', 't_create', 't_update', 't_delete'
    )
}

def get_db_table_name(filename):
    max_similarity = 0
    table_name = ""
    for table in DATABASE_TABLES:
        similarity = SequenceMatcher(None, table, filename).ratio()
        if similarity > max_similarity:
            table_name = table
    return table_name


def format_headers(headers):
    formatted_headers = []
    for header in headers:
        formatted_headers.append(header.replace(" ", "_").lower())

    return formatted_headers