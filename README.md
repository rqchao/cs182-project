# From Fiction to Function: Leveraging Fine-Tuned Open-Domain Models for Character Mimicry

## Overview
This repository contains a collection of experiments and analyses focused on the parameter-efficient fine-tuning of Large Language Models (LLMs) to mimic fictional characters. We use Spongebob as an example. The experiments are primarily conducted using Python and Jupyter Notebooks.

## Repository Structure
Below is the structure of the repository with a brief description of each component:

- `README.md`: This file, providing an overview and instructions for the repository.
- `data`: Directory containing datasets used in the experiments.
- `falcon_lora.ipynb`: Jupyter Notebook for the Falcon LoRa experiment.
- `gpt_finetune.ipynb`: Jupyter Notebook for fine-tuning GPT models.
- `graphing`: Folder containing scripts and notebooks for graphing and visualizing data with custom formatting.
- `outputs`: Directory where output files from experiments are stored.
- `peft.ipynb`: Jupyter Notebook for experimenting with PEFT (Performance-Efficient Fine-Tuning).
- `prefix_tuning.ipynb`: Jupyter Notebook for prefix tuning experiments.
- `prompt_tuning.ipynb`: Jupyter Notebook for prompt tuning experiments.
- `requirements.txt`: File listing the necessary Python packages.
- `scripts`: Miscellaneous scripts used in various parts of the project.
- `soft_prompt_tuning.ipynb`: Jupyter Notebook for soft prompt tuning experiments.
- `temp.py`: Temporary Python script for auxiliary purposes.
- `testing`: Directory for testing scripts and experimental code.

## Getting Started

### Installation
To get started, clone the repository and install the required packages:

```bash
git clone [repository URL]
cd [repository name]
pip install -r requirements.txt
```

### Running the Experiments
Each experiment is contained within its own Jupyter Notebook. To run an experiment:

1. Navigate to the notebook file (e.g., `gpt_finetune.ipynb`).
2. Open the notebook using Jupyter Lab or Jupyter Notebook.
3. Run the cells in the notebook sequentially.

These notebooks were run on a set of 8GB GPUs and should take a couple of hours to execute completely. 

### Validating the Results
After running the experiments, you can validate the results by comparing the generated graphs and outputs with those in the `outputs` directory. The graphs and output metrics should be comparable to ours with reasonable accuracy if the experiments are executed correctly. We generally saved our data and and re-graphed them using the scripts in the `graphing` library, but this was purely for formatting purposes. Given constraints, we were unable to save weights.

## Support
For any queries or issues, please contact us at rqchao@berkeley.edu, or any of the other listed authors.

---
