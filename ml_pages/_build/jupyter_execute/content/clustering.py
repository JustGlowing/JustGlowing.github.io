# The clustering exploration

When we look at the way we organize objects, it's easy to spot the tendency to group similar objects together. Just think about your drawers. Socks are, usually, all in the same drawer. This way it's easy to pick a pair when necessary. Most of the pens are in a holder on our desk so that we know where to pick one when inspiration strikes. Also, in our pens holder we mights find some pencils, which are similar to pens but with a slightly different functionality.

If we look back at our dataset of seeds introduced when talking about classification {doc}`classification`, we can see how a machine can mimic this behavior.

from mlpages_lib import *
%matplotlib inline

data = pd.read_csv('../data/seeds_dataset.txt', 
                    names=['area', 'perimeter', 'compactness', 'length_kernel', 'width_kernel',
                   'asymmetry_coefficient', 'length_kernel_groove', 'target'], 
                   sep='\t+', engine='python')
data = data[data.target!=1]

fig = plt.figure()
plt.scatter(data['length_kernel'], data['width_kernel'])
plt.xlabel('length (mm)')
plt.ylabel('width (mm)')
glue("seeds_cluster_fig_1", fig, display=False)

```{glue:figure} seeds_cluster_fig_1
:name: "seeds-cluster-fig-1"

Length versus width of the kernels.
```

In {ref}`this figure <seeds-cluster-fig-1>` we have a subset of the data. Looking at it we can see two groups of points that have similar features, one close to the bottom left corner and another one to the top right. These two groups take the name of **clusters**.  

fig = plt.figure()
for i, c in enumerate(data['target'].unique()):
    plt.scatter(data['length_kernel'][data.target==c],
                data['width_kernel'][data.target==c],
                c='C'+str(i+1))
    plt.xlabel('length (mm)')
    plt.ylabel('width (mm)')
glue("seeds_cluster_fig_2", fig, display=False)

```{glue:figure} seeds_cluster_fig_2
:name: "seeds-cluster-fig-2"

Two clusters highlighted in the seeds dataset.
```

Given that a machine can easily compute the distance between two points on a plane like one, it can also group points into clusters that contain points that are closer to one another. In {ref}`the figure above <seeds-cluster-fig-2>` the two clusters just discussed are highlighted with different colors. These two clusters also correspond to two varieties of seeds (Canadian and Rosa).

