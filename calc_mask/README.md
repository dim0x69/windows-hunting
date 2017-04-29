## calc_mask
Simple tool to calculate die Process Security and Access Rights Mask:

https://msdn.microsoft.com/de-de/library/windows/desktop/ms684880(v=vs.85).aspx

## Build
go build calc_mask.go

## use
$ ./calc_mask -m "PROCESS_VM_READ | PROCESS_VM_WRITE | PROCESS_VM_OPERATION |
PROCESS_QUERY_INFORMATION"

0x1438

please note: currently not all rights are implemented... i will implement them
as i need them :)
