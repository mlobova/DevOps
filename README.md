## [DONE] Service programming
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>Folder <strong>app</strong>/ content:</p>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'><strong>python_service.py</strong> - the script to update /etc/motd file and having REST API GET /info method<br><strong>python_rest_api.service</strong> - systemd service which run python_service.py script</p>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>In order to update message of the day on the daily basis, cron task must be running in container:<br><span style="font-size: 15px; line-height: 107%; font-family: Courier New, courier;"><em><span style="color: rgb(71, 85, 119);"></span></em></span></p>

    0 0 * * *  systemctl restart python_rest_api.service

<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>The cron is included into <strong>Dockerfile </strong>as a part of deployment</p>
<p>&nbsp;</p>

## Packer
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>Folder <strong>Packer</strong>/ content:</p>
<p><strong>centos7-new.json</strong> - Packer JSON to build image<br><strong>playbook.yml</strong> - YAML file to build the packer image<br><strong>installation.log&nbsp;</strong>- errors while building</p>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'><em></em><em></em></p>

    # PACKER_LOG=1 packer.io build centos7-new.json

<p>The error returns on both CentOS and Ubuntu VMs:<br><em>gmem.c:489: custom memory allocation vtable not supported</em></p>
<p>&nbsp;</p>

## [DONE] Docker
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'><strong>Dockerfile&nbsp;</strong>contains the following operations:</p>
<div style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>
    <ul style="margin-bottom:0in;list-style-type: disc;">
        <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>Install packages/lib: &nbsp;python3, flask, cronie</li>
        <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>Copy <strong>app</strong>/ content to image</li>
        <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>Move script <strong>python_rest_api.service</strong> file to /etc/systemd/system</li>
        <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>Move<strong>&nbsp;</strong>script <strong>python_service.py</strong> to /usr/local/lib/</li>
        <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>Enable <strong>python_rest_api.service</strong></li>
        <li style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>Create cron task to update motd once a day</li>
    </ul>
    <p>Creating of a container from this image requires privileged permissions (to make the service running):</p>
    
    # docker build -t <repository>:<tag> .
    # docker exec -it --privileged <container_nabme&gt> /bin/bash
    # docker run -d --name <container_name> --privileged=true <image_id> /usr/sbin/init
    
<p>&nbsp;</p>
  
## [DONE] (optional) Public clouds
<p>How to authenticate to Yandex Cloud: <a href="https://cloud.yandex.com/en/docs/cli/quickstart">https://cloud.yandex.com/en/docs/cli/quickstart</a><br /> Pushing a Docker image to a registry <a href="https://cloud.yandex.com/en/docs/managed-kubernetes/tutorials/container-registry">https://cloud.yandex.com/en/docs/managed-kubernetes/tutorials/container-registry</a> :</p>
<ol>
<li>Create a container registry<br /> <em></em></li>
    
    # yc container registry create --name <registry_name>
    
<li>Configure the Docker Credential helper<em><br /></em></li>
    
    # yc container registry configure-docker
    
<li><em>Get the ID of the previously created registry and write it to the variable<br /></em></li>
    
    # REGISTRY_ID=$(yc container registry get --name yc-auto-cr --format json | jq .id -r)
    
<li>Push the Docker image to the registry<em><br /></em></li>
    
    # docker push cr.yandex/${REGISTRY_ID}/<repositor>:<tag>
    
<li><em>Make sure the Docker image was pushed to the registry<br /></em><em></em></li>
    
    # yc container image list
    
</ol>
<p>&nbsp;</p>

## [DONE] Kubernetes
    
    # kubectl apply -f app-deployment_v2.yml
    
<p> API GET request: </p>
    
    http://51.250.27.79:31522/info
    	
    {"date":"2022-03-28","hash":-7162813333160064537,"ip":"10.112.130.20","time":"10:09:54.148635"}
    

<p>File <strong>app-deployment_v2.yml</strong> description:<br /> <strong>Deployment</strong> from yc cloud image in privileged mode<br /> <strong>Service</strong> of type <strong>NodePort</strong> will be accessible by cluster node Public IP and nodePort: 30300:<br /></p>
check the pod NODE
    
    # kubectl apply -f app-deployment_v2.yml
to find EXTERNAL-IP of the NODE
    
    # kubectl get pods -o wide
<p>&nbsp;</p>
    
## (optional) Continuous Integration / Continuous Delivery / Continuous Deployment
Jenkins deployed: http://51.250.96.151:32000/
    
    # kubectl get services -n devops-tools
    NAME              TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
    jenkins-service   NodePort   10.96.137.105   <none>        8080:32000/TCP   25h
    
<p>&nbsp;</p>
    
    
## (optional) Monitoring
Prometheus deployed: http://51.250.27.79:30000/
    
    # kubectl get services -n monitoring
    NAME                 TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
    prometheus-service   NodePort   10.96.141.223   <none>        8080:30000/TCP   19h
    
<p>&nbsp;</p>
    
    
## [DONE] Public services
    # git clone https://github.com/mlobova/DevOps.git
    # cd DevOps
    make changes
    # git status
    # git add
    # git checkout
    # git commit -m "Changes description"
    # git push -u origin
      login:
      api key:

<p>Pull request:</p>

    # cd DevOps
    # git pull
    make changes
