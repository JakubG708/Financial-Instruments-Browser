import yfinance as yf



#aby poprawnie zdobyć ticker etfu z pliku musimy lookupem
#wyszukać isin etfa, jako że isin jest unikalny 
#to dostaniemy tylko jeden wynik
#wynik można przeparsować żeby mieć tylko jego symbol
#aymbol można zapisać jako ticker


#przykład
lookup = yf.Lookup("LU1737652823")
df = lookup.get_etf(count=1)

symbol = df.index[0]

print(symbol)
