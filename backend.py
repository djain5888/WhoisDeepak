# Backend - FastAPI Server
from fastapi import FastAPI
import yfinance as yf
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/stock/{ticker}")
def get_stock_data(ticker: str):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="7d")
    hist.reset_index(inplace=True)
    hist['Date'] = hist['Date'].dt.strftime('%Y-%m-%d')
    return hist[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']].to_dict(orient='records')
