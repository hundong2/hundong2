# context box

## explanation

- textbox의 우클릭 시 context 내용 표시 및 동작. 

### 기본

```csharp
<TextBox>
    <TextBox.ContextMenu>
        <ContextMenu>
            <MenuItem Name="mBold" Header="Bold" Click="mBoldClicked"></MenuItem>
        </ContextMenu>
    </TextBox.ContextMenu>
</TextBox>
```

### check menu 이용 시 ( check, uncheck)

```csharp
<TextBox>
    <TextBox.ContextMenu>
        <ContextMenu>
            <MenuItem Name="mBold" Header="Bold" 
            IsCheckable="True" Checked="mlBold_checked" Unchecked="mlBold_unchecked"></MenuItem>
        </ContextMenu>
    </TextBox.ContextMenu>
</TextBox>
```