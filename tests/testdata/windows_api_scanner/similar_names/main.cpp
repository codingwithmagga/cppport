#include "non_windows.h"

void MyCreateFileWrapper() {

  GetProcessHandler();
  SleepTime(100);
  CreateFileWriter();
}

int main() {

  MyCreateFileWrapper();

  return 0;
}