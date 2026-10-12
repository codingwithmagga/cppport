#include <windows.h>

void windows_only() {
  CreateFileA("test.txt", GENERIC_READ, 0, nullptr, OPEN_EXISTING,
              FILE_ATTRIBUTE_NORMAL, nullptr);
}