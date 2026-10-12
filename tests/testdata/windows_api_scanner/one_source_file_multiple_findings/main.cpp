#include <windows.h>

void windows_only() {
  CreateFileA("test.txt", GENERIC_READ, 0, nullptr, OPEN_EXISTING,
              FILE_ATTRIBUTE_NORMAL, nullptr);

  CreateFileW(L"test.txt", GENERIC_READ, 0, nullptr, OPEN_EXISTING,
              FILE_ATTRIBUTE_NORMAL, nullptr);

  LoadLibraryA("kernel32.dll");
  LoadLibraryW(L"kernel32.dll");

  GetModuleHandleA("kernel32.dll");
  GetProcAddress(GetModuleHandleA("kernel32.dll"), "CreateFileW");
}