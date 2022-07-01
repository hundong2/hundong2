# slider 

## slider example 

- TextBlock size binding example

```xml
<Slider
    x:Name="mySlider"
    Maximum="100" TickPlacement="BottomRight" TickFrequency="10"
    IsSnaptoTickEnabled="True"
    Value="50"
    ValueChanged="mySlider_ValueChanged"
></Slider>
<Textblock x:Name="myTextBlock" FontSize="{
    Binding ElementName=mySlider, Path=Value, UpdateSourceTrigger=PropertyChanged}"
}></TextBlock>
```