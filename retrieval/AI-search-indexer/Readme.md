
## Overview
Here, we configure
- a datasource
- an indexer: the pipeline engine
- a skillset to implement
  - text splitting (chunking)
  - embedding with Azure OpenAI
- an index


    <img src="https://learn.microsoft.com/en-us/azure/search/media/vector-search-integrated-vectorization/integrated-vectorization-architecture.png" width="700" />


## Exercise
:point_right: we'll first use the portal to auto-generate the required assets

:point_right: and then explore the [management interface with a notebook](./management/manage.ipynb) to highlight that these are fully customisable. 





# Further Reading
- [API reference](https://learn.microsoft.com/en-us/rest/api/searchservice/?view=rest-searchservice-2024-05-01-preview)
- [Get started with Vector Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-vector?tabs=azure-cli)

## New features
- [integrated vectorisation] https://learn.microsoft.com/en-us/azure/search/vector-search-integrated-vectorization
- [custom embedding models for integrated vectorisation]https://learn.microsoft.com/en-us/azure/search/vector-search-integrated-vectorization-ai-studio?tabs=inference-text
