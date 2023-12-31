# JSON, YAML, Linux servers

![Alt text](image.png)

### variables in bash: 
![Alt text](image-1.png)

### JSON 
JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate. It is based on a subset of the JavaScript Programming Language Standard.
JSON is an key-value document.

eg: <{
    "skills":"DevOps",
    
    "Year":2023,
    "Tech":{
          "Cloud": "AWS",
          "Containers":"K8s",
          "CICD": "Jenkins",
          "GitOps":[
              "Gitlab",
              "ArgoCD",
              "Tekton"
        ]
    }
}>
![Alt text](image-2.png)

### YAML 

YAML is a human-readable data serialization language that is often used for writing configuration files. Depending on whom you ask, YAML stands for yet another markup language or YAML ain’t markup language (a recursive acronym), which emphasizes that YAML is for data, not documents. 

eg: 

<
devops: 

  skills: DevOps
    
  Year: 2023
  Tech:
        Cloud: AWS
        Containers: K8s
        CICD: Jenkins
        GitOps:
            -  Gitlab
            -  ArgoCD
            -  Tekton
>

The equivalent of the above YAML code is: 
![Alt text](image-3.png)
        