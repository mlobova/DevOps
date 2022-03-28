## [DONE] Service programming
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>Folder <strong>app</strong>/ content:</p>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'><strong>python_service.py</strong> - the script to update /etc/motd file and having REST API GET /info method<br><strong>python_rest_api.service</strong> - systemd service which run python_service.py script</p>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>In order to update message of the day on the daily basis, cron task must be running in container:<br><span style="font-size: 15px; line-height: 107%; font-family: Courier New, courier;"><em><span style="color: rgb(71, 85, 119);">0 0 * * * &nbsp;systemctl restart python_rest_api.service</span></em></span></p>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>The cron is included into <strong>Dockerfile </strong>as a part of deployment</p>

## Packer
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>Folder <strong>Packer</strong>/ content:</p>
<p><strong>centos7-new.json</strong> - Packer JSON to build image<br><strong>playbook.yml</strong> - YAML file to build the packer image<br><strong>installation.log&nbsp;</strong>- errors while building</p>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'><em>#&nbsp;</em><em>PACKER_LOG=1 packer.io build centos7-new.json</em></p>
<p>The error returns on both CentOS and Ubuntu VMs:<br><em>gmem.c:489: custom memory allocation vtable not supported</em></p>

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
    <p>Creating of a container from this image requires privileged permissions (to make the service running):<br><em># docker build -t &lt;repository&gt;:&lt;tag&gt; .<br># docker run -d --name &lt;container_name&gt; --privileged=true &lt;image_id&gt; /usr/sbin/init<br># docker exec -it --privileged &lt;container_nabme&gt; /bin/bash</em><br></p>
  
## [DONE] (optional) Public clouds
