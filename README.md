
# Comparative Analysis of Bitcoin and Gold Prices Across Global Markets

[![Licence](https://img.shields.io/badge/Licence-MIT-orange)](https://opensource.org/license/mit/)
[![python](https://img.shields.io/badge/Python-3.10-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=flat&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets)
[![Bitcoin](https://img.shields.io/badge/Bitcoin-FF9900?style=flat&logo=bitcoin&logoColor=white)](https://www.kaggle.com/datasets/varpit94/bitcoin-data-updated-till-26jun2021)
[![Gold](https://img.shields.io/badge/Gold-FFD700?style=flat&logo=gold&logoColor=white)](https://www.kaggle.com/datasets/odins0n/monthly-gold-prices)

## Overview

This project aims to conduct a comparative analysis of Bitcoin and gold prices across global markets, investigating how Bitcoin price fluctuations may impact gold prices in diverse economic and regulatory contexts. Utilizing datasets from Kaggle on Bitcoin and monthly gold prices, the project will encompass data collection, cleaning, and preparation, followed by analysis, with the ultimate goal of interpreting and understanding the relationship between these two valuable assets on a global scale.

In the `project` folder you find all additional informations about the project, like what datasources where used. 

The final report about the findings from the processed data you can see in the [report.ipynb](https://github.com/ruchita-nathani/made-template/blob/main/project/report.ipynb).



# Kaggle Authentication

For accessing the dataset provided by Kaggle, it is necessary to use their authentication to download the kaggle.json file and place it inside the `/project/kaggle.json` directory.

```
path: /project/kaggle.json
{ 
	"username":"ru*********i",
	"key":"d8b2**************************b2"
}
```
# Give an execute permission to the script file of pipeline
```[bash]
chmod +x ./project/pipeline.sh
```
# Run pipeline 
```[bash]
cd project && ./pipeline.sh
```
## Run test pipeline
```
cd project && ./tests.sh
```