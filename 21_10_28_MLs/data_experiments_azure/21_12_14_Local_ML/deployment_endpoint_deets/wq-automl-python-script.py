#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from azureml.core import Workspace, Dataset
from datetime import datetime


# In[3]:


# azureml-core of version 1.0.72 or higher is required
# azureml-dataprep[pandas] of version 1.1.34 or higher is required


subscription_id = '915afd81-6fbf-40c3-9ea7-6321aaeafa5f'
resource_group = 'AIoT_SS_2022_Resource_Grp'
workspace_name = 'AIoT_SS_2022'

workspace = Workspace(subscription_id, resource_group, workspace_name)

dataset = Dataset.get_by_name(workspace, name='wq-all-train-data')
df = dataset.to_pandas_dataframe()
df = df.reset_index()
df = df.drop(labels='index', axis=1)
df.head()


# In[9]:


#Configure Workspace
from azureml.core.workspace import Workspace
ws = Workspace.from_config()


# In[10]:


#Define training settings

import logging

automl_settings = {
    "iteration_timeout_minutes": 30,
    "experiment_timeout_hours": 1,
    "enable_early_stopping": True,
    "primary_metric": 'normalized_root_mean_squared_error',
    "featurization": 'auto',                                   #Indicates that as part of preprocessing, data guardrails and featurization steps are performed automatically. 
    "verbosity": logging.INFO,
    "n_cross_validations": 10
}


# In[11]:


from azureml.train.automl import AutoMLConfig

automl_config = AutoMLConfig(task='regression',
                             debug_log='wq_22_automated_ml_errors.log',
                             training_data=df,
                             label_column_name="chl-a",
                             **automl_settings)


# In[12]:


### Train the automatic regression model

from azureml.core.experiment import Experiment
experiment = Experiment(ws, "wq-22-jupy-train")
local_run = experiment.submit(automl_config, show_output=True)


# In[13]:


#Explore the results

from azureml.widgets import RunDetails
RunDetails(local_run).show()


# In[14]:


### Retrieve the best model

best_run, fitted_model = local_run.get_output()
print(best_run)
print(fitted_model)


# In[ ]:




