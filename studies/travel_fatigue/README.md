# NBA Travel Fatigue & Schedule Density Analysis

This study examines how NBA travel demands, rest patterns, and schedule density influence team performance over the course of a season. Using historical NBA schedules and team-level game data, the analysis quantifies fatigue exposure and evaluates its impact on defensive efficiency and win probability.

The project focuses on understanding whether structural scheduling factors, such as back-to-backs, compressed game stretches, and long travel sequences, produce measurable competitive advantages or disadvantages across teams.

## Core Questions

- How common are high-density schedule stretches (e.g., 4 games in 6 nights) across NBA seasons?
- How have league-wide travel and rest patterns evolved over time?
- Do rest and travel disadvantages affect on-court performance metrics?
- How many wins can be attributed to schedule-related advantages or disadvantages?

## Methodology Overview

The analysis combines data engineering, exploratory analysis, visualization, and statistical modeling:

- **Schedule & Travel Metrics**  
  Constructed team-level fatigue indicators including rest days, back-to-back flags, rolling travel distance, and time-zone changes using historical NBA schedules and arena location data.

- **Exploratory & League-Wide Analysis**  
  Quantified schedule density trends from 2014–2024, identifying how often teams face compressed stretches and how league scheduling has changed over time.

- **Performance Case Studies**  
  Evaluated defensive efficiency (eFG%) under rest-disadvantaged opponent conditions to assess short-term fatigue effects.

- **Schedule-Adjusted Win Modeling**  
  Applied logistic regression with counterfactual neutralization to estimate the number of wins gained or lost due solely to schedule-related factors.

## Key Findings

- Schedule compression and short rest periods are associated with modest but consistent performance effects.
- Defensive efficiency improves slightly when opponents are on the second night of a back-to-back.
- League scheduling reforms since 2014 have reduced overall fatigue exposure.
- Schedule-related advantages typically account for approximately ±1–2 wins per team per season.

## Structure

```text
travel_fatigue/
├── notebooks/     # Analysis notebooks
├── data/          # Raw input datasets used in the study
├── README.md
