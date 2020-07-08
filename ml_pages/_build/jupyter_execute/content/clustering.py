# The clustering approach



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

fig = plt.figure()
for i, c in enumerate(data['target'].unique()):
    plt.scatter(data['length_kernel'][data.target==c],
                data['width_kernel'][data.target==c],
                c='C'+str(i+1))
    plt.xlabel('length (mm)')
    plt.ylabel('width (mm)')
glue("seeds_cluster_fig_2", fig, display=False)

