# SQLite for C# Language 

## CREATE TABLE

```SQL
CREATE TABLE '[TABLE NAME]' ([ROW NAME] [TYPE OF VALUE], ...)
```

## INSERT TO TABLE

```SQL
INSERT INTO '[TABLE NAME]' ([ROW NAME],...) values ([ROW VALUE],...)
```

### Example 

```csharp
string ConnectionSource = @"Data Source= [File Path];";
string CreatCmd = "CREATE TABLE 'mytable' (test int, test2 int)";
string InsertCmd = "INSERT INTO 'mytable' (test, test1) values (0, 1)";
SQLiteConnection conn = new SQLiteConnetion(ConnectionSource);
if( conn != null)
{
    conn.Open();
    SQLiteCommand mCmd = new SQLiteCommand(CreateCmd, conn);
    mCmd.ExecuteNonQuery();
    mCmd.Dispose();

    mCmd = new SQLiteCommand(InsertCmd, conn);
    mCmd.ExecuteNonQuery();
    mCmd.Dispose();


}
conn.Close();
```