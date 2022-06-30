# Csharp app.conf file usage

## using example

```xml
<connectionString>
    <add name="DefaultConnectingString"
         connetingString="Data Source=serverName;
                          Initial Catalog=MyCatalog;
                          Persist Security Info=true;
                          User ID=userName;Password=password"
        providerName="System.Data,SqlClient"
    />
</connectionStrings>
```

### access source
```csharp
public MainWindow()
{
    InitializeComponent();
    string dbConnStr = ConfigurationManager.ConnectionStrings["DefaultConnectingString"].connectingString;
}
```