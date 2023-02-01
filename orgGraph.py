# import config
# from terrasoftConnector import terrasoftConnector
#
# terrasoft = terrasoftConnector(config.terrasoft_config, "tsv_DepartmentForSimpleOrgStructure")
# y = terrasoft.get_column_names()
# x = terrasoft.run_custom_query("SELECT S.Name , R.Name FROM tsv_DepartmentForSimpleOrgStructure as S join tsv_DepartmentForSimpleOrgStructure as R ON R.ID = S.ParentDepartmentID", ['Name', 'ParentName'])
# x.to_csv('orgStructure.csv')
import matplotlib
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('orgStructure.csv')

G = nx.from_pandas_edgelist(data, 'ParentName', 'Name')

sub_graphs = [G.subgraph(c) for c in nx.connected_components(G)]

fig = plt.figure(1, figsize=(200, 200), dpi=50)
# plt.subplot(221)
nx.draw(sub_graphs[3], with_labels = True)
# plt.subplot(222)
# nx.draw(sub_graphs[1], with_labels = True)
# plt.subplot(223)
# nx.draw(sub_graphs[2], with_labels = True)
# plt.subplot(224)
# nx.draw(sub_graphs[3], with_labels = True)
# matplotlib.rcParams.update({'font.size': 10})
plt.show()
# graph = nx.from_pandas_edgelist(data)
# print (graph)