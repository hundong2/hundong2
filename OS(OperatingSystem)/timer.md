# time setting for linux 

## description

- `Local time` : current time local.
- `Universal time ( UTC )` : Coordinated Universal Time.  
- `RTC time`: Real Time Clock, Hardware clock time. ( Mainboard battery ).  
- `Time Zone`: national time.   
- `KST` : Korean Standard Time.   

## timedatectl

`timedatectl set-time "YYYY-MM-dd HH:mm:ss"`

## date

`date MMddHHmmYYYY.SS`

## RTC Time 

`cat /proc/driver/rtc`.  
`cat /proc/interrupts`  

## hwclock 

- `hwclock -r`.  
- `hwclock -w`. 