# Glossary

Every term the series uses, defined exactly as the engine uses it. Hover a term in any article to see
its definition.

## Holdings

### Instrument

The terms of a contract (a bond, future, or swap), priced per unit of notional. Holds no quantity.

### Position

A signed quantity of one Instrument held in a Book. Several Positions can reference the same Instrument. Where the Instrument's own terms already say which side the holder is on — a swap paying or receiving fixed, an FX Forward buying or selling the base currency — the quantity is its notional and is always positive.

### Position Value

A Position's dirty value per unit times its signed quantity. It is zero for Instruments margined daily, such as futures, whose gains and losses are settled every day.

### Book

The set of Positions that risk rolls up to.

## Time

### Tick

One step of the simulation. It advances simulated time by a fixed amount and moves the market factors.

*In plain words:* One heartbeat of the simulated market.

### Valuation Date

The simulated calendar date that pricing uses for accrual, time to maturity, and cash flow schedules. It stays fixed within a simulated day.

### Day Rollover

The moment the Valuation Date advances by one simulated day. Every Instrument is aged and repriced at this point, and Lifecycle Events take effect.

### Lifecycle Event

A cash flow a Position receives or pays at Day Rollover: a coupon, a redemption, or a swap leg payment.

### Fixing

The rate of the floating index recorded on a reset date. Once recorded it never changes, and it sets the known coupon for every swap period starting that day.

## Market and risk factors

### Risk Factor

An identified piece of simulated market state that Instrument prices depend on. It is either continuous, such as a curve Pillar's zero rate, a futures Basis, a Systemic or Sector Factor, or an issuer's Mark, or discrete, such as the Valuation Date, a future's current Proxy Bond, or an issuer's Rating Bucket, where any change counts as a move. Every Risk Factor belongs to a currency.

### Dependency

A Risk Factor whose move can trigger an Instrument's reprice: every non-curve Risk Factor it is priced from, plus the Pillars that carry a material share of its Bucketed DV01. An Instrument's Dependencies can change while the system runs.

### Pillar

A fixed curve tenor (e.g. 2Y, 5Y, 10Y, 30Y) at which bucketed DV01 is measured.

### Basis

The difference between a Treasury future's price and the price implied by the curve, simulated as its own mean-reverting Risk Factor.

### Proxy Bond

A synthetic fixed-coupon bond that stands in for a Treasury future's cheapest-to-deliver bond. The future is priced from it.

### CTD Switch

A simulated change of a future's Proxy Bond, together with a discrete jump in the Basis.

### Curve Source

Where one currency's starting curve came from: live, cached, or bundled. Reported per currency, because each has its own publisher and they fall back independently. A Curve Source hands back a curve ready to discount with; whether that needed a bootstrap is its own business, not its caller's.

## Repricing

### Materiality Threshold

How far a Risk Factor has to move since an Instrument was last priced before that Instrument is repriced.

### Staleness

How far a Risk Factor has moved since an Instrument that depends on it was last priced. It never exceeds that factor's Materiality Threshold.

*In plain words:* How out of date a displayed price is allowed to get before the engine bothers to reprice it.

## Credit

### Systemic Factor

The observable, index-like component of spread that is shared by every issuer.

### Sector Factor

The observable, index-like component of spread that is shared by every issuer in one Rating Bucket.

### Idiosyncratic Factor

The unobservable component of spread that belongs to a single issuer.

### Rating Bucket

A (sector, rating) pair, such as BBB Industrials, with its own sector spread factor. Every issuer belongs to exactly one Rating Bucket at a time.

### Credit Event

A sudden jump in one issuer's spread that can also trigger a Rating Migration. The jump is unobservable and becomes known only through later Prints.

### Rating Migration

An issuer moving from one Rating Bucket to another, usually as a result of a Credit Event. Like a real rating agency action, it is public the moment it happens.

### Latent Spread

An issuer's hidden "true" spread: one flat Z-spread over the Treasury curve that applies to all its bonds, made of the Systemic, Sector, and Idiosyncratic Factors plus any Credit Event jump. The risk engine never sees it.

### Print

A simulated trade report for an issuer's bonds that reveals the Latent Spread with noise, arriving at random intervals.

### Quote

A simulated dealer quote for an issuer's bonds that reveals the Latent Spread with more noise than a Print.

### Mark

The flat Z-spread the risk engine prices all of an issuer's bonds with. It resets to the observed spread on each Print or Quote, and in between it is carried forward by Matrix Pricing.

*In plain words:* The spread the risk system believes an issuer trades at right now, pieced together from the few trades and quotes it has seen.

### Matrix Pricing

Carrying a Mark forward between observations using only the moves in the observable Systemic Factor and the issuer's Sector Factor.

## FX

### FX Forward

An agreement to exchange two currency amounts on a future date at a rate agreed today. Deliverable: both legs settle in full.

### NDF

A forward on a currency that cannot be freely delivered, settled as a single net payment in the settlement currency rather than an exchange of both amounts.

### FX Spot

The current exchange rate for a currency pair, written base first and quoted in the second currency, and the Risk Factor every FX Position depends on. Unlike every other continuous factor in the engine, it does not mean-revert. The engine holds its logarithm, so a difference in the factor is a relative move.

### Forward Points

The difference between an NDF's quoted forward rate and FX Spot, simulated as its own Risk Factor. A deliverable forward has no Forward Points: its forward rate is derived from the two currencies' curves.

### FX Fixing

The exchange rate of a currency pair recorded on a fixing date. Once recorded it never changes, and it sets an NDF's settlement amount. Distinct from a Fixing, which sets a coupon.

### Notional Currency

The currency an FX Position's notional is denominated in, which need not be the currency it is valued in. It is part of the contract, because markets differ: a deliverable outright is struck on the pair's base amount, an NDF on the deliverable one it settles in.

## Sensitivities

### DV01

The change in value for a 1bp parallel shift of the zero rates on one currency's output curve, with every other curve held fixed. Reported per currency; a Book-level total across currencies is labelled "all curves, 1bp each", because a basis point of one currency's curve is not a basis point of another's.

*In plain words:* How many dollars a Position gains if interest rates fall by one hundredth of a percent. The bigger the number, the more rate risk.

### Bucketed DV01

DV01 measured by shifting the zero rate at a single Pillar of one currency's curve, with the shift fading linearly to zero at the neighbouring Pillars.

*In plain words:* DV01 split up by maturity, so you can see whether the rate risk sits in the 2-year, 10-year or 30-year part of the curve.

### CS01

The change in value for a 1bp shift in an issuer's Mark.

*In plain words:* Like DV01, but for credit spreads: how many dollars a Position gains if its issuer's spread tightens by one hundredth of a percent.

### FX Delta

The change in value for a 1% move in a currency against the Reporting Currency, reported per currency because exposures in different currencies do not net.

### Reporting Currency

The currency all Book-level value and risk is expressed in (USD). Values in other currencies are converted at FX Spot. Rates risk is reported per currency rather than converted, because a basis point of one currency's curve is not a basis point of another's.

## Options

### Swaption

An option to enter a specified Interest Rate Swap on a single future date. European only: one Exercise Decision, on the Expiry date. Its terms are the Expiry plus the underlying swap, so the strike is that swap's fixed rate and paying or receiving fixed is that swap's direction.

### Expiry

The date a Swaption's Exercise Decision is made, and the date its underlying swap starts. Distinct from the underlying's maturity.

### Exercise Decision

Whether a Swaption was exercised, recorded once at the Day Rollover onto its Expiry and never revisited, even if rates move back through the strike afterwards. It is not a Lifecycle Event: it pays nothing, it changes what the Position is. An exercised Swaption is worth its underlying swap; an unexercised one is worth zero and stays in the Book.

### Surface Point

An (expiry, tenor) coordinate on the volatility surface, such as 1Mx5Y, at which a Normal Volatility is quoted. Every Swaption prices from exactly one, and only the points the Book needs exist.

### Normal Volatility

The volatility a Surface Point is quoted at, in basis points per annum, under the Bachelier model. It is the engine's first Risk Factor that no curve can produce: it is quoted by the market rather than derived from anything, and here it is simulated rather than observed.

### Forward Swap Rate

The fixed rate that would make a Swaption's underlying swap worth zero at Expiry, read off the curve. Compared against the strike, it is what the Exercise Decision turns on.

### Annuity

The discounted value of a swap's fixed-leg accruals per unit of notional. It is the factor a Swaption's value scales with, and the reason a swaption's price is quoted in the same units as the swap it exercises into.

### Vega

The change in value for a 1bp move in a Surface Point's Normal Volatility. Only Swaptions have it.

### Gamma

The change in DV01 for a 25bp parallel shift of the curve: how much an Instrument's rates risk moves when rates do. Reported with its shift size attached, because the number is meaningless without it. Distinct from a bond's convexity, which measures the curvature of a price already known in closed form.

## Risk stream

### Repricing Cycle

One pass of the risk engine that prices the newest market and publishes one Risk Update. Ticks that arrive while a cycle is running are coalesced into the next one: their events are kept, but only the newest market is priced.

### Risk Update

An incremental message to the front-end, one per Repricing Cycle, that carries only the Positions, rollups, and curve points that changed, stamped with the newest Tick it priced.

### Risk Snapshot

A complete picture of every Position, rollup, and curve point, sent when a client connects or has missed a Risk Update.
