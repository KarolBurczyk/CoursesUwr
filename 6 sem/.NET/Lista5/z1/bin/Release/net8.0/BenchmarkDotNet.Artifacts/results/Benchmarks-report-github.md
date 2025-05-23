```

BenchmarkDotNet v0.14.0, Windows 11 (10.0.26100.3775)
Intel Core i5-9300H CPU 2.40GHz, 1 CPU, 8 logical and 4 physical cores
.NET SDK 9.0.200
  [Host]     : .NET 8.0.14 (8.0.1425.11118), X64 RyuJIT AVX2
  DefaultJob : .NET 8.0.14 (8.0.1425.11118), X64 RyuJIT AVX2


```
| Method  | Mean       | Error     | StdDev    |
|-------- |-----------:|----------:|----------:|
| DoWork1 |  0.0591 ns | 0.0200 ns | 0.0187 ns |
| DoWork2 | 11.1834 ns | 0.1149 ns | 0.1018 ns |
