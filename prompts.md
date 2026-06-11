# Live demo prompts — AI for the Wet Lab

Copy-paste these during the workshop. Run them in Claude Code inside this folder.

---

## Demo 1 — scite MCP literature search

```
Use scite to find recent (post-2024) papers on CUT&RUN protocols
for low-input samples. For the top 3 results, summarise the
protocol and tell me whether subsequent papers have supported
or contrasted the approach. Give me DOI links for everything.
```

If `scite` is not yet installed:

```
claude mcp add scite --scope user -- npx -y @scite/mcp-server
```

---

## Demo 2 — messy CSV → plot (use Plan mode: Shift+Tab twice)

```
I have @demo/messy_plate_reader.csv. The first 15 rows are
metadata, then a blank row, then the header. Read the data
starting at the header, drop blank rows, then:

  1. Subtract the BLANK mean from every Fluorescence reading
  2. Use the STD_* rows to build a linear standard curve
  3. Compute IL-6 concentration (ng/mL) for SAMPLE_A, B, C
  4. Plot a bar chart of mean concentration per sample with
     SD error bars
  5. Save the figure to figures/il6_quant.png at 300 dpi

Use pandas + matplotlib. Comment every line in plain English.
Show me the plan before writing any code.
```

---

## Demo 3 — "Explain it like I'm a biologist"

```
Open @demo/handed_down_script.py. I'm a wet-lab biologist
with no formal CS training. Walk me through what this script
does in plain English, line by line.

Then tell me exactly which line I'd change to:
  (a) point it at a different input CSV
  (b) save the output PNG at 600 dpi instead of 150
  (c) use a different colour for the bars
```

---

## Bonus — the Dummy Data pattern

```
Here is a 5-row mock dataset that has the same shape as my
real patient data (which I cannot share):

@demo/mock_data_template.csv

Write me a Python script that:
  1. Loads a CSV with these columns
  2. Drops rows where qc_flag != "pass"
  3. Computes mean assay_value per treatment x timepoint
  4. Runs a Mann-Whitney U test comparing drug vs vehicle
     at the 24-hour timepoint
  5. Prints a tidy summary table

I will run the script myself on the real data. The mock data
never sees the real values.
```
