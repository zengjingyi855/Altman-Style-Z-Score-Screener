# Altman-Style-Z-Score-Screener

An interactive Fintech web app for corporate bankruptcy prediction, using the Altman Z-Score model and TEJ data. Built with Python &amp; Streamlit.

## Project Snapshot

This project implements an **adapted Altman-style Z-Score framework** in Python to screen for financial distress using firm-level accounting ratios. The analysis is built in a Jupyter Notebook and uses the **Taiwan Economic Journal Bankruptcy Prediction Dataset** from Kaggle.

Rather than building a black-box model, the project focuses on a more practical question for finance and risk analysis: **can a transparent accounting-based score meaningfully rank firms by bankruptcy risk in this sample?**

### Highlights

- Built an interpretable **financial distress screening workflow** in Python
- Mapped available dataset variables into the **five classic Altman dimensions**
- Evaluated score quality with **ROC-AUC, PR-AUC, decile analysis, and robustness checks**
- Showed that the score works better as a **relative risk-ranking tool** than as a direct application of the original Altman cutoff zones

## Why This Project Matters

This notebook is a small but complete example of how a classic finance framework can be translated into a structured data-analysis project.

It demonstrates three things clearly:

- how to turn accounting ratios into an interpretable composite risk score
- how to evaluate a screening tool in an **imbalanced dataset**
- how to discuss model usefulness and model limits in a disciplined way

That makes the project suitable for coursework, GitHub portfolio display, and applications for internships in areas such as **finance, risk analysis, credit analysis, and data analytics**.

## Dataset

- **Dataset**: Taiwan Economic Journal Bankruptcy Prediction Dataset
- **Source**: Kaggle
- **Coverage noted in the notebook**: 2015 to 2024
- **Sample size**: 6,819 firm observations
- **Bankrupt observations**: 220
- **Non-bankrupt observations**: 6,599
- **Bankrupt share**: 3.23%

The notebook checks the selected variables used in score construction and reports:

- no missing values in the selected fields
- no duplicate rows in the raw dataset

## Business Question

The project focuses on one core question:

**Can an adapted Altman-style score separate bankrupt firms from non-bankrupt firms in this dataset, and can it provide a useful ranking of relative financial distress risk?**

This is a screening problem rather than a full prediction system. The aim is to build a score that is easy to interpret, easy to reproduce, and still informative in practice.

## Method

The notebook applies an **adapted Altman-style score**, not a literal reconstruction of the original Altman Z-Score. The reason is that the dataset provides ratio-based proxy variables rather than the original raw statement inputs.

The composite score is:

```text
Z = 1.2X1 + 1.4X2 + 3.3X3 + 0.6X4 + 1.0X5
```

where:

- **X1 Liquidity** = Working Capital / Total Assets
- **X2 Cumulative Profitability** = Retained Earnings / Total Assets
- **X3 Core Earnings Power** = ROA(C) before interest and depreciation before interest
- **X4 Solvency** = Equity / Liability
- **X5 Operating Efficiency** = Total Income / Total Expense

The notebook also reports the classical Altman reference zones:

- **Distress**: Z < 1.81
- **Grey**: 1.81 ≤ Z ≤ 2.99
- **Safe**: Z > 2.99

However, these thresholds are treated as **reference only**, because the available inputs are scaled proxy ratios rather than the exact accounting items used in the original model.

## Analytical Workflow

The notebook follows a full analysis pipeline:

1. Load the dataset and inspect relevant variables
2. Check missing values and duplicates
3. Map available fields to Altman-style components
4. Construct the composite Z-Score
5. Compare score distributions by bankruptcy status
6. Evaluate ranking performance with ROC-AUC and PR-AUC
7. Group firms by score deciles and compare bankruptcy rates
8. Review classical risk-zone classification for reference
9. Visualize score distributions, curves, and component behaviour
10. Perform a robustness check after winsorizing extreme values

## Key Results

### 1. Bankrupt firms have lower Altman-style scores

| Group | Mean Z-Score | Median Z-Score | Std. Dev. | Count |
|---|---:|---:|---:|---:|
| Non-bankrupt | 3.9977 | 3.9829 | 0.2463 | 6599 |
| Bankrupt | 3.5660 | 3.6355 | 0.3139 | 220 |

This shows that firms labelled as bankrupt tend to have systematically weaker overall financial profiles in this sample.

### 2. The score ranks risk well despite class imbalance

Because only 3.23% of observations are bankrupt, simple accuracy would not be meaningful. The notebook therefore evaluates ranking performance directly:

- **ROC-AUC**: 0.9021
- **PR-AUC**: 0.2690

These results indicate that lower scores are strongly associated with higher bankruptcy risk.

### 3. Decile analysis is more informative than direct use of classical cutoffs

| Risk Decile | Observations | Bankrupt Count | Bankruptcy Rate (%) |
|---|---:|---:|---:|
| D1 | 682 | 135 | 19.79 |
| D2 | 682 | 48 | 7.04 |
| D3 | 682 | 18 | 2.64 |
| D4 | 682 | 9 | 1.32 |
| D5 | 682 | 6 | 0.88 |
| D6 | 681 | 2 | 0.29 |
| D7 | 682 | 0 | 0.00 |
| D8 | 682 | 2 | 0.29 |
| D9 | 682 | 0 | 0.00 |
| D10 | 682 | 0 | 0.00 |

The lowest-score decile has a bankruptcy rate of **19.79%**, while the highest deciles are close to **0%**. In this dataset, the score is more useful as a **relative ranking tool** than as a literal application of the original threshold system.

### 4. Classical Altman zones have limited transferability here

| Risk Zone | Observations | Bankrupt Count | Bankruptcy Rate (%) |
|---|---:|---:|---:|
| Distress | 3 | 0 | 0.00 |
| Grey | 23 | 14 | 60.87 |
| Safe | 6793 | 206 | 3.03 |

Almost all observations fall into the safe zone. This suggests that the classical cutoff values are not well calibrated to this proxy-ratio dataset.

### 5. The main findings remain stable after winsorization

After winsorizing the five component ratios at the 1st and 99th percentiles, the results remain similar:

- **Robust ROC-AUC**: 0.9046
- **Robust PR-AUC**: 0.2851

| Group | Mean Z-Score | Median Z-Score | Std. Dev. | Count |
|---|---:|---:|---:|---:|
| Non-bankrupt | 3.9974 | 3.9829 | 0.2275 | 6599 |
| Bankrupt | 3.6102 | 3.6411 | 0.2146 | 220 |

This supports the view that the main result is not driven only by a small number of extreme values.

## Visual Outputs

The notebook includes supporting visualizations such as:

- ROC curve
- precision-recall curve
- bankruptcy rate by Z-Score decile
- density comparison of Z-Score distributions
- Spearman correlation heatmap
- component-level boxplots by bankruptcy status

These plots help connect the composite score back to the underlying financial ratios.

## Skills Demonstrated

This project demonstrates practical skills that transfer well to internship work:

- **Financial analysis**: interpreting liquidity, profitability, solvency, and efficiency ratios
- **Python data analysis**: using pandas and numpy for cleaning, transformation, and score construction
- **Model evaluation**: assessing performance in an imbalanced setting with ROC-AUC, PR-AUC, and decile ranking
- **Data visualization**: presenting model behaviour clearly with charts and summary tables
- **Risk interpretation**: distinguishing between score usefulness, calibration issues, and business limits
- **Analytical communication**: writing results and limitations in a clear and disciplined way

## Tools and Libraries

The notebook uses:

- Python
- Jupyter Notebook
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

Install dependencies with:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

## How to Run

1. Place `data.csv` in the same folder as the notebook.
2. Open the notebook in Jupyter Notebook or JupyterLab.
3. Run the cells from top to bottom.

```bash
jupyter notebook
```

The notebook currently loads the dataset with:

```python
df = pd.read_csv("data.csv")
```

## What I Did in This Project

The value of this project is not just the final metric. It is the full workflow:

- selected a finance-relevant problem with a clear screening objective
- translated a classical model into a reproducible Python notebook
- handled basic data checks before analysis
- evaluated the score with appropriate metrics for an imbalanced dataset
- tested robustness instead of relying on one headline result
- explained why a model can be useful even when classical thresholds do not transfer perfectly

## Limitations

This project is intentionally presented as a **screening exercise**, not a production-grade bankruptcy prediction system.

Main limitations include:

- the notebook uses **proxy ratios**, not the exact original Altman inputs
- the score is **not recalibrated** for this specific dataset
- the original Altman model was developed in a different industrial context and may fit modern asset-light firms less well
- the analysis uses **accounting variables only**, so it does not include market-based or macroeconomic information
- winsorization is helpful, but it is only one robustness check

These limits do not remove the value of the project. They define the scope of what the score can and cannot say.

## Possible Next Steps

Reasonable extensions would include:

- comparing the Altman-style score with logistic regression or tree-based benchmarks
- adding train-test split validation
- analysing results by year or industry
- incorporating market-based indicators
- packaging the notebook into a lightweight dashboard or app

## Conclusion

This project shows that an adapted Altman-style score can still provide useful **relative bankruptcy-risk screening value** when it is implemented carefully and interpreted conservatively.

The strongest part of the project is not model novelty. It is the combination of:

- clear financial logic
- transparent implementation
- appropriate evaluation for an imbalanced sample
- honest discussion of model boundaries

For internship use, this is the kind of project that can credibly show **analytical thinking, Python execution, and finance-oriented interpretation** without overstating what the model can do.
