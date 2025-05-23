
//  Microsoft (R) .NET Framework IL Disassembler.  Version 4.8.3928.0
//  Copyright (c) Microsoft Corporation.  All rights reserved.



// Metadata version: v4.0.30319
.assembly extern mscorlib
{
  .publickeytoken = (B7 7A 5C 56 19 34 E0 89 )                         // .z\V.4..
  .ver 4:0:0:0
}
.assembly Program
{
  .custom instance void [mscorlib]System.Runtime.CompilerServices.CompilationRelaxationsAttribute::.ctor(int32) = ( 01 00 08 00 00 00 00 00 ) 
  .custom instance void [mscorlib]System.Runtime.CompilerServices.RuntimeCompatibilityAttribute::.ctor() = ( 01 00 01 00 54 02 16 57 72 61 70 4E 6F 6E 45 78   // ....T..WrapNonEx
                                                                                                             63 65 70 74 69 6F 6E 54 68 72 6F 77 73 01 )       // ceptionThrows.

  // --- The following custom attribute is added automatically, do not uncomment -------
  //  .custom instance void [mscorlib]System.Diagnostics.DebuggableAttribute::.ctor(valuetype [mscorlib]System.Diagnostics.DebuggableAttribute/DebuggingModes) = ( 01 00 07 01 00 00 00 00 ) 

  .hash algorithm 0x00008004
  .ver 0:0:0:0
}
.module Program.exe
// MVID: {6ACB5707-D8A4-4B71-9C24-F5B9D6B2EB24}
.custom instance void System.Runtime.CompilerServices.RefSafetyRulesAttribute::.ctor(int32) = ( 01 00 0B 00 00 00 00 00 ) 
.imagebase 0x00400000
.file alignment 0x00000200
.stackreserve 0x00100000
.subsystem 0x0003       // WINDOWS_CUI
.corflags 0x00000001    //  ILONLY
// Image base: 0x05760000


// =============== CLASS MEMBERS DECLARATION ===================

.class private auto ansi sealed beforefieldinit Microsoft.CodeAnalysis.EmbeddedAttribute
       extends [mscorlib]System.Attribute
{
  .custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = ( 01 00 00 00 ) 
  .custom instance void Microsoft.CodeAnalysis.EmbeddedAttribute::.ctor() = ( 01 00 00 00 ) 
  .method public hidebysig specialname rtspecialname 
          instance void  .ctor() cil managed
  {
    // Code size       8 (0x8)
    .maxstack  8
    IL_0000:  ldarg.0
    IL_0001:  call       instance void [mscorlib]System.Attribute::.ctor()
    IL_0006:  nop
    IL_0007:  ret
  } // end of method EmbeddedAttribute::.ctor

} // end of class Microsoft.CodeAnalysis.EmbeddedAttribute

.class private auto ansi sealed beforefieldinit System.Runtime.CompilerServices.RefSafetyRulesAttribute
       extends [mscorlib]System.Attribute
{
  .custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = ( 01 00 00 00 ) 
  .custom instance void Microsoft.CodeAnalysis.EmbeddedAttribute::.ctor() = ( 01 00 00 00 ) 
  .custom instance void [mscorlib]System.AttributeUsageAttribute::.ctor(valuetype [mscorlib]System.AttributeTargets) = ( 01 00 02 00 00 00 02 00 54 02 0D 41 6C 6C 6F 77   // ........T..Allow
                                                                                                                         4D 75 6C 74 69 70 6C 65 00 54 02 09 49 6E 68 65   // Multiple.T..Inhe
                                                                                                                         72 69 74 65 64 00 )                               // rited.
  .field public initonly int32 Version
  .method public hidebysig specialname rtspecialname 
          instance void  .ctor(int32 A_1) cil managed
  {
    // Code size       15 (0xf)
    .maxstack  8
    IL_0000:  ldarg.0
    IL_0001:  call       instance void [mscorlib]System.Attribute::.ctor()
    IL_0006:  nop
    IL_0007:  ldarg.0
    IL_0008:  ldarg.1
    IL_0009:  stfld      int32 System.Runtime.CompilerServices.RefSafetyRulesAttribute::Version
    IL_000e:  ret
  } // end of method RefSafetyRulesAttribute::.ctor

} // end of class System.Runtime.CompilerServices.RefSafetyRulesAttribute

.class public auto ansi sealed TestProgram.TestDelegate
       extends [mscorlib]System.MulticastDelegate
{
  .method public hidebysig specialname rtspecialname 
          instance void  .ctor(object 'object',
                               native int 'method') runtime managed
  {
  } // end of method TestDelegate::.ctor

  .method public hidebysig newslot virtual 
          instance void  Invoke(string message) runtime managed
  {
  } // end of method TestDelegate::Invoke

  .method public hidebysig newslot virtual 
          instance class [mscorlib]System.IAsyncResult 
          BeginInvoke(string message,
                      class [mscorlib]System.AsyncCallback callback,
                      object 'object') runtime managed
  {
  } // end of method TestDelegate::BeginInvoke

  .method public hidebysig newslot virtual 
          instance void  EndInvoke(class [mscorlib]System.IAsyncResult result) runtime managed
  {
  } // end of method TestDelegate::EndInvoke

} // end of class TestProgram.TestDelegate

.class public auto ansi beforefieldinit TestProgram.TestClass
       extends [mscorlib]System.Object
{
  .custom instance void [mscorlib]System.Reflection.DefaultMemberAttribute::.ctor(string) = ( 01 00 04 49 74 65 6D 00 00 )                      // ...Item..
  .field private class TestProgram.TestDelegate TestEvent
  .custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = ( 01 00 00 00 ) 
  .custom instance void [mscorlib]System.Diagnostics.DebuggerBrowsableAttribute::.ctor(valuetype [mscorlib]System.Diagnostics.DebuggerBrowsableState) = ( 01 00 00 00 00 00 00 00 ) 
  .field private int32 _number
  .method public hidebysig specialname instance void 
          add_TestEvent(class TestProgram.TestDelegate 'value') cil managed
  {
    .custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = ( 01 00 00 00 ) 
    // Code size       41 (0x29)
    .maxstack  3
    .locals init (class TestProgram.TestDelegate V_0,
             class TestProgram.TestDelegate V_1,
             class TestProgram.TestDelegate V_2)
    IL_0000:  ldarg.0
    IL_0001:  ldfld      class TestProgram.TestDelegate TestProgram.TestClass::TestEvent
    IL_0006:  stloc.0
    IL_0007:  ldloc.0
    IL_0008:  stloc.1
    IL_0009:  ldloc.1
    IL_000a:  ldarg.1
    IL_000b:  call       class [mscorlib]System.Delegate [mscorlib]System.Delegate::Combine(class [mscorlib]System.Delegate,
                                                                                            class [mscorlib]System.Delegate)
    IL_0010:  castclass  TestProgram.TestDelegate
    IL_0015:  stloc.2
    IL_0016:  ldarg.0
    IL_0017:  ldflda     class TestProgram.TestDelegate TestProgram.TestClass::TestEvent
    IL_001c:  ldloc.2
    IL_001d:  ldloc.1
    IL_001e:  call       !!0 [mscorlib]System.Threading.Interlocked::CompareExchange<class TestProgram.TestDelegate>(!!0&,
                                                                                                                     !!0,
                                                                                                                     !!0)
    IL_0023:  stloc.0
    IL_0024:  ldloc.0
    IL_0025:  ldloc.1
    IL_0026:  bne.un.s   IL_0007

    IL_0028:  ret
  } // end of method TestClass::add_TestEvent

  .method public hidebysig specialname instance void 
          remove_TestEvent(class TestProgram.TestDelegate 'value') cil managed
  {
    .custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = ( 01 00 00 00 ) 
    // Code size       41 (0x29)
    .maxstack  3
    .locals init (class TestProgram.TestDelegate V_0,
             class TestProgram.TestDelegate V_1,
             class TestProgram.TestDelegate V_2)
    IL_0000:  ldarg.0
    IL_0001:  ldfld      class TestProgram.TestDelegate TestProgram.TestClass::TestEvent
    IL_0006:  stloc.0
    IL_0007:  ldloc.0
    IL_0008:  stloc.1
    IL_0009:  ldloc.1
    IL_000a:  ldarg.1
    IL_000b:  call       class [mscorlib]System.Delegate [mscorlib]System.Delegate::Remove(class [mscorlib]System.Delegate,
                                                                                           class [mscorlib]System.Delegate)
    IL_0010:  castclass  TestProgram.TestDelegate
    IL_0015:  stloc.2
    IL_0016:  ldarg.0
    IL_0017:  ldflda     class TestProgram.TestDelegate TestProgram.TestClass::TestEvent
    IL_001c:  ldloc.2
    IL_001d:  ldloc.1
    IL_001e:  call       !!0 [mscorlib]System.Threading.Interlocked::CompareExchange<class TestProgram.TestDelegate>(!!0&,
                                                                                                                     !!0,
                                                                                                                     !!0)
    IL_0023:  stloc.0
    IL_0024:  ldloc.0
    IL_0025:  ldloc.1
    IL_0026:  bne.un.s   IL_0007

    IL_0028:  ret
  } // end of method TestClass::remove_TestEvent

  .method public hidebysig specialname instance int32 
          get_Number() cil managed
  {
    // Code size       12 (0xc)
    .maxstack  1
    .locals init (int32 V_0)
    IL_0000:  nop
    IL_0001:  ldarg.0
    IL_0002:  ldfld      int32 TestProgram.TestClass::_number
    IL_0007:  stloc.0
    IL_0008:  br.s       IL_000a

    IL_000a:  ldloc.0
    IL_000b:  ret
  } // end of method TestClass::get_Number

  .method public hidebysig specialname instance void 
          set_Number(int32 'value') cil managed
  {
    // Code size       9 (0x9)
    .maxstack  8
    IL_0000:  nop
    IL_0001:  ldarg.0
    IL_0002:  ldarg.1
    IL_0003:  stfld      int32 TestProgram.TestClass::_number
    IL_0008:  ret
  } // end of method TestClass::set_Number

  .method public hidebysig specialname instance string 
          get_Item(int32 index) cil managed
  {
    // Code size       22 (0x16)
    .maxstack  2
    .locals init (string V_0)
    IL_0000:  nop
    IL_0001:  ldstr      "Index {0}"
    IL_0006:  ldarg.1
    IL_0007:  box        [mscorlib]System.Int32
    IL_000c:  call       string [mscorlib]System.String::Format(string,
                                                                object)
    IL_0011:  stloc.0
    IL_0012:  br.s       IL_0014

    IL_0014:  ldloc.0
    IL_0015:  ret
  } // end of method TestClass::get_Item

  .method public hidebysig instance void 
          TriggerEvent() cil managed
  {
    // Code size       25 (0x19)
    .maxstack  8
    IL_0000:  nop
    IL_0001:  ldarg.0
    IL_0002:  ldfld      class TestProgram.TestDelegate TestProgram.TestClass::TestEvent
    IL_0007:  dup
    IL_0008:  brtrue.s   IL_000d

    IL_000a:  pop
    IL_000b:  br.s       IL_0018

    IL_000d:  ldstr      "Event triggered!"
    IL_0012:  callvirt   instance void TestProgram.TestDelegate::Invoke(string)
    IL_0017:  nop
    IL_0018:  ret
  } // end of method TestClass::TriggerEvent

  .method public hidebysig instance void 
          Loop() cil managed
  {
    // Code size       42 (0x2a)
    .maxstack  2
    .locals init (int32 V_0,
             bool V_1)
    IL_0000:  nop
    IL_0001:  ldc.i4.0
    IL_0002:  stloc.0
    IL_0003:  br.s       IL_0021

    IL_0005:  nop
    IL_0006:  ldstr      "Loop iteration: {0}"
    IL_000b:  ldloc.0
    IL_000c:  box        [mscorlib]System.Int32
    IL_0011:  call       string [mscorlib]System.String::Format(string,
                                                                object)
    IL_0016:  call       void [mscorlib]System.Console::WriteLine(string)
    IL_001b:  nop
    IL_001c:  nop
    IL_001d:  ldloc.0
    IL_001e:  ldc.i4.1
    IL_001f:  add
    IL_0020:  stloc.0
    IL_0021:  ldloc.0
    IL_0022:  ldc.i4.5
    IL_0023:  clt
    IL_0025:  stloc.1
    IL_0026:  ldloc.1
    IL_0027:  brtrue.s   IL_0005

    IL_0029:  ret
  } // end of method TestClass::Loop

  .method public hidebysig instance void 
          Condition(int32 x) cil managed
  {
    // Code size       55 (0x37)
    .maxstack  2
    .locals init (bool V_0,
             bool V_1)
    IL_0000:  nop
    IL_0001:  ldarg.1
    IL_0002:  ldc.i4.0
    IL_0003:  cgt
    IL_0005:  stloc.0
    IL_0006:  ldloc.0
    IL_0007:  brfalse.s  IL_0016

    IL_0009:  ldstr      "Positive"
    IL_000e:  call       void [mscorlib]System.Console::WriteLine(string)
    IL_0013:  nop
    IL_0014:  br.s       IL_0036

    IL_0016:  ldarg.1
    IL_0017:  ldc.i4.0
    IL_0018:  clt
    IL_001a:  stloc.1
    IL_001b:  ldloc.1
    IL_001c:  brfalse.s  IL_002b

    IL_001e:  ldstr      "Negative"
    IL_0023:  call       void [mscorlib]System.Console::WriteLine(string)
    IL_0028:  nop
    IL_0029:  br.s       IL_0036

    IL_002b:  ldstr      "Zero"
    IL_0030:  call       void [mscorlib]System.Console::WriteLine(string)
    IL_0035:  nop
    IL_0036:  ret
  } // end of method TestClass::Condition

  .method public hidebysig instance void 
          Switch(int32 day) cil managed
  {
    // Code size       57 (0x39)
    .maxstack  2
    .locals init (int32 V_0,
             int32 V_1)
    IL_0000:  nop
    IL_0001:  ldarg.1
    IL_0002:  stloc.1
    IL_0003:  ldloc.1
    IL_0004:  stloc.0
    IL_0005:  ldloc.0
    IL_0006:  ldc.i4.1
    IL_0007:  beq.s      IL_0011

    IL_0009:  br.s       IL_000b

    IL_000b:  ldloc.0
    IL_000c:  ldc.i4.2
    IL_000d:  beq.s      IL_001e

    IL_000f:  br.s       IL_002b

    IL_0011:  ldstr      "Monday"
    IL_0016:  call       void [mscorlib]System.Console::WriteLine(string)
    IL_001b:  nop
    IL_001c:  br.s       IL_0038

    IL_001e:  ldstr      "Tuesday"
    IL_0023:  call       void [mscorlib]System.Console::WriteLine(string)
    IL_0028:  nop
    IL_0029:  br.s       IL_0038

    IL_002b:  ldstr      "Other day"
    IL_0030:  call       void [mscorlib]System.Console::WriteLine(string)
    IL_0035:  nop
    IL_0036:  br.s       IL_0038

    IL_0038:  ret
  } // end of method TestClass::Switch

  .method public hidebysig specialname rtspecialname 
          instance void  .ctor() cil managed
  {
    // Code size       8 (0x8)
    .maxstack  8
    IL_0000:  ldarg.0
    IL_0001:  call       instance void [mscorlib]System.Object::.ctor()
    IL_0006:  nop
    IL_0007:  ret
  } // end of method TestClass::.ctor

  .event TestProgram.TestDelegate TestEvent
  {
    .addon instance void TestProgram.TestClass::add_TestEvent(class TestProgram.TestDelegate)
    .removeon instance void TestProgram.TestClass::remove_TestEvent(class TestProgram.TestDelegate)
  } // end of event TestClass::TestEvent
  .property instance int32 Number()
  {
    .get instance int32 TestProgram.TestClass::get_Number()
    .set instance void TestProgram.TestClass::set_Number(int32)
  } // end of property TestClass::Number
  .property instance string Item(int32)
  {
    .get instance string TestProgram.TestClass::get_Item(int32)
  } // end of property TestClass::Item
} // end of class TestProgram.TestClass

.class private auto ansi beforefieldinit TestProgram.Program
       extends [mscorlib]System.Object
{
  .class auto ansi serializable sealed nested private beforefieldinit '<>c'
         extends [mscorlib]System.Object
  {
    .custom instance void [mscorlib]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = ( 01 00 00 00 ) 
    .field public static initonly class TestProgram.Program/'<>c' '<>9'
    .field public static class TestProgram.TestDelegate '<>9__0_0'
    .method private hidebysig specialname rtspecialname static 
            void  .cctor() cil managed
    {
      // Code size       11 (0xb)
      .maxstack  8
      IL_0000:  newobj     instance void TestProgram.Program/'<>c'::.ctor()
      IL_0005:  stsfld     class TestProgram.Program/'<>c' TestProgram.Program/'<>c'::'<>9'
      IL_000a:  ret
    } // end of method '<>c'::.cctor

    .method public hidebysig specialname rtspecialname 
            instance void  .ctor() cil managed
    {
      // Code size       8 (0x8)
      .maxstack  8
      IL_0000:  ldarg.0
      IL_0001:  call       instance void [mscorlib]System.Object::.ctor()
      IL_0006:  nop
      IL_0007:  ret
    } // end of method '<>c'::.ctor

    .method assembly hidebysig instance void 
            '<Main>b__0_0'(string msg) cil managed
    {
      // Code size       8 (0x8)
      .maxstack  8
      IL_0000:  ldarg.1
      IL_0001:  call       void [mscorlib]System.Console::WriteLine(string)
      IL_0006:  nop
      IL_0007:  ret
    } // end of method '<>c'::'<Main>b__0_0'

  } // end of class '<>c'

  .method private hidebysig static void  Main() cil managed
  {
    .entrypoint
    // Code size       90 (0x5a)
    .maxstack  3
    .locals init (class TestProgram.TestClass V_0)
    IL_0000:  nop
    IL_0001:  newobj     instance void TestProgram.TestClass::.ctor()
    IL_0006:  stloc.0
    IL_0007:  ldloc.0
    IL_0008:  ldsfld     class TestProgram.TestDelegate TestProgram.Program/'<>c'::'<>9__0_0'
    IL_000d:  dup
    IL_000e:  brtrue.s   IL_0027

    IL_0010:  pop
    IL_0011:  ldsfld     class TestProgram.Program/'<>c' TestProgram.Program/'<>c'::'<>9'
    IL_0016:  ldftn      instance void TestProgram.Program/'<>c'::'<Main>b__0_0'(string)
    IL_001c:  newobj     instance void TestProgram.TestDelegate::.ctor(object,
                                                                       native int)
    IL_0021:  dup
    IL_0022:  stsfld     class TestProgram.TestDelegate TestProgram.Program/'<>c'::'<>9__0_0'
    IL_0027:  callvirt   instance void TestProgram.TestClass::add_TestEvent(class TestProgram.TestDelegate)
    IL_002c:  nop
    IL_002d:  ldloc.0
    IL_002e:  callvirt   instance void TestProgram.TestClass::TriggerEvent()
    IL_0033:  nop
    IL_0034:  ldloc.0
    IL_0035:  callvirt   instance void TestProgram.TestClass::Loop()
    IL_003a:  nop
    IL_003b:  ldloc.0
    IL_003c:  ldc.i4.s   -5
    IL_003e:  callvirt   instance void TestProgram.TestClass::Condition(int32)
    IL_0043:  nop
    IL_0044:  ldloc.0
    IL_0045:  ldc.i4.1
    IL_0046:  callvirt   instance void TestProgram.TestClass::Switch(int32)
    IL_004b:  nop
    IL_004c:  ldloc.0
    IL_004d:  ldc.i4.2
    IL_004e:  callvirt   instance string TestProgram.TestClass::get_Item(int32)
    IL_0053:  call       void [mscorlib]System.Console::WriteLine(string)
    IL_0058:  nop
    IL_0059:  ret
  } // end of method Program::Main

  .method public hidebysig specialname rtspecialname 
          instance void  .ctor() cil managed
  {
    // Code size       8 (0x8)
    .maxstack  8
    IL_0000:  ldarg.0
    IL_0001:  call       instance void [mscorlib]System.Object::.ctor()
    IL_0006:  nop
    IL_0007:  ret
  } // end of method Program::.ctor

} // end of class TestProgram.Program


// =============================================================

// *********** DISASSEMBLY COMPLETE ***********************
// WARNING: Created Win32 resource file Pro.res
