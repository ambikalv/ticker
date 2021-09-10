from flask import Flask
import pandas 

app = Flask(__name__)

@app.route("/<companies>")


def tics(companies):
	xls = ExcelFile("tickers.xlsx")
	data = xls.parse(xls.sheet_names[0])
	tickers = dict(zip(data.fullname,data.ticker))
	tickers = {x.lower(): v for x,v in tickers.items()}
	tickers = {x.replace(' ', ''): v for x, v in tickers.items()}
	print("hi")

	goodcomps = []
	badcomps = []
	for company in companies:
		if company in tickers:
			ticker = tickers[company]
			goodcomps.append(ticker)
		else:
			badcomps.append(company)
	print("tickers are")
	print(goodcomps)
	print("not found")
	print(badcomps)

if __name__ == "__main__":        # on running python app.py
    app.run()
