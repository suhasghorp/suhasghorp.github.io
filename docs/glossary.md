# Glossary

Every term the series uses, defined exactly as the engine uses it. Hover a term in any article to see
its definition.

## Holdings

### Instrument

The terms of a contract (a bond, future, or swap), priced per unit of notional. Holds no quantity.

### Position

A signed quantity of one Instrument held in a Book. Several Positions can reference the same Instrument. For a swap, the quantity is its notional and is always positive; paying or receiving fixed is part of the Instrument.

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

Where the day's starting Treasury curve came from: live, cached, or bundled.

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

## Sensitivities

### DV01

The change in value for a 1bp parallel shift of the zero rates on the model's output curve.

*In plain words:* How many dollars a Position gains if interest rates fall by one hundredth of a percent. The bigger the number, the more rate risk.

### Bucketed DV01

DV01 measured by shifting the zero rate at a single Pillar, with the shift fading linearly to zero at the neighbouring Pillars.

*In plain words:* DV01 split up by maturity, so you can see whether the rate risk sits in the 2-year, 10-year or 30-year part of the curve.

### CS01

The change in value for a 1bp shift in an issuer's Mark.

*In plain words:* Like DV01, but for credit spreads: how many dollars a Position gains if its issuer's spread tightens by one hundredth of a percent.

### Reporting Currency

The currency all Book-level risk is expressed in (USD). Values in other currencies are converted at the current FX spot rate.

## Risk stream

### Repricing Cycle

One pass of the risk engine that prices the newest market and publishes one Risk Update. Ticks that arrive while a cycle is running are coalesced into the next one: their events are kept, but only the newest market is priced.

### Risk Update

An incremental message to the front-end, one per Repricing Cycle, that carries only the Positions, rollups, and curve points that changed, stamped with the newest Tick it priced.

### Risk Snapshot

A complete picture of every Position, rollup, and curve point, sent when a client connects or has missed a Risk Update.
