
- Create a pod with environment variables as var1=value1.Check the environment variable in pod
- List the nginx pod with custom columns POD_NAME and POD_STATUS
- Create a pod as follows:Name:mongo, Using Image:mongo, new namespace named:my-website
- Set the node named ek8s-node-1as unavailable and reschedule all the pods running on it.

- Create a persistent volume with nameapp-data, of capacity2Giandaccess modeReadWriteMany. Thetype of volume ishostPathand itslocation is/srv/app-data.

- List pod logs named ??frontend?? and search for the pattern ??started?? and write it to a file ??/opt/error-logs??
- List all the pods showing name and namespace with a json path expression

```sh
Create a deployment as follows:
Name:nginx-app
Using containernginxwithversion 1.11.10-alpine
The deployment should contain3replicas
Next, deploy the application with newversion1.11.13-alpine, byperforming a rolling update.
Finally, rollback that update to theprevious version1.11.10-alpine.
```

```sh
Schedule a pod as follows:
Name: nginx-kusc00101
Image: nginx
Node selector: disk=ssd
```
