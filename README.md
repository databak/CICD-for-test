CICD-FOR-TEST/
├── README.md               <-- Root README for GitHub (docs/overview of the repo)
├── App/                    <-- App folder dedicated to Hugging Face deployment ,
│                              for adding web app classifier file, app README file with metadata, and requirement.txt │                              for installing necessary packages.
│   ├── README.md           <-- THIS is where the HF metadata goes!
│   ├── drug_app.py         <-- Your Gradio app script
│   └── requirements.txt    <-- Dependencies specifically needed for HF Space
├── Data/
├── Model/                 <-- saving trained model file
└── Results/               <-- for saving metrics and result 


# notice
app dir is going to launch inside HF space 
HF space is git repo for deploying and running ml model , in CD , github action will upload related file to HF
github repo is main repo to handling and managing , local machine works only with github repo 
github has server to launc : github page/action