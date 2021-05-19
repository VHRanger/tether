<div style="background:#4c96c6;color:#fff;border: 10px solid SteelBlue;">
  I realize most of my readership doesn't care about crypto. Good for you. But tether is likely a fraud on the scale of Enron and we're in the middle of a bubble for the history books, so bear with me.<br /> <b>Disclaimer:</b> I have short positions on Bitcoin, largely through MSTR puts, since early January 2021.
</div>

**Thesis:** When looking at all the possible explanations of the current BTC bubble, "tether did it" is the most likely.

### Possible causes of the BTC bubble

It's something awesome to live through one of the great bubbles of history. You get to see in real time some of the great speculative mania stories, like my veterinarian casually mentionning she's looking to invest in crypto (at the all time high), [people paying millions for a hash of a tweet conferring no legal claim](https://gizmodo.com/for-whatever-reason-people-are-willing-to-pay-up-to-1-1846423546) and of course the classic "[yoga instructor selling her house to go all in on it](https://www.reddit.com/r/Bitcoin/comments/lqdgku/sold_my_house_last_monthly_to_buy_bitcoin_bought/)"

But what caused this bubble? Today we're going to dive into the main driver: what is presumably **the largest Ponzi scheme in history**.

# What's Tether?

USDT is a "stablecoin" -- a cryptocurrency whose price is supposed to be pegged to the US dollar -- managed by a company called tether.

Initially tether said they enforced the peg by having each USDT be backed by a USD in a bank account. Then tether ran into all sorts of hilarious hijinks over the years, many of which we only found out because they [were made public in NYAG litigation](https://ag.ny.gov/sites/default/files/2021.02.17_-_settlement_agreement_-_execution_version.b-t_signed-c2_oag_signed.pdf), including:

- Having all of tether's money in their lawyer's personal bank account (May 2017)

- Not having any bank account anywhere in the world for 6 months [footnote]march to september 2017[/footnote] to receive money in. Yet still emitting $400m new tethers in that period [footnote]Their lawyer's personal account had, at most, $60m at any point. Bitfinex had two institutional deposits in that whole period, neither of whom purchased tether[/footnote].

- Failing to complete an audit and settling on an attestation[footnote]An audit verifies where money comes from. An attestation is just an accoutnant saying "there was money in a bank account on that date"[/footnote] "for transparency". The morning of the attestation, tether moved $380m from sister company bitfinex into a bank account the morning of the day of the attestation.

 - Losing $900M to their money launderer, and covering those losses by commingling bitfinex customer funds with tether reserve funds (2018)

 - Finding the last bank on earth, [Deltec Bank from Cayman islands](https://www.deltecbank.com/) willing to do business with them after Wells Fargo and HSBC fired them as clients. Remember HSBC has the kind of risk tolerance leaving them to [willingly deals with drug cartels](https://www.icij.org/investigations/fincen-files/hsbc-moved-vast-sums-of-dirty-money-after-paying-record-laundering-fine/). No bank wants tether as a client.

 - Paying for the $18.5m NYAG fine [with, as far as we know, $18.5m in new tethers](https://tronscan.org/#/transaction/c211c48892027bd4accf75ac9a3ecc6ac870e266694895d5ae08cf4792dca8c2) sent to affiliated company FTX. Of tether's major partners only FTX has access to USD banking[footnote]Bitfinex, FTX, Binance, Huobi are the major clients. Only FTX has access to a Citigroup USD account. All others only have dodgy offshore bank accounts.[/footnote]

Just read section 2 and 3 of the NYAG settlement. It's a blast. The best recap on the tether saga is by [Amy Castor](https://amycastor.com/2019/01/17/the-curious-case-of-tether-a-complete-timeline-of-events/), but [Patrick McKenzie][3] also has a good write up. Note that Patrick's piece is quaint now -- it was written back in 2019 when tether's balance sheet was $2B. Tether now has over $58B on their balance sheet[footnote]Who knows what it will be when you read this[/footnote]:

<img src="https://www.singlelunch.com/wp-content/uploads/2021/02/Screen-Shot-2021-02-07-at-9.37.05-PM-1024x655.png" alt="" width="660" height="422" class="alignnone size-large wp-image-1449" />

As far as we know, there was no point in history at which USDT in circulation were backed 1-to-1 by USD in a bank account. At this point, they stopped even pretending -- each tether in circulation is backed by... tether's "reserves". 

![][2]

# The "Reserves"

For a long time, tether's "reserves" were a mystery. As found in the NYAG investigation, tether likely never had a dollar in a bank account for each USDT, ever. They're now forced to reveal the makeup in May 2021 as per their settlement. They found a 5-person accounting firm in the Cayman islands willing to do an [attestation]](https://tether.to/wp-content/uploads/2021/03/tether-assurance-feb-2021.pdf), which states they have 0.36% more assets than liabilities[footnote]Remember this 0.36%, it'll come back[/footnote].

They recently posted this [glorious pie chart](https://tether.to/wp-content/uploads/2021/05/tether-march-31-2021-reserves-breakdown.pdf):

GLORIOUS PIE CHART

Which [has](https://protos.com/tether-pie-chart-usdt-dollar-pegged-crypto-stablecoin-dollar-value/) [prompted](https://bennettftomlin.com/2021/05/13/for-every-1-of-tether-there-are-0-03-in-cash/) [many](https://finance.yahoo.com/news/tether-first-breakdown-shows-token-120000439.html) [more](https://www.ft.com/content/529eb4e6-796a-4e81-8064-5967bbe3b4d9) [questions](https://davidgerard.co.uk/blockchain/2021/05/13/tether-publishes-two-pie-charts-of-its-reserves/). First, we can view the actual debt in this form, as [broken Intel Jackal](https://twitter.com/intel_jakal):

INTEL JACKAL BREAKDOWN

Almost all of the reserves are in some form of loan to a commercial company (corporate bonds, commercial paper, secured loans). Only around 5% are in assets whose value we know (cash, T-Bills).

### Inconsistencies

Tether's general counsel, Stuart Hoegner, [footnote]Yes, the one who held money in a personal account for tether, is shown to be a liar by the NYAG[/footnote] posted a [highly unusual blog post](https://stuarthoegner.medium.com/tether-is-setting-a-new-standard-for-transparency-and-responding-to-criticism-that-is-fc130e08319b) in which he claims this is good debt by any standard. This raises many inconsistencies, which are easy to see given the magnitude of the numbers at hand.

1. Stuart claims they don't hold Treasury Bills because the interest rate is close to 0%. If they hold this risky debt as reserves because it pays higher interest, **how do tether only have 0.36% more assets than liabilities?** Either thether's management is looting the difference and leaving USDT holders with the debt's risk, or we're being lied to.

2. With $20B in commercial paper at the time of the attestation, and 50% more USDT on the market since, tether presumably has **$30B in commercial paper** at time of writing. The [entire commercial paper market](https://sec.gov/files/primer-money-market-funds-commercial-paper-market.pdf) in the US is around $1T per year.

We're supposed to believe that tether holds 3% of the commercial paper market at time of writing, and that they *apparently bought 1% of the entire market in the last month alone*.

3. The asset allocation strategy in the reserves seems to be [copied from](https://twitter.com/intel_jakal/status/1394562510070583296) an investment fund at tether's bank, Deltec. This investment fund apparently manages $425M, rather than $60B.

4. If the reserves are such regular financial assets, how come respectable accounting firms won't even touch it for a simple attestation?

We know that some of the money used for USDT come from Chinese money laundering because a tether shareholder [was recently charged](https://protos.com/china-crypto-otc-king-zhao-dong-criminal-charges-court-docs-show/). But we see no mention of frozen accounts in the reserves. Moreover, this amounts to less than $0.5B, and the perpetrator was nicknamed the "Chinese OTC King" -- so even in the charitable case where USDT are fully backed by money laundering, this raises inconsistencies.

### Reminder: non-USD reserves for a stablecoin are a problem

As noted by [Frances Coppola](https://www.coppolacomment.com/2021/05/tethers-smoke-and-mirrors.html), it's dangerous to guarantee to clients that something is worth $1 when your assets backing it are not dollars. The value of the USD changes very little. The value of crypto changes a lot.

If you want to enforce a market price of $1 for something backed by not-dollars, then the quantity of reserves needs to go up and down with the asset price changes. Otherwise, you'll eventually become insolvent, when asset prices become lower than what you bought them for.

# Who are these loan to?

The following sections are done using public blockchain data and exchange-listed prices. All code is available on github.

Tether has lost the privilege of the benefit of doubt a long time ago. Here is how tether's Ponzi scheme likely works:

- All their commercial debt is to the related exchanges (Binance, FTX, Bitfinex - see below) or their affiliated shell companies.

- Tether make new USDT out of thin air and send them against a dollar-denominated loan to these affiliates

- The affiliates use the new USDT to put market buy-orders for crypto, putting them on the new USDT on market

- Crypto goes up in value becaue of the new demand pressure. This overcollateralizes the affiliated loans, justifying more loans. 

- Rinse, repeat.

We can track who new USDT go to directly by looking at their [TRON](https://tronscan.org/#/address/TKHuVq1oKVruCGLvqVexFs6dawKv6fQgFs/transfers), [ethereum](https://etherscan.io/address/0x5754284f345afc66a98fbb0a0afe71e0f007b949#tokentxns), [OMNI](https://omniexplorer.info/address/1NTMakcgVwQpMdGxRQnFKyb3G1FAJysSfz) and [Solana](https://explorer.solana.com/address/Q6XprfkF8RQQKoQVG33xT88H7wi8Uk1B1CC7YAs69Gi) blockchain addresses. By matching the blockchain addresses new USDT are sent to to known parties, we can track who are the ones sending new USDT on the market:

TETHER COUNTERPARTIES PLOT

The counterparties are largely Binance, FTX, Bitfinex, and other exchanges. The commercial paper is presumably to affiliated shell companies. I wouldn't put those companies debt at a dollar-to-dollar valuation; for instance [Binance is currently under investigation by the DOJ and IRS](https://www.bloomberg.com/news/articles/2021-05-13/binance-probed-by-u-s-as-money-laundering-tax-sleuths-bore-in).

# But how does the $1 peg hold?

This isn't a hard one. [FTX happily admits to enforcing the dollar peg](https://twitter.com/AlamedaTrabucco/status/1348773044873949185):

TWITTER SCREENSHOT

You can easily enforce the dollar peg by wash-trading around the $1 price and arbitraging on exchanges who don't. 

FTX don't even need to be complicit to the scheme for this to make financial sense: if FTX can get new USDT for $1 on an infinite loan margin from tether, it's perfectly sensible to buy USDT when it's below $1 and shortsell USDT when it's above.

# The Mississippi bubble, 2021 style

The cryptocurrency ecosystem is conceptually simple. Money comes in from new investors buying, and the same money comes out to pay those cashing out. It would be a zero-sum ecosystem, except for the fact that miners have to pay their bills in dollars[footnote]There are some other forces, like lost coins reducing supply and driving up price, new coins increasing supply and driving down price. But these are orders of magnitude smaller, so speculation and mining are the major forces we need to consider[/footnote]

![](CRYPTO_ECOSYSTEM_IMAGE)

This is why "bitcoin investors" feel an immediate urge to tell everyone else to invest in bitcoin -- if no new money comes in, the financial structure eventually collapses under the miner's sell pressure.

Note how this is different than buying a company's stock. People buy and sell stocks on a stock exchange, but the companies independently have money coming in (from their clients) which can eventually justify the valuation. The stock of a profitable company is a positive-sum ecosystem.

When tether comes in with their scheme, they put demand pressure on BTC then add a supply constraint on BTC (also driving up the price!) by reducing the total supply of BTC to hoard in their reserves.

![](CRYPTO_TETHER_IMAGE)

Notice that even though bitcoin prices are higher, **no additional money entered the ecosystem** in the tether pump. Like a Ponzi scheme, we *can't pay everyone off at the inflated price* using the pool of money that's in the crypto ecosystem[footnote]More specifically, the pool of money in the crypto exchange's customer fund bank accounts[/footnote]. When enough money starts looking for the exit door, a $50B hole gets torn into the ecosystem, and someone has to pay for it.

![](masterpiece.gif)

# The danger zone happens when BTC drops below $18,500 

Assuming that each new USDT is used to instantly buy BTC at market prices [footnote]This is a lower bound estimate, since USDT are issued on the market between mint periods, where price is increasing[/footnote], we can track where the BTC "price of no return" is -- where reserve BTC were paid for more overall than they're now worth.

TETHER INSOLVENCY PLOT

We can play around with parameters (they might buy ETH or Dogecoin rather than BTC, etc.) but most calculations land the death zone in the $17k-$20k range -- prices we were at around December 2020.

Note that the scheme can easily collapse above this point. Bernie Madoff's customer deposits was around $18B against a $65B promised liabilities, but his scheme collapsed way before $40B in funds were withdrawn, because fraudsters tend to mismanage and embezzle some of the money for themselves.

Notice that the last point in time where BTC price went significantly below the death zone is the March 2020 COVID price crash -- which is also the point where USDT were started to be minted at a parabolic rate.

# OK, really convince me that unbacked tethers are supply-pushed

If you're running a pseudo-dollar, you can either emit a new coin only after people have given you money. This is being **demand-pulled**. The best case scenario for tether is that they're actually demand-pulled by [Chinese gambling and capital controls evasion](https://asia.nikkei.com/Spotlight/Caixin/How-illegal-online-gambling-launders-150bn-from-China). In the demand-pull case, a Chinese national gives Yuen to their money launderer, say, hypothetically, FTX's OTC desk. Now FTX has real money to pay cryptocurrency holders who want to cash out[footnote]If they felt like it. They might decide to go build an orphanage in India instead[/footnote].

On the other hand, if you print new tethers before having them in your reserve, you are **supply-pushing** them. In the supply-push cast the tether is immediately on an exchange, with a buy order appearing out of nowhere:

----> Market Depth Chart <-----

The important difference between the two is that if tether is merely aiding and abetting money laundering, there's money for everyone to cash out[footnote]As long as bank accounts don't get frozen[/footnote]. If tether is supply-pushing USDT then the ecosystem is in a Ponzi-scheme state, where promised liabilities are higher than what can be paid back.

### A literature review

There's actually a small literature on the tether fraud.

- **"Is BTC Really Untethered"** by Griffin & Shams (G&S 2018) analyzes tether in the distant days of the 2017-2018 cryptocurrency bubble. The paper is great research, and tests several hypotheses related to USDT being pushed vs pulled. It finds that tethers are pushed on the market, often at predictable round-number thresholds, with significant price effect.

Note that G&S 2018 was proven correct by the 2021 NYAG findings that tether pushed $400M USDT *without any way to get money for them* through the 2017 period that they had no bank.

The one methodological issue with G&S 2018 is that it uses the highest volume hours in trading over the time period[footnote]Otherwise you'd have attenuation bias in the statistical measurement[/footnote]. Some of those hours are particularly important. Fellow data scientist and tether skeptic [Bennett Tomlin notes](https://twitter.com/BennettTomlin/status/1191844248120938499?s=20) specifically the hours around the September 2017 attestation being removed from the dataset drives statistical significance in the result. But note that **tether fraudulently moved money for this attestation**: tether knew in advance that this time would be a high volume trading day. In retrospect, this adds, not removes, confidence in the G&S 2018 results.

- **"What Keeps Stablecoins Stable"** by Lyons & Viswanath-Natraj (L&V 2019) analyzes USDT like other currencies and finds that the price stability come from arbitrage and market demand, unlike central bank currencies where price level is often enforced by managing money supply. Note USDT supply has only ever really moved up.

While L&V 2019 is sometimes used as "proof that tether is not manipulating markets", it does no such thing. It simply resolves the conundrum of how the $1 price peg held with ever-increasing supply: the price is enforced with ~~wash trading by affiliates~~ ahem, "arbitrage".

It's much harder to replicate G&S 2018 for the 2021 cryptocurrency bubble data, because USDT are issued through a complex network of partner exchanges on multiple blockchains now.

### The DeFi boom started with the USDT flood

This is a sidenote to this story, but the Decentralized Finance (DeFi) boom started because of USDT flooding the market. DeFi is not a new invention: it's existed since the 2017 bubble. No one picked it up because it's a fairly useless idea: lock up more collateral for a crypto loan than the loan's value and use the loan. 

DeFi is exclusively used to leverage trading - eg. lock up BTC, keep the BTC exposure, and use the loan to buy more BTC. You can't buy a house or start a business on a DeFi loan -- the point of normal loans is to use personal creditworthiness and **under**collateralization to move future cashflows into the present. For these reasons, no one picked it up for years:

DEFIPULSE TVL PLOT

But notice something happened around the same time as USDT exploded. We can track what happened to DeFi by getting historical borrowing rates and matching them to total money in DeFi (TVL), USDT in DeFi and total USDT:

MY DEFI PLOT

A clear story emerges:

BLA BLA BLA BLA BLA

# The noose is tightening

At the time of writing, BTC crashed from a high of $64k to around $41k. But more importantly, for the first time in months, we're starting to see **significant backflows** into tether addresses, largely from Binance. Here are the outflows and inflows (excluding newly minted USDT) into the tether address on Tron, for example:



The music could stop at any moment now. It could take hours, or it could take months.

 [1]: https://www.singlelunch.com/2021/01/24/the-next-btc-crash-could-be-truly-epic/
 [2]: https://www.singlelunch.com/wp-content/uploads/2021/02/reserves.gif
 [3]: https://www.kalzumeus.com/2019/10/28/tether-and-bitfinex/
 [4]: https://en.wikipedia.org/wiki/Boiler_room_(business)
 [5]: https://en.wikipedia.org/wiki/Long-Term_Capital_Management
