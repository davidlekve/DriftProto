Remember you had to follow this: 
https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-web-api?view=aspnetcore-6.0&tabs=visual-studio-code

First:
dotnet dev-certs https --trust


Run the app:

Press Ctrl+F5.
At the Select environment prompt, choose .NET Core.
Select Add Configuration > .NET: Launch a local .NET Core Console App.
In the configuration JSON:
Replace <target-framework> with net6.0.
Replace <project-name.dll> with TodoApi.dll.
Press Ctrl+F5.
In the Could not find the task 'build' dialog, select Configure Task.
Select Create tasks.json file from template.
Select the .NET Core task template.
Press Ctrl+F5.



In a browser, navigate to https://localhost:<port>/swagger, where <port> is the randomly chosen port number displayed in the output.


To access data from external processes:

