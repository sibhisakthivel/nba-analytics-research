"""
NBA Analytics Research Portfolio - Streamlit app.
Showcases three research studies with expandable summaries.
"""

import streamlit as st

st.set_page_config(
    page_title="NBA Analytics Research | Portfolio",
    page_icon="🏀",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for larger fonts and layout
st.markdown("""
<style>
    h1 {
        font-size: 3.5rem !important;
        line-height: 1.2 !important;
        text-align: center !important;
    }
    h2 {
        font-size: 2.5rem !important;
        text-align: center !important;
    }
    h3 {
        font-size: 2rem !important;
    }
    h4 {
        font-size: 1.75rem !important;
    }
    .stMarkdown p {
        font-size: 1.25rem !important;
        line-height: 1.6 !important;
    }
    .stMarkdown li {
        font-size: 1.25rem !important;
        line-height: 1.6 !important;
    }
    .portfolio-header {
        position: relative;
        left: 50%;
        transform: translateX(-50%);
        width: fit-content;
        text-align: center;
    }
    .portfolio-description {
        font-size: 1.75rem !important;
        line-height: 1.6 !important;
    }
    /* Override .stMarkdown p for the description (higher specificity) */
    .stMarkdown p.portfolio-description {
        font-size: 1.75rem !important;
        line-height: 1.6 !important;
    }
    main .block-container {
        max-width: 88rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }
    /* Custom study dropdowns - bar style, full title inside bar, ">" aligned across bars */
    .study-details {
        width: 100%;
        margin-bottom: 0.75rem;
    }
    .study-details summary {
        display: flex;
        align-items: center;
        padding: 1rem 1.25rem;
        font-size: 1.7rem;
        line-height: 1.4;
        cursor: pointer;
        list-style: none;
        white-space: nowrap;
        overflow: visible;
        background: rgba(151, 166, 195, 0.15);
        border: 1px solid rgba(151, 166, 195, 0.25);
        border-radius: 0.5rem;
        transition: background 0.15s ease;
        box-sizing: border-box;
    }
    .study-details summary:hover {
        background: rgba(151, 166, 195, 0.22);
    }
    .study-details[open] summary {
        border-radius: 0.5rem 0.5rem 0 0;
    }
    .study-details summary::-webkit-details-marker { display: none; }
    .study-details summary::before {
        content: ">";
        flex-shrink: 0;
        width: 1.5rem;
        min-width: 1.5rem;
        text-align: left;
    }
    .study-details[open] summary::before { content: "\\25BC"; width: 1.5rem; min-width: 1.5rem; }
    .study-content {
        padding: 1rem 1.25rem 1.5rem;
        background: rgba(151, 166, 195, 0.08);
        border: 1px solid rgba(151, 166, 195, 0.25);
        border-top: none;
        border-radius: 0 0 0.5rem 0.5rem;
    }
    .study-content h4 { margin-top: 1rem; margin-bottom: 0.5rem; }
    .study-content h4:first-of-type { margin-top: 0; }
    .study-content p, .study-content ul { margin-bottom: 0.75rem; font-size: 1.25rem; line-height: 1.6; }
    .study-link { margin-top: 0; margin-bottom: 1rem; font-size: 1.1rem; }
    .study-link a { color: #6ea8fe; text-decoration: none; }
    .study-link a:hover { text-decoration: underline; }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Header & description
# -----------------------------------------------------------------------------
st.markdown('''
<div class="portfolio-header">
    <h1 style="white-space: nowrap;">NBA Analytics Research Portfolio</h1>
    <h2 style="font-size: 2rem; font-weight: normal; margin-top: -0.5rem;">Sibhi Sakthivel</h2>
</div>
''', unsafe_allow_html=True)
st.markdown("---")
st.markdown(
    '<p class="portfolio-description" style="font-size: 1.75rem; line-height: 1.6;">'
    'A portfolio of NBA research studies driven by curiosity about what influences '
    'player performance, explored through data science with a strong emphasis on '
    'statistical testing and analysis.</p>',
    unsafe_allow_html=True,
)
st.markdown("---")

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# Study 1: Streak Performance v1
# -----------------------------------------------------------------------------
st.markdown("""
<details class="study-details">
<summary>Study 1: NBA Scoring Streak Performance Analysis (v1)</summary>
<div class="study-content">
<p class="study-link"><a href="https://github.com/sibhisakthivel/nba-analytics-research/tree/main/studies/streak_performance/streak_analysis_v1" target="_blank" rel="noopener noreferrer">View study files →</a></p>
<h4>Summary</h4>
<p>This study tests whether NBA scoring streaks, "hot" or "cold" players, meaningfully
affect next-game scoring once player-specific baselines and uncertainty are accounted for.
It uses game-level data, rolling season baselines, and formal hypothesis testing
(player-level deviations, one-sample t-tests, bootstrap CIs) to separate real effects
from randomness and regression to the mean.</p>
<h4>Key findings</h4>
<ul>
<li>Average player-level deviations from baseline <strong>after</strong> scoring streaks are <strong>near zero</strong>.</li>
<li>Global tests <strong>fail to reject</strong> the null of no effect; bootstrap CIs include zero.</li>
<li>Stratified checks (streak direction, length) show <strong>no robust conditional patterns</strong>.</li>
<li>Streaks do <strong>not</strong> provide reliable predictive signal for next-game scoring once
player heterogeneity and uncertainty are properly handled.</li>
</ul>
<h4>Takeaways</h4>
<p>Despite "hot hand" narratives, streak-based effects largely vanish under rigorous
statistical analysis. The work underscores baseline-centered analysis, aggregation
before inference, and explicit uncertainty quantification.</p>
</div>
</details>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Study 2: Streak Performance v2
# -----------------------------------------------------------------------------
st.markdown("""
<details class="study-details">
<summary>Study 2: NBA Scoring Streak Performance Analysis (v2)</summary>
<div class="study-content">
<p class="study-link"><a href="https://github.com/sibhisakthivel/nba-analytics-research/tree/main/studies/streak_performance/streak_analysis_v2" target="_blank" rel="noopener noreferrer">View study files →</a></p>
<h4>Summary</h4>
<p>Building on v1, this study asks whether streaks add <strong>incremental explanatory value</strong>
once core game context (opponent defensive strength, home/away, etc.) is included.
It uses an experimentation-style setup: a <strong>context-only</strong> model as control vs. a
<strong>context-plus-streak</strong> model as treatment. The aim is to test if streak information
improves explanatory power, with clear uncertainty quantification and practical relevance.</p>
<h4>Research question</h4>
<p><strong>Do scoring streaks explain additional variation in next-game scoring beyond
player baselines and game context?</strong></p>
<h4>Approach</h4>
<ul>
<li><strong>Null:</strong> Streak indicators do not explain extra variation after controlling for
baselines and context.</li>
<li><strong>Alternative:</strong> Streaks do explain additional variation.</li>
<li>Emphasizes regression-based inference, baseline construction, and experiment-style
decision reasoning rather than causal claims about psychology or momentum.</li>
</ul>
</div>
</details>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Study 3: Travel Fatigue
# -----------------------------------------------------------------------------
st.markdown("""
<details class="study-details">
<summary>Study 3: NBA Travel Fatigue & Schedule Density Analysis</summary>
<div class="study-content">
<p class="study-link"><a href="https://github.com/sibhisakthivel/nba-analytics-research/tree/main/studies/travel_fatigue" target="_blank" rel="noopener noreferrer">View study files →</a></p>
<h4>Summary</h4>
<p>This study examines how NBA travel, rest patterns, and schedule density affect
team performance. Using historical schedules and team-level game data, it constructs
fatigue indicators (rest days, back-to-backs, travel distance, time-zone changes)
and evaluates their impact on defensive efficiency and win probability.</p>
<h4>Key findings</h4>
<ul>
<li>Schedule compression and short rest are linked to <strong>modest but consistent</strong>
performance effects.</li>
<li><strong>Defensive efficiency</strong> (eFG%) improves when opponents are on the second night
of a back-to-back.</li>
<li>League scheduling changes since ~2014 have <strong>reduced</strong> overall fatigue exposure.</li>
<li>Schedule-related advantages typically account for about <strong>±1–2 wins per team
per season</strong> (from logistic regression with counterfactual neutralization).</li>
</ul>
<h4>Methodology</h4>
<p>Combines schedule and travel metrics, exploratory and league-wide trend analysis,
performance case studies (e.g., defensive efficiency under rest-disadvantaged
opponents), and schedule-adjusted win modeling.</p>
</div>
</details>
""", unsafe_allow_html=True)

st.markdown("---")

