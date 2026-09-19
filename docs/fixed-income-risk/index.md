# Building a Fixed Income Risk Engine

*How real-time risk works, and a working engine to prove it.*

A developer joining a bank, an asset manager or a fintech hears "DV01", "the curve", "marks" and
"reprice" in the first week. This series explains what those words mean in a real fixed income risk
system, and why such systems are built the way they are, using a complete, working engine you can run
yourself.

The engine simulates a market anchored to the real US Treasury curve, holds a Book of Treasuries,
Treasury futures, corporate bonds and interest rate swaps, and reprices it selectively as the market
moves, streaming risk to a browser.

## Reading order

1. [What a risk system is for](01-what-a-risk-system-is-for.md): What a fixed income desk holds, why it needs continuous risk, and a tour of the running engine.
2. [The yield curve](02-the-yield-curve.md): From published par yields to zero rates and discount factors: building today's real Treasury curve.
3. [Moving the curve through time](03-moving-the-curve-through-time.md): Hull-White, simulated time, and why the Valuation Date moves only at Day Rollover.
4. [Pricing a bond and measuring its risk](04-pricing-a-bond-and-measuring-its-risk.md): Clean and dirty prices, DV01, Bucketed DV01, and rolling risk up across a Book.
5. [Real-time risk without recomputing everything](05-real-time-risk-without-recomputing-everything.md): Risk Factors, Dependencies, Materiality Thresholds and Staleness: the central engineering problem.
6. [Treasury futures](06-treasury-futures.md): The cheapest-to-deliver, conversion factors, the Basis, and why a future carries risk but no value.
7. [Credit and the missing tape](07-credit-and-the-missing-tape.md): Spreads, Latent Spreads vs Marks, Prints and Quotes, Matrix Pricing and CS01.
8. [When credit breaks](08-when-credit-breaks.md): Credit Events, Rating Migrations, and Dependencies that change while the engine runs.
9. [Interest rate swaps](09-interest-rate-swaps.md): Fixed vs floating, Fixings, the par trick, and single-curve vs OIS.
10. [Correlation](10-correlation.md): Flight to quality, and generating correlated shocks with a Cholesky factor.
11. [The runtime](11-the-runtime.md): Threads, a latest-wins hand-off, coalescing, a worker pool, and streaming risk to the browser.

Each article stands alone, and every term links to the [glossary](glossary.md).

!!! tip "Run the demo"

    Every number and screenshot in the series comes from one reproducible run:

    ```bash
    git clone https://github.com/suhasghorp/fixed-income-risk-engine.git
    cd fixed-income-risk-engine/backend && mvn spring-boot:run -Dspring-boot.run.profiles=demo
    # in another terminal
    cd fixed-income-risk-engine/frontend && npm install && npm run dev
    ```

    Then open <http://localhost:5173>. Articles add `--risk.simulation.stop-at-tick=N` to freeze the run at
    the exact state they describe.
