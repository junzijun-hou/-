# Mobile Phone Battery SOC Dataset Resources

This document compiles resources for datasets related to mobile phone battery SOC (State of Charge).

## What is SOC?

SOC (State of Charge) represents the remaining battery capacity as a percentage of total capacity. Accurate SOC estimation is crucial for Battery Management Systems (BMS) to:
- Predict remaining battery runtime
- Prevent overcharging and over-discharging
- Extend battery lifespan
- Optimize charging strategies

## Publicly Available Battery Datasets

### 1. NASA Battery Dataset
**Source**: NASA Ames Research Center  
**Link**: https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/  
**Description**: 
- Li-ion battery charge/discharge cycle data under various operating conditions
- Includes voltage, current, temperature, capacity parameters
- Suitable for battery life prediction and SOC estimation research
- Format: MATLAB files (.mat)

**Features**:
- Battery type: 18650 Li-ion batteries
- Test conditions: Multiple charge/discharge rates and temperatures
- Cycle count: Hundreds of cycles
- Applications: Aerospace, electric vehicles

### 2. Oxford Battery Degradation Dataset
**Source**: University of Oxford  
**Link**: https://ora.ox.ac.uk/objects/uuid:03ba4b01-cfed-46d3-9b1a-7d4a7bdf6fac  
**Description**:
- Commercial Li-ion battery aging and degradation data
- Test data under different charge/discharge protocols
- Includes voltage, current, temperature, internal resistance
- Format: CSV and MATLAB files

**Features**:
- Battery type: Commercial Li-ion batteries
- Test period: Long-term cycling tests
- Data dimensions: Multi-dimensional features
- Applications: Battery health assessment, SOC/SOH estimation

### 3. University of Maryland Battery Dataset (CALCE)
**Source**: Center for Advanced Life Cycle Engineering, University of Maryland  
**Link**: https://web.calce.umd.edu/batteries/data.htm  
**Description**:
- Test data for various Li-ion batteries
- Battery performance under different temperatures and load conditions
- Battery cycle life data
- Format: Excel and MATLAB files

**Features**:
- Multiple battery types: Cylindrical, prismatic, pouch cells
- Test environments: Various temperature and load conditions
- Data completeness: Complete charge/discharge curves
- Applications: Battery modeling, SOC estimation, life prediction

### 4. Samsung SDI Battery Dataset
**Source**: Academic research collaboration projects  
**Link**: https://data.mendeley.com/datasets/cp3473x7xv/3  
**Description**:
- Li-ion battery data for mobile phones and electric vehicles
- Fast charging and standard charging data
- Temperature, voltage, current time series data

**Features**:
- Real-world application scenarios
- Multiple charging strategies
- High sampling frequency
- Applications: Mobile battery management, fast charging research

### 5. LG Battery Dataset
**Source**: Korean battery research institutions  
**Link**: https://data.mendeley.com/datasets/wykht8y7tg/1  
**Description**:
- Commercial 18650 Li-ion battery data
- Performance data at different ambient temperatures
- Battery aging process data

**Features**:
- Full lifecycle coverage
- Multi-temperature testing
- Detailed electrochemical parameters
- Applications: Joint SOC/SOH estimation

### 6. MIT Battery Dataset
**Source**: Massachusetts Institute of Technology  
**Link**: https://data.matr.io/1/  
**Description**:
- Fast charging optimization research data
- Data from 124 commercial Li-ion batteries
- Performance comparison under different charging strategies

**Features**:
- Large-scale parallel testing
- Focus on fast charging scenarios
- Machine learning friendly format
- Applications: Fast charging optimization, battery life prediction

### 7. Toyota Battery Dataset
**Source**: Toyota Research Institute  
**Link**: https://data.matr.io/3/  
**Description**:
- Electric vehicle battery data
- Long-term cycling test data
- Calendar aging and cycle aging data

**Features**:
- Automotive-grade batteries
- Long-term test data (2-3 years)
- Real usage scenario simulation
- Applications: Electric vehicle battery management

## Chinese Domestic Datasets

### 8. Beijing Institute of Technology Battery Dataset
**Source**: National Engineering Laboratory for Electric Vehicles, BIT  
**Description**:
- Electric vehicle power battery data
- Real vehicle operation data and laboratory test data
- Usually requires academic collaboration to access

### 9. Chinese Academy of Sciences Battery Data
**Source**: Institute of Physics, CAS  
**Description**:
- New battery material test data
- Various battery chemistry systems
- Access through academic channels

### 10. Tsinghua University Battery Data
**Source**: Department of Automotive Engineering, Tsinghua University  
**Description**:
- Electric vehicle battery pack data
- BMS data and thermal management data
- Available for academic research upon application

## Data Acquisition Channels

### Academic Databases
- **Kaggle**: https://www.kaggle.com/ (search "battery" "SOC" "lithium-ion")
- **IEEE DataPort**: https://ieee-dataport.org/
- **Mendeley Data**: https://data.mendeley.com/
- **Zenodo**: https://zenodo.org/

### Open Source Platforms
- **GitHub**: Search for related projects, many researchers share data and code
- **Google Dataset Search**: https://datasetsearch.research.google.com/

### Research Papers with Accompanying Data
Many papers published in these journals include datasets:
- Journal of Power Sources
- Applied Energy
- Energy
- IEEE Transactions on Industrial Electronics
- Journal of Energy Storage

## Common SOC Estimation Algorithms

After obtaining datasets, you can use these algorithms for SOC estimation:

### Traditional Methods
1. **Coulomb Counting (Ampere-hour Integration)**
   - Pros: Simple and direct
   - Cons: Large cumulative error

2. **Open Circuit Voltage (OCV) Method**
   - Pros: High accuracy
   - Cons: Requires rest time

3. **Kalman Filter**
   - Pros: Good real-time performance, high accuracy
   - Cons: Requires accurate battery model

### Machine Learning Methods
1. **Neural Networks**
   - Feedforward Neural Networks
   - Recurrent Neural Networks (RNN/LSTM/GRU)
   
2. **Support Vector Machine (SVM)**

3. **Random Forest**

4. **Deep Learning Methods**
   - CNN for feature extraction
   - LSTM for time series prediction
   - Transformer for long-term dependency modeling

## Data Preprocessing Recommendations

1. **Data Cleaning**
   - Remove outliers
   - Handle missing values
   - Filtering and denoising

2. **Feature Engineering**
   - Voltage, current, temperature
   - Charge/discharge rate
   - Cycle count
   - Time series features

3. **Data Normalization**
   - Min-Max normalization
   - Z-score standardization

4. **Data Augmentation**
   - Sliding window
   - Data interpolation
   - SMOTE (Synthetic Minority Over-sampling)

## Related Tools and Libraries

### Python Libraries
```python
# Data processing
import pandas as pd
import numpy as np

# Machine learning
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Deep learning
import tensorflow as tf
import torch

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
```

### MATLAB Toolboxes
- Battery Management System Toolbox
- Simscape Battery

## Reference Resources

### Online Courses
- Coursera: "Battery State-of-Health (SOH)"
- edX: "Electric Cars: Technology"

### Technical Documentation
- IEC 62660: Li-ion battery standards
- SAE J2464: Electric vehicle battery performance standards

### Research Communities
- Battery Archive: https://www.batteryarchive.org/
- Energy Storage Research Network

## Important Notes

1. **Data Usage License**: Carefully read the license agreement before using datasets
2. **Citation Requirements**: Cite properly when using datasets in papers or projects
3. **Data Quality**: Quality and completeness vary across datasets, careful evaluation needed
4. **Privacy Protection**: Be mindful of privacy when data involves user devices
5. **Update Frequency**: Some datasets are regularly updated, stay informed of latest versions

## Contact

For more information or dataset recommendations:
- GitHub Issues
- Academic forum discussions
- Contact research groups via email

---

**Last Updated**: January 30, 2026

**Document Contribution**: This document compiles publicly available battery SOC dataset resources for learning and research purposes.
