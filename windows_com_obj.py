import win32com.client

o = win32com.client.Dispatch("CATC.PETracer")

print(o.GetVersion(0))
print(o.GetSerialNumber())