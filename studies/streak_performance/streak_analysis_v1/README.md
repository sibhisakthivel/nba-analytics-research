# NBA Scoring Streak Performance Analysis (v1)

This study examines whether NBA scoring streaks—commonly described as players being “hot” or “cold”—meaningfully affect next-game scoring performance once player-specific baselines and uncertainty are properly accounted for.

Using game-level NBA player data and formal statistical inference, the analysis tests whether streak-conditioned performance differs from baseline behavior, or whether apparent streak effects are largely attributable to randomness and regression to the mean.

This version represents the initial, completed analysis and is preserved as a historical snapshot of methodology and results.

---

## Research Questions

The study is structured around two primary questions:

1. **Global Effect**  
   Do scoring streaks, on average, change a player’s probability of exceeding their typical scoring performance in the following game?

2. **Conditional Effects**  
   If any effect exists, does it vary by:
   - streak direction (over-performance vs. under-performance)
   - streak length (short vs. extended streaks)?

---

## Methodology Overview

The analysis follows a standard data science workflow with a strong emphasis on statistical rigor and uncertainty-aware conclusions:

- **Data Construction**  
  - Game-level player scoring data were processed using SQL and Python.
  - Analysis was restricted to high-usage players to reduce noise.
  - Player-specific baselines were defined using rolling season averages.
  - All streak indicators were constructed strictly from prior games to preserve temporal integrity.

- **Exploratory Analysis**  
  - Examined streak frequencies and apparent performance patterns.
  - Identified visually compelling effects that warranted formal testing.

- **Formal Inference**  
  - Computed player-level deviations between streak-conditioned performance and baseline rates.
  - Conducted global inference using one-sample t-tests and bootstrap confidence intervals.
  - Performed stratified analyses by streak direction and length as exploratory checks.

Inference was conducted at the **player level** rather than the game level to preserve independence and avoid inflated sample sizes.

---

## Key Findings

- Average player-level deviations from baseline following scoring streaks are **near zero**.
- Global hypothesis tests fail to reject the null hypothesis of no effect.
- Bootstrap confidence intervals comfortably include zero.
- Stratified analyses show no consistent or robust conditional patterns.
- Any isolated nominal significance is small in magnitude and not stable across bins.

Overall, scoring streaks do **not** appear to provide reliable predictive signal for next-game scoring performance once player heterogeneity and uncertainty are properly accounted for.

---

## Interpretation

Despite strong intuitive narratives around “hot” and “cold” players, streak-based effects largely disappear under formal statistical scrutiny. Apparent patterns observed during exploratory analysis are consistent with random variation around player-specific baselines rather than systematic performance shifts.

This study highlights the importance of:
- baseline-centered analysis
- aggregation before inference
- explicit uncertainty quantification

Negative results, when obtained through careful methodology, are informative and valuable.

---

## Structure

```text
streak_analysis_v1/
├── notebooks/
│   ├── 01_dataset_construction.ipynb
│   ├── 02_eda_streaks.ipynb
│   └── 03_formal_inference_and_hypothesis_testing.ipynb
├── data/        # Supporting data utilities and raw inputs
├── sql/         # Database schema and feature construction logic
└── README.md
```

## Notes

This version was conducted using an earlier local database setup and standalone workflow. While the analysis logic and conclusions remain valid, the data pipeline is preserved for reference rather than ongoing reuse.

Future versions of this study rebuild the pipeline and methodology using updated infrastructure and expanded statistical techniques.