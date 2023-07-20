
print("This a DevOps course!")

skill = "DevOps" #string varaible.
print(skill)
print("I am learning " + skill)

#Integers: 

print("*******Integers******")
nums=10
print(nums)


#list
print("This is a list")
tools = ["Jenkins","Docker","K8s","Terraform",90]
print(tools)
print(tools[0])
print(tools[-1])

print("Printing range of list: ")
print(tools[1:3])

#tuple
print("")
print("THis is a tuple")
tools1 = {"Jenkins","Docker","K8s"}
print(tools1)

#dictonary: It stores in key-value format. 
print("")

print("This is a dictonary")



devops={
    
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
}



print(devops)
print(devops["skills"])
print(devops["Year"])
