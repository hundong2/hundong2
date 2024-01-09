# File 관련 

## 1.file line count 

- file에 작성 된 line number를 구하는 방법. 
```csharp
FileInfo mFileInfo = new FileInfo([filepath]);
long filelinelegth = File.ReadLines(mFileInfo.FullName).Count();
```

