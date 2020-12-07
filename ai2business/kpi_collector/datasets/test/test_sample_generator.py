from ai2business.kpi_collector.datasets import sample_generator

ref_DOW = {
    "American Express Co": "AXP",
    "Amgen Inc": "AMGN",
    "Apple Inc": "AAPL",
    "Boeing Co": "BA",
    "Caterpillar Inc": "CAT",
    "Cisco Systems Inc": "CSCO",
    "Chevron Corp": "CVX",
    "Goldman Sachs Group Inc": "GS",
    "Home Depot Inc": "HD",
    "Honeywell International Inc": "HON",
    "International Business Machines Corp": "IBM",
    "Intel Corp": "INTC",
    "Johnson & Johnson": "JNJ",
    "Coca-Cola Co": "KO",
    "JPMorgan Chase & Co": "JPM",
    "McDonald's Corp": "MCD",
    "3M Co": "MMM",
    "Merck & Co Inc": "MRK",
    "Microsoft Corp": "MSFT",
    "Nike Inc": "NKE",
    "Procter & Gamble Co": "PG",
    "Travelers Companies Inc": "TRV",
    "UnitedHealth Group Inc": "UNH",
    "Salesforce.Com Inc": "CRM",
    "Verizon Communications Inc": "VZ",
    "Visa Inc": "V",
    "Walgreens Boots Alliance Inc": "WBA",
    "Walmart Inc": "WMT",
    "Walt Disney Co": "DIS",
    "Dow Inc": "DOW",
}


def test_load_default() -> None:
    assert sample_generator.stock_market() == ref_DOW


def test_load_failed() -> None:
    assert sample_generator.stock_market("STOCK") == None