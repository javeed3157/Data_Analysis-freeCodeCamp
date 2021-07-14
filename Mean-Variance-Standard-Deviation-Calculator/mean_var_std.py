import numpy as np

def calculate(list):
  if(len(list)==9):
    re=np.reshape(list,(3,3))
    calculations={'mean':[np.mean(re,axis=0).tolist(),np.mean(re,axis=1).tolist(),np.mean(re.flatten())],
                  'variance':[np.var(re,axis=0).tolist(),np.var(re,axis=1).tolist(),np.var(re.flatten())],
                  'standard deviation':[np.std(re,axis=0).tolist(),np.std(re,axis=1).tolist(),np.std(re.flatten())],
                  'max':[np.max(re,axis=0).tolist(),np.max(re,axis=1).tolist(),np.max(re.flatten())],
                  'min':[np.min(re,axis=0).tolist(),np.min(re,axis=1).tolist(),np.min(re.flatten())],
                  'sum':[np.sum(re,axis=0).tolist(),np.sum(re,axis=1).tolist(),np.sum(re.flatten())]
    }
    return calculations
  else:
      raise ValueError("List must contain nine numbers.")