# HelloFlaskWorld
Simple flask application for GCP automated deployment example.

# Manual Deployment
## Critical Files:
- Create App.yaml to specify the runtime env. Only one line is required: `runtime: python38`

## How to deploy
1) Create/select GCP Project
  1) In the top left bar, next to “Google Cloud Platform”, there is a drop down. It will say the name of your current project. Click on it.
  2) Select an existing project or “New Project” and continue through the creation options
2) Open Cloud Shell and editor: 
  1) Click on the terminal icon on the top-right menu bar
  2) Select `Open Editor` to access a full IDE
3) Test by running locally. 
  1) From terminal, type: `python3 main.py`
  2) selecting `Web Preview` from top right menu bar in the editor to open the site

## Automating Deployment (triggered by git event):

## Critical Files:
- Create App.yaml to specify the runtime env
- “main.py” is default entry point, so name is important (or additional GCP configuration is required)
- Cloudbuild.yaml - tells cloud build what to do for deployment

## How to deploy
1) Open Cloud Build (just use the search bar to find it)
2) Create a Trigger
  1) Main Menu --> Triggers --> Create Trigger...Follow wizard to set: event to invoke trigger, repository, etc.
3) Enable:
  1) Settings →App Engine → Enable
  2) Settings → Service Accounts → Enable 
  3) You may be required to install App Engine Admin API. Follow the prompts.


