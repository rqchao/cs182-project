import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

dropout_colors = {0.01: 'red', 0.05: 'blue'}

def process_lora_file(filename):
    sns.set_theme()

    # Initialize an empty DataFrame
    df = pd.DataFrame(columns=['r', 'lora_alpha', 'lora_dropout', 'Training Loss', 'Epoch'])

    # Read and parse the file
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('r='):
                parts = line.strip().split(', ')
                r = int(parts[0].split('=')[1])
                lora_alpha = int(parts[1].split('=')[1])
                lora_dropout = float(parts[2].split('=')[1])
            else:
                losses = np.array([float(x) for x in line.strip()[1:-1].split(', ')])
                for epoch, loss in enumerate(losses):
                    df = df._append({'r': r, 'lora_alpha': lora_alpha, 'lora_dropout': lora_dropout, 
                                    'Training Loss': loss, 'Epoch': epoch}, ignore_index=True)

    # Plotting
    df['Legend'] = 'r=' + df['r'].astype(str) + ', lora_alpha=' + df['lora_alpha'].astype(str) + ', lora_dropout=' + df['lora_dropout'].astype(str)
    for (r, lora_alpha), group in df.groupby(['r', 'lora_alpha']):
        plt.figure(figsize=(10, 6))
        sns.lineplot(
            x='Epoch', 
            y='Training Loss', 
            hue='Legend', 
            # palette=dropout_colors, 
            data=group
        )
        plt.title(f'Training Loss for r={r}, lora_alpha={lora_alpha}')
        plt.legend(loc='upper right')
        plt.subplots_adjust(left=0.05, bottom=0.08, right=1.00, top=1.00)
        plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
        plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
        plt.savefig(f'lora_vloss_plot_{r}_{lora_alpha}.png')


# def process_softprompting_file(filename):
#     sns.set_theme()

#     # Initialize an empty DataFrame
#     df = pd.DataFrame()

#     # Read and parse the file
#     with open(filename, 'r') as file:
#         lines = file.readlines()
#         for i in range(0, len(lines), 2):
#             header = lines[i].strip()
#             values = lines[i + 1].strip()

#             # Extracting data from the header
#             parts = header.split(', ')
#             prompt_tuning_init = parts[0].split('=')[1]
#             num_virtual_tokens = int(parts[1].split('=')[1])
            
#             # Extracting loss values
#             losses = np.array([float(x) for x in values[1:-1].split(',')])
#             for j in range(4):
#                 for epoch, loss in enumerate(losses):
#                     df = df._append({'prompt_tuning_init': prompt_tuning_init, 
#                                     'num_virtual_tokens': num_virtual_tokens, 
#                                     'Validation Loss': loss, 'Epoch': epoch, 'Set': j}, ignore_index=True)

#         # Calculate min, max, and average for each group
#         grouped = df.groupby(['prompt_tuning_init', 'num_virtual_tokens', 'Epoch'])
#         # df_agg = grouped.agg(['mean', 'min', 'max']).reset_index()
#         # df_agg.columns = ['prompt_tuning_init', 'num_virtual_tokens', 'Epoch', 'Mean', 'Min', 'Max']
#         df_agg = grouped['Validation Loss'].agg(['mean', 'min', 'max']).reset_index()



#     # Plotting
#     for prompt_tuning_init, group in df_agg.groupby('prompt_tuning_init'):
#         plt.figure(figsize=(10, 6))
#         plt.title(f'Averaged Validation Loss per Epoch for {prompt_tuning_init}')
#         for num_virtual_tokens, sub_group in group.groupby('num_virtual_tokens'):
#             plt.fill_between(sub_group['Epoch'], sub_group['min'], sub_group['max'], alpha=0.3)
#             sns.lineplot(
#                 x='Epoch', 
#                 y='mean', 
#                 # hue='num_virtual_tokens', 
#                 label=str(num_virtual_tokens),
#                 # palette='tab10', 
#                 data=sub_group,
#             )
#         # plt.subplots_adjust(left=0.1, bottom=0.08, right=0.97, top=0.95)
#         plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
#         plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
#         plt.legend(title='num_virtual_tokens', loc='upper right')
#         plt.savefig(f'soft_prompt{prompt_tuning_init}.png')


# Modify the following line to change the data source
process_file('./soft_test.txt')
