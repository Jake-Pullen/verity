# Money

## how to handle all the different currencies of the world.

We will be using an approach used by [YNAB in their API Docs](https://api.ynab.com/#formats)
essentially 1000 units of our generic currency = 1 of a "normal" currency.
This means we will have to at some point in the future add the "exchange rate" of all the currencies for display purposes, but also means that we will not have to do large scale refactors if we want to add / change currencies.

| Used Currency | Generic Currency | Amount |
|---------------|------------------|--------|
| GBP (£)       | 1000             | 1      |
| GBP (£)       | 475970           | 475.97 |
| USD ($)       | 8990             | 8.99   |
| Euro(€)       | 29380            | 29.38  |
