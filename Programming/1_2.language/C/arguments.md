# Arguments are pushed in the reverse order

## example

```c
 foo( arg1, arg2, ... argN )
 ```

then "argument order" would be left to right (arg1 to argN). Function calling code would be:

```c
  push  arg1
  push  arg2
  ...
  push  argN
  call  foo
```

"Reverse order (right to left)" would be argN to arg1:  

```c
  push  argN
  ...
  push  arg1
  call  foo
```

The args of course may not be single DWORDS, and thus the push operations might not be single instructions. The compiler might also be very clever, and preallocate the stack space for the args, and then accomplish filling the arguments via various MOV instructions to offsets in the allocated stack space, possibly not in any specific order. So interpret the "pushes arguments" according to the idea "as if" pushes had been done.  

### reference 

[stackoverflow](https://stackoverflow.com/questions/27979376/what-does-it-mean-when-they-say-arguments-are-pushed-in-the-reverse-order)  

