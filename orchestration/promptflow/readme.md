# Introducing Promptflow locally
This repo contains a very simple promptflow example taken from here:
[promptflow quickstart](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html)

To run it:

# Linux
```bash
# deactivate any existing venv
deactivate

cd orchestration/promptflow
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# run the example
pf flow test --flow main:chat --inputs question="What's the smallest island in the pacific"
```

review and explore the trace url returned in the response - this spins up a local UI.

# Windows
```cmd
:: deactivate any existing venv on Windows
deactivate

cd orchestration/promptflow
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt

:: you can use the same cli command as above, or use the --ui option:
pf flow test --flow main:chat --ui 

```

# Azure ML PromptFlow tooling

:point_right: Demonstrate / follow along:
  - a simple chat flow
  - a simple chat with your data flow
  - deploying your flows to a managed endpoint

    ![Azure ML Managed Endpoints](https://techcommunity.microsoft.com/t5/image/serverpage/image-id/282439iF10292F821EBDBBB/image-size/medium?v=v2&px=600)

# Further reading
- [About Azure ML Managed Endpoints](https://techcommunity.microsoft.com/t5/ai-machine-learning-blog/announcing-managed-endpoints-in-azure-machine-learning-for/ba-p/2366481)
- [About Prompflow](https://microsoft.github.io/promptflow/)
- [Promptflow in Azure ML](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/overview-what-is-prompt-flow?view=azureml-api-2)
- [PromptFlow with Azure AI Studio](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/flow-develop)