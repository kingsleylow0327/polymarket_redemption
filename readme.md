# Disclaimer, all address found in this repo are official Polymarket and USDC smart contract addresses, you can verify it on [Polygonscan](https://polygonscan.com/)

# How to Start?
## 0. To try, make sure you have:
1. Some POL in your Metamask wallet
2. You have a Unredeemed position in Polymarket

## 1. Copy environment
1. Copy .env_example as .env
2. Fill in METAMASK_ADDRESS

## 2. Get your Polymarket Proxy Address
1. Go to [Polymarket](https://polymarket.net/)
2. Click on your profile picture in the top right corner
3. Click on "Profile"
4. Copy your proxy address
5. Fill it as POLYMARKET_FUNDER in .env file

## 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 4. Run the script
```bash
py redeem_service.py
```

## Things to take note
### When you have ran the script, check if your machine match any error during Polymarket connection, if you have any error, try to reorder the sequence of RPC_URLS in .env file. The first RPC_URLS that works will be used.

### If you need to implement this script to your code, you may refer to line 99 in redeem_service.py