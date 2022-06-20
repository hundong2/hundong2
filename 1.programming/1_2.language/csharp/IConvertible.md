# IConvertible Interface
## definition
- namespace : System
- Assembly : System.Runtime.dll

```
중요
이 API는 CLS 규격이 아닙니다.
```
구현하는 참조의 값 또는 값 형식을 같은 값의 공용 언어 런타임 형식으로 변환하는 메서드를 정의합니다.  

```csharp
[System.CLSCompliant(false)]
public interface IConvertible
```

## Example 
- 다음 코드 샘플에서는 복소수 클래스에 IConvertible 대한 구현을 보여 줍니다. 이 클래스를 먼저 a Double 로 캐스팅한 다음 해당 Double클래스에서 정적 Convert 멤버를 호출할 수 있습니다.  
```csharp
using System;

namespace ConsoleApplication2
{

    /// Class that implements IConvertible
    class Complex : IConvertible
    {
        double	x;
        double	y;

        public Complex(double x, double y)
        {
            this.x = x;
            this.y = y;
        }

        public TypeCode GetTypeCode()
        {
            return TypeCode.Object;
        }

        bool IConvertible.ToBoolean(IFormatProvider provider)
        {
            if(	(x != 0.0) || (y != 0.0) )
                return true;
            else
                return false;
        }

        double GetDoubleValue()
        {
            return Math.Sqrt(x*x + y*y);
        }

        byte IConvertible.ToByte(IFormatProvider provider)
        {
            return Convert.ToByte(GetDoubleValue());
        }

        char IConvertible.ToChar(IFormatProvider provider)
        {
            return Convert.ToChar(GetDoubleValue());
        }

        DateTime IConvertible.ToDateTime(IFormatProvider provider)
        {
            return Convert.ToDateTime(GetDoubleValue());
        }

        decimal IConvertible.ToDecimal(IFormatProvider provider)
        {
            return Convert.ToDecimal(GetDoubleValue());
        }

        double IConvertible.ToDouble(IFormatProvider provider)
        {
            return GetDoubleValue();
        }

        short IConvertible.ToInt16(IFormatProvider provider)
        {
            return Convert.ToInt16(GetDoubleValue());
        }

        int IConvertible.ToInt32(IFormatProvider provider)
        {
            return Convert.ToInt32(GetDoubleValue());
        }

        long IConvertible.ToInt64(IFormatProvider provider)
        {
            return Convert.ToInt64(GetDoubleValue());
        }

        sbyte IConvertible.ToSByte(IFormatProvider provider)
        {
            return Convert.ToSByte(GetDoubleValue());
        }

        float IConvertible.ToSingle(IFormatProvider provider)
        {
            return Convert.ToSingle(GetDoubleValue());
        }

        string IConvertible.ToString(IFormatProvider provider)
        {
            return String.Format("({0}, {1})", x, y);
        }

        object IConvertible.ToType(Type conversionType, IFormatProvider provider)
        {
            return Convert.ChangeType(GetDoubleValue(),conversionType);
        }

        ushort IConvertible.ToUInt16(IFormatProvider provider)
        {
            return Convert.ToUInt16(GetDoubleValue());
        }

        uint IConvertible.ToUInt32(IFormatProvider provider)
        {
            return Convert.ToUInt32(GetDoubleValue());
        }

        ulong IConvertible.ToUInt64(IFormatProvider provider)
        {
            return Convert.ToUInt64(GetDoubleValue());
        }
    }

    /// <summary>
    /// Summary description for Class1.
    /// </summary>
    class Class1
    {
        static void Main(string[] args)
        {

            Complex		testComplex = new Complex(4,7);

            WriteObjectInfo(testComplex);
            WriteObjectInfo(Convert.ToBoolean(testComplex));
            WriteObjectInfo(Convert.ToDecimal(testComplex));
            WriteObjectInfo(Convert.ToString(testComplex));
        }

        static void WriteObjectInfo(object testObject)
        {
            TypeCode	typeCode = Type.GetTypeCode( testObject.GetType() );

            switch( typeCode )
            {
                case TypeCode.Boolean:
                    Console.WriteLine("Boolean: {0}", testObject);
                    break;

                case TypeCode.Double:
                    Console.WriteLine("Double: {0}", testObject);
                    break;
                                
                default:
                    Console.WriteLine("{0}: {1}", typeCode.ToString(), testObject);
                    break;
            }
        }
    }
}
```

## Explanation

이 인터페이스는 구현 형식의 인스턴스 값을 동일한 값을 가진 공용 언어 런타임 형식으로 변환하는 메서드를 제공합니다. 공용 언어 런타임 형식은 Boolean, ,, Byte, Int16, UInt16Int32, UInt32, Int64DecimalCharUInt64SingleDoubleDateTime, 및 String입니다. SByte  
공용 언어 런타임 형식으로 의미 있는 변환이 없으면 특정 인터페이스 메서드 구현이 throw됩니다 InvalidCastException. 예를 들어 이 인터페이스가 부울 형식에서 구현되는 경우 부울 형식에 해당하는 의미 DateTime 있는 형식이 없으므로 메서드 구현 ToDateTime 은 예외를 throw합니다.  

공용 언어 런타임은 일반적으로 클래스를 통해 인터페이스를 IConvertible Convert 노출합니다. 또한 공용 언어 런타임은 명시적 인터페이스 구현에서 내부적으로 인터페이스를 사용하여 IConvertible 클래스 및 기본 공용 언어 런타임 형식의 Convert 변환을 지원하는 데 사용되는 코드를 간소화합니다.  

인터페이스 외에도 IConvertible .NET Framework 사용자 정의 데이터 형식을 다른 데이터 형식으로 변환하기 위한 형식 변환기라는 클래스를 제공합니다. 자세한 내용은 일반화된 형식 변환 항목을 참조하세요.  

## reference 
[docs microsoft iconvertible](https://docs.microsoft.com/ko-kr/dotnet/api/system.iconvertible?view=net-6.0 "iconvertible")  
