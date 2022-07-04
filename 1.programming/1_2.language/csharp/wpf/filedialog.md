# C# file open dialog 정리 

## class 

- c#에서 file save/open dialog 사용 예제. 

### Class Name

- OpenFileDialog 
#### example 

```csharp
OpenfileDialog openFileDialog = new OpenFileDialog();
if(openFileDialog.showDialog() == true)
{
    myTextBox.Text = File.ReadAllText(openFileDialog.FileName); //File Text Read All
}
```

- SaveFileDialog

#### example 

```csharp
SaveFileDialog saveFileDialog = new SaveFileDialog();
saveFileDialog.filter = //something filter 
saveFileDialog.ShowDialog();
```

### Filter 적용 방법

```csharp
OpenFileDialog dlg = new OpenFileDialog();
dlg.Filter = "database file|*.db";
dlg.ShowDialog();
```