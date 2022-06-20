# IFormattable 
## definition
- namespace : System  
- assembly : System.Runtime.dll  

개체의 값을 문자열 표현으로 서식 지정하는 기능을 제공합니다.  
```csharp
public interface IFormattable
```

## example
다음 예제에서는 Temperature 인터페이스를 구현하는 IFormattable 클래스를 정의합니다. 이 클래스는 4 명의 형식 지정 자가 지원: 온도 섭씨;에 표시 되는 여부를 나타내는 "G" 및 "C" "F" 온도를 화씨로; 표시할 임을 나타냅니다 및 "K" 온도를 켈빈 표시할 임을 나타냅니다. 또한 합니다 IFormattable.ToString 구현도 처리할 수는 서식 문자열입니다 null 이거나 비어 있습니다. 다른 두 ToString 정의한 메서드를 Temperature 클래스는 호출을 래핑하는 IFormattable.ToString 구현 합니다.  
```csharp
using System;
using System.Globalization;

public class Temperature : IFormattable
{
   private decimal temp;

   public Temperature(decimal temperature)
   {
      if (temperature < -273.15m)
        throw new ArgumentOutOfRangeException(String.Format("{0} is less than absolute zero.",
                                              temperature));
      this.temp = temperature;
   }

   public decimal Celsius
   {
      get { return temp; }
   }

   public decimal Fahrenheit
   {
      get { return temp * 9 / 5 + 32; }
   }

   public decimal Kelvin
   {
      get { return temp + 273.15m; }
   }

   public override string ToString()
   {
      return this.ToString("G", CultureInfo.CurrentCulture);
   }

   public string ToString(string format)
   {
      return this.ToString(format, CultureInfo.CurrentCulture);
   }

   public string ToString(string format, IFormatProvider provider)
   {
      if (String.IsNullOrEmpty(format)) format = "G";
      if (provider == null) provider = CultureInfo.CurrentCulture;

      switch (format.ToUpperInvariant())
      {
         case "G":
         case "C":
            return temp.ToString("F2", provider) + " °C";
         case "F":
            return Fahrenheit.ToString("F2", provider) + " °F";
         case "K":
            return Kelvin.ToString("F2", provider) + " K";
         default:
            throw new FormatException(String.Format("The {0} format string is not supported.", format));
      }
   }
}
```

다음 예제에서는 호출을 IFormattable.ToString 구현을 직접 또는 합성 서식 문자열을 사용 하 여 합니다.  
```csharp
public class Example
{
   public static void Main()
   {
      // Use composite formatting with format string in the format item.
      Temperature temp1 = new Temperature(0);
      Console.WriteLine("{0:C} (Celsius) = {0:K} (Kelvin) = {0:F} (Fahrenheit)\n", temp1);

      // Use composite formatting with a format provider.
      temp1 = new Temperature(-40);
      Console.WriteLine(String.Format(CultureInfo.CurrentCulture, "{0:C} (Celsius) = {0:K} (Kelvin) = {0:F} (Fahrenheit)", temp1));
      Console.WriteLine(String.Format(new CultureInfo("fr-FR"), "{0:C} (Celsius) = {0:K} (Kelvin) = {0:F} (Fahrenheit)\n", temp1));

      // Call ToString method with format string.
      temp1 = new Temperature(32);
      Console.WriteLine("{0} (Celsius) = {1} (Kelvin) = {2} (Fahrenheit)\n",
                        temp1.ToString("C"), temp1.ToString("K"), temp1.ToString("F"));

      // Call ToString with format string and format provider
      temp1 = new Temperature(100)      ;
      NumberFormatInfo current = NumberFormatInfo.CurrentInfo;
      CultureInfo nl = new CultureInfo("nl-NL");
      Console.WriteLine("{0} (Celsius) = {1} (Kelvin) = {2} (Fahrenheit)",
                        temp1.ToString("C", current), temp1.ToString("K", current), temp1.ToString("F", current));
      Console.WriteLine("{0} (Celsius) = {1} (Kelvin) = {2} (Fahrenheit)",
                        temp1.ToString("C", nl), temp1.ToString("K", nl), temp1.ToString("F", nl));
   }
}
// The example displays the following output:
//    0.00 °C (Celsius) = 273.15 K (Kelvin) = 32.00 °F (Fahrenheit)
//
//    -40.00 °C (Celsius) = 233.15 K (Kelvin) = -40.00 °F (Fahrenheit)
//    -40,00 °C (Celsius) = 233,15 K (Kelvin) = -40,00 °F (Fahrenheit)
//
//    32.00 °C (Celsius) = 305.15 K (Kelvin) = 89.60 °F (Fahrenheit)
//
//    100.00 °C (Celsius) = 373.15 K (Kelvin) = 212.00 °F (Fahrenheit)
//    100,00 °C (Celsius) = 373,15 K (Kelvin) = 212,00 °F (Fahrenheit)
```

## Explanation
IFormattable 인터페이스 개체는 형식 문자열과 형식 공급자에 따라 해당 문자열 표현으로 변환 합니다.  

형식 문자열에는 일반적으로 개체의 전반적인 모양은 정의합니다. 예를 들어 다음.NET Framework를 지원합니다.  

열거형 값의 서식을 지정 하는 것에 대 한 표준 형식 문자열 (참조 열거형 형식 문자열).  

숫자 값의 서식을 지정 하는 것에 대 한 표준 및 사용자 지정 형식 문자열 (참조 Standard Numeric Format Strings 하 고 Custom Numeric Format Strings).  

날짜 및 시간 값의 서식을 지정 하는 것에 대 한 표준 및 사용자 지정 형식 문자열 (참조 표준 날짜 및 시간 서식 문자열 하 고 사용자 지정 날짜 및 시간 형식 문자열).  

시간 간격 형식 지정에 대 한 표준 및 사용자 지정 형식 문자열 (참조 표준 TimeSpan 서식 문자열 하 고 사용자 지정 TimeSpan 형식 문자열).  

또한 애플리케이션 정의 형식의 서식 지정을 지원 하기 위해 사용자 고유의 형식 문자열을 정의할 수 있습니다.  

형식 공급자는 일반적으로 개체를 문자열 표현으로 변환할 때 사용 되는 기호를 정의 하는 서식 지정 개체를 반환 합니다. 예를 들어 통화 값을 숫자로 변환할 때 형식 공급자는 결과 문자열에 표시 되는 통화 기호를 정의 합니다. .NET Framework는 세 가지 형식 공급자를 정의합니다.  

합니다 System.Globalization.CultureInfo 중 하나를 반환 하는 클래스를 NumberFormatInfo 숫자 값의 서식을 지정 하는 것에 대 한 개체 또는 DateTimeFormatInfo 날짜 및 시간 값의 서식을 지정 하는 것에 대 한 개체입니다.  

System.Globalization.NumberFormatInfo 숫자 값의 서식을 지정 하는 것에 대 한 자체의 인스턴스를 반환 하는 클래스입니다.  

System.Globalization.DateTimeFormatInfo 날짜 및 시간 값의 서식을 지정 하는 것에 대 한 자체의 인스턴스를 반환 하는 클래스입니다.  

또한 문화권별, 직업 별로 제공할 사용자 고유의 사용자 지정 형식 공급자를 정의할 수 있습니다 또는 산업별 정보 서식 지정에 사용 합니다. 사용자 지정 형식 공급자를 사용 하 여 사용자 지정 서식을 구현 하는 방법에 대 한 자세한 내용은 참조 하세요. ICustomFormatter합니다.  

합니다 IFormattable 는 단일 메서드를 정의 하는 인터페이스 ToString를 구현 하는 형식에 대 한 서식 지정 서비스를 제공 하는 합니다. ToString 메서드를 직접 호출할 수 있습니다. 또한 라고 자동으로 Convert.ToString(Object) 및 Convert.ToString(Object, IFormatProvider) 메서드 및 사용 하는 방법으로는 복합 서식 지정 기능 .NET Framework에서. 이러한 메서드를 포함 Console.WriteLine(String, Object), String.Format, 및 StringBuilder.AppendFormat(String, Object), 특히 합니다. ToString 메서드의 형식 문자열의 각 서식 항목에 대 한 호출 됩니다.  

IFormattable 인터페이스는 기본 데이터 형식으로 구현 됩니다.  

## reference 
[microsoft docs Iformattable](https://docs.microsoft.com/ko-kr/dotnet/api/system.iformattable?view=net-6.0 "iformattable")  
